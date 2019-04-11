
$("#tags div").click(function(event) {
    $(this).toggleClass("active");
    $(".project").show();
    $(".tag").removeClass("active");
    $.each($(".active"), function() {
        $(".project").not($("." + $(this).attr("id"))).hide();
        $(".tag." + $(this).attr("id")).addClass("active");
    });
});

function tagClick(selection) {
    $("#" + selection).click();
}
