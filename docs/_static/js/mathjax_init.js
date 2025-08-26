window.MathJax = {
    chtml: {
        fontURL: "/_static/fonts/mathjax"
    },
    tex: {
        inlineMath: [["\\(", "\\)"]],
        displayMath: [["\\[", "\\]"]],
        processEscapes: true,
        processEnvironments: true
    },
    options: {
        enableMenu: false,
        menuOptions: {
            settings: {
                enrich: false
            }
        },
        ignoreHtmlClass: ".*|",
        processHtmlClass: "arithmatex"
    },
};
