use DBI;
use CGI;
use CGI::Cookie

$q = new CGI;

my $host = "opatija.sdsu.edu";
my $port = "3306";
my $database = "jadrn034";
my $username = "jadrn034";
my $password = "suitcase";
my $database_source = "dbi:mysql:$database:$host:$port";


my $sku_del = $q->param("sku_del");




my $dbh = DBI->connect($database_source, $username, $password)
	or die "Cannot connect to DB";
my $sth = $dbh->prepare("Delete from product where sku = '$sku_del'");


$sth->execute();
my $number_of_rows = $sth->rows;
$sth->finish();
$dbh->disconnect();


print "content-type: text/html\n\n";
if($number_of_rows == 0) {
	
	

print "Error";

	}
else {

print "deleted";

	
	}
    