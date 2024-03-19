document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("switch-movies").addEventListener("click", function () {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                document.getElementById("post-section").innerHTML = xhr.responseText;
            }
        };
        xhr.open("GET", "{% url 'GUFilmmakingApp:short_movies' %}", true);
        xhr.send();
    });
});