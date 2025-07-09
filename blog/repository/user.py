from fastapi import HTTPException
from sqlalchemy.orm import Session
from blog import models, hashing


def create(request, db:Session):
    new_user = models.User(name = request.name, email= request.email, password = hashing.Hash.bcrypt(request.password ))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def all(db:Session):
    users = db.query(models.User).all()
    return users

def show(id, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = 404, detail = f'user with id {id} is not Available')
    return user

def delete(id, db:Session):
    user = db.query(models.User).filter(models.User.id == id).delete(synchronize_session = False)
    if not user:
        raise HTTPException(status_code = 404, detail = f'user with id {id} is not available')
    db.commit()
    return 'done'