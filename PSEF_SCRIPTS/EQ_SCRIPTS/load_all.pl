#!/usr/bin/perl

# Loads config files on all equipment (one vy one).
# Run the script cput_txt.pl sequentially for each hosts in array @cisco_list,
# then run the script jput_xml.pl sequentially for each hosts in array @juniper_list

sub cisco_load_config {
    my $host = shift;
    print "$host...\n";
    my $output = system ("perl cput_txt.pl -h $host > ./cisco/$host_out.txt 2 > $host_err.txt");
    print "$host OK\n";
}

sub juniper_load_config {
    my $host = shift;
    print "$host...\n"; 
    my $output = system ("perl jput_xml.pl -h $host > ./juniper/$host_out.txt 2 > $host_err.txt");
    print "$host OK\n";
}

@cisco_list = ('192.168.31.133', '192.168.31.136', '192.168.31.137', '192.168.31.138', '192.168.31.139');
@juniper_list = ('192.168.31.134');

foreach (@cisco_list) {
#     print "$_\n";
    cisco_load_config($_);
}
foreach (@juniper_list) {
#    print "$_\n";
    juniper_load_config($_);
} 