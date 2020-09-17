$(function(){
    // 회원가입, 로그인 창 닫기
    $('.btn-close').click(function(e){
        // 회원가입, 로그인 창 닫을 시 현재 화면으로 새로고침
        location.reload();
    });
    $('.btn-login').click(function(e){
        e.preventDefault();
        var url = $(this).attr('href');
        var form = $('#user-login')[0];
        var formData = new FormData(form);

        $.ajax({
            url : url,
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            cache: false,
            method : 'POST',
            data : formData,
        }).done(function(data){
            if(data.works){
                alert('로그인되었습니다.')
                location.reload();
            } else if(data.wrongInformation) {
                alert('입력된 정보와 일치하는 회원 정보가 없습니다.');
                $('#login-user-email').val("");
                $('#login-user-password').val("");

            } else if(data.noEmail) {
                alert('이메일 주소를 입력해주세요.');
                $('#login-user-password').val("");
            } else if(data.noPassword) {
                alert('비밀번호를 입력해주세요.');
            } else {
                alert('정상 요청이 아닙니다.');
            }
        });
    });
});