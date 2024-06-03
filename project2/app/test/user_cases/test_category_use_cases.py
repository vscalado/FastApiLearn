from app.use_cases.category import CategoryUseCases
from app.db.models import Category as CategoryModel
from app.schemas.category import Category

def test_add_category_uc(db_session):
    uc = CategoryUseCases(db_session)

    category = Category(
        name='Sapato',
        slug='sapato'
    )
    uc.add_category(category=category)

    categories_on_db = db_session.query(CategoryModel).all()

    assert len(categories_on_db) == 1
    assert categories_on_db[0].name == 'Sapato'
    assert categories_on_db[0].slug == 'sapato'

    db_session.delete(categories_on_db[0])
    db_session.commit()