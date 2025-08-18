// =============================
// Fix RTL
// =====
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

// =============================
// Headline tag
// =====
const el = document.querySelector(".md-content h1");
if (el) {
    el.innerHTML = el.innerHTML
        // {tag} is a category
        .replace(/\{([^}]+)\}/g, '<span class="title-tag title-tag__category">$1</span>')
        // [tag] is a special topic
        .replace(/\[([^\]]+)\]/g, '<span class="title-tag title-tag__special_topic">$1</span>')
}

// =============================
// Menu tag
// =====
document.querySelectorAll(".md-sidebar .md-nav__link").forEach(link => {
    const textContainer = link.querySelector(".md-ellipsis");

    if (textContainer) {
        const originalText = textContainer.innerHTML;

        const newHTML = originalText
            // {tag} is a category
            .replace(/\{([^}]+)\}/g, '<span class="nav-tag nav-tag__category">$1</span>')
            // [tag] is a special topic
            .replace(/\[([^\]]+)\]/g, '<span class="nav-tag nav-tag__special_topic">$1</span>')
            // The rest of the text
            .replace(/^([^<]+)/, match => `<span class="nav-text" title="${match.trim()}">${match.trim()}</span>`);

        // Replace the container's old content with the new structured HTML
        textContainer.innerHTML = newHTML;
    }
});

document.querySelectorAll(".nav-tag + .nav-tag").forEach(tag => {
    const previousTag = tag.previousElementSibling;

    if (previousTag) {
        // Calculate the negative margin needed to overlap X% of the previous tag.
        const overlap = previousTag.offsetWidth * 0.9;

        // Set this calculated value as a CSS variable on the current tag
        tag.style.setProperty("--overlap-margin", `-${overlap}px`);
    }
});

// =============================
// Toggle sidebar
// =====
const fullscreenPath = "M4 4h6v2H6v4H4V4zm16 0h-6v2h4v4h2V4zM4 20h6v-2H6v-4H4v6zm16 0h-6v-2h4v-4h2v6z";
const exitFullscreenPath = "M4 10h6V4H8v4H4v2zm16 0h-6v-6h2v4h4v2zM4 14h6v6H8v-4H4v-2zm16 0h-6v6h2V16h4V14z";

let isSidebarVisible = false;

function updateSidebarButtonIcon() {
    const svgPath = document.querySelector(".mkdocs-toggle-sidebar-button svg path");
    svgPath.setAttribute("d", isSidebarVisible ? fullscreenPath : exitFullscreenPath);
    isSidebarVisible = !isSidebarVisible;
}

const sidebarButtonObserver = new MutationObserver(() => {
    const btn = document.querySelector(".mkdocs-toggle-sidebar-button");
    if (btn) {
        const nav = document.querySelector(".md-sidebar");
        if (nav && !nav.hasAttribute("hidden")) {
            btn.addEventListener("click", updateSidebarButtonIcon);
            updateSidebarButtonIcon(); // Initial icon update
        } else {
            btn.style.display = "none";
        }
        sidebarButtonObserver.disconnect();
    }
});

sidebarButtonObserver.observe(document.body, { childList: true, subtree: true });

// =============================
// Show container
// =====
document.querySelector(".md-container").style.opacity = "1";
