(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Navbar on scrolling
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.navbar').fadeIn('slow').css('display', 'flex');
        } else {
            $('.navbar').fadeOut('slow').css('display', 'none');
        }
    });


    // Smooth scrolling on the navbar links
    $(".navbar-nav a").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            
            $('html, body').animate({
                scrollTop: $(this.hash).offset().top - 45
            }, 1500, 'easeInOutExpo');
            
            if ($(this).parents('.navbar-nav').length) {
                $('.navbar-nav .active').removeClass('active');
                $(this).closest('a').addClass('active');
            }
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });
    

    // Typed Initiate
    if ($('.typed-text-output').length == 1) {
        var typed_strings = $('.typed-text').text();
        var typed = new Typed('.typed-text-output', {
            strings: typed_strings.split(', '),
            typeSpeed: 100,
            backSpeed: 20,
            smartBackspace: false,
            loop: true
        });
    }


    // Modal Video
    var $videoSrc;
    $('.btn-play').click(function () {
        $videoSrc = $(this).data("src");
    });
    console.log($videoSrc);
    $('#videoModal').on('shown.bs.modal', function (e) {
        $("#video").attr('src', $videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0");
    })
    $('#videoModal').on('hide.bs.modal', function (e) {
        $("#video").attr('src', $videoSrc);
    })


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Skills
    $('.skill').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, {offset: '80%'});


    // Portfolio isotope and filter
    var portfolioIsotope = $('.portfolio-container').isotope({
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });
    $('#portfolio-flters li').on('click', function () {
        $("#portfolio-flters li").removeClass('active');
        $(this).addClass('active');

        portfolioIsotope.isotope({filter: $(this).data('filter')});
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 1,
        dots: true,
        loop: true,
    });

	// Vars.
	var $form = document.querySelectorAll('#contact-form')[0],
	$submit = document.querySelectorAll('#contact-form input[type="submit"]')[0],
	$message;

	// Bail if addEventListener isn't supported.
	if (!('addEventListener' in $form))
		return;

	// Message.
	$message = document.createElement('span');
	$message.classList.add('message');
	$form.appendChild($message);

	$message._show = function(type, text) {

	$message.innerHTML = text;
	$message.classList.add(type);
	$message.classList.add('visible');

	window.setTimeout(function() {
		$message._hide();
	}, 3000);

	};

	$message._hide = function() {
	$message.classList.remove('visible');
	};

	var form = document.querySelector("#contact-form");
	form.addEventListener("submit", function(event) {
    event.preventDefault();
    //const csrfToken = Cookies.get('csrftoken');
    var xhr = new XMLHttpRequest();
    xhr.open("POST", window.location.href);
    //xhr.setRequestHeader("X-CSRFToken", csrfToken);
    xhr.onload = function() {
        if (xhr.status === 200) {
            // handle the success response
            $message._show('success', xhr.responseText);
        } else {
            // handle the error response
            $message._show('failure', xhr.responseText);
        }
    };
    xhr.onerror = function() {
        // handle the error
        console.error("Request failed.");
    };
    xhr.send(new FormData(form));
    form.reset();
	});    
    
})(jQuery);

