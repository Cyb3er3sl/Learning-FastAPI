from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate
import datetime

def create_post(db: Session, user_id:int, post: PostCreate):
    db_post = Post(

        title = post.title, 
        content = post.content, 
        author_id = user_id, 
        created_at = datetime.datetime.now()
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts_for_user(db: Session, user_id:int):
    return db.query(Post).filter(Post.author_id  == user_id).all()