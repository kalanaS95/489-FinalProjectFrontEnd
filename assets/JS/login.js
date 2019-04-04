function authenticate(googleUser)
{
    //window.location.replace('html/mainpage.html');

    var profile = googleUser.getBasicProfile();
    console.log(profile);
    var imageURL = profile.getImageUrl();
    var emailAddr = profile.getEmail();
    console.log(imageURL);
    console.log(emailAddr);

}