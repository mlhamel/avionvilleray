$(document).ready(function() {
    $('.image').magnificPopup({
        gallery:{
            enabled:true
        },
        type: 'image',
        zoom: {
            enabled: true, // By default it's false, so don't forget to enable it

            duration: 300, // duration of the effect, in milliseconds
            easing: 'ease-in-out' // CSS transition easing function
        }
    });
});
