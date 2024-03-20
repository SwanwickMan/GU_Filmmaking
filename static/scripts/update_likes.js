function changeImage() {
    var img = document.getElementById('likes-image');
    if (img.src.match("empty_like.png")) {
        img.src = "likes.png"; // Change this to the path of your new image
    } else {
        img.src = "likes.png"; // Change this to the path of your original image
    }
}