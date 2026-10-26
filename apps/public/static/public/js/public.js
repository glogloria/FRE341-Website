
const filterButtons = document.querySelectorAll(".filter-btn");
const books = document.getElementById("books");
const blindbox = document.getElementById("blindbox");

filterButtons.forEach(btn => {
    btn.addEventListener("click", function() {
        if (btn.dataset.target == "blindbox") {
            books.hidden = true;
            blindbox.hidden = false;
        } else {
            books.hidden = false;
            blindbox.hidden = true;
        }

        // Update Bootstrap button styles.
        filterButtons.forEach(button => {
            const isActive = button === btn;

            button.classList.toggle("active", isActive);
            button.classList.toggle("btn-dark", isActive);
            button.classList.toggle("btn-outline-dark", !isActive);
            button.setAttribute("aria-pressed", String(isActive));
        });
    });
});