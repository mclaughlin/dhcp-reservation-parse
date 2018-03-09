# dhcp-reservation-parse
---
These scripts parse DHCP reservcation configs, both from [config-to-csv](https://github.com/mclaughlin/dhcp-reservation-parse/blob/master/csv-to-config.py>) and [csv-to-config](https://github.com/mclaughlin/dhcp-reservation-parse/blob/master/config-to-csv.py).

csv-to-conifg.py usage:
------------

Example csv input (from file):

    host my-printer,#comments #location: my desk,fixed-address 10.1.2.3,hardware ethernet 00:ef:29:21:ba:6b,option routers 10.1.1.1,option subnet-mask 255.255.0.0,option domain-name "domain-name.com"

Example call (this will output to stdout):

    ./csv-to-config.py src/dhcp.csv

...or to run using pipenv:

    $ pipenv run ./csv-to-config.py src/dhcp.csv

Specify an output file:

    $ ./csv-to-config.py src/dhcp.csv output/printers.conf

...or redirect stdout to a file:

    $ ./csv-to-config.py src/dhcp.csv > output/printers.conf

Example output:

    host my-printer {
        #comment #location: my desk
        fixed-address 10.1.2.3;
        hardware ethernet 00:ef:29:21:ba:6b;
        option routers 10.1.1.1;
        option subnet-mask 255.255.0.0;
        option domain-name "domain-name.com";
    }

config-to-csv.py usage:
------------

Example dhcp config input (from file):

    host my-printer {
        #comment #location: my desk
        fixed-address 10.1.2.3;
        hardware ethernet 00:ef:29:21:ba:6b;
        option routers 10.1.1.1;
        option subnet-mask 255.255.0.0;
        option domain-name "domain-name.com";
    }

Example call:

    ./config-to-csv.py src/printers.conf

...or to run using pipenv:

    pipenv run ./config-to-csv.py src/printers.conf

Specify an output file:

    $ ./config-to-csv.py src/printers.conf output/dhcp.csv

...or redirect stdout to a file:

    $ ./config-to-csv.py src/printers.conf > output/dhcp.csv

Example output:

    host my-printer,#comments #location: my desk,fixed-address 10.1.2.3,hardware ethernet 00:ef:29:21:ba:6b,option routers 10.1.1.1,option subnet-mask 255.255.0.0,option domain-name "domain-name.com"
