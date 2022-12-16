// Get a reference to the create account form
var form = document.getElementById("create-account-form");

// Add an event listener that listens for the submit event
form.addEventListener("submit", function(event) {
// Prevent the form from submitting
event.preventDefault();

// Get the values from the create account form
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;

// Store the values in local storage
localStorage.setItem("username", username);
localStorage.setItem("password", password);

// Redirect the user to the login page
window.location.href = "login.html";
});





// Get a reference to the login form
var form = document.getElementById("login-form");

// Add an event listener that listens for the submit event
form.addEventListener("submit", function(event) {
// Prevent the form from submitting
event.preventDefault();

// Get the values from the login form
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;

// Get the values stored in local storage
var storedUsername = localStorage.getItem("username");
var storedPassword = localStorage.getItem("password");

// Check if the values from the login form match the stored values
if (username === storedUsername && password === storedPassword) {
// Display a message to the user indicating that they have logged in successfully
alert("You have logged in successfully!");
} else {
// Display an error message
alert("Incorrect username or password. Please try again.");
}
});