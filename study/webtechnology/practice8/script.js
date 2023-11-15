// Задача 1: Функции

function describeCountry(country, population, capital) {
    return `${country} has ${population} million people, and its capital is ${capital}`;
}

const result1 = describeCountry('Finland', 6, 'Helsinki');
const result2 = describeCountry('China', 1441, 'Beijing');
const result3 = describeCountry('USA', 331, 'Washington');

console.log(result1);
console.log(result2);
console.log(result3);

// Задача 2: Объявление и выражение функций

function percentageWorld(population) {
    return (population / 7900) * 100;
}

const perc1 = percentageWorld(1441);
const perc2 = percentageWorld(331);
const perc3 = percentageWorld(126);

console.log(perc1);
console.log(perc2);
console.log(perc3);

const percWorldExpr = function (population) {
    return (population / 7900) * 100;
};

const perc4 = percWorldExpr(1441);
const perc5 = percWorldExpr(331);
const perc6 = percWorldExpr(126);

console.log(perc4);
console.log(perc5);
console.log(perc6);

// Задача 3: Стрелочные функции

const percWorldArrow = population => (population / 7900) * 100;

const perc7 = percWorldArrow(1441);
const perc8 = percWorldArrow(331);
const perc9 = percWorldArrow(126);

console.log(perc7);
console.log(perc8);
console.log(perc9);

// Задача 4: Функции, вызывающие другие функции

function describePop(country, population) {
    const perc = percentageWorld(population);
    return `${country} has ${population} million people, about ${perc.toFixed(1)}% of the world.`;
}

const desc1 = describePop('China', 1441);
const desc2 = describePop('USA', 331);
const desc3 = describePop('India', 1393);

console.log(desc1);
console.log(desc2);
console.log(desc3);

// Задача 5: Функция для получения количества дней в году

function daysInYear(year) {
    return (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)) ? 366 : 365;
}

console.log(daysInYear(2021));
console.log(daysInYear(2022));

// Задача 6: Функции и стрелочные функции

const calcAvg = (score1, score2, score3) => (score1 + score2 + score3) / 3;

const avgYesylData1 = calcAvg(44, 23, 71);
const avgYertysData1 = calcAvg(65, 54, 49);

const avgYesylData2 = calcAvg(85, 54, 41);
const avgYertysData2 = calcAvg(23, 34, 27);

function checkWinner(avgYesyl, avgYertys) {
    if (avgYesyl >= 2 * avgYertys) {
        console.log(`Yesyl win (${avgYesyl} vs. ${avgYertys})`);
    } else if (avgYertys >= 2 * avgYesyl) {
        console.log(`Yertys win (${avgYertys} vs. ${avgYesyl})`);
    } else {
        console.log("No team wins!");
    }
}

checkWinner(avgYesylData1, avgYertysData1);
checkWinner(avgYesylData2, avgYertysData2);
