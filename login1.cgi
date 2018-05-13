use CGI;
use CGI::Session;
use CGI::Carp qw (fatalsToBrowser);
use Crypt::Password;

##---------------------------- MAIN ---------------------------------------
print "Content-type: text/html\n\n";

my $q = new CGI;
my $user = "";

if(authenticate_user()) {
    send_to_main();   
    }
else {
    send_to_login_error();
    }    
###########################################################################

###########################################################################
sub authenticate_user {
    $user = $q->param("user");
    my $password = $q->param("password");       
    open DATA, "</srv/www/cgi-bin/jadrn034/passwords.dat" 
        or die "Cannot open file.";
    @file_lines = <DATA>;
    close DATA;

    $OK = 0; #not authorized

    foreach $line (@file_lines) {
        chomp $line;
        ($stored_user, $stored_pass) = split /=/, $line;    
    if($stored_user eq $user && check_password($stored_pass, $password)) {
        $OK = 1;
        last;
        }
    }
          
    return $OK;
    }
###########################################################################

###########################################################################
sub send_to_login_error {
    print <<END;

<html>
<head>
    <meta http-equiv="refresh" 
        content="0; url=http://jadran.sdsu.edu/~jadrn034/proj1/error.html" />
</head><body></body>
</html>

END
    }  
    
###########################################################################
      
###########################################################################
sub send_to_main {
# args are DRIVER, CGI OBJECT, SESSION LOCATION
# default for undef is FILE, NEW SESSION, /TMP 
# for login.html, don't look for any existing session.
# Always start a new one.  \
# This example uses URL re-writing
  
my $session = new CGI::Session(undef, undef, {Directory=>'/tmp'});
$session->expires('+1d');    
my $sid = $session->id;
$session->param('user',$user);
print <<END;
   
<html>
<head>

<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
<meta http-equiv="Pragma" content="no-cache" />
<meta http-equiv="Expires" content="0" /> 
 
 
 <link rel="stylesheet" type="text/css" href="/~jadrn034/proj1/page.css">    

</head>
<body>
<p>Click on the buttons inside the tabbed menu:</p>

<div class ="tabs">
  <button class="tablinks" onclick="openCity(event, 'newEntry')" id="defaultOpen">New Entry</button>
  <button class="tablinks" onclick="openCity(event, 'updateEntry')">Update Entry</button>
  <button class="tablinks" onclick="openCity(event, 'deleteEntry')">Delete Entry</button>
</div>

<div id="newEntry" class="tabcontent">
  <h3>newEntry</h3>
 <table>
   <tr><td>SKU: <input type="text" name="sku" id="sku" size="7" /> <br></td></td>
   <tr><td>category: <select name="category" id="category"></select><br></td></td>
   <tr><td>Vendor: <select name="vendor" id="vendor"></select><br></td></td>
   <tr><td>Manufacturer: <input type="text" name="mfid" id="mfid" size="15"><br></td></td>
   <tr><td>Description: <textarea rows="4" cols="40" name="desc" id="desc"></textarea><br></td></td>
    <tr><td>Features: <textarea rows="4" cols="40" name="features" id="features"></textarea><br></td></td>
    <tr><td>Cost: <input type="text" size="15" name="cost" id="cost"><br></td></td>
    <tr><td>Retail: <input type="text" size="15" name="retail" id="retail" class="retail"><br></td></td>
    <tr><td>Quantity: <input type="text" size="15" name="quantity" id="quantity"><br></td></td>
</table>


</div>

<div id="updateEntry" class="tabcontent">
  <h3>updateEntry</h3>
  <p>updateEntry is the capital of France.</p> 
</div>

<div id="deleteEntry" class="tabcontent">
  <h3>deleteEntry</h3>
  <p>deleteEntry is the capital of Japan.</p>
</div>




<script>
function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
</script>
<p>
This is the page that is protected.<br />
The session ID is $sid
</p>

<br />
<a href="/perl/jadrn000/sessions/logout.cgi?jadrn000SID=$sid">Logout Now</a>
</body>
</html>

END
}
###########################################################################    
    





