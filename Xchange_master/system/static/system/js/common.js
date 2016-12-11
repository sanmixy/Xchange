$(function () {
    bingEvents();

    function bingEvents() {
        $('a#sign_out_hook').click(function () {
            sender('/system/logout', function () {
                window.location.href = '/';
            })
        });
    }
});