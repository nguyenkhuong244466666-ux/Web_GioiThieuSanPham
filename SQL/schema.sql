-- ============================================
-- CỬA NHÔM NGUYỄN NGHIỆM - Database Schema
-- ============================================

-- Tạo database
CREATE DATABASE IF NOT EXISTS cua_nhom_nguyen_nghiem
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE cua_nhom_nguyen_nghiem;

-- ============================================
-- Bảng admin: Quản lý tài khoản admin
-- ============================================
CREATE TABLE IF NOT EXISTS admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================
-- Bảng category: Danh mục sản phẩm
-- ============================================
CREATE TABLE IF NOT EXISTS category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) NOT NULL UNIQUE,
    parent_id INT DEFAULT NULL,
    display_order INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_id) REFERENCES category(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================
-- Bảng product: Sản phẩm (hình ảnh)
-- ============================================
CREATE TABLE IF NOT EXISTS product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    image VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================
-- Index để tối ưu truy vấn
-- ============================================
CREATE INDEX idx_category_slug ON category(slug);
CREATE INDEX idx_category_parent ON category(parent_id);
CREATE INDEX idx_product_category ON product(category_id);
CREATE INDEX idx_product_created ON product(created_at);
