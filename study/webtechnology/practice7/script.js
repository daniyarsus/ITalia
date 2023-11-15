// Task 26
var x = prompt();

if (x <= 0) {
    x = -x;
} else if (x > 0 && x < 2) {
    x = x * x;
} else {
    x = 4;
}

document.write(x);

// Task 27
var x = prompt();

if (x < 0) {
    x = 0;
} else if (x % 2 === 0) {
    x = 1;
} else {
    x = -1;
}

document.write(x);

// Task 28
var x = prompt();

if (x % 4 === 0 && x % 100 === 0 && x % 400 !== 0) {
    document.write(x + " високосный");
} else {
    document.write(x + " не високосный");
}

// Task 29
var x = prompt();

if (x < 0 && x % 2 === 0) {
    document.write("отрицательное четное число");
} else if (x > 0 && x % 2 === 0) {
    document.write("положительное четное число");
} else if (x < 0 && x % 2 !== 0) {
    document.write("отрицательное нечетное число");
} else if (x > 0 && x % 2 !== 0) {
    document.write("положительное нечетное число");
} else {
    document.write("нулевое число");
}

// Task 30
var x = prompt();

if (~~(x / 100) !== 0 && x % 2 === 0) {
    document.write("трехзначное четное число");
} else if (~~(x / 100) !== 0 && x % 2 !== 0) {
    document.write("трехзначное нечетное число");
} else if (~~(x / 10) !== 0 && x % 2 === 0) {
    document.write("двухзначное четное число");
} else if (~~(x / 10) !== 0 && x % 2 !== 0) {
    document.write("двухзначное нечетное число");
} else if (x % 2 === 0) {
    document.write("однозначное четное число");
} else if (x % 2 !== 0) {
    document.write("однозначное нечетное число");
}


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

// Task 17
let x = prompt();
let ii = "учебных заданий";

switch (parseInt(x)) {
    case 11:
        document.write("11 " + ii);
        break;
    case 12:
        document.write("12 " + ii);
        break;
    case 13:
        document.write("13 " + ii);
        break;
    case 14:
        document.write("14 " + ii);
        break;
    case 15:
        document.write("15 " + ii);
        break;
    case 16:
        document.write("16 " + ii);
        break;
    case 17:
        document.write("17 " + ii);
        break;
    case 18:
        document.write("18 " + ii);
        break;
    case 19:
        document.write("19 " + ii);
        break;
    default:
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
        }

        switch (x % 10) {
            case 0:
                document.write(" учебных заданий");
                break;
            case 1:
                document.write(" 1 ");
                break;
            case 2:
                document.write(" 2 ");
                break;
            case 3:
                document.write(" 3 ");
                break;
            case 4:
                document.write(" 4 ");
                break;
            case 5:
                document.write(" 5 ");
                break;
            case 6:
                document.write(" 6 ");
                break;
            case 7:
                document.write(" 7 ");
                break;
            case 8:
                document.write(" 8 ");
                break;
            case 9:
                document.write(" 9 ");
                break;
        }

        switch (x % 10) {
            case 5:
            case 6:
            case 7:
            case 8:
            case 9:
                document.write(ii);
                break;
            case 1:
                document.write("учебное задание");
                break;
            case 2:
            case 3:
            case 4:
                document.write("учебных задания");
                break;
        }
}

// Task 18
let x = prompt();

let description = "";

switch (~~(x / 100)) {
    case 1:
        description += "100 ";
        break;
    case 2:
        description += "200 ";
        break;
    case 3:
        description += "300 ";
        break;
    case 4:
        description += "400 ";
        break;
    case 5:
        description += "500 ";
        break;
    case 6:
        description += "600 ";
        break;
    case 7:
        description += "700 ";
        break;
    case 8:
        description += "800 ";
        break;
    case 9:
        description += "900 ";
        break;
}

switch (x % 100) {
    case 10:
        description += "10";
        break;
    case 11:
        description += "11";
        break;
    case 12:
        description += "12";
        break;
    case 13:
        description += "13";
        break;
    case 14:
        description += "14";
        break;
    case 15:
        description += "15";
        break;
    case 16:
        description += "16";
        break;
    case 17:
        description += "17";
        break;
    case 18:
        description += "18";
        break;
    case 19:
        description += "19";
        break;
    default:
        switch (~~((x % 100) / 10)) {
            case 2:
                description += "20 ";
                break;
            case 3:
                description += "30 ";
                break;
            case 4:
                description += "40 ";
                break;
            case 5:
                description += "50 ";
                break;
            case 6:
                description += "60 ";
                break;
            case 7:
                description += "70 ";
                break;
            case 8:
                description += "80 ";
                break;
            case 9:
                description += "90 ";
                break;
        }

        switch (x % 10) {
            case 1:
                description += "1";
                break;
            case 2:
                description += "2";
                break;
            case 3:
                description += "3";
                break;
            case 4:
                description += "4";
                break;
            case 5:
                description += "5";
                break;
            case 6:
                description += "6";
                break;
            case 7:
                description += "7";
                break;
            case 8:
                description += "8";
                break;
            case 9:
                description += "9";
                break;
        }
}

document.write(description);

// Task 19
let year = prompt();

const yearDiff = year - 1984;
const num_year_in_cycle = yearDiff % 60;

let color, animal;

switch (~~(num_year_in_cycle / 12)) {
    case 0:
        color = "зеленой";
        break;
    case 1:
        color = "красной";
        break;
    case 2:
        color = "желтой";
        break;
    case 3:
        color = "белой";
        break;
    case 4:
        color = "черной";
        break;
}

// Determine the animal
switch (num_year_in_cycle % 12) {
    case 0:
        animal = "крысы";
        break;
    case 1:
        animal = "коровы";
        break;
    case 2:
        animal = "тигра";
        break;
    case 3:
        animal = "зайца";
        break;
    case 4:
        animal = "дракона";
        break;
    case 5:
        animal = "змеи";
        break;
    case 6:
        animal = "лошади";
        break;
    case 7:
        animal = "овцы";
        break;
    case 8:
        animal = "обезьяны";
        break;
    case 9:
        animal = "курицы";
        break;
    case 10:
        animal = "собаки";
        break;
    case 11:
        animal = "свиньи";
        break;
}

document.write("год " + color + " " + animal);

// Task 20
let D = prompt();
let M = prompt();

let ans;

switch (parseInt(M)) {
    case 1:
        if (D >= 20) {
            ans = "Водолей";
        } else {
            ans = "Козерог";
        }
        break;
    case 2:
        if (D <= 18) {
            ans = "Водолей";
        } else {
            ans = "Рыбы";
        }
        break;
    case 3:
        if (D <= 20) {
            ans = "Рыбы";
        } else {
            ans = "Овен";
        }
        break;
    case 4:
        if (D <= 19) {
            ans = "Овен";
        } else {
            ans = "Телец";
        }
        break;
    case 5:
        if (D <= 20) {
            ans = "Телец";
        } else {
            ans = "Близнецы";
        }
        break;
    case 6:
        if (D <= 21) {
            ans = "Близнецы";
        } else {
            ans = "Рак";
        }
        break;
    case 7:
        if (D <= 22) {
            ans = "Рак";
        } else {
            ans = "Лев";
        }
        break;
    case 8:
        if (D <= 22) {
            ans = "Лев";
        } else {
            ans = "Дева";
        }
        break;
    case 9:
        if (D <= 22) {
            ans = "Дева";
        } else {
            ans = "Весы";
        }
        break;
    case 10:
        if (D <= 22) {
            ans = "Весы";
        } else {
            ans = "Скорпион";
        }
        break;
    case 11:
        if (D <= 22) {
            ans = "Скорпион";
        } else {
            ans = "Стрелец";
        }
        break;
    case 12:
        if (D <= 21) {
            ans = "Стрелец";
        } else {
            ans = "Козерог";
        }
        break;
}

document.write(ans);

// Task 36
let N = prompt();
let K = prompt();

let ans = 0;

for (let i = 1; i <= N; i++){
    ans += i ** K;
}

document.write(ans);

// Task 37
let N = prompt();

let ans = 0;

for (let i = 1; i <= N; i++){
    ans += i ** i;
}

document.write(ans);

// Task 38
let N = prompt();

let ans = 0;

for (let i = 0; i < N; i++){
    ans += (i + 1) ** (N - i);
}

document.write(ans);

// Task 39
let A = prompt();
let B = prompt();

for (let i = parseInt(A); i <= parseInt(B); i++){
    for (let j = 0; j < i; j++){
        document.write(i + " ");
    }
    document.write("<br>");
}

// Task 40
let A = prompt();
let B = prompt();

for (let i = parseInt(A), k = 0; i <= parseInt(B); i++, k++){
        for (let j = 0; j <= k; j++){
            document.write(i + " ");
        }
        document.write("<br>");
    }

// while 26
let N = prompt();

let ans = 2;

let F1 = 1, F2 = 1;

while (F2 != parseInt(N)) {
    let F3 = F2;
    F2 = F1 + F2;
    F1 = F3;

    ans++;
}

document.write(F1 + " " + (F1 + F2));


// while 27
let N = prompt();

let ans = 2;

let F1 = 1, F2 = 1;

while (F2 != parseInt(N)) {
    let F3 = F2;
    F2 = F1 + F2;
    F1 = F3;

    ans++;
}

document.write(ans);

// while 28
let E = prompt();

let A1 = 2
let A2 = 2 + (1 / A1);

let K = 2;

while (Math.abs(A2 - A1) >= E){
    A1 = A2;
    A2 = 2 + (1 / A1);
    K++;
}

document.write(K + " " + A1 + " " + A2)

// while 29
let E = prompt();

let A1 = 1;
let A2 = 2;

let K = 2;

while (Math.abs(A2 - A1) >= E){
    let A = A2;
    A2 = (A1 + 2 * A2) / 3;
    A1 = A;
    K++;
}

document.write(K + " " + A1 + " " + A2)

// while 30
let A = prompt();
let B = prompt();
let C = prompt();

let ans = 0;

while (A - C >= 0){
    A -= C;

    let k = B;
    while (k - C >= 0){
        k -= C;
        ans++;
    }
}

document.write(ans);