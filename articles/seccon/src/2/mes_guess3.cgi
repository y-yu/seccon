my $q = CGI->new;

my $name     = $q->param('name');
my $email    = $q->param('email');
my $contents = $q->param('contents');
my $key      = $q->param('mail_to');
my $mail_to  = $mail_to{$key};

open my $mh, "|/usr/sbin/sendmail -t $mail_to";

# header
print $mh "From: $email\n";
print $mh "To: $mail_to\n";
print $mh "Subject: User Message\n\n";

# body
print $mh "User Name: $name\n";
print $mh "-------------";
print $mh $contents;
print $mh "-------------";

close $mh;

