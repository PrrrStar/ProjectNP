// slick.js
$(".products__slider").slick({
    slidesToShow: 4,
    slidesToScroll: 4,
});

const slideElements = document.querySelectorAll(".slick-slide");

// slider 요소의 인라인 width 값을 조정
window.onload = function () {
    for (var i = 0; i < slideElements.length; i++) {
        slideElements[i].style.width = "250px";
    }
}