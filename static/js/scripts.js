/*
* Start Bootstrap - Landing Page v6.0.5 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

//ログインアラート
function Login_alert() {
  alert("ログインしてください。")
}

  function dragstart_handler(ev) {
    // Add the target element's id to the data transfer object
    ev.dataTransfer.setData("text/plain", ev.target.id);
  }

  window.addEventListener("DOMContentLoaded", () => {
    // Get the element by id
    const element = document.getElementById("saf");
    // Add the ondragstart event listener
    element.addEventListener("dragstart", dragstart_handler);
  });

  function dragover_handler(ev) {
    ev.preventDefault();
    ev.dataTransfer.dropEffect = "move";
  }
  function drop_handler(ev) {
    ev.preventDefault();
    // 移動された要素のidを取得して、その要素をtargetのDOMに追加する
    const data = ev.dataTransfer.getData("text/plain");
    ev.target.appendChild(document.getElementById("saf"));
  }
