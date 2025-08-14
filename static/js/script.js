// Health check (index page)
document.addEventListener("DOMContentLoaded", () => {
  const checkBtn = document.getElementById("checkBtn");
  const resp = document.getElementById("response");
  if (checkBtn) {
    checkBtn.addEventListener("click", () => {
      fetch("/ping")
        .then(res => res.text())
        .then(data => {
          resp.innerText = "Response: " + data;
        })
        .catch(() => {
          resp.innerText = "Error: API not reachable";
        });
    });
  }
});
