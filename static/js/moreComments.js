var comments = document.querySelectorAll(".comments");
var showMore = document.querySelector(".comments__showMore");
var startNum = 3;

if (comments.length > 3) {
  for (i = 3; i < comments.length; i++) {
    comments[i].style.display = "none";
  }
}

if (comments.length <= 3) {
  showMore.style.display = "none";
}

function showMoreComments() {
  if (showMore.innerText == "접기"){
    for (i = 3; i < comments.length; i++) {
      comments[i].style.display = "none";
    }
  }
  
  if (comments.length - startNum > 3) {
    for (i = startNum; i < startNum + 3; i++) {
      comments[i].style.display = "flex";
    }
    startNum = startNum + 3;
  } else {
    for (i = startNum; i < comments.length; i++) {
      comments[i].style.display = "flex";
    }
    showMore.innerHTML="접기";
   // showMore.style.display = "none";
  }

}

showMore.addEventListener("click", showMoreComments);
