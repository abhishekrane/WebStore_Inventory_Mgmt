use CGI;
use CGI::Session;
use CGI::Carp qw (fatalsToBrowser);

my $q = new CGI;
my $sid = $q->cookie("jadrn034SID") || undef;
$session = new CGI::Session(undef, $sid, {Directory => '/tmp'});
$session->delete();
my $cookie = $q->cookie(jadrn034SID => '');
print $q->header( -cookie=>$cookie ); #send cookie with session ID to browser  


print <<END;    
    
<html>
<head>


</head>
<body>


<h2>Success, the details has been uploaded</h2>
<table>
<tr><td>SKU: $sku</td></tr>
<tr><td>Category ID: $category</td></tr>
<tr><td>Vendor ID: $vendor</td></tr>
<tr><td>Manufacturer ID: $mfid</td></tr>
<tr><td>Description: $desc</td></tr>
<tr><td>Features: $features</td></tr>
<tr><td>cost: $cost</td></tr>
<tr><td>Retail: $retail </td></tr>
<tr><td>Quantiy: $quantity</td></tr>

</table>
<input type="button" onclick="location.href='http://jadran.sdsu.edu/~jadrn034/proj1/';" value="Login" />
<h2> You are been logged out. CLick here to Login. </h2>
</body>
</html>





END