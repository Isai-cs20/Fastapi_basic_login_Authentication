from fastapi import APIRouter, Depends, HTTPException
from blog import schemas, models, database, oauth2
from sqlalchemy.orm import Session
from typing import List
from blog.repository import blog

router = APIRouter(
    tags = ['Blogs'],
    prefix = "/blog"
)

@router.get('/', response_model = List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.get_all(db)

@router.post('/', status_code = 201)
def create(request : schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.create(request,db)

@router.get('/{id}', status_code = 200, response_model = schemas.ShowBlog)
def show(id, db:Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)

@router.delete('/{id}', status_code = 204)
def destroy(id, db:Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.destroy(id, db)

@router.put("/{id}", status_code = 202)
def update(id, request: schemas.Blog, db:Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, db)