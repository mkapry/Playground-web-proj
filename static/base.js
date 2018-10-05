$(document).on('click', 'button.ajaxlike', function(e) {
        var data = $(this).data();
        console.log(data);
        var likesSpan = $('#likes-' + data.postid);
        likesSpan.html("like");
        return false;
    });

//$('click')
//$.ajax({
//url: 'likes',
//data: {pk=post.pk}).done(function(data, status, response) {console.log(data, status, response)});


$(document).ready(
    function() {
        $(".chosen-select").chosen();

        function csrfSafeMethod(method) {
             //these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });
    }
);

//$.ajax({url: ссылка, method: 'POST', data: $('form').serialize()})