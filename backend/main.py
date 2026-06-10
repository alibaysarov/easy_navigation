from fastapi import FastAPI, Depends

from db import get_db
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User
from routers import base_router

app = FastAPI()

app.include_router(base_router)



@app.get("/users")
def get_users(session: Session = Depends(get_db)):
    stmt = select(User.id, User.name).limit(10)
    items = session.execute(stmt).all()

    return {"users": [{"id": str(row.id), "name": row.name} for row in items]}


# def main():

#     print("Hello from backend!")


# if __name__ == "__main__":
#     main()
