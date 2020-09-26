$(function(){
    $('.naeggu__slider').slick({
      slide: 'div',		//슬라이드 되어야 할 태그 ex) div, li 
				infinite : false, 	//무한 반복 옵션	 
				slidesToShow : 3,		// 한 화면에 보여질 컨텐츠 개수
				slidesToScroll : 3,		//스크롤 한번에 움직일 컨텐츠 개수
				speed : 200,	 // 다음 버튼 누르고 다음 화면 뜨는데까지 걸리는 시간(ms)
				arrows : true, 		// 옆으로 이동하는 화살표 표시 여부
				dots : false, 		// 스크롤바 아래 점으로 페이지네이션 여부
				vertical : true,		// 세로 방향 슬라이드 옵션
				prevArrow : $('.naeggu__slider__prev'),		// 이전 화살표 모양 설정
				nextArrow : $('.naeggu__slider__next'),		// 다음 화살표 모양 설정
				// dotsClass : "slick-dots", 	//아래 나오는 페이지네이션(점) css class 지정
				draggable : false, 	//드래그 가능 여부
				
    });

    // $(".naeggu__slider").on("init", function(event, slick, currentSlider){
    //     $(".naeggu__slider__count").text(parseInt(slick.currentSlide + 1) + ' / ' + slick.slideCount);
    // });
    // 처음 로드시 페이지 카운트 표시가 되지 않아 1 / {{user.product_likes.all|length}} 로 표시했습니다. 

    $(".naeggu__slider").on("afterChange", function(event, slick, currentSlide){
        $(".naeggu__slider__count").text(parseInt(slick.currentSlide + 1) + ' / ' + slick.slideCount);
    });
  })
  const slideElements = document.querySelectorAll(".naeggu__list");

  window.onload = function () {
  for (var i = 0; i < slideElements.length; i++) {
    slideElements[i].style.height = "120px";
    slideElements[i].style.marginBottom = "10px";
  }
};
