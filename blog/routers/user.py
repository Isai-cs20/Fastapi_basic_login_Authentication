from fastapi import APIRouter,Depends
from blog import schemas,database
from sqlalchemy.orm import Session
from typing import List
from blog.repository import user

router = APIRouter(
    tags = ['Users'],
    prefix = "/user"
)

@router.post("/")
def create_user(request : schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)

@router.get('/', response_model = List[schemas.ShowUser])
def all(db: Session = Depends(database.get_db)):
    return user.all(db)

@router.get('/{id}', status_code = 200)
def show_user(id, db:Session = Depends(database.get_db)):
    return user.show(id, db)

@router.delete('/{id}', status_code = 204)
def delete_user(id, db:Session = Depends(database.get_db)):
    return user.delete(id, db)