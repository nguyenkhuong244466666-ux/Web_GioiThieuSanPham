document.addEventListener('DOMContentLoaded', function () {


    // ==========================
    // MOBILE MENU
    // ==========================

    const mobileToggle = document.getElementById('mobileToggle');
    const mainNav = document.querySelector('.main-nav');


    if (mobileToggle && mainNav) {


        mobileToggle.addEventListener('click', function () {


            // mở / đóng menu
            mainNav.classList.toggle('active');


            // khóa / mở cuộn trang chính
            document.body.classList.toggle('menu-open');


        });


    }




    // ==========================
    // FLASH MESSAGE
    // ==========================


    const flashMessages = document.querySelectorAll('.flash-item');


    if (flashMessages.length > 0) {


        setTimeout(function () {


            flashMessages.forEach(function(msg){


                msg.style.transition='opacity 0.5s ease';

                msg.style.opacity='0';



                setTimeout(function(){

                    msg.remove();

                },500);



            });


        },4000);


    }


});