from fastapi import APIRouter
from fastapi import Depends, status, HTTPException

from .. import models, schemas, database
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Authentication']
)



@router.post("/login")
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    
    
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
        
        
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect Password")
