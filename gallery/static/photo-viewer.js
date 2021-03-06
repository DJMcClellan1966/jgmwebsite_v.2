var request;                            // Latest image to be requested
var $current;                           // Image currently being shown
var cache = {};                         // Cache object
var $frame = $('#photo-viewer');        // Container for image
var $thumbs = $('.thumbs');             // Container for thumbnails

function crossfade($img) {              // Function to fade between images
                                        // Pass in new image as parameter
  if ($current) {                       // If there is currently an image showing
    $current.stop().fadeOut('slow');    // Stop animation and fade it fadeOut
  }

  $img.css({                            // set the css margins for the image
    marginLeft: -$img.width()/2,        // Negative margin of half image's width
    marginTop:  -$img.height()/2        // Negative margin of half image's height
  });

  $img.stop().fadeTo('slow', 1);        // Stop animation on new image and fade in

  $current = $img;                      // New image becomes current image
}
