var clickMeButton = document.createElement('button');
clickMeButton.id = 'myButton';
var number = 0
clickMeButton.innerHTML = number;
document.body.appendChild(clickMeButton);
clickMeButton.addEventListener("click", function() {
    number += 1;
    clickMeButton.innerHTML = number;
});