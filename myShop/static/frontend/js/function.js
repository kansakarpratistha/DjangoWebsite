$(document).on("show.bs.dropdown", function () {
    var dropdownToggle = $(this).find(".dropdown-toggle");
    var dropdownMenu = $(this).find(".dropdown-menu");
    dropdownMenu.css({
      "top": (dropdownToggle.position().top + dropdownToggle.outerHeight()) + "px",
      "left": dropdownToggle.position().left + "px"
    });
  });

$('.single-item').slick();