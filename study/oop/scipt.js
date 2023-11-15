const Person  = function (firsname, birthYear) {
    this.firstname = firsname;
    this.birthYear = birthYear;
};

const samel = new Person('sanuel', 1989);
console.log(samel);