
$('.user-logout').click(function(e){
    e.preventDefault();
    var url = $(this).attr('href');
    var check = confirm('로그아웃 하시겠습니까?');
    if(check==true){
        $.ajax({
            url : url,
            method : "POST",
        }).done(function(data){
            if(data.works){
                alert('로그아웃 되었습니다.');
                location.reload();
            } else {
                alert('정상 요청이 아닙니다.');
            }
        });
    } else {
        location.reload();
    }
});
