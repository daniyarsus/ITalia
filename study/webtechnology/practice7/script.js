// Task 16
let x = prompt();

switch (~~(x / 10)) {
    case 2:
        document.write("20");
        break;
    case 3:
        document.write("30");
        break;
    case 4:
        document.write("40");
        break;
    case 5:
        document.write("50");
        break;
    case 6:
        document.write("60");
        break;
}

switch (x % 10) {
    case 0:
        document.write(" лет");
        break;
    case 1:
        document.write(" 1 год");
        break;
    case 2:
        document.write(" 2 года");
        break;
    case 3:
        document.write(" 3 года");
        break;
    case 4:
        document.write(" 4 года");
        break;
    case 5:
        document.write(" 5 лет");
        break;
    case 6:
        document.write(" 6 лет");
        break;
    case 7:
        document.write(" 7 лет");
        break;
    case 8:
        document.write(" 8 лет");
        break;
    case 9:
        document.write(" 9 лет");
        break;
}