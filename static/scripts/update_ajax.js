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

function updateLikes(postId) {
    $.ajax({
        type: 'POST',
        url: '/update_likes/',
        data: {
            'post_id': postId,
            'csrfmiddlewaretoken': getCookie('csrftoken')
        },
        success: function (response) {
            $('#likes-count-' + postId).text(response.likes);
        },
        error: function (xhr, status, error) {
            console.error(xhr.responseText);
        }
    });
}
