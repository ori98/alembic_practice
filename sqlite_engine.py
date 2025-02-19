from sqlmodel import SQLModel, Session, create_engine

import models

# Creating the sqlite engine
sqlite_db_file_name = "test.db"
sqlite_url = f"sqlite:///{sqlite_db_file_name}"

# Engine
engine = create_engine(sqlite_url, echo=True)

# Conditionally create the tables
SQLModel.metadata.create_all(bind=engine)

# Get session object
def get_session():
    with Session(bind=engine) as session:
        yield session