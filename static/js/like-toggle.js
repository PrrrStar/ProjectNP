$("#btn-like").click(function (e) {
  e.preventDefault();
  var likeCount = $("#like-count");
  var likeURL = $(this).attr("data-url");
  var likeBtn = $("#btn-like");
  $.ajax({
    url: likeURL,
    method: "GET",
    data: {},
    success: function (data) {
      console.log(data);
      var newLikes;
      if (data.liked) {
        newLikes = parseInt(likeCount.text()) + 1;
        likeCount.text(newLikes);
        likeBtn.css("backgroundColor", "#fe4737");
      } else {
        newLikes = parseInt(likeCount.text()) - 1;
        likeCount.text(newLikes);
        likeBtn.css("backgroundColor", "#BBBBBB");
      }
    },
    error: function (error) {
      alert('내꺼하기 실패 ㅠ')
      console.log(error);
    },
  });
});

