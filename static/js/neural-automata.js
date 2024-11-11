// static/js/neural-automata.js
const canvas = document.getElementById('neural-automata-canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    // Add your neural automata drawing logic here
    requestAnimationFrame(draw);
}

draw();