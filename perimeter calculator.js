
let shape = prompt("Enter shape (circle, triangle, square, rectangle, parallelogram):");

shape = shape.toLowerCase();

let perimeter;

switch(shape) {

    case "circle":
        let radius = parseFloat(prompt("Enter radius:"));
        perimeter = 2 * Math.PI * radius;
        break;

    case "triangle":
        let a = parseFloat(prompt("Enter side a:"));
        let b = parseFloat(prompt("Enter side b:"));
        let c = parseFloat(prompt("Enter side c:"));
        perimeter = a + b + c;
        break;

    case "square":
        let side = parseFloat(prompt("Enter side length:"));
        perimeter = 4 * side;
        break;

    case "rectangle":
        let length = parseFloat(prompt("Enter length:"));
        let width = parseFloat(prompt("Enter width:"));
        perimeter = 2 * (length + width);
        break;

    case "parallelogram":
        let base = parseFloat(prompt("Enter base:"));
        let sideP = parseFloat(prompt("Enter side:"));
        perimeter = 2 * (base + sideP);
        break;

    default:
        alert("Invalid shape!");
        perimeter = null;
}

if (perimeter !== null) {
    alert("The perimeter is: " + perimeter);
}