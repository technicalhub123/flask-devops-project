document.getElementById("checkBtn").addEventListener("click", () => {
  fetch("/ping")
    .then(res => res.text())
    .then(data => {
      document.getElementById("response").innerText = "Response: " + data;
    })
    .catch(() => {
      document.getElementById("response").innerText = "Error: API not reachable";
    });
});

