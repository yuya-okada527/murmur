from fastapi import (
    FastAPI,
    status,
    Request
)
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .middleware.security import origins
from .infra import models
from .infra.database import engine
from .routers import murmurs, sample

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Murmur",
    description="2020 Golden Week Project.",
    version="0.0.1"
)

app.include_router(
    murmurs.router,
    prefix="/murmurs",
    tags=["murmurs"]
)
app.include_router(
    sample.router,
    prefix="/sample",
    tags=["sample"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


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
