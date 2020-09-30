//댓글 삭제 AJAX 요청
$(".comment_delete").click(function () {

  var message = confirm('댓글을 삭제하시겠어요?');
  var url = $(this).attr('data-url');
  var csrf = $('input[name=csrfmiddlewaretoken]').val();
  if (message == true) {
    current_comment = $(this).parents('.comments');
    $.ajax({
      type: "POST",
      url: url,
      data: {'csrfmiddlewaretoken': csrf}, 
      dataType: "json",
      success: function (response) { 
        current_comment.replaceWith('<div class="comments"><div class="comments__content">삭제된 댓글이에요</div></div>');
      },
      error: function (request, status, error) {
        alert("댓글 삭제 실패 ㅠ")
      },
    });
  }
})

//댓글 쓰기 눌렀을 때 모달 form 을 띄웁니다.
$(".comment_write").click(function(e){
  e.preventDefault();
  var url = $(this).attr('data-url');
  $("#comment-modal").modal("show");
  $("#comment-form").attr("action", url);
})

//댓글 쓰기 눌렀을 때 모달 form 을 띄웁니다.
$(".comment_update").click(function (e) {
  e.preventDefault();
  var message = confirm('댓글을 수정하시겠어요?');
  var url = $(this).attr('data-url');

  if (message == true) {
    $("#comment-modal").modal("show");
    $("#comment-form").attr("action", url);
  }
})

//댓글 Validation : 100자 제한
var commentAlert = (e) => {
  if (e.value.length > e.maxLength) {
      alert("100자 이상 작성하실 수 없습니다.");
  }
}