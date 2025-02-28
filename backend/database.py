
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://dev-admin:password123@db:5432/health_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
            