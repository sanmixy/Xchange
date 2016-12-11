/**
 * Created by Administrator on 16-12-7.
 */

function sender(url, callback, data) {
    $.ajax({
        url: url,
        data: data,
        dataType: 'JSON',
        type: 'POST',
        cache: false,
        success: callback
    });
}

(function () {
    $.fn.shake = function (intShakes, intDistance, intDuration) {
        this.each(function () {
            $(this).css({
                position: "relative"
            });
            for (var x = 1; x <= intShakes; x++) {
                $(this).animate({
                    left: (intDistance * -1)
                }, (((intDuration / intShakes) / 4))).animate({
                    left: intDistance
                }, ((intDuration / intShakes) / 2)).animate({
                    left: 0
                }, (((intDuration / intShakes) / 4)));
            }
        });
        return this;
    };
})();

(function ($) {
    $.get_param = function (name) {
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
        var r = window.location.search.substr(1).match(reg);
        if (r != null) return unescape(r[2]);
        return null;
    }
})(jQuery);