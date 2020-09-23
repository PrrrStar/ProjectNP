
$(document).on('submit', '.comment-form', function(e){
    e.preventDefault();
    var id = $(this).attr('value');
    $.ajax({
        url: $(this).attr('action'),
        enctype: "multipart/form-data",
        processData: false,
        contentType: false,
        cache: false,
        method: 'POST',
        data: $(this).serialize(),
        dataType: 'json',
        success: function(response){
            $('.main-comment-section').html(response['form']);
            $('textarea').val('');
        },
        error: function(rs, e){
            console.log(rs.responseText);
        }
    });
});