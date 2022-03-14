from typing import List

from sqlalchemy.orm import Session  # type: ignore

from models.orm import UsersOrm





def get_items(session: Session, skip: int = 0, limit: int = 100) -> List[UsersOrm]:
    return session.query(UsersOrm).offset(skip).limit(limit).all()
