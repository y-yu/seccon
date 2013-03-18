%mail_to = (
	tech     => 'tech@some.addr',
	support  => 'support@some.addr',
	customer => 'customer@some.addr',
	other    => 'other@some.addr',
	maintain => 'maintain@some.addr',
);

my $key     = $q->param('mail_to');
my $mail_to = $mail_to{$key};
