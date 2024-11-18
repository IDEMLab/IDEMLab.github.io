---
title: Internal
nav:
  order: 5
  tooltip: Internal Resources
---

<style>
    #loginForm {
        display: flex;
        flex-direction: column;
        width: 300px;
        margin: 0 auto; /* Center the form horizontally */
    }

    label, input {
        margin-bottom: 15px;
    }

    input[type="submit"] {
        margin-top: 10px;
        cursor: pointer;
    }
</style>

<form id="loginForm" onsubmit="return authenticate(event)">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
    <input type="submit" value="Login">
</form>

<script>
    function authenticate(event) {
        event.preventDefault(); // Prevent form submission

        const validUsername = "michelmannlab"; // Set your username here
        const validPassword = "michelmannlab"; // Set your password here

        const usernameInput = document.getElementById("username").value;
        const passwordInput = document.getElementById("password").value;

        if (usernameInput !== validUsername || passwordInput !== validPassword) {
            alert("You don’t have access to this section. If you believe this is an error, please reach out to our lab manager.");
            return false;
        }

        // Redirect if both username and password are correct
        window.location.href = "https://www.notion.so/96e0c6e6f0d943029988054fd986bebf?v=23c4cb74bf1544c881156cb745594944"; // Replace with your desired redirect URL
        return false;
    }
</script>
