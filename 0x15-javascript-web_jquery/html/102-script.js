window.addEventListener('DOMContentLoaded', function () {
    $("INPUT#btn_translate").click(function() {
        const lang_code = $("INPUT#language_code").val();
        $.get("https://fourtonfish.com/hellosalut/?lang=" + lang_code, function(data) {
            $("DIV#hello").text(data.hello);
        });
        });
    });