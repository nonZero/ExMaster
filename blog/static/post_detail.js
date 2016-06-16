"use strict";

$(function () {

    $("#commentform").submit(function () {
        var form = $(this);
        var data = {
            title: $("#id_title").val(),
            content: $("#id_content").val()
        };
        $.post("", data).then(function (resp) {
            var el = $(resp);
            $("#comments").prepend(el);
            form.get(0).reset();
        }).fail(function(resp) {
            console.error(resp.responseJSON);
            alert('something bad happend');
        });
        return false;
    });

});
