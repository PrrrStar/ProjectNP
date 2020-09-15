var parent = document.querySelector('.current__parent');
parent.style.backgroundColor = "lavender";
var child = document.querySelector('.current__category')
child.style.backgroundColor = "LightBlue"
for (var i = 0; i < children.length; i++) {
  for (var i = 0; i < children.length; i++) {
    if (parent.getAttribute("value") == children[i].getAttribute("value")) {
      children[i].style.display = "flex";
    }
  }
  parent.setAttribute("drop", "t");
}