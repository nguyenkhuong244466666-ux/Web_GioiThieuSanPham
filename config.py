import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Cấu hình ứng dụng Flask"""

    # Secret Key
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "cua_nhom_nguyen_nghiem_secret_2026"
    )

    # Database
    # Trên Render: bắt buộc thêm biến môi trường DATABASE_URL
    # Trên máy cá nhân: nếu chưa có DATABASE_URL thì dùng SQLite
    database_url = os.environ.get("DATABASE_URL")

    # Một số dịch vụ trả về mysql://, SQLAlchemy cần mysql+pymysql://
    if database_url and database_url.startswith("mysql://"):
        database_url = database_url.replace(
            "mysql://",
            "mysql+pymysql://",
            1
        )

    SQLALCHEMY_DATABASE_URI = database_url or (
        "sqlite:///" + os.path.join(BASE_DIR, "database.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

    # Định dạng ảnh cho phép
    ALLOWED_EXTENSIONS = {
        "jpg",
        "jpeg",
        "png",
        "webp"
    }

    # Giới hạn upload 16MB
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024