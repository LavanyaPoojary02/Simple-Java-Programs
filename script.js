alert("Welcome to Lavanya's Portfolio!");
document.querySelectorAll("nav ul li a").forEach(link => {
  link.addEventListener("click", function(e) {
    e.preventDefault();

    const targetId = this.getAttribute("href");
    const targetSection = document.querySelector(targetId);
    targetSection.scrollIntoView({
      behavior: "smooth"
    });
  });
});
