'''
When there are no  any saved psefabric configs, you need to create pse-config-initial.xml. 
We need something to compare our new config with. So the next config will be compared with this one.
'''

import os

PSEFABRIC = os.environ['PSEFABRIC'] + "/PSEFABRIC"

from ncclient import manager

filename = '%s/PSEF_CONF/pse-config-initial.xml' % PSEFABRIC

with manager.connect(host='127.0.0.1', port=2022, username='admin', password='admin', hostkey_verify=False) as m:
    c = m.get_config(source='running').data_xml
    with open(filename, 'a') as fl:
        fl.write(c)
        fl.flush()
