document.addEventListener('DOMContentLoaded', function () {
    // 1. Xử lý Toggle Mobile Menu
    const mobileToggle = document.getElementById('mobileToggle');
    const mainNav = document.querySelector('.main-nav');

    if (mobileToggle && mainNav) {
        mobileToggle.addEventListener('click', function () {
            mainNav.classList.toggle('active');
        });
    }

    // 2. Xử lý Fallback Logo (khi ảnh logo chính bị lỗi/không tồn tại)
    const logoImg = document.querySelector('.logo-img');
    if (logoImg) {
        logoImg.addEventListener('error', function () {
            this.src = '/static/images/default/logo-placeholder.png';
        });
    }

    // 3. Tự động ẩn thông báo Flash sau 4 giây
    const flashMessages = document.querySelectorAll('.flash-item');
    if (flashMessages.length > 0) {
        setTimeout(function () {
            flashMessages.forEach(function (msg) {
                msg.style.transition = 'opacity 0.5s ease';
                msg.style.opacity = '0';
                setTimeout(function () {
                    msg.remove();
                }, 500);
            });
        }, 4000);
    }
});