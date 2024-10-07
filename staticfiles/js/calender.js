$(function() {
    // Get the current date and tomorrow's date
    const currentDate = new Date();
    const tomorrowDate = new Date(currentDate);
    tomorrowDate.setDate(currentDate.getDate() + 1);
  
    // Initialize the datepicker
    $("#date").datepicker({
        beforeShowDay: function(date) {
            const day = date.getDay(); // Get the day of the week (0 - 6)
            const isDayEnabled = disabledDays.indexOf(day) === -1;
            const isAfterToday = date >= currentDate;
            const notTomorrow = !isSameDay(date, tomorrowDate);
  
            return [isDayEnabled && isAfterToday && notTomorrow, ""];
        },
        showAnim: "drop" // Apply the "drop" effect permanently
    });
  
    // Function to check if two dates are the same day
    function isSameDay(date1, date2) {
        return date1.getTime() === date2.getTime();
    }
  
    // Custom validation to check if a date is selected
    $("form").on("submit", function(event) {
        const selectedDate = $("#date").datepicker("getDate");
        if (!selectedDate) {
            event.preventDefault(); // Prevent form submission if no date is selected
            alert("Please select a valid date.");
            $("#date").focus();
        }
    });
  });
  