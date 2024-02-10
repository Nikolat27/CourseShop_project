document.querySelectorAll('.section').forEach(section => {
    const title = section.querySelector('h2');
    title.addEventListener('click', () => {
        section.classList.toggle('active');
    });
});
