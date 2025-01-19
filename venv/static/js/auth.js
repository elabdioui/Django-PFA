
document.addEventListener('DOMContentLoaded', () => {
    const signUpButton = document.getElementById('signup_ghost');
    const signInButton = document.getElementById('signin_ghost');
    const containerWrapper = document.getElementById('container_wrapper');
    const closeButton = document.getElementById('btn-close-auth');
    
    const handleSignUpClick = () => {
      $(containerWrapper).addClass('right-panel-active');
    };
  
    const handleSignInClick = () => {
      $(containerWrapper).removeClass('right-panel-active');
    };
  
    // Show/hide close button based on URL
    if (location.pathname === "/register" || location.pathname === "/signup" || location.pathname === "/registration") {
      handleSignUpClick();
    }
  
    signUpButton.addEventListener('click', handleSignUpClick);
    signInButton.addEventListener('click', handleSignInClick);
    closeButton.addEventListener('click', () => {
      $(containerWrapper).removeClass('right-panel-active');
    });

});



function generatePassword() {
  while (true) {
    let password = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for (let i = 0; i < 10; i++) {
      password += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    if(regex_psw.test(password)){
      return password;
    }
    else{
      generatePassword();
    }
  
  }
}
$(function(e) {
$("#generate-btn").click(function() {
  let newPassword = generatePassword();
  console.log(newPassword);
  $("#password").val(newPassword);
  psw_tester();
});
});

const regex_mail=/^[a-zA-Z0-9_.-]{1,64}@[a-zA-Z0-9-.]{1,63}\.[a-zA-Z]{2,63}$/;
const regex_psw=/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
var mailvalid=false;
var pswvalid=false;

mail_tester=()=>{
  let mail=$("#email").val();
  if(!regex_mail.test(mail)){
      $(".mail_ready").css('display','none');
      $(".mail_error").css('display','inline');
      mailvalid=false;    
  }else{
      $(".mail_ready").css('display','inline');
      $(".mail_error").css('display','none');
      mailvalid=true;
  }
  combined_tester();
}

login_mail_tester=()=>{
  let mail=$("#login_email").val();
  if(!regex_mail.test(mail)){
      $(".login_mail_ready").css('display','none');
      $(".login_mail_error").css('display','inline');
      mailvalid=false;    
  }else{
      $(".login_mail_ready").css('display','inline');
      $(".login_mail_error").css('display','none');
      mailvalid=true;
  }
  combined_tester();
}

psw_tester=()=>{
  let psw=$("#password").val();
  if(!regex_psw.test(psw)){   
      $(".psw_ready").css('display','none');
      $(".psw_error").css('display','inline');
      let newpswd=generatePassword();
      console.log(newpswd);
      $("#generated_password").text(newpswd);
      pswvalid=false;
  }else{
      $(".psw_ready").css('display','inline');
      $(".psw_error").css('display','none');
      pswvalid=true;
  }
  combined_tester();
}
login_psw_tester=()=>{
  let psw=$("#login_password").val();
  if(!regex_psw.test(psw)){   
      $(".login_psw_ready").css('display','none');
      $(".login_psw_error").css('display','inline');
  }else{
      $(".login_psw_ready").css('display','inline');
      $(".login_psw_error").css('display','none');
      pswvalid=true;
  }
  combined_tester();
}

function combined_tester() {
  let user=$("#name").val();
  if (mailvalid && pswvalid && (user!=="")) {
      $(".auth_button").removeAttr("disabled");
      $(".form_ready").css('display', 'inline');

  } else {
      $(".auth_button").attr("disabled", "disabled");
      $(".form_ready").css('display', 'none');
  }
}