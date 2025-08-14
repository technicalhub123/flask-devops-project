document.addEventListener("DOMContentLoaded", () => {
  const tbody = document.querySelector("#usersTable tbody");
  const usersMsg = document.getElementById("usersMsg");
  const refreshBtn = document.getElementById("refreshUsers");
  const usersCount = document.getElementById("usersCount");

  async function loadUsers() {
    showMessage("⏳ Loading users...", "info");
    
    try {
      const res = await fetch("/auth/users");
      
      if (!res.ok) {
        const error = await res.json();
        throw new Error(error.error || "Failed to fetch users");
      }
      
      const users = await res.json();
      renderUsers(users);
      
      // Update count
      usersCount.textContent = `${users.length} ${users.length === 1 ? 'user' : 'users'}`;
      showMessage("✅ Users loaded successfully", "success");
    } catch (err) {
      console.error(err);
      showMessage(`⚠️ ${err.message}`, "error");
    }
  }

  function renderUsers(users) {
    tbody.innerHTML = "";
    
    if (!users || users.length === 0) {
      tbody.innerHTML = `
        <tr>
          <td colspan="5" class="text-center">No users found</td>
        </tr>
      `;
      return;
    }
    
    users.forEach(user => {
      const tr = document.createElement("tr");
      tr.className = "fade-in";
      tr.innerHTML = `
        <td>${user.id}</td>
        <td>${user.email}</td>
        <td>${user.username}</td>
        <td>${formatDate(user.created_at)}</td>
        <td>
          <button class="btn-icon" title="Edit">
            <i class="icon-edit"></i>
          </button>
          <button class="btn-icon" title="Delete">
            <i class="icon-delete"></i>
          </button>
        </td>
      `;
      tbody.appendChild(tr);
    });
  }
  
  function formatDate(dateString) {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString();
  }
  
  function showMessage(text, type) {
    usersMsg.textContent = text;
    usersMsg.className = `notification notification-${type}`;
    usersMsg.style.display = "flex";
  }

  // Initial load
  loadUsers();
  
  // Refresh button
  refreshBtn.addEventListener("click", loadUsers);
});
