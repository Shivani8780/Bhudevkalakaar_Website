// Toggle mobile menu for Info Page (copied from Contact Page)
document.addEventListener('DOMContentLoaded', function() {
    var menuButton = document.querySelector('.mobile-menu-button');
    var mobileMenu = document.getElementById('mobile-menu');
    var closeButton = document.querySelector('.mobile-menu-close');

    if (menuButton && mobileMenu) {
        menuButton.addEventListener('click', function() {
            mobileMenu.style.display = 'block';
            setTimeout(function() {
                mobileMenu.classList.add('open');
            }, 10);
        });
    }
    if (closeButton && mobileMenu) {
        closeButton.addEventListener('click', function() {
            mobileMenu.classList.remove('open');
            setTimeout(function() {
                mobileMenu.style.display = 'none';
            }, 300);
        });
    }
    // Hide menu on outside click
    document.addEventListener('click', function(e) {
        if (mobileMenu && mobileMenu.classList.contains('open') && !mobileMenu.contains(e.target) && !menuButton.contains(e.target)) {
            mobileMenu.classList.remove('open');
            setTimeout(function() {
                mobileMenu.style.display = 'none';
            }, 300);
        }
    });
    // Hide menu on escape
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && mobileMenu && mobileMenu.classList.contains('open')) {
            mobileMenu.classList.remove('open');
            setTimeout(function() {
                mobileMenu.style.display = 'none';
            }, 300);
        }
    });
    // Hide by default
    if (mobileMenu) {
        mobileMenu.style.display = 'none';
    }
});
