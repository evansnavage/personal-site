document.addEventListener('scroll', function() {
    const scrollPosition = window.pageYOffset;
    document.body.style.backgroundPositionY = `${-scrollPosition * 0.2}px`; // Adjust 0.2 for desired parallax speed
});