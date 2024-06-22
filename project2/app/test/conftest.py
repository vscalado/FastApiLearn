import pytest
from app.db.connection import Session
from app.db.models import Category as CategoryModels

@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()
        
@pytest.fixture()
def categories_on_db(db_session):
    categories = [
        CategoryModels(name= 'Roupa', slug='roupa'),
        CategoryModels(name= 'Vestido', slug='vestido'),
        CategoryModels(name= 'Tenis Corrida', slug='tenis-corrida'),
        CategoryModels(name= 'Itens de Cozinha', slug='itens-de-cozinha')
    ]

    for category in categories:
        db_session.add(category)
    db_session.commit()

    for category in categories:
        db_session.refresh(category)
    
    yield categories

    for category in categories:
        db_session.delete(category)
    db_session.commit()