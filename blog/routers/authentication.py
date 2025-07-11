from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from blog import schemas, database, models, hashing, token
from sqlalchemy.orm import Session

router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = 404, detail = f"Invalid User email")
    
    if not hashing.Hash.verify(request.password, user.password):
        raise HTTPException(status_code = 404, detail = f"Invalid Password")
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type":"bearer"}