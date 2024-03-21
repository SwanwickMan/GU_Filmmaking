function likePost(postId, likeUrl) {
    $.ajax({
        url: likeUrl.replace('0', postId),
        type: 'POST',
        data: JSON.stringify({ 'post_id': postId }),
        headers: { 'X-CSRFToken': getCookie('csrftoken') },
        contentType: 'application/json',
        dataType: 'json',
        success: function (data) {
            $('#likes-count-' + postId).text(data.likes);
            var img = $('#likes-img-' + postId);
            if (data.liked) {
                img.attr('src', '/static/images/likes.png');  // Adjust path as needed
            } else {
                img.attr('src', '/static/images/empty_like.png');  // Adjust path as needed
            }
        },
        error: function (xhr, status, error) {
            console.error('Error:', error);
        }
    });
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
