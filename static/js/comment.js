
$("#btn-comment").click(function (e) {
  e.preventDefault();
  $("#comment-modal").modal("hide");
  var comment_form = $("#comment-form")[0];
  var comment_formData = new FormData(comment_form);
  var url = $("#comment-form").attr("action");

  $.ajax({
    url: url,
    enctype: "multipart/form-data",
    type: "POST",
    data: comment_formData,
    async: true,
    processData: false,
    contentType: false,
    dataType: "json",
    success: function (response) {
      $(".detail__comment").html(response.form);
      $("#comment-form").attr("action", "");
      $("#id_content").val("");
      
    },
    error: function (rs, e) {
      console.log(rs.responseText);
    },
  });
});