
// Smooth scroll for all internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Fade-in animation on scroll
window.addEventListener('scroll', function () {
    let sections = document.querySelectorAll("section");
    sections.forEach(section => {
        let position = section.getBoundingClientRect().top;
        let screenPosition = window.innerHeight / 1.3;

        if (position < screenPosition) {
            section.style.opacity = "1";
            section.style.transform = "translateY(0px)";
        }
    });
});

// Initial hidden state for animation
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("section").forEach(section => {
        section.style.opacity = "0";
        section.style.transform = "translateY(40px)";
        section.style.transition = "all 0.6s ease";
    });
});
