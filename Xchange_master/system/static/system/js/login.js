/**
 * Created by Xnus on 16-12-4.
 */
$(function () {
    function add_events() {
        $('button#sign_in_button').click(function () {
            var username = $('input#username_field').val().trim(),
                passcode = $('input#passcode_field').val();
            if (username) {
                sender('/system/login', {'username': username, 'passcode': passcode}, process_login_result);
            }
        });

        function process_login_result(result) {
            alert(JSON.stringify(result));
        }
    }

    add_events();
});
