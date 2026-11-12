from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

class DatasetCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = None
    file_type: str = Field(..., min_length=1, max_length=20)
    records: int = Field(default=0, ge=0)
    status: Literal["Active", "Inactive"] = "Active"

class DatasetUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = None
    file_type: str = Field(..., min_length=1, max_length=20)
    records: int = Field(..., ge=0)
    status: Literal["Active", "Inactive"]

class DatasetResponse(BaseModel):
    id: int
    name: str
    description: str | None
    file_type: str
    records: int
    status: str
    model_config = ConfigDict(from_attributes=True)
