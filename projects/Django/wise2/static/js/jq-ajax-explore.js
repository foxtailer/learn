$(document).ready(function () {
    const csrfToken = $('meta[name="csrf-token"]').attr('content');

    $.ajaxSetup({
        headers: {
            'X-CSRFToken': csrfToken
        }
    });


    $(document).on("click", "#next_btn", function (e) {
        e.preventDefault();

        var wisdom_id = $("#wisdom").data("wisdom-id");
        var $container = $("#wisdom");

        $.ajax({
            type: "POST",
            url: "",
            data: {
                wisdom_id: wisdom_id,
            },
        
            success: function (data) {
                $container.html(data.wisdom);

                $container.attr("data-wisdom-id", data.wisdom_id);
                $container.removeData("wisdom-id"); 
                
                document.getElementById("mail_btn").setAttribute("href", "mailto:" + data.email);
                if (data.reply) {
                    document.getElementById("mail_btn").setAttribute("class", "control-element " + "active ");
                } else {
                    document.getElementById("mail_btn").setAttribute("class", "control-element " + "off");
                    document.getElementById("mail_btn").setAttribute("href", "");
                }
            },

            error: function (data) {
                console.log("Ошибка");
            },
        });
    });


    $(document).on("click", "#like_btn", function (e) {
        e.preventDefault();

        var wisdom_id = $("#wisdom").data("wisdom-id");

        $.ajax({
            type: "PATCH",
            url: "",
            contentType: 'application/json',
            data: JSON.stringify({
                user_id: userId,
                post_id: wisdom_id,
            }),
        
            success: function (data) {
                console.log('+')
            },

            error: function (data) {
                console.log("Ошибка");
            },
        });
    });


    $(document).on("click", "#report_btn", function (e) {
        e.preventDefault();

        var wisdom_id = $("#wisdom").data("wisdom-id");

        $.ajax({
            type: "PATCH",
            url: "",
            contentType: 'application/json',
            data: JSON.stringify({
                user_id: userId,
                post_id: wisdom_id,
            }),
        
            success: function (data) {
                console.log('+')
            },

            error: function (data) {
                console.log("Ошибка");
            },
        });
    });
});