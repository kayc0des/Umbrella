const primaryNav = document.querySelector('.primary-navigation');
const navToggle = document.querySelector('.mobile-nav-toggle');

navToggle.addEventListener('click', () => {
    const visibility = primaryNav.getAttribute('data-visible');

    if (visibility === "false") {
        primaryNav.setAttribute('data-visible', true);
        navToggle.setAttribute('aria-expanded', true);
    } else {
        primaryNav.setAttribute('data-visible', false);
        navToggle.setAttribute('aria-expanded', false);
    }
})

const sections = document.querySelectorAll('.section');
let currentSection = 0;

window.addEventListener('wheel', handleScroll);
window.addEventListener('keydown', handleKeyDown);

function handleScroll(e) {
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
    handleKeyDown(e); // Call handleKeyDown to handle keyboard input
}

function handleKeyDown(e) {
    if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
        // Scroll down
        if (currentSection < sections.length - 1) {
            currentSection++;
            scrollToSection(currentSection);
        }
    } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
        // Scroll up
        if (currentSection > 0) {
            currentSection--;
            scrollToSection(currentSection);
        }
    }
}

// function scrollToSection(sectionIndex) {
//     window.scrollTo({
//         top: sections[sectionIndex].offsetTop,
//         behavior: 'smooth'
//     });
// }