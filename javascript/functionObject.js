function Rectangle(a, b) {
    this.length = a;
    this.width = b;
    this.perimeter = (a + b) * 2;
    this.area = a * b;
}

const rec = new Rectangle(4, 9);

console.log(rec.length);
console.log(rec.width);
console.log(rec.perimeter);
console.log(rec.area);