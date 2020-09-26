$(function () {
  $("#comment-form").submit(function (e) {
    e.preventDefault();
    $("#comment-modal").modal("hide");
    var url = $(this).attr("action");
    var form = $(this).serialize();
    $.ajax({
      url: url,
      enctype: "multipart/form-data",
      method: "POST",
      data: form,
      processData: false,
      contentType: false,
      dataType: "json",
      success: function(response){
        $('#id_content').val("");
        $("#id_img").val("");
        $(".comment__comments").html(response['form']);
      },
      
      error: function(rs, e){
        console.log(rs.responseText);
      },
    });
  });
});
