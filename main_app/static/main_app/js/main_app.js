document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('input-form');

    form.addEventListener('submit', function(event) {
        // Prevent the form from submitting immediately
        event.preventDefault();
        document.getElementById("processing").style.display = "block";
        form.submit();
        });
    });