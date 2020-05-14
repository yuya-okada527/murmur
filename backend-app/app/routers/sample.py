from typing import Optional

from fastapi import Depends, UploadFile, File, Form, HTTPException, APIRouter
from starlette import status

from app.middleware.security import oauth2_scheme

router = APIRouter()


@router.get("/security")
def security(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@router.post("/image", deprecated=True)
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


@router.get("/exception")
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
