$(document).on("change", "select.filter-option", function(event) {
    $(this).parent("div").parent("form").submit();
});