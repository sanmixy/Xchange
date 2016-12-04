$(function () {
    bingEvents();

    function bingEvents() {
        $('button#login_button').click(function () {
            var username = $('input#username_field').val(),
                passcode = $('input#passcode_field').val();
            $.ajax({
                url: '/account/login',
                data: {
                    username: username,
                    passcode: passcode
                },
                type: 'POST',
                dataType: 'JSON',
                cache: false,
                success: function (answer) {
                    if (answer) {
                        if (answer['result'] || null) {
                            window.location.reload();
                        }
                    }
                }
            });
        });
    }
});

function to_login() {
    $('div#login_modal').modal('show');
}

function to_user_center(name) {
    alert(name);
}