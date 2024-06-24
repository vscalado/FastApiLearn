from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.schemas.user import User
from app.routes.deps import get_db_session
from app.use_cases.user import UserUseCases

router = APIRouter(prefix='/user', tags=['User'])

@router.post('/register', status_code=status.HTTP_201_CREATED, description="Register a new User")
def register_user(
    user: User,
    db_session: Session = Depends(get_db_session)
):
    uc = UserUseCases(db_session=db_session)
    uc.register_user(user=user)
    
    return Response(status_code=status.HTTP_201_CREATED)
