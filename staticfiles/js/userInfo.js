if ("geolocation" in navigator) {
    // Geolocation is available
    var watchId = navigator.geolocation.watchPosition(function(position) {
      // Get latitude and longitude
      var latitude = position.coords.latitude;
      var longitude = position.coords.longitude;
      
      console.log("Latitude: " + latitude + ", Longitude: " + longitude);
      
      // You can use these coordinates for various purposes, such as displaying a map or providing location-based services.
    }, function(error) {
      // Handle errors if any occur
      switch(error.code) {
        case error.PERMISSION_DENIED:
          console.log("User denied the request for geolocation.");
          break;
        case error.POSITION_UNAVAILABLE:
          console.log("Location information is unavailable.");
          break;
        case error.TIMEOUT:
          console.log("The request to get user location timed out.");
          break;
        case error.UNKNOWN_ERROR:
          console.log("An unknown error occurred.");
          break;
      }
    });
  } else {
    // Geolocation is not available in this browser
    console.log("Geolocation is not supported by this browser.");
  }
  
  

// Get the user agent string from the navigator
var userAgent = navigator.userAgent;
console.log("User Agent: " + userAgent);

// Regular expressions to match common mobile device patterns and their associated device names
var mobileDevicePatterns = [
  { pattern: /Android\s([^\s;]+)/, name: "Android" },
  { pattern: /iPhone\sOS\s([\d_]+)/, name: "iPhone" },
  { pattern: /iPad;\sCPU\sOS\s([\d_]+)/, name: "iPad" },
  { pattern: /Windows\sPhone\sOS\s([\d.]+)/, name: "Windows Phone" },
  // Add more patterns as needed for other devices
];

// Initialize a variable to store the device name
var deviceName = "Unknown Device";

// Iterate through the patterns and extract the device information if a match is found
for (var i = 0; i < mobileDevicePatterns.length; i++) {
  var match = userAgent.match(mobileDevicePatterns[i].pattern);
  if (match && match.length > 1) {
    deviceName = mobileDevicePatterns[i].name + " " + match[1];
    break; // Exit the loop if a match is found
  }
}

console.log("Device Name: " + deviceName);

