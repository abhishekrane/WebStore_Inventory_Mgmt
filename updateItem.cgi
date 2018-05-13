use CGI;
use DBI;
use CGI::Carp qw (fatalsToBrowser);
use File::Basename;


$q = new CGI;
my $sku_upd = $q->param("sku_upd");
my $category_upd  = $q->param("category_upd");
my $vendor_upd  = $q->param("vendor_upd");
my $mfid_upd  = $q->param("mfid_upd");
my $desc_upd = $q->param("desc_upd");
my $features_upd = $q->param("features_upd");
my $cost_upd  = $q->param("cost_upd");
my $retail_upd  = $q->param("retail_upd");
my $quantity_upd = $q->param("quantity_upd");
my $image = $q->param('pic_upd2');

my $host = 'opatija.sdsu.edu';
my $port = '3306';
my $database = 'jadrn034';
my $username = 'jadrn034';
my $password = 'suitcase';

my $database_source = "dbi:mysql:$database:$host:$port";
my $dbh = DBI->connect($database_source, $username, $password)
	or die "Cannot connect to DB";

if($image){
my $sth = $dbh->prepare("UPDATE product SET catID = '$category_upd', venID='$vendor_upd', vendorModel='$mfid_upd', description='$desc_upd', features = '$features_upd', cost= '$cost_upd', retail= '$retail_upd', quantity = '$quantity_upd', image ='$image' where sku = '$sku_upd'");
$sth->execute();
my $number_of_rows = $sth->rows;
$sth->finish();

}
else{
my $sth = $dbh->prepare("UPDATE product SET catID = '$category_upd', venID='$vendor_upd', vendorModel='$mfid_upd', description='$desc_upd', features = '$features_upd', cost= '$cost_upd', retail= '$retail_upd', quantity = '$quantity_upd' where sku = '$sku_upd'");
$sth->execute();
my $number_of_rows = $sth->rows;
$sth->finish();
}


$dbh->disconnect();





####################################################################
### constants
$CGI::POST_MAX = 1024 * 3000; # Limit file size to 3MB
my $upload_dir = '/home/jadrn034/public_html/proj1/file_upload';
my $safe_filename_chars = "a-zA-Z0-9_.-";
####################################################################


my $filename = $q->param("pic_upd2");
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
my $filehandle = $q->upload("pic_upd2"); 

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


if($number_of_rows == 0) {
	
print <<EOF;
Content-type:  text/html

<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
	<meta http-equiv="content-type" 
		content="text/html;charset=utf-8" />
		<meta http-equiv="refresh"
   content="2; url=http://jadran.sdsu.edu/~jadrn034/proj1/index.html">	
	<link rel="stylesheet" href="/~jadrn034/proj1/confirm.css" type="text/css"> 
	
</head>
<body>
<h2>Success, the details has been uploaded</h2>
<table>
<tr><td>SKU: $sku_upd</td></tr>
<tr><td>Category ID: $category_upd</td></tr>
<tr><td>Vendor ID: $vendor_upd</td></tr>
<tr><td>Manufacturer ID: $mfid_upd</td></tr>
<tr><td>Description: $desc_upd</td></tr>
<tr><td>Features: $features_upd</td></tr>
<tr><td>cost: $cost_upd</td></tr>
<tr><td>Retail: $retail_upd </td></tr>
<tr><td>Quantiy: $quantity_upd</td></tr>

</table>
<input type="button" onclick="location.href='http://jadran.sdsu.edu/~jadrn034/proj1/';" value="Login" />
<h2> You are been logged out. CLick here to Login. </h2>
</body>
</html>
EOF

	}
else {

print $filename;

	
	}