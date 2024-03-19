document.addEventListener("DOMContentLoaded", function () {
    console.log("Button clicked"); // Add this line inside your event listener

    document.getElementById("switch-movies").addEventListener("click", function () {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                document.getElementById("post-section").innerHTML = xhr.responseText;
            }
        };
        xhr.open("GET", "{% url 'GUFilmmakingApp:long_movies' %}", true);
        xhr.send();
    });
});
