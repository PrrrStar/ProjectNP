var commentImage = document.querySelectorAll(".fake-image");
var layer = document.querySelector(".image-layer");

function enlargeImage(event) {
    if (event.target.getAttribute("enlarge") == "f") {
        event.target.style.position = "fixed";
        event.target.style.top = "50%";
        event.target.style.left = "50%";
        event.target.style.width = "500px"
        event.target.style.height = "500px"
        event.target.style.transform = "translateY(-50%)";
        event.target.style.margin = "0px 0px 0px -250px";
        event.target.style.zIndex = "10";
        layer.classList.add("blind");
        event.target.setAttribute("enlarge", "t");
    } else {
        event.target.style.position = "static";
        event.target.style.removeProperty('top');
        event.target.style.removeProperty('left');
        event.target.style.removeProperty('transform');
        event.target.style.removeProperty('margin');
        layer.classList.remove("blind");
        event.target.style.zIndex = "0";
        event.target.style.width = "100px";
        event.target.style.height = "100px";
        event.target.setAttribute("enlarge", "f");
    }
}

for (i = 0; i < commentImage.length; i++) {
    commentImage[i].addEventListener("click", enlargeImage);
}