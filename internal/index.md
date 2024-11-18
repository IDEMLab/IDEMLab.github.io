
---
title: Internal
nav:
  order: 5
url: https://www.notion.so/96e0c6e6f0d943029988054fd986bebf?v=23c4cb74bf1544c881156cb745594944
external: true
---


<button onclick="authenticate()">Access Internal Page</button>


<script>
    function authenticate() {
        const validUsername = "michelmannlab@nyu.edu"; // Set your username here
        const validPassword = "michelmannlab"; // Set your password here

        const usernameInput = prompt("Username:");
        if (usernameInput !== validUsername) {
            alert("You don’t have access to this section. If you believe this is an error, please reach out to our lab manager.");
            return;
        }

        const passwordInput = prompt("Enter your password:");
        if (passwordInput !== validPassword) {
            alert("You don’t have access to this section. If you believe this is an error, please reach out to our lab manager.");
            return;
        }

        // Redirect if both username and password are correct
        window.location.href = "[https://example.com/redirect](https://www.notion.so/96e0c6e6f0d943029988054fd986bebf?v=23c4cb74bf1544c881156cb745594944)"; // Replace with your desired redirect URL
    }
</script>
