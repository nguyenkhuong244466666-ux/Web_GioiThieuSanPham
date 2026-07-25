-- ============================================
-- CỬA NHÔM NGUYỄN NGHIỆM - Sample Data
-- ============================================

USE cua_nhom_nguyen_nghiem;

-- ============================================
-- Tạo tài khoản admin mặc định
-- Password: admin123 (đã hash bằng werkzeug)
-- ============================================
INSERT INTO admin (username, password) VALUES 
('admin', 'pbkdf2:sha256:600000$XyZ123AbC$e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855');

-- ============================================
-- Tạo danh mục sản phẩm
-- ============================================

-- Danh mục cấp 1 (không có parent)
INSERT INTO category (id, name, slug, parent_id, display_order) VALUES
(1, 'Cửa cái', 'cua-cai', NULL, 1),
(2, 'Cửa phòng', 'cua-phong', NULL, 2),
(3, 'Cửa toilet', 'cua-toilet', NULL, 3),
(4, 'Cửa sổ', 'cua-so', NULL, 4),
(5, 'Tủ', 'tu', NULL, 5),
(6, 'Vách ngăn', 'vach-ngan', NULL, 6);

-- Danh mục con của "Cửa sổ" (parent_id = 4)
INSERT INTO category (id, name, slug, parent_id, display_order) VALUES
(7, 'Cửa sổ kéo', 'cua-so-keo', 4, 1),
(8, 'Cửa sổ lùa', 'cua-so-lua', 4, 2);

-- Danh mục con của "Tủ" (parent_id = 5)
INSERT INTO category (id, name, slug, parent_id, display_order) VALUES
(9, 'Tủ bếp', 'tu-bep', 5, 1),
(10, 'Tủ quần áo', 'tu-quan-ao', 5, 2),
(11, 'Tủ chén', 'tu-chen', 5, 3),
(12, 'Tủ trang trí', 'tu-trang-tri', 5, 4);

-- ============================================
-- Dữ liệu mẫu cho sản phẩm (hình ảnh demo)
-- ============================================

-- Cửa cái
INSERT INTO product (category_id, title, image) VALUES
(1, 'Cửa cái nhôm kính cao cấp', 'cua-cai-01.jpg'),
(1, 'Cửa cái nhôm xingfa', 'cua-cai-02.jpg'),
(1, 'Cửa cái 4 cánh', 'cua-cai-03.jpg');

-- Cửa phòng
INSERT INTO product (category_id, title, image) VALUES
(2, 'Cửa phòng ngủ nhôm kính', 'cua-phong-01.jpg'),
(2, 'Cửa phòng khách hiện đại', 'cua-phong-02.jpg');

-- Cửa toilet
INSERT INTO product (category_id, title, image) VALUES
(3, 'Cửa toilet nhôm kính mờ', 'cua-toilet-01.jpg'),
(3, 'Cửa toilet chống nước', 'cua-toilet-02.jpg');

-- Cửa sổ kéo
INSERT INTO product (category_id, title, image) VALUES
(7, 'Cửa sổ kéo 2 cánh', 'cua-so-keo-01.jpg'),
(7, 'Cửa sổ kéo có lưới', 'cua-so-keo-02.jpg');

-- Cửa sổ lùa
INSERT INTO product (category_id, title, image) VALUES
(8, 'Cửa sổ lùa 3 ray', 'cua-so-lua-01.jpg'),
(8, 'Cửa sổ lùa nhôm xingfa', 'cua-so-lua-02.jpg');

-- Tủ bếp
INSERT INTO product (category_id, title, image) VALUES
(9, 'Tủ bếp nhôm kính hiện đại', 'tu-bep-01.jpg'),
(9, 'Tủ bếp chữ L', 'tu-bep-02.jpg');

-- Tủ quần áo
INSERT INTO product (category_id, title, image) VALUES
(10, 'Tủ quần áo cửa lùa', 'tu-quan-ao-01.jpg'),
(10, 'Tủ quần áo 4 cánh', 'tu-quan-ao-02.jpg');

-- Tủ chén
INSERT INTO product (category_id, title, image) VALUES
(11, 'Tủ chén nhôm kính', 'tu-chen-01.jpg'),
(11, 'Tủ chén 3 tầng', 'tu-chen-02.jpg');

-- Tủ trang trí
INSERT INTO product (category_id, title, image) VALUES
(12, 'Tủ trang trí phòng khách', 'tu-trang-tri-01.jpg'),
(12, 'Kệ trang trí nhôm kính', 'tu-trang-tri-02.jpg');

-- Vách ngăn
INSERT INTO product (category_id, title, image) VALUES
(6, 'Vách ngăn văn phòng', 'vach-ngan-01.jpg'),
(6, 'Vách ngăn phòng khách', 'vach-ngan-02.jpg'),
(6, 'Vách ngăn cầu thang', 'vach-ngan-03.jpg');
