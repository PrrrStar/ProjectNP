

$("#btn-like").click(function(e){
    e.preventDefault();
    var likeCount =$('#like-count')
    var likeURL = $(this).attr('data-url');
    $.ajax({
      url:likeURL,
      method:"GET",
      data:{},
      success:function(data){
        console.log(data);
        var newLikes;
        if (data.liked){
            newLikes = parseInt(likeCount.text()) + 1
            likeCount.text(newLikes)
        }else{
            newLikes = parseInt(likeCount.text()) -1
            likeCount.text(newLikes)
        }
      }, error:function(error){
        console.log(error);
        console.log("error");
      }
    })
})

