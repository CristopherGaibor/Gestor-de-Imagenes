from sqlmodel import SQLModel, Field, create_engine


sqlite_file = "users.db"
engine = create_engine(f"sqlite:///{sqlite_file}")


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    encrypted_password: str 

def create_db():
    SQLModel.metadata.create_all(engine)