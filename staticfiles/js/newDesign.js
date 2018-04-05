$(document).ready(main);

function main() {
// alert("Welcome to suveen.me")

    /*
    ==============================================================================
                                    Sticky Navbar
    ==============================================================================
     */
    $('#nav').affix({
        offset: {
            top: $('header').height()
        }
    });

    $("#nav").wrap("<div class='nav-placeholder'></div>");
    $(".nav-placeholder").height($("#nav").outerHeight());

    /*
    ==============================================================================
                                Skills Progress Bar
    ==============================================================================
     */
    $(document).on('scroll', function () {
        // console.log($('html,body').scrollTop())
        // console.log(($('header').outerHeight() - 10))
        if ($('html,body').scrollTop() > ($('header').outerHeight() - 10)) {
            $('.progress .progress-bar').css("width",
                function () {
                    return $(this).attr("aria-valuenow") + "%";
                }
            )
        }
    });


    /*
    ==============================================================================
                                Ending tag for main()
    ==============================================================================
     */
}