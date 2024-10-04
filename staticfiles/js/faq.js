document.addEventListener('DOMContentLoaded', function () {
    const faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(question => {
        question.addEventListener('click', function () {
            // Toggle active class
            this.classList.toggle('active');
            
            // Toggle the answer display
            const answer = this.nextElementSibling;
            if (answer.style.display === "block") {
                answer.style.display = "none";
            } else {
                answer.style.display = "block";
            }

            // Rotate arrow on button (optional, if you want to add an icon)
            this.classList.toggle('rotate');
        });
    });
});
