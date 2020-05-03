from typing import Optional

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Form,
    HTTPException,
    status,
    Request,
    Depends
)
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/all_murmurs", response_model=schemas.Murmurs)
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


@app.post("/murmur", response_model=schemas.Murmur)
def create_murmur(murmur: schemas.Murmur, db: Session = Depends(get_db)):
    """
    Create murmur.

    """
    return crud.create_murmur(db, murmur)


@app.get("/security", tags=["sample"])
def security(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@app.post("/image", deprecated=True, tags=["sample"])
async def create_image(
        image: UploadFile = File(...),
        user_id: str = Form(...)
):
    content = await image.read()
    return {
        "filename": image.filename,
        "content": content,
        "user_id": user_id
    }


@app.get("/exception", tags=["sample"])
def exception(nullable: Optional[str] = None):
    if nullable is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "reason": "field is required.",
                "field": "id",
                "value": nullable
            }
        )

    return {"id": nullable}


@app.exception_handler(RequestValidationError)
def validation_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({
            "request": {
                "url": request.url,
                "method": request.method,
                "queries": request.query_params.items(),
                "body": exc.body
            },
            "detail": exc.errors(),
        })
    )
