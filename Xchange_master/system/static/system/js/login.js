/**
 * Created by Xnus on 16-12-4.
 */
$(function () {
    function add_events() {
        $('button#sign_in_button').click(function () {
            var username = $('input#username_field').val().trim(),
                passcode = $('input#passcode_field').val();
            if (username) {
                sender('/system/login', process_login_result, {'username': username, 'passcode': passcode});
            }
        });

        function process_login_result(answer) {
            var next = $.get_param('next') || '/';
            if (answer.result)
                window.location.href = next;
            else
                $('div#login_area').shake(4, 20, 200);
        }
    }

    add_events();
});
