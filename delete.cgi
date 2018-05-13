use CGI;
use DBI;

my $q = new CGI;
my $sku = $q->param('sku_del');

my $host = 'opatija.sdsu.edu';
my $port = '3306';
my $database = 'jadrn034';
my $username = 'jadrn034';
my $password = 'suitcase';
my $response = "";
my $database_source = "dbi:mysql:$database:$host:$port";
my $dbh = DBI->connect($database_source, $username, $password)
	or die "Cannot connect to DB";
	
my $sth = $dbh->prepare("SELECT * FROM product where sku='$sku'");
$sth->execute();
my $number_of_rows = $sth->rows;

while(my @row=$sth->fetchrow_array()) {
    foreach $item (@row) {    
        $response .= $item."|"; #field separator
        }
    $response = substr $response, 0, (length($response)-1);  
    $response .= "||";  #record separator
    } 
    $response = substr $response, 0, (length($response)-2);     
unless($response) {
    $response = "invalid";
    }    



$sth->finish();
$dbh->disconnect();
print "content-type: text/html\n\n";
if($number_of_rows == 1) {
	print $response;

	}
else {
	print "No such SkU";
	}
