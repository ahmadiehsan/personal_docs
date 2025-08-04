// Fix RTL
document.querySelectorAll(".md-content span[dir='rtl']").forEach(span => {
    const parent = span.parentElement;
    if (parent && ["p", "h1", "h2", "h3", "h4", "h5", "h6", "td"].includes(parent.tagName.toLowerCase())) {
        parent.setAttribute("dir", "rtl");
        span.removeAttribute("dir");
    }

    const grandparent = parent?.parentElement;
    if (grandparent && grandparent.tagName.toLowerCase() === "ul") {
        grandparent.setAttribute("dir", "rtl");
        span.removeAttribute("dir");
    }
});

// Headline tag
const el = document.querySelector(".md-content h1");
if (el) {
    el.innerHTML = el.innerHTML
        .replace(/\{([^}]+)\}/g, '<span class="md-title__tag md-title__tag__category">$1</span>')
        .replace(/\[([^\]]+)\]/g, '<span class="md-title__tag md-title__tag__topic">$1</span>');
}

// Menu tag
document.querySelectorAll(".md-sidebar .md-nav__link").forEach(el => {
    el.innerHTML = el.innerHTML
        .replace(/\{([^}]+)\}/g, '<span class="md-nav__tag md-nav__tag__category">$1</span>')
        .replace(/\[([^\]]+)\]/g, '<span class="md-nav__tag md-nav__tag__topic">$1</span>');
});

// Show container
document.querySelector(".md-container").style.opacity = "1";
