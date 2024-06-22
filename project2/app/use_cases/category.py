from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
from app.db.models import Category as CategoryModels
from app.schemas.category import Category, CategoryOutput

class CategoryUseCases:
    def __init__(self, db_session:Session):
        self.db_session = db_session

    def add_category(self, category: Category):
        category_model = CategoryModels(**category.dict())
        self.db_session.add(category_model)
        self.db_session.commit()
    
    def list_categories(self):
        categories_on_db = self.db_session.query(CategoryModels).all()
        categories_output = [
            self.serialize_category(category_model)
            for category_model in categories_on_db
        ]
        return categories_output
    
    def delete_category(self, id= int):
        category_model = self.db_session.query(CategoryModels).filter_by(id=id).first()

        if not category_model:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
        
        self.db_session.delete(category_model)
        self.db_session.commit()

    def serialize_category(self, category_model: CategoryModels):
        return CategoryOutput(**category_model.__dict__)

