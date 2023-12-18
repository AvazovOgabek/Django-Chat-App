document.addEventListener('DOMContentLoaded', function() {
const expandableImages = document.querySelectorAll('.expandable-image');

expandableImages.forEach(function(image) {
    image.addEventListener('click', function() {
    const fullscreenDiv = document.createElement('div');
    fullscreenDiv.classList.add('fullscreen');

    const img = document.createElement('img');
    img.src = this.src;

    fullscreenDiv.appendChild(img);
    document.body.appendChild(fullscreenDiv);

    fullscreenDiv.addEventListener('click', function() {
        document.body.removeChild(fullscreenDiv);
    });
    });
});
});