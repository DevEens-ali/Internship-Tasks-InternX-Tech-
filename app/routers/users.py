from fastapi import APIRouter, Depends

from app.dependencies import get_current_user
from app.models import User
from app.schemas import UserResponse,UserUpdate
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.auth import hash_password

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me", response_model=UserResponse)
def get_my_profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/", response_model=list[UserResponse])
def get_users(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    users = db.query(User).all()

    return users

@router.get("/{id}", response_model=UserResponse)
def get_user(
    id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user
# @router.put("/{id}", response_model=UserResponse)
# def update_user(
#     id: int,
#     current_user: User = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     existing_user = db.query(User).filter(User.id == user.id).first()
    
#     if existing_user is None:
#             raise HTTPException(
#                 status_code=404,
#                 detail="User not found"
#             )
    
#     existing_user.name = User.name,
#     existing_user.email = User.email,
#     existing_user.password= User.password,
#     db.commit()
#     db.refresh(existing_user)

#     return existing_user
    
@router.put("/{id}", response_model=UserResponse)
def update_user(
    id: int,
    user: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.id == id).first()

    if existing_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    existing_user.name = user.name
    existing_user.email = user.email
    existing_user.password = hash_password(user.password)

    db.commit()
    db.refresh(existing_user)

    return existing_user
    
    
# @app.put("/posts/{id}", response_model=PostResponse)
# def update_post(
#     id: int,
#     post: PostUpdate,
#     db: Session = Depends(get_db)
# ):
#     existing_post = db.query(Post).filter(Post.id == id).first()

#     if existing_post is None:
#         raise HTTPException(
#             status_code=404,
#             detail=f"Post with id {id} not found"
#         )

#     existing_post.title = post.title
#     existing_post.content = post.content
#     existing_post.published = post.published

#     db.commit()
#     db.refresh(existing_post)

#     return existing_post
@router.delete("/{id}")
def delete_user(
    id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail=f"User with id {id} not found"
        )

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}