from fastapi import (
    Depends,
    APIRouter
)
from sqlalchemy.orm import Session

from ..routers import schemas
from ..infra import crud
from ..infra.database import get_db

router = APIRouter()


@router.get("/all", response_model=schemas.Murmurs)
def search_all(
        limit: int = 10,
        offset: int = 1,
        db: Session = Depends(get_db)
):
    """
    Search all murmurs.

    """
    murmurs, total_num = crud.get_all_murmurs(db=db, limit=limit, offset=offset)
    return schemas.Murmurs(
        total_num=total_num,
        returned_num=len(murmurs),
        offset=offset,
        limit=limit,
        result=murmurs
    )


@router.post("", response_model=schemas.Murmur)
def create_murmur(murmur: schemas.Murmur, db: Session = Depends(get_db)):
    """
    Create murmur.

    """
    return crud.create_murmur(db, murmur)
