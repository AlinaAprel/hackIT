const canvas = document.getElementById('paintCanvas');
const ctx = canvas.getContext('2d');
const pencilButton = document.getElementById('pencil');
const eraserButton = document.getElementById('eraser');
const colorPicker = document.getElementById('colorPicker');
const brushSize = document.getElementById('brushSize');
const brushSizeValue = document.getElementById('brushSizeValue');

let isDrawing = false;
let currentTool = 'pencil';
let currentColor = '#000000';
let currentSize = 5;

canvas.width = window.innerWidth * 0.8;
canvas.height = window.innerHeight * 0.8;

function startDrawing(e) {
    isDrawing = true;
    draw(e);
}

function stopDrawing() {
    isDrawing = false;
    ctx.beginPath();
}

function draw(e) {
    if (!isDrawing) return;

    ctx.lineWidth = currentSize;
    ctx.lineCap = 'round';

    if (currentTool === 'eraser') {
        ctx.strokeStyle = '#ffffff';
    } else {
        ctx.strokeStyle = currentColor;
    }

    ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
}

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mousemove', draw);

pencilButton.addEventListener('click', () => {
    currentTool = 'pencil';
});

eraserButton.addEventListener('click', () => {
    currentTool = 'eraser';
});

colorPicker.addEventListener('input', (e) => {
    currentColor = e.target.value;
});

brushSize.addEventListener('input', (e) => {
    currentSize = e.target.value;
    brushSizeValue.textContent = currentSize;
});