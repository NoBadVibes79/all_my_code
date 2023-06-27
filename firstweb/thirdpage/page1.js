var nextPageBtn = document.getElementById("npage1"); // находим кнопку по id

nextPageBtn.addEventListener("click", function() { // добавляем обработчик события
  window.location.href = "../index.php"; // переходим на следующую страницу
});