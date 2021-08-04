let loginButton = document.getElementById('loginbtn');
let loginWrapper = document.getElementById('login-wrapper')

loginButton.addEventListener('click', function() {
  loginWrapper.classList.toggle("login-page-reveal");
  loginWrapper.classList.toggle("");
});