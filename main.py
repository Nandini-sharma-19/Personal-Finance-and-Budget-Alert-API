from fastapi import FastAPI,Depends,HTTPException
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
import database
import models
import schemas

@asynccontextmanager
async def lifespan(app:FastAPI):
  database.init_db()
  yield

app=FastAPI(title="Personal Finance & Budget Alert API",lifespan=lifespan)


# A helper function to open and close a database connection safely for every request
def get_db():
  db=database.SessionLocal()
  try:
    yield db
  finally:
    db.close()

# Our absolute first testing endpoint to make sure things run!
@app.get("/")
def home():
  return {"message":"Welcome to your Personnel Finance API! Head to /docs to test it."}

@app.post("/users",response_model=schemas.UserResponse)
def create_user(user_data:schemas.UserCreate,db:Session=Depends(get_db)):
  existing_user=db.query(models.User).filter(models.User.username==user_data.username).first()
  if existing_user:
    raise HTTPException(status_code=400,detail="Username is already taken")
  new_user=models.User(username=user_data.username,monthly_limit=user_data.monthly_limit)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  return new_user