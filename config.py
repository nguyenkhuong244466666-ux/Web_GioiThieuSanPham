import os

# Thư mục gốc của project
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Cấu hình ứng dụng Flask"""

    # Khóa bí mật
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "cua_nhom_nguyen_nghiem_secret_2026"
    )

    # Database
    # Trên Render nếu có DATABASE_URL thì dùng.
    # Nếu không có thì dùng SQLite.
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "database.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Thư mục upload
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

    # Định dạng ảnh cho phép
    ALLOWED_EXTENSIONS = {
        "jpg",
        "jpeg",
        "png",
        "webp"
    }

    # Giới hạn upload (16MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024