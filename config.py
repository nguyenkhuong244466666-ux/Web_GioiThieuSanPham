import os

class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "cua_nhom_nguyen_nghiem_secret_2026"
    )

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join("static", "uploads")

    ALLOWED_EXTENSIONS = {
        "jpg",
        "jpeg",
        "png",
        "webp"
    }

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024