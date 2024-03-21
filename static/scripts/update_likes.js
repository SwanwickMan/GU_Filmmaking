function likePost(postId, likeUrl) {
    fetch(likeUrl.replace('0', postId), {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('likes-count-' + postId).innerText = data.likes;
            var img = document.getElementById('likes-img-' + postId);
            if (data.liked) {
                img.src = '/static/images/likes.png';  // Adjust path as needed
            } else {
                img.src = '/static/images/empty_like.png';  // Adjust path as needed
            }
        })
        .catch(error => console.error('Error:', error));
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
