from fastapi import APIRouter,Depends, status
from .. import schemas, database
from sqlalchemy.orm import Session

from ..repository import blog

get_db = database.get_db


router = APIRouter()


router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)


@router.get("/", response_model=list[schemas.ShowBlog])  
def fetch_blog(db :Session = Depends(get_db)):
    return blog.get_all(db)

    
@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show_blog(id, db :Session = Depends(get_db)):
    return blog.show_blog(db, id)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request :schemas.Blog, db :Session = Depends(get_db)):
   return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db :Session = Depends(get_db)):
    return blog.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request :schemas.Blog, db :Session = Depends(get_db)):
        return blog.update(id, request, db)
    