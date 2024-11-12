// static/js/game_of_life.js

const canvas = document.getElementById('game-of-life-canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const resolution = 10;
const COLS = Math.floor(canvas.width / resolution);
const ROWS = Math.floor(canvas.height / resolution);

// Define color schemes
const colorSchemes = {
    scheme1: { alive: '#3498db', dead: '#ecf0f1' },
    scheme2: { alive: '#e74c3c', dead: '#2c3e50' },
    scheme3: { alive: '#2ecc71', dead: '#34495e' },
};

// Choose a color scheme
const colors = colorSchemes.scheme1;

function buildGrid() {
    return new Array(COLS).fill(null)
        .map(() => new Array(ROWS).fill(null)
        .map(() => Math.floor(Math.random() * 2)));
}

let grid = buildGrid();
let previousGrid = buildGrid();

function render(grid, previousGrid) {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas before rendering
    for (let col = 0; col < grid.length; col++) {
        for (let row = 0; row < grid[col].length; row++) {
            const cell = grid[col][row];
            const prevCell = previousGrid[col][row];
            ctx.beginPath();
            ctx.rect(col * resolution, row * resolution, resolution, resolution);
            if (cell !== prevCell) {
                ctx.fillStyle = cell ? colors.alive : colors.dead;
                ctx.globalAlpha = 0.5; // Adjust opacity for fade effect
            } else {
                ctx.fillStyle = cell ? colors.alive : colors.dead;
                ctx.globalAlpha = 1;
            }
            ctx.fill();
            ctx.stroke();
        }
    }
}

function nextGen(grid) {
    const nextGen = grid.map(arr => [...arr]);

    for (let col = 0; col < grid.length; col++) {
        for (let row = 0; row < grid[col].length; row++) {
            const cell = grid[col][row];
            let numNeighbors = 0;
            for (let i = -1; i < 2; i++) {
                for (let j = -1; j < 2; j++) {
                    if (i === 0 && j === 0) {
                        continue;
                    }
                    const x_cell = col + i;
                    const y_cell = row + j;

                    if (x_cell >= 0 && y_cell >= 0 && x_cell < COLS && y_cell < ROWS) {
                        const currentNeighbor = grid[col + i][row + j];
                        numNeighbors += currentNeighbor;
                    }
                }
            }

            // rules of life
            if (cell === 1 && numNeighbors < 2) {
                nextGen[col][row] = 0;
            } else if (cell === 1 && numNeighbors > 3) {
                nextGen[col][row] = 0;
            } else if (cell === 0 && numNeighbors === 3) {
                nextGen[col][row] = 1;
            }
        }
    }
    return nextGen;
}

function update() {
    previousGrid = grid.map(arr => [...arr]);
    grid = nextGen(grid);
    render(grid, previousGrid);
    setTimeout(update, 500); // Adjust the delay (in milliseconds) to control the speed
}

render(grid, previousGrid);
setTimeout(update, 500); // Adjust the delay (in milliseconds) to control the speed