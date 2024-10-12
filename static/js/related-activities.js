// Optional JavaScript for sliding effect
document.querySelector('.related-activities-slider').addEventListener('wheel', (evt) => {
    evt.preventDefault();
    document.querySelector('.related-activities-slider').scrollBy({
        left: evt.deltaY < 0 ? -300 : 300
    });
});
