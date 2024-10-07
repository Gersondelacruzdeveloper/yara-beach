document.addEventListener("DOMContentLoaded", function () {
  const reviews = document.querySelectorAll(".review");
  const ratingFilters = document.querySelectorAll('input[name="rating"]');

  // Function to filter reviews based on rating
  function filterReviews(rating) {
    reviews.forEach((review) => {
      const reviewRating = review.getAttribute("data-rating");
      // Show the review if the rating matches or if 'all' is selected
      if (rating === "all" || reviewRating === rating) {
        review.style.display = "block";
      } else {
        review.style.display = "none";
      }
    });
  }

  // Listen for changes in the rating filter
  ratingFilters.forEach((filter) => {
    filter.addEventListener("change", function () {
      filterReviews(this.value);
    });
  });
});
