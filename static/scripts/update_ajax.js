$(document).ready(function () {
    function updateLikes(postId) {
        $.ajax({
            type: 'POST',
            url: '/update_likes/',
            data: {
                'post_id': postId,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function (response) {
                $('#likes_count_' + postId).text(response.likes);
            },
            error: function (xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    }

    $('.post').each(function () {
        var postId = $(this).attr('data-post-id');
        updateLikes(postId);
    });
});

