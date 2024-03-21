function changeImage() {
    var img = document.getElementById('likes-img');
    var fileName = img.src.split("/")[img.src.split("/").length - 1];
    if (fileName === "empty_like.png") {
        img.src = " /static/images/likes.png"; // Change this to the path of your new image
    } else {
        img.src = " /static/images/empty_like.png"; // Change this to the path of your original image
    }
}