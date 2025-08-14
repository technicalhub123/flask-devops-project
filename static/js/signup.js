document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("signupForm");
  const messageContainer = document.getElementById("message");

  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    
    // Show loading state
    const submitBtn = form.querySelector('button[type="submit"]');
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<div class="spinner"></div> Creating account...';
    
    showMessage("Creating your account...", "info");

    const payload = {
      email: document.getElementById("email").value,
      username: document.getElementById("username").value,
      password: document.getElementById("password").value
    };

    try {
      const res = await fetch("/auth/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      const data = await res.json();
      
      if (res.ok) {
        showMessage("🎉 Account created successfully! Redirecting to users page...", "success");
        setTimeout(() => { 
          window.location.href = "/users-page"; 
        }, 1500);
      } else {
        const errorMsg = data.error || "Signup failed. Please try again.";
        showMessage(`❌ ${errorMsg}`, "error");
      }
    } catch (err) {
      console.error(err);
      showMessage("⚠️ Network error. Please check your connection.", "error");
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = "Create Account";
    }
  });

  function showMessage(text, type) {
    messageContainer.textContent = text;
    messageContainer.className = `notification notification-${type}`;
    messageContainer.style.display = "flex";
    
    // Auto-hide success messages
    if (type === "success") {
      setTimeout(() => {
        messageContainer.style.display = "none";
      }, 5000);
    }
  }
});
