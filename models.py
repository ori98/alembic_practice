from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

class Employee(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=lambda: uuid4().bytes)
    name: str
    age: int | None
    # is_active: bool # added new field