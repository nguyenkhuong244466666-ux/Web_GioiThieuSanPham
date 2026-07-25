import os

class Config:
    """Cấu hình ứng dụng Flask và SQLAlchemy."""

    # Khóa bí mật cho Session
    SECRET_KEY = os.environ.get('SECRET_KEY', 'cua_nhom_nguyen_nghiem_secret_2026')

    # Chuỗi kết nối Database với SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 
        'mysql+pymysql://root:1234@localhost:3306/cua_nhom_nguyen_nghiem'
    )

    # Thư mục lưu trữ Uploads
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    
    # Định dạng ảnh cho phép upload
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp'}
    
    # Giới hạn dung lượng file upload (tối đa 16MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024