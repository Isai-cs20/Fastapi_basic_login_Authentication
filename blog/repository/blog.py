from sqlalchemy.orm import Session
from fastapi import HTTPException
from blog import models

def get_all(db: Session):
     blog = db.query(models.Blog).all()
     return blog

def create(request, db:Session):
    new_blog = models.Blog(title = request.title, body = request.body, user_id =1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = 404, detail = f'Blog with id {id} is not Available')
    return blog

def destroy(id, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session = False)
    if not blog:
        raise HTTPException(status_code = 404, detail = f'Blog with id {id} is not available')
    db.commit()
    return 'done'

def update(id, db:Session):
    blog = db.query(models.blog).filter(models.Blog.id == id).update({'title':'updated title'})
    if not blog:
        raise HTTPException(status_code = 404, detail = f'Blog with id {id} is not available')
    db.commit()
    return 'updated'