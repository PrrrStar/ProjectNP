$(function () {
  // 회원가입, 로그인 창 닫기
  $(".btn-close").click(function (e) {
    // 회원가입, 로그인 창 닫을 시 현재 화면으로 새로고침
    location.reload();
  });
  $("#btn-login").click(function (e) {
    e.preventDefault();
    var url = $(this).attr("href");
    var form = $("#user-login")[0];

    var formData = new FormData(form);
    $.ajax({
      url: url,
      enctype: "multipart/form-data",
      processData: false,
      contentType: false,
      cache: false,
      method: "POST",
      data: formData,
    }).done(function (data) {
      if (data.works) {
        alert("내편이군요 환영합니다!");
        location.reload();
      } else if (data.wrongInformation) {
        alert("당신은 내편이 아닙니다.");
        $("#login-user-email").val("");
        $("#login-user-password").val("");
      } else if (data.noEmail) {
        alert("이메일 주소를 입력해주세요.");
        $("#login-user-password").val("");
      } else if (data.noPassword) {
        alert("비밀번호를 입력해주세요.");
      } else {
        alert("정상 요청이 아닙니다.");
      }
    });
  });
});

const loginForm = document.getElementById("user-login");
const loginBtn = document.getElementById("btn-login");

function login(event) {
  const keyCode = event.keyCode;

  if (keyCode == 13) {
    loginBtn.click();
  }
}

loginForm.addEventListener("keydown", login);
