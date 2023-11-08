var userInput = prompt("Введите число:"); // Пользователь вводит число

// Преобразуем введенную строку в число (если возможно)
var number = parseInt(userInput);

if (!isNaN(number)) {
    if (number % 2 === 0) {
        console.log("Четное");
    } else {
        console.log("Нечетное");
    }
} else {
    console.log("Вы ввели не число или ничего не ввели.");
}
