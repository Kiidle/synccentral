function toggleProfileMenu() {
  var menu = document.getElementById("profileMenu");
  if (menu.classList.contains("show")) {
    menu.classList.remove("show");
  } else {
    menu.classList.add("show");
  }
}
window.onclick = function (event) {
  if (!event.target.matches(".pb img")) {
    var menus = document.getElementsByClassName("menu");
    for (var i = 0; i < menus.length; i++) {
      menus[i].classList.remove("show");
    }
  }
};
