document.querySelectorAll("span[dir='rtl']").forEach(span => {
    const parent = span.parentElement;
    if (parent && parent.tagName.toLowerCase() === "p") {
        parent.setAttribute("dir", "rtl");
        span.removeAttribute("dir");
    }

    const grandparent = parent?.parentElement;
    if (grandparent && grandparent.tagName.toLowerCase() === "ul") {
        grandparent.setAttribute("dir", "rtl");
        span.removeAttribute("dir");
    }
});
