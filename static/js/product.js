document.addEventListener('DOMContentLoaded', function () {
    const galleryItems = document.querySelectorAll('.gallery-item');
    const lightbox = document.getElementById('imageLightbox');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxCaption = document.getElementById('lightboxCaption');
    const lightboxClose = document.getElementById('lightboxClose');
    const lightboxPrev = document.getElementById('lightboxPrev');
    const lightboxNext = document.getElementById('lightboxNext');

    let currentIndex = 0;
    const imagesList = [];

    // Thu thập danh sách ảnh trong trang hiện tại
    galleryItems.forEach(function (item, index) {
        const imgUrl = item.getAttribute('data-image');
        const imgTitle = item.getAttribute('data-title') || '';
        imagesList.push({ url: imgUrl, title: imgTitle });

        // Sự kiện click mở Lightbox
        item.addEventListener('click', function () {
            openLightbox(index);
        });
    });

    function openLightbox(index) {
        if (imagesList.length === 0) return;
        currentIndex = index;
        updateLightboxContent();
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden'; // Khóa cuộn trang
    }

    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = 'auto'; // Mở lại cuộn trang
    }

    function updateLightboxContent() {
        const currentData = imagesList[currentIndex];
        lightboxImg.src = currentData.url;
        lightboxCaption.textContent = currentData.title;
    }

    function showPrevImage() {
        currentIndex = (currentIndex - 1 + imagesList.length) % imagesList.length;
        updateLightboxContent();
    }

    function showNextImage() {
        currentIndex = (currentIndex + 1) % imagesList.length;
        updateLightboxContent();
    }

    // Gắn sự kiện nút bấm Lightbox
    if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
    if (lightboxPrev) lightboxPrev.addEventListener('click', showPrevImage);
    if (lightboxNext) lightboxNext.addEventListener('click', showNextImage);

    // Đóng khi click ngoài vùng ảnh
    if (lightbox) {
        lightbox.addEventListener('click', function (e) {
            if (e.target === lightbox) {
                closeLightbox();
            }
        });
    }

    // Hỗ trợ phím mũi tên và ESC trên bàn phím
    document.addEventListener('keydown', function (e) {
        if (!lightbox || !lightbox.classList.contains('active')) return;

        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowLeft') showPrevImage();
        if (e.key === 'ArrowRight') showNextImage();
    });
});