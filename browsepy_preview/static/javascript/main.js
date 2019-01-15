if (!window.parent || !window.parent.frames["main-frame"]) {
    // If not in a frame, redirect self in a frame
    window.location.replace("/preview/parent-window/" + window.location.pathname.slice(1));
}
else {
    document.addEventListener("DOMContentLoaded", function() {
        var elements = document.getElementsByClassName("preview");
        for (var i = 0; i < elements.length; ++i) {
            var element = elements[i];
            element.addEventListener("click", previewClicked);
        }
    });
}

function previewClicked(e) {
    e.preventDefault();
    window.parent.preview_open(e.target.href);
}
