$('.gallery').each(function () { // the containers for all your galleries
    $(this).magnificPopup({
        delegate: '.gallery-item', // the selector for gallery item
        type: 'image',
        gallery: {
            enabled: true
        }
    });
});