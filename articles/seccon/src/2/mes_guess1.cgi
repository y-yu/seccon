use strict;
use CGI;

my $q = CGI->new;

my $mail_to  = $q->param('mail_to');
my $contents = $q->param('comments');

open my $mh, "|/usr/sbin/sendmail -t $mail_to";

print $mh "From: .......\n";
print $mh "To: .......\n";
print $mh "Subject: .......\n\n";
print $mh $comments;

close $mh;

print $q->header;
print "<html>\n"
...
