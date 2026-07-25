from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config

# Tạo Engine kết nối tới MySQL
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
    pool_recycle=3600
)

# Khởi tạo Session factory
LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base Model cho các bảng ORM
Base = declarative_base()

def get_db():
    """Generator function để quản lý Session Database cho mỗi request."""
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()