var parent = document.querySelector('.current__parent');
var child = document.querySelector('.current__category')
parent.style.backgroundColor = "lavender";
child.style.backgroundColor = "LightBlue"
for (var i = 0; i < children.length; i++) {
  for (var i = 0; i < children.length; i++) {
    if (parent.getAttribute("value") == children[i].getAttribute("value")) {
      children[i].style.display = "flex";
    }
  }
  parent.setAttribute("drop", "t");
}