// Hero section background images
const heroImages = [
    {
        url: "img1.jpg",
        title: "Event Highlight 1",
        subtitle: "Memorable moments from our events"
    },
    {
        url: "img2.jpg",
        title: "Event Highlight 2",
        subtitle: "Celebrating culture and art"
    },
    {
        url: "img3.jpg",
        title: "Event Highlight 3",
        subtitle: "Joyful performances and gatherings"
    },
    {
        url: "img4.jpg",
        title: "Event Highlight 4",
        subtitle: "Tradition meets creativity"
    }
];

// Theme data
const themes = [
    {
        name: 'Sunset Vibes',
        class: 'theme-sunset'
    },
    {
        name: 'Ocean Dreams',
        class: 'theme-ocean'
    },
    {
        name: 'Forest Magic',
        class: 'theme-forest'
    },
    {
        name: 'Royal Purple',
        class: 'theme-royal'
    },
    {
        name: 'Rose Gold',
        class: 'theme-rose'
    }
];

let currentImageIndex = 0;
let currentTheme = 0;

// Mobile menu functionality
document.addEventListener('DOMContentLoaded', function () {
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuLinks = mobileMenu ? mobileMenu.querySelectorAll('a') : [];
    const closeButton = mobileMenu ? mobileMenu.querySelector('.mobile-menu-close') : null;
    let isAnimating = false;

    if (mobileMenuButton && mobileMenu) {
        // Mark active link based on path
        try {
            const current = window.location.pathname.replace(/\\/g, '/');
            menuLinks.forEach(a => {
                const href = a.getAttribute('href');
                if (!href) return;
                // Normalize relative paths
                if (current.endsWith(href) || current.includes(href)) {
                    a.classList.add('active-link');
                }
            });
        } catch (_) { }
        const toggleMenu = (open) => {
            if (open) {
                mobileMenu.classList.add('show');
                mobileMenuButton.setAttribute('aria-expanded', 'true');
                document.body.classList.add('menu-open');
                // Reset link animation baseline
                menuLinks.forEach(link => {
                    link.style.opacity = '0';
                    link.style.transform = 'translateX(100px)';
                });
            } else {
                menuLinks.forEach(link => {
                    link.style.opacity = '0';
                    link.style.transform = 'translateX(100px)';
                });
                setTimeout(() => {
                    mobileMenu.classList.remove('show');
                    mobileMenuButton.setAttribute('aria-expanded', 'false');
                    document.body.classList.remove('menu-open');
                }, 300);
            }
        };

        mobileMenuButton.addEventListener('click', function (e) {
            e.stopPropagation();
            if (isAnimating) return;
            isAnimating = true;
            const opening = !mobileMenu.classList.contains('show');
            toggleMenu(opening);
            setTimeout(() => { isAnimating = false; }, opening ? 800 : 350);
        });

        // Close button click
        if (closeButton) {
            closeButton.addEventListener('click', function (e) {
                e.stopPropagation();
                if (mobileMenu.classList.contains('show')) {
                    toggleMenu(false);
                    mobileMenuButton.focus();
                }
            });
        }

        // Close on outside click
        document.addEventListener('click', function (event) {
            if (mobileMenu.classList.contains('show') &&
                !event.target.closest('.mobile-menu') &&
                !event.target.closest('.mobile-menu-button')) {
                toggleMenu(false);
            }
        });

        // Close on Escape key
        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape' && mobileMenu.classList.contains('show')) {
                toggleMenu(false);
                mobileMenuButton.focus();
            }
        });
    }
});
const eventDate = new Date('2025-10-15T18:00:00');

// Initialize the hero section
function initHero() {
    setupBackgroundImages();
    setupImageDots();
    setupParticles();
    setupCountdown();
    setupThemeRotation();
    updateCurrentYear();
}

// Setup background images
function setupBackgroundImages() {
    const container = document.getElementById('hero-backgrounds');
    heroImages.forEach((image, index) => {
        const div = document.createElement('div');
        div.className = `absolute inset-0 transition-opacity duration-1000 ${index === 0 ? 'opacity-100' : 'opacity-0'}`;
        div.innerHTML = `
            <div class="absolute inset-0 bg-cover bg-center bg-no-repeat" style="background-image: url(${image.url}?w=1920&h=1080&fit=crop)"></div>
            <div class="absolute inset-0 bg-black/50"></div>
        `;
        container.appendChild(div);
    });

    // Auto-rotate images
    setInterval(() => {
        rotateImages();
    }, 4000);
}

// Rotate background images
function rotateImages() {
    const images = document.querySelectorAll('#hero-backgrounds > div');
    currentImageIndex = (currentImageIndex + 1) % images.length;

    images.forEach((img, index) => {
        img.style.opacity = index === currentImageIndex ? '1' : '0';
    });

    // Update image dots
    updateImageDots();
}

// Setup image navigation dots
function setupImageDots() {
    const dotsContainer = document.getElementById('image-dots');
    heroImages.forEach((_, index) => {
        const dot = document.createElement('button');
        dot.className = `image-dot ${index === 0 ? 'active' : ''}`;
        dot.onclick = () => {
            currentImageIndex = index;
            updateBackgroundImage();
            updateImageDots();
        };
        dotsContainer.appendChild(dot);
    });
}

// Update image dots
function updateImageDots() {
    const dots = document.querySelectorAll('.image-dot');
    dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentImageIndex);
    });
}

// Update background image
function updateBackgroundImage() {
    const images = document.querySelectorAll('#hero-backgrounds > div');
    images.forEach((img, index) => {
        img.style.opacity = index === currentImageIndex ? '1' : '0';
    });
}

// Setup animated particles
function setupParticles() {
    const container = document.getElementById('particles');
    if (!container) return;
    for (let i = 0; i < 30; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.top = `${Math.random() * 100}%`;
        particle.style.width = particle.style.height = `${Math.random() * 3 + 2}px`;
        particle.style.animationDelay = `${Math.random() * 2}s`;
        particle.style.animationDuration = `${3 + Math.random() * 2}s`;
        container.appendChild(particle);
    }
}

// Setup countdown timer
function setupCountdown() {
    const countdownContainer = document.getElementById('countdown');
    if (!countdownContainer) return;
    const items = [
        { label: 'Days', icon: 'fa-calendar' },
        { label: 'Hours', icon: 'fa-clock' },
        { label: 'Minutes', icon: 'fa-bolt' },
        { label: 'Seconds', icon: 'fa-sparkles' }
    ];

    items.forEach(item => {
        const div = document.createElement('div');
        div.className = `countdown-card backdrop-blur-lg border-white/20 p-2 sm:p-3 text-center transform hover:scale-105 transition-all duration-300 rounded-lg`;
        div.innerHTML = `
            <div class="flex flex-col items-center">
                <i class="fas ${item.icon} countdown-icon w-4 h-4 sm:w-5 sm:h-5 mb-1"></i>
                <div class="text-xl sm:text-2xl md:text-3xl font-bold text-white mb-1 animate-pulse" data-countdown="${item.label.toLowerCase()}">00</div>
                <div class="text-xs text-white/70 uppercase tracking-wide">${item.label}</div>
            </div>
        `;
        countdownContainer.appendChild(div);
    });

    updateCountdown();
    setInterval(updateCountdown, 1000);
}

// Update countdown values
function updateCountdown() {
    const now = new Date().getTime();
    const distance = eventDate.getTime() - now;

    if (distance > 0) {
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        const daysEl = document.querySelector('[data-countdown="days"]');
        const hoursEl = document.querySelector('[data-countdown="hours"]');
        const minutesEl = document.querySelector('[data-countdown="minutes"]');
        const secondsEl = document.querySelector('[data-countdown="seconds"]');
        if (daysEl) daysEl.textContent = String(days).padStart(2, '0');
        if (hoursEl) hoursEl.textContent = String(hours).padStart(2, '0');
        if (minutesEl) minutesEl.textContent = String(minutes).padStart(2, '0');
        if (secondsEl) secondsEl.textContent = String(seconds).padStart(2, '0');
    }
}

// Setup theme rotation
function setupThemeRotation() {
    const countdown = document.getElementById('countdown');
    if (!countdown) return;
    countdown.className += ` ${themes[0].class}`;

    setInterval(() => {
        currentTheme = (currentTheme + 1) % themes.length;
        countdown.className = countdown.className.replace(/theme-\w+/, themes[currentTheme].class);
    }, 60000);
}

// Update copyright year
function updateCurrentYear() {
    const yearElement = document.getElementById('current-year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
}

// Initialize everything when the page loads
document.addEventListener('DOMContentLoaded', function () {
    if (document.getElementById('hero-backgrounds')) {
        initHero();
    }
});

