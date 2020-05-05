from typing import List, Tuple

from sqlalchemy.orm import Session

from app.routers import schemas
from app.infra import models


def get_all_murmurs(
        db: Session,
        offset: int,
        limit: int) -> Tuple[List[schemas.Murmur], int]:
    query = db.query(models.Murmur)
    db_murmurs = query.order_by(models.Murmur.time) \
        .limit(limit) \
        .offset(offset) \
        .all()
    murmurs = list(map(lambda murmur: schemas.Murmur(
        id=murmur.id,
        user_id=murmur.user_id,
        user_name=murmur.user_name,
        message=murmur.message,
        time=murmur.time
    ), db_murmurs))
    return murmurs, query.count()


def create_murmur(db: Session, murmur: schemas.Murmur) -> models.Murmur:
    db_murmur = models.Murmur(**murmur.dict())
    db.add(db_murmur)
    db.commit()
    db.refresh(db_murmur)
    return db_murmur
