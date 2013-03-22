my $q = CGI->new;

my $mail_to = $q->param('mail_to');

open my $mh, "|/usr/sbin/sendmail -t $mail_to";
