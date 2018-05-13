#!/usr/bin/perl 

#   file upload script.  
#   Remember that you MUST use enctype="mulitpart/form-data"
#   in the web page that invokes this script, and the destination 
#   directory for the uploaded file must have permissions set to 777.  
#   Do NOT set 777 permission on any other directory in your account!
#   
#   CS645, Spring 2013
#   Alan Riggins
use DBI;
use CGI;
use CGI::Carp qw (fatalsToBrowser);
use File::Basename;

####################################################################
### constants
$CGI::POST_MAX = 1024 * 3000; # Limit file size to 3MB
my $upload_dir = '/home/jadrn034/public_html/proj1/file_upload';
my $safe_filename_chars = "a-zA-Z0-9_.-";
####################################################################

my $q = new CGI;
my $filename = $q->param("pic");
unless($filename) {
    die "There was a problem uploading the image; ".
        "it's probably too big.";
    }
    
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





my $q = new CGI;





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

my $dbh1 = DBI->connect($database_source, $username, $password)
    or die "Cannot connect to DB";
my $dbh2 = DBI->connect($database_source, $username, $password)
    or die "Cannot connect to DB";

my $sth1 = $dbh1->prepare("SELECT sku FROM product where sku='$sku'");
$sth1->execute();
my $number_of_rows = $sth1->rows;
$sth1->finish();
$dbh1->disconnect();


print "content-type: text/html\n\n";
if($number_of_rows == 0) {
    
    print "$filename";
 my $sth2 = $dbh2->prepare("INSERT INTO product (sku, catID, venID,vendorModel,description,features,cost, retail, quantity,image) VALUES('$sku','$category','$vendor','$mfid','$desc','$features','$cost','$retail','$quantity','$filename');");

$sth2->execute();

$sth2->finish();
$dbh2->disconnect();
    }
else {
    print " The sku is Duplicate";
    }
