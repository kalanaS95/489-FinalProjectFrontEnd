/*function authenticate(googleUser)
{
    //window.location.replace('html/mainpage.html');

    var profile = googleUser.getBasicProfile();
    console.log(profile);
    var imageURL = profile.getImageUrl();
    var emailAddr = profile.getEmail();
    console.log(imageURL);
    console.log(emailAddr);

}*/

function onLoadGoogleCallback(){
    gapi.load('auth2', function() {
      auth2 = gapi.auth2.init({
        client_id: '582903321253-ftsq8n0a06v7qu4snejqqoh2t6qhq6o9.apps.googleusercontent.com',
        cookiepolicy: 'single_host_origin',
        scope: 'profile'
      });
  
    auth2.attachClickHandler(element, {},
      function(googleUser) {
          console.log('Signed in: ' + googleUser.getBasicProfile().getName());
        }, function(error) {
          console.log('Sign-in error', error);
        }
      );
    });
  
    element = document.getElementById('loginBtn');
  }