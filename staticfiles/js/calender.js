$(function() {
    // Get the current date
    var currentDate = new Date();
  
    $("#date").datepicker({
      beforeShowDay: function(date) {
        var day = date.getDay(); // Get the day of the week (0 - 6)
        // Disable days specified in the array and tomorrow
        return [
          disabledDays.indexOf(day) === -1 && date >= currentDate && !isTomorrow(date, tomorrowDate),
          ""
        ]; // [disable/enable, CSS class]
      },
      showAnim: "drop" // Apply the "drop" effect permanently
    });
  
    // Function to check if the given date is tomorrow
    function isTomorrow(date, tomorrow) {
      return (
        date.getDate() === tomorrow.getDate() &&
        date.getMonth() === tomorrow.getMonth() &&
        date.getFullYear() === tomorrow.getFullYear()
      );
    }
  });
  