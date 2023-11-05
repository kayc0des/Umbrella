const sections = document.querySelectorAll('.section');
let currentSection = 0;

window.addEventListener('wheel', (e) => {
    if (e.deltaY > 0) {
        // Scrolling down
        if (currentSection < sections.length - 1) {
            currentSection++;
        }
    } else {
        // Scrolling up
        if (currentSection > 0) {
            currentSection--;
        }
    }

    scrollToSection(currentSection);
});

function scrollToSection(sectionIndex) {
    window.scrollTo({
        top: sections[sectionIndex].offsetTop,
        behavior: 'smooth'
    });
}