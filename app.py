import os
from datetime import datetime
from functools import wraps
from flask import (
    Flask, render_template, request, redirect, 
    url_for, flash, session
)
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from database import Base, engine, get_db

app = Flask(__name__)
app.config.from_object(Config)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class AdminModel(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class CategoryModel(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False, unique=True)
    parent_slug = Column(String(100), nullable=True)

    products = relationship("ProductModel", back_populates="category", cascade="all, delete-orphan")


class ProductModel(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
    title = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    category = relationship("CategoryModel", back_populates="products")


class ContactModel(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            flash('Vui lòng đăng nhập để truy cập trang quản trị!', 'danger')
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function


def get_products_by_category_slug(slug):
    db = next(get_db())
    category = db.query(CategoryModel).filter(CategoryModel.slug == slug).first()
    if not category:
        return [], None
    products = db.query(ProductModel).filter(ProductModel.category_id == category.id).order_by(ProductModel.id.desc()).all()
    return products, category


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        fullname = request.form.get('fullname', '').strip()
        phone = request.form.get('phone', '').strip()
        message = request.form.get('message', '').strip()

        if not fullname or not phone or not message:
            flash('Vui lòng điền đầy đủ thông tin!', 'warning')
        else:
            db = next(get_db())
            new_contact = ContactModel(fullname=fullname, phone=phone, message=message)
            db.add(new_contact)
            db.commit()
            flash('Cảm ơn bạn đã liên hệ! Chúng tôi sẽ phản hồi sớm nhất.', 'success')
            return redirect(url_for('contact'))

    return render_template('contact.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/cua-cai')
def cua_cai():
    items, category = get_products_by_category_slug('cua-cai')
    return render_template('cua-cai.html', products=items, category=category)


@app.route('/cua-phong')
def cua_phong():
    items, category = get_products_by_category_slug('cua-phong')
    return render_template('cua-phong.html', products=items, category=category)


@app.route('/cua-toilet')
def cua_toilet():
    items, category = get_products_by_category_slug('cua-toilet')
    return render_template('cua-toilet.html', products=items, category=category)


@app.route('/cua-so')
def cua_so():
    return render_template('cua-so.html')


@app.route('/cua-so-keo')
def cua_so_keo():
    items, category = get_products_by_category_slug('cua-so-keo')
    return render_template('cua-so-keo.html', products=items, category=category)


@app.route('/cua-so-lua')
def cua_so_lua():
    items, category = get_products_by_category_slug('cua-so-lua')
    return render_template('cua-so-lua.html', products=items, category=category)


@app.route('/tu')
def tu():
    return render_template('tu.html')


@app.route('/tu-bep')
def tu_bep():
    items, category = get_products_by_category_slug('tu-bep')
    return render_template('tu-bep.html', products=items, category=category)


@app.route('/tu-quan-ao')
def tu_quan_ao():
    items, category = get_products_by_category_slug('tu-quan-ao')
    return render_template('tu-quan-ao.html', products=items, category=category)


@app.route('/tu-chen')
def tu_chen():
    items, category = get_products_by_category_slug('tu-chen')
    return render_template('tu-chen.html', products=items, category=category)


@app.route('/tu-trang-tri')
def tu_trang_tri():
    items, category = get_products_by_category_slug('tu-trang-tri')
    return render_template('tu-trang-tri.html', products=items, category=category)


@app.route('/vach-ngan')
def vach_ngan():
    items, category = get_products_by_category_slug('vach-ngan')
    return render_template('vach-ngan.html', products=items, category=category)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if 'admin_logged_in' in session:
        return redirect(url_for('admin_dashboard'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        db = next(get_db())
        admin = db.query(AdminModel).filter(AdminModel.username == username).first()

        if admin and (check_password_hash(admin.password, password) or admin.password == password):
            session['admin_logged_in'] = True
            session['admin_username'] = admin.username
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không chính xác!', 'danger')

    return render_template('admin/login.html')


@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    db = next(get_db())
    total_products = db.query(ProductModel).count()
    total_contacts = db.query(ContactModel).count()
    recent_contacts = db.query(ContactModel).order_by(ContactModel.id.desc()).limit(5).all()
    return render_template('admin/dashboard.html', total_products=total_products, total_contacts=total_contacts, contacts=recent_contacts)


@app.route('/admin/products')
@login_required
def admin_products():
    db = next(get_db())
    products_list = db.query(ProductModel).order_by(ProductModel.id.desc()).all()
    return render_template('admin/products.html', products=products_list)


@app.route('/admin/upload', methods=['GET', 'POST'])
@login_required
def admin_upload():
    db = next(get_db())
    categories = db.query(CategoryModel).filter(
        CategoryModel.slug.notin_(['cua-so', 'tu'])
    ).all()

    if request.method == 'POST':
        category_id = request.form.get('category_id')
        title = request.form.get('title', '').strip()
        files = request.files.getlist('images')

        if not category_id or not files:
            flash('Vui lòng chọn danh mục và ít nhất 1 ảnh!', 'warning')
            return redirect(url_for('admin_upload'))

        category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
        if not category:
            flash('Danh mục không hợp lệ!', 'danger')
            return redirect(url_for('admin_upload'))

        target_folder = os.path.join(app.config['UPLOAD_FOLDER'], category.slug)
        os.makedirs(target_folder, exist_ok=True)

        uploaded_count = 0
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                unique_filename = f"{int(datetime.utcnow().timestamp())}_{filename}"
                file_path = os.path.join(target_folder, unique_filename)
                file.save(file_path)

                new_product = ProductModel(
                    category_id=category.id,
                    title=title or category.name,
                    image=unique_filename
                )
                db.add(new_product)
                uploaded_count += 1

        db.commit()
        flash(f'Tải lên thành công {uploaded_count} hình ảnh!', 'success')
        return redirect(url_for('admin_products'))

    return render_template('admin/upload.html', categories=categories)


@app.route('/admin/delete/<int:product_id>', methods=['POST'])
@login_required
def admin_delete_product(product_id):
    db = next(get_db())
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    
    if product:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], product.category.slug, product.image)
        if os.path.exists(file_path):
            os.remove(file_path)

        db.delete(product)
        db.commit()
        flash('Đã xóa hình ảnh thành công!', 'success')
    else:
        flash('Sản phẩm không tồn tại!', 'danger')

    return redirect(url_for('admin_products'))


@app.route('/admin/logout')
def admin_logout():
    session.clear()
    flash('Đã đăng xuất thành công!', 'info')
    return redirect(url_for('admin_login'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)