document.getElementById('sort-options').addEventListener('change', function() {
    var url = this.value;
    window.location.href = url; // Redirect to the selected URL
});