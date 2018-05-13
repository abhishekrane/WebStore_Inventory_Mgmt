use DBI;
use CGI;
$q = new CGI;
use CGI::Carp qw (fatalsToBrowser);
use File::Basename;

    ####################################################################
### constants
$CGI::POST_MAX = 1024 * 3000; # Limit file size to 3MB
my $upload_dir = '/home/jadrn034/public_html/proj1/file_upload';
my $safe_filename_chars = "a-zA-Z0-9_.-";
####################################################################

my $filename = $q->param("pic");
if(!$filename) {
    
    }
   else{ 
my ($name, $path, $extension) = fileparse($filename, '/..*/');
$filename = $name.$extension;
$filename =~ s/ //; #remove any spaces
if($filename !~ /^([$safe_filename_chars]+)$/) {
    die "Sorry, invalid character in the filename.";
    }   

$filename = untaint($filename);

# get a handle on the uploaded image     
my $filehandle = $q->upload("pic"); 

unless($filehandle) { die "Invalid handle"; }

# save the file
open UPLOADFILE, ">$upload_dir/$filename" or die
    "Error, cannot save the file.";
binmode UPLOADFILE;
while(<$filehandle>) {
    print UPLOADFILE $_;
    }
close UPLOADFILE;



# this is needed because mod_perl runs with -T (taint mode), and thus the
# filename is insecure and disallowed unless untainted. Return values
# from a regular expression match are untainted.
sub untaint {
    if($filename =~ m/^(\w+)$/) { die "Tainted filename!"; }
    return $1;
    }


}



my $host = "opatija.sdsu.edu";
my $port = "3306";
my $database = "jadrn034";
my $username = "jadrn034";
my $password = "suitcase";
my $database_source = "dbi:mysql:$database:$host:$port";


my $sku = $q->param("sku");
my $category  = $q->param("category");
my $vendor  = $q->param("vendor");
my $mfid  = $q->param("mfid");
my $desc = $q->param("desc");
my $features = $q->param("features");
my $cost  = $q->param("cost");
my $retail  = $q->param("retail");
my $quantity = $q->param("quantity");

my $filename = $q->param("pic");

my $dbh = DBI->connect($database_source, $username, $password)
	or die "Cannot connect to DB";
my $sth = $dbh->prepare("INSERT INTO product (sku, catID, venID,vendorModel,description,features,cost, retail, quantity,image) VALUES('$sku','$category','$vendor','$mfid','$desc','$features','$cost','$retail','$quantity','$filename');");

$sth->execute();
my $number_of_rows = $sth->rows;
$sth->finish();
$dbh->disconnect();

if($number_of_rows == 1){
print <<EOF;
Content-type:  text/html

<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<meta http-equiv="refresh"
   content="2; url=http://jadran.sdsu.edu/~jadrn034/proj1/index.html">

<head>
	<meta http-equiv="content-type" 
		content="text/html;charset=utf-8" />	
	<link rel="stylesheet" href="/~jadrn034/proj1/confirm.css" type="text/css"> 
	
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
EOF







	}
else {
	print " The sku is Duplicate";
	}
    



