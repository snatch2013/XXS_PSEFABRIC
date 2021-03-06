'''
The psefabric.py is the dataflow manager. It runs scripts in the correct order and is responsible for exchanging data between them.
'''

import xmltodict
from deepdiff import DeepDiff
import re
from ncclient import manager
import os
import versionfile as vrs

import cda
import psef_index
import multiplexer
import cfg
import mult_cfg
import json
import psef_debug
import copy

PSEFABRIC =os.environ['PSEFABRIC'] + "/PSEFABRIC"

def version_file(flg_ok_):
    if (re.search (flg_ok_, "OK")):
        if os.path.isfile("%s/PSEF_CONF/pse-config.xml" % PSEFABRIC):
            if (vrs.VersionFile("%s/PSEF_CONF/pse-config.xml" % PSEFABRIC)):
                with open('%s/PSEF_CONF/pse-config.xml' % PSEFABRIC, 'w') as f3:
                    f3.write(c)
                    f3.flush()
                print ("OK")
            else:
                print ("Versioning file failed")
        else:
            if (os.system("cp $PSEFABRIC/PSEFABRIC/PSEF_CONF/pse-config-initial.xml $PSEFABRIC/PSEFABRIC/PSEF_CONF/pse-config.xml.000 2>/dev/null")):
                print ("cp pse-config-initial.xml pse-config.xml failed")
            else:
                with open('%s/PSEF_CONF/pse-config.xml' % PSEFABRIC, 'w') as f4:
                    f4.write(c)
                    f4.flush()
                print("OK")


########  Main body ########

# logins
username='admin'
password='admin'
host='127.0.0.1'
port = 2022
diff_dict_full =''
diff_dict = ''

# take new and old xml config files and transfirm them to the dictionaries

with manager.connect(host = '127.0.0.1', port = 2022, username = 'admin', password = 'admin', hostkey_verify=False) as m:
    c = m.get_config(source='running').data_xml
    psef_conf_new_ = xmltodict.parse(c)

if os.path.isfile('%s/PSEF_CONF/pse-config.xml' % PSEFABRIC):
    with open('%s/PSEF_CONF/pse-config.xml' % PSEFABRIC) as fd2:
        psef_conf_old_  = xmltodict.parse(fd2.read())
    fd2.close() 
elif os.path.isfile('%s/PSEF_CONF/pse-config-initial.xml' % PSEFABRIC):
    with open('%s/PSEF_CONF/pse-config-initial.xml' % PSEFABRIC) as fd1:
        psef_conf_old_  = xmltodict.parse(fd1.read())
    fd1.close()
else:
#    if (os.system("python create_pse_config_initial.py 2>/dev/null")):
    if (os.system("python $PSEFABRIC/PSEFABRIC/PSEF_SCRIPTS/create_pse_config_initial.py")):
        print "Failed to create pse-config-initial.xml"
    else:
        print "pse-config-initial.xml has been created"
        with open('%s/PSEF_CONF/pse-config-initial.xml' % PSEFABRIC) as fd1:
            psef_conf_old_  = xmltodict.parse(fd1.read())
        fd1.close()

# correct these dictionaries with the def cda.dict_correct (see the description of the dict_correct)

cda.psef_conf_new =  cda.dict_correct(psef_conf_new_)
cda.psef_conf_old =  cda.dict_correct(psef_conf_old_)


# make indexation by addresses and address-sets with the def cda.address_index (see the description of the address_index)

(psef_index.address_index_new, psef_index.address_set_index_new)  = psef_index.address_index (cda.psef_conf_new)
(psef_index.address_index_old, psef_index.address_set_index_old)  = psef_index.address_index (cda.psef_conf_old)

(psef_index.service_index_new, psef_index.service_set_index_new)  = psef_index.service_index (cda.psef_conf_new)
(psef_index.service_index_old, psef_index.service_set_index_old)  = psef_index.service_index (cda.psef_conf_old)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('psef_conf_new', cda.psef_conf_new)
    psef_debug.WriteDebug('psef_conf_old', cda.psef_conf_old)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('address_index_new', psef_index.address_index_new)
    psef_debug.WriteDebug('address_index_old', psef_index.address_index_old)
    psef_debug.WriteDebug('address_set_index_new', psef_index.address_set_index_new)
    psef_debug.WriteDebug('address_set_index_old', psef_index.address_set_index_old)
    psef_debug.WriteDebug('service_index_new', psef_index.service_index_new)
    psef_debug.WriteDebug('service_index_old', psef_index.service_index_old)
    psef_debug.WriteDebug('service_set_index_new', psef_index.service_set_index_new)
    psef_debug.WriteDebug('service_set_index_old', psef_index.service_set_index_old)



# make the difference between new and old configs


cda.psef_conf_new = cda.dict_full_policy(cda.psef_conf_new, psef_index.address_set_index_new, psef_index.service_set_index_new, psef_index.address_index_new, psef_index.service_index_new)
cda.psef_conf_old = cda.dict_full_policy(cda.psef_conf_old, psef_index.address_set_index_old, psef_index.service_set_index_old, psef_index.address_index_old, psef_index.service_index_old)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('psef_conf_policy_full_new', cda.psef_conf_new)
    psef_debug.WriteDebug('psef_conf_policy_full_old', cda.psef_conf_old)

ddiff = DeepDiff(cda.psef_conf_old, cda.psef_conf_new, verbose_level=2, ignore_order=True, report_repetition=False)


if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('ddiff', ddiff)

# transform the structure of the ddiff dictionary to more convinient view
diff_dict_full = cda.ddiff_dict(ddiff)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('diff_dict_full', diff_dict_full)

#diff_dict = cda.diff_opt(diff_dict_full)

#if psef_debug.deb:   # if debuging is on then:
#    psef_debug.WriteDebug('diff_dict', diff_dict)

# Extract set of commands for each MO

multiplexer.cmd_for_host = {}
multiplexer.policy_index_ = {}
multiplexer.initiate_cmd_for_host()
multiplexer.policy_index_ = {'ad':[], 'rm':[]}
multiplexer.multiplex(diff_dict_full)

cmd_for_host_full = copy.deepcopy(multiplexer.cmd_for_host)
policy_index_full = copy.deepcopy(multiplexer.policy_index_)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('cmd_for_host_full', cmd_for_host_full)
    psef_debug.WriteDebug('policy_index', policy_index_full)

cmd_for_host_diff = multiplexer.policy_opt(cmd_for_host_full)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('cmd_for_host_diff', cmd_for_host_diff)

# Create configyration
cfg.cfg = cfg.create_configs(cmd_for_host_diff, cmd_for_host_full)
if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('cfg', cfg.cfg)

# Write configuration to files
flg_ok = mult_cfg.mult_cfg(cfg.cfg)

# Write configuration of psefabric
version_file(flg_ok)

