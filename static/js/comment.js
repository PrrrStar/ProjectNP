$(function () {
  $("#btn-comment").click(function (e) {
    e.preventDefault();
    $("#comment-modal").modal("hide");
    var comment_form = $("#comment-form")[0];
    var comment_formData = new FormData(comment_form);

    var url = $("#comment-form").attr("action");
    var form = $("#comment-form").serialize();

    $.ajax({
      url: url,
      enctype: "multipart/form-data",
      method: "POST",
      data: comment_formData,
      async: true,
      processData: false,
      contentType: false,
      dataType: "json",
      success: function (response) {
        $(".comment__comments").html(response.form);
      },
      error: function (rs, e) {
        console.log(rs.responseText);
      },
    });
  });
});