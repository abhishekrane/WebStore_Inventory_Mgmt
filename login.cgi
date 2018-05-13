# Abhishek Rane
# REd id- 822056658
# Account- Jadrn034 

use CGI;
use CGI::Session;
use CGI::Carp qw (fatalsToBrowser);
use Crypt::Password;

##---------------------------- MAIN ---------------------------------------

my $q;
if(authenticate_user()) {
    send_to_main();   
    }
else {
    send_to_login_error();
    }    
###########################################################################

###########################################################################
sub authenticate_user {
    $q = new CGI;
    my $user = $q->param("user");
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
    print $q->redirect('http://jadran.sdsu.edu/~jadrn034/proj1/error.html');
    exit;
    }
    
###########################################################################
      
###########################################################################
sub send_to_main {
# args are DRIVER, CGI OBJECT, SESSION LOCATION
# default for undef is FILE, NEW SESSION, /TMP 
# for login.html, don't look for any existing session.
# Always start a new one.  Send a cookie to the browser.
# Default expiration is when the browser is closed.
# WATCH YOUR COOKIE NAMES! USE JADRNXXX_SID  
    my $session = new CGI::Session(undef, undef, {Directory=>'/tmp'});
    $session->expires('+1d');
    my $cookie = $q->cookie(jadrn034SID => $session->id);
    print $q->header( -cookie=>$cookie ); #send cookie with session ID to browser    
    my $sid = $session->id;
   

    print <<END_CONTENT;


<html>
<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <META HTTP-EQUIV="Cache-Control" CONTENT="no-cache">
    <META HTTP-EQUIV="Pragma" CONTENT="no-cache">
    <META HTTP-EQUIV="Expires" CONTENT="0">
    

 
 <link rel="stylesheet" type="text/css" href="/~jadrn034/proj1/page.css">   

</head>
<body>

<div class ="tabs">
  <button class="tablinks" onclick="openCity(event, 'newEntry')" id="defaultOpen">New Entry</button>
  <button class="tablinks" onclick="openCity(event, 'updateEntry')">Update Entry</button>
  <button class="tablinks" onclick="openCity(event, 'deleteEntry')">Delete Entry</button>
  <button class="tablinks" onclick="location.href='/~jadrn034/proj1/index.html';">Logout Now</a>

</div>

<div id="newEntry" class="tabcontent">
  

  <form id="newForm"  method="post" enctype="multipart/form-data" action="/perl/jadrn034/addInven.cgi"><br>
   <h2>Add New Item</h2>
   <table>

    <div id="addmessage"></div>
   <tr><td> SKU: <input type="text" name="sku" id="sku" maxlength="7" pattern="[A-Z]{3}-[0-9]{3}" autofocus required/></td></tr>

   <tr><td>category: <select name="category" id="category" required>
                     <option value="1">Dark Choclate</option>
                     <option value="2">Milk Choclate</option>
                     <option value="3">Truffle</option>
                     <option value="4">Nuts</option>
                     </select><br></td></tr>
  
   <tr><td>Vendor: <select name="vendor" id="vendor" required>
                   <option value="1">Hershey</option>
                   <option value="2">Dairy Milk</option>
                   <option value="3">Nestle</option>
                   <option value="4">Bournville</option>
                   </select><br></td></tr>

   <tr><td>Manufacturer: <input type="text" name="mfid" id="mfid" required></td></tr>
   
   <tr><td>Description: <textarea rows="5" cols="50" name="desc" id="desc" required></textarea></td></tr>
    
    <tr><td>Features: <textarea rows="5" cols="50" name="features" id="features" required></textarea></td></tr>
    
    <tr><td>Cost:  <input type="number"  min="0.00" max="10000.00" step="0.01"  name="cost" id="cost" required></td></tr>
    
    <tr><td>Retail: <input type="number"  min="0.00" max="10000.00" step="0.01"  name="retail" id="retail" class="retail" required></td></tr>
    
    <tr><td>Quantity: <input  type="number" min="1" max="1000" step="1"  name="quantity" id="quantity" required></td></tr>
      <tr>
         <td>Image:<input id ="pic" name="pic" type ="file" accept="image/*" required /> </td>
         </tr>


   <tr><td><input type="reset" name="reset_add" id="reset_add" class="btn btn-primary btn-lg">
  <input type="submit" id="add" name="add" value="Add Product" class="btn btn-primary btn-lg"></td></tr>
</table>

</form>

</div>

<div id="updateEntry" class="tabcontent">
  
 
<form id="updateForm"  method="Post" enctype="multipart/form-data" action="/perl/jadrn034/updateItem.cgi"><br>
   <h2>Update Item</h2>
   <table>
    
   <tr><td>SKU: <input type="text" name="sku_upd" id="sku_upd" maxlength="7" pattern="[A-Z]{3}-[0-9]{3}" autofocus required /></td></tr>

   <tr><td>category: <select name="category_upd" id="category_upd" required >
                     <option value="1">Dark Choclate</option>
                     <option value="2">Milk Choclate</option>
                     <option value="3">Truffle</option>
                     <option value="4">Nuts</option>
    </select></td></tr>

   <tr><td>Vendor: <select name="vendor_upd" id="vendor_upd" required >
                   <option value="1">Hershey</option>
                   <option value="2">Dairy Milk</option>
                   <option value="3">Nestle</option>
                   <option value="4">Bournville</option>
                   </select></td></tr>

   <tr><td>Manufacturer: <input type="text" name="mfid_upd" id="mfid_upd" required></td></tr>

   <tr><td>Description: <textarea rows="5" cols="50" name="desc_upd" id="desc_upd" required></textarea></td></tr>

    <tr><td>Features: <textarea rows="5" cols="50" name="features_upd" id="features_upd" required></textarea></td></tr>

    <tr><td>Cost: <input type="number"  min="0.00" max="10000.00" step="0.01"  name="cost_upd" id="cost_upd" required></td></tr>

    <tr><td>Retail: <input type="number"  min="0.00" max="10000.00" step="0.01"  name="retail_upd" id="retail_upd" class="retail" required ></td></tr>

    <tr><td>Quantity: <input type="number" min="1" max="1000" step="1" name="quantity_upd" id="quantity_upd" required></td></tr>

       <tr style="display: flex; justify-content: center;">
         <td><img id ="pic_upd" name="pic_upd"  type="hidden" height="150" width="150"  /> </td>
         </tr>
         <tr>
         <td><input id ="pic_upd3" name="pic_upd3"  type="hidden" height="42" width="42" /> </td>
         </tr>
         <tr>
         <td>Image: <input id ="pic_upd2" name="pic_upd2" type ="file" accept="image/*"  /> </td>
         </tr>




   <tr><td><input type="reset" name ="reset_upd" id="reset_upd" class="btn btn-primary btn-lg">
  <input type="submit" id="update" name="update" value="update Product" class="btn btn-primary btn-lg"></td></tr>
</table>

</form>

 
 
</div>

<div id="deleteEntry" class="tabcontent">
 
  <form id="deleteForm"  method="Post" enctype="multipart/form-data"><br>
   <h2>Delete Item</h2>
   <table>
    
   <tr><td>SKU: <input type="text" name="sku_del" id="sku_del" maxlength="7" pattern="[A-Z]{3}-[0-9]{3}" autofocus required/> </td></tr>

   <tr><td>category: <select name="category_del" id="category_del" disabled/>
                     <option value="1">Dark Choclate</option>
                     <option value="2">Milk Choclate</option>
                     <option value="3">Truffle</option>
                     <option value="4">Nuts</option>
                     </select></td></tr>
   
   <tr><td>Vendor: <select name="vendor_del" id="vendor_del" disabled/>
                   <option value="1">Hershey</option>
                   <option value="2">Dairy Milk</option>
                   <option value="3">Nestle</option>
                   <option value="4">Bournville</option>
                   </select></td></tr>

   <tr><td>Manufacturer: <input type="text" name="mfid_del" id="mfid_del" disabled /></td></tr>

   <tr><td>Description: <textarea rows="5" cols="50" name="desc_del" id="desc_del" disabled /></textarea></td></tr>

    <tr><td>Features: <textarea rows="5" cols="50" name="features_del" id="features_del" disabled /></textarea></td></tr>

    <tr><td>Cost: <input type="number"  min="0.00" max="10000.00" step="0.01"  name="cost_del" id="cost_del" disabled /><br></td></tr>

    <tr><td>Retail: <input type="number"  min="0.00" max="10000.00" step="0.01"  name="retail_del" id="retail_del" class="retail" disabled /></td></tr>

    <tr><td>Quantity: <input type="number" min="1" max="1000" step="1"  name="quantity_del" id="quantity_del" disabled /></td></tr>
       
       <tr style="display: flex; justify-content: center;">
         <td><img id ="pic_del" name="pic_del" alt="your image" height="150" width="150" disabled /> </td>
         </tr>


   <tr><td><input type="reset" name ="reset_del" id="reset_del" class="btn btn-primary btn-lg">

  <input type="submit" id="delete" name="delete" value="delete Product" class="btn btn-primary btn-lg"></td></tr>
</table>

</form>

</div>





<script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
<script type="text/javascript" src="/~jadrn034/proj1/myScript.js"></script> 
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

</body>
</html>

END_CONTENT
}
###########################################################################    
    





