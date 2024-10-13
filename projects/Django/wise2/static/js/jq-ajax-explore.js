$(document).ready(function () {
    $(document).on("click", "#next_btn", function (e) {
        e.preventDefault();

        var wisdom_id = $(this).data("wisdom-id");
        var $button = $(this);

        $.ajax({
            type: "POST",
            url: '',
            data: {
                except_id: wisdom_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
        
            success: function (data) {
                var wisdom = $(".wisdom");
                wisdom.html(data.wisdom);

                $button.attr("data-wisdom-id", data.wisdom_id);
                $button.removeData("wisdom-id");  
            },

            error: function (data) {
                console.log("Ошибка");
            },
        });
    });
});