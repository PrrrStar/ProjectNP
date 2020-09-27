$(function () {
  $('.naeggu__slider').slick({
    slide: 'div',		//슬라이드 되어야 할 태그 ex) div, li 
    infinite: false, 	//무한 반복 옵션	 
    slidesToShow: 3,		// 한 화면에 보여질 컨텐츠 개수
    slidesToScroll: 3,		//스크롤 한번에 움직일 컨텐츠 개수
    speed: 200,	 // 다음 버튼 누르고 다음 화면 뜨는데까지 걸리는 시간(ms)
    arrows: true, 		// 옆으로 이동하는 화살표 표시 여부
    dots: false, 		// 스크롤바 아래 점으로 페이지네이션 여부
    vertical: true,		// 세로 방향 슬라이드 옵션
    prevArrow: $('.naeggu__slider__prev'),		// 이전 화살표 모양 설정
    nextArrow: $('.naeggu__slider__next'),		// 다음 화살표 모양 설정
    // dotsClass : "slick-dots", 	//아래 나오는 페이지네이션(점) css class 지정
    draggable: false, 	//드래그 가능 여부

  });

  $(".naeggu__slider").on("afterChange", function (event, slick) {
    var text = parseInt(slick.currentSlide) / 3 + 1;
    text += ' / ';
    text += parseInt((slick.slideCount-1)/3) + 1;
    $(".naeggu__slider__count").text(text);
    
  });
})

const slideElements = document.querySelectorAll(".naeggu__list");

window.onload = function () {
  var addElement = (slideElements.length % 3 == 0)? 0: (3 - slideElements.length % 3);

  for (var i = 0; i < slideElements.length; i++) {
    slideElements[i].style.height = "120px";
    slideElements[i].style.marginBottom = "10px";
  }
  
  for(var i = 0; i < addElement; i++) {
    console.log(addElement);
    $('.naeggu__slider').slick('slickAdd','<div></div>');  
  }
};

if(slideElements.length > 3) {
  text = ' 1 / '
              + (parseInt((slideElements.length-1)/3) + 1);
  $(".naeggu__slider__count").text(text);
  $('.naeggu__slider').slick('slickAdd','<div>add</div>');
}

