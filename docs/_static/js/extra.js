document.querySelectorAll("span[dir='rtl']").forEach(span => {
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
