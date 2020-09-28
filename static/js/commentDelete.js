$(".comment_delete").click(function () {

  var delete_warning = confirm('댓글을 삭제하시겠습니까?');
  var url = $(this).parents('.comment__editForm').attr('action');
  var csrf = $('input[name=csrfmiddlewaretoken]').val();
  if (delete_warning == true) {
    current_comment = $(this).parents('.comments');
    console.log(current_comment)
    $.ajax({ // ajax로 서버와 통신
      type: "POST", // 데이터를 전송하는 방법
      url: url, // 통신할 url을 지정
      data: {'csrfmiddlewaretoken': csrf}, // 서버로 데이터 전송시 옵션
      dataType: "json",
      success: function (response) { // 성공
        current_comment.replaceWith('<div class="comments"><div class="comments__content">삭제된 댓글이에요</div></div>');
      },
      error: function (request, status, error) { // 실패
        alert("댓글 삭제 실패 ㅠ")
  //      window.location.replace("/") // 로그인 페이지로 넘어가기
      },
    });
  }
})