if (!window.parent || !window.parent.frames["main-frame"]) {
    // If not in a frame, redirect self in a frame
    window.location.replace("/preview/parent-window/" + window.location.pathname.slice(1));
}
else {
    var open_prefix = "/open/";
    document.addEventListener("DOMContentLoaded", function() {
        var elements = document.getElementsByTagName("a");
        for (var i = 0; i < elements.length; ++i) {
            var element = elements[i];
            
            if (element.pathname.startsWith(open_prefix)) {
                element.pathname = "/preview/preview_info/" + element.pathname.slice(open_prefix.length);
                element.addEventListener("click", previewClicked);
            }
        }
        window.parent.history.replaceState(null, window.location, window.location);
    });
}

function previewClicked(e) {
    e.preventDefault();
    window.parent.preview_request(e.target.href);
}
