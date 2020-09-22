const parents = document.querySelectorAll(".category__parent");
const children = document.querySelectorAll(".category__children");

function dropUD(event) {
  name = event.target.getAttribute("value");
  if (event.target.getAttribute("drop") == "f") {
    for (var i = 0; i < children.length; i++) {
      if (name == children[i].getAttribute("value")) {
        children[i].style.display = "flex";
      }
    }
    event.target.setAttribute("drop", "t")
  }
  else {
    for (var i = 0; i < children.length; i++) {
      if (name == children[i].getAttribute("value")) {
        children[i].style.display = "none";
      }
    }
    event.target.setAttribute("drop", "f")
  }
}

for (var i = 0; i < parents.length; i++) {
  parents[i].addEventListener("click", dropUD);
}