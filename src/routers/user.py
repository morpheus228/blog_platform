from fastapi import APIRouter,Depends, status, HTTPException
from typing import List

from .. import models, schemas, database, hashing
from sqlalchemy.orm import Session
from ..repository import user

get_db = database.get_db

router = APIRouter()




router = APIRouter(
    prefix="/user",
    tags=['Users']
)
# for users 

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return user.createUser(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.showUser(id,db)
