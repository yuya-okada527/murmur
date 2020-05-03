from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class Murmur(BaseModel):
    id: int = Field(
        None,
        description="Unique id for each murmur.",
        ge=1
    )
    user_id: str = Field(
        ...,
        description="Unique id for each user.",
        regex="^[0-9a-z]{8}$"
    )
    user_name: str = Field(
        ...,
        description="User name.",
        max_length=32
    )
    message: str = Field(
        ...,
        description="Message for murmur.",
        max_length=128
    )
    time: datetime = Field(
        None,
        description="Datetime at posting message.<br>"
                    "This field requires ISO 8601 format.<br>"
                    "ISO 8601 format: YYYY-MM-DD[T]HH:MM[:SS[.ffffff]][Z[±]HH[:]MM]]]"
    )

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "user_id": "12345678",
                "user_name": "user_name",
                "message": "message",
                "time": "2032-04-23T10:20:30.400+02:30"
            }
        }
        orm_mode = True


class Murmurs(BaseModel):
    total_num: int
    returned_num: int
    offset: int
    limit: int
    result: List[Murmur]
