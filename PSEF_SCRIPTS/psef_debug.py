'''
There is a powful debuging mechanism in psefabric. You may examine almost any essential internal data exhange.
If debugging is on this information is saved in the folder PSEFABRIC/PSEF_LOGS/.
For comfort of reading they will be saved in json format.
'''
import versionfile
import json
import os
import versionfile as vrs
import copy

deb = True # globaly turns on/off the debuging 

# tuns on/off the debugging per element
debug   = {}
debug['psef_conf_new'] = True
debug['psef_conf_old'] = True
debug['address_index_new'] = True
debug['address_index_old'] = True
debug['address_set_index_new'] = True
debug['address_set_index_old'] = True
debug['policy_index'] = True
debug['ddiff'] = True
debug['diff_dict'] = True
debug['cmd_for_host'] = True
debug['cfg'] = True

def version_file(dict_name, dict_debug):

##########  Description  #######
    '''
    '''
#############  BODY ############

    path_ = '../PSEF_LOGS/%s.txt' % dict_name
    if not  os.path.isfile(path_):
        open(path_, 'a')
    if (vrs.VersionFile(path_)):
        with open(path_, 'w') as f10:
            f10.write(dict_debug)
            f10.flush()
    else:
        print ("Versioning file failed")

def ChangeType (dict_, type_):

##########  Description  #######
    '''
    For using json.dumps we need to change tuple type of the keys (DC, VRF) to str type 
    '''
#############  BODY ############

    if (type_ == "policy"):
        policy_ = copy.deepcopy(dict_)
        for policy_element in policy_['rm']:
            for struct_key in policy_element['match']['source-addresses'].keys():
                new_str_key = "(%s,%s)" % struct_key
                policy_element['match']['source-addresses'][new_str_key] = policy_element['match']['source-addresses'][struct_key]
                del policy_element['match']['source-addresses'][struct_key]
            for struct_key in policy_element['match']['destination-addresses'].keys():
                new_str_key = "(%s,%s)" % struct_key
                policy_element['match']['destination-addresses'][new_str_key] = policy_element['match']['destination-addresses'][struct_key]
                del policy_element['match']['destination-addresses'][struct_key]
        for policy_element in policy_['ad']:
            for struct_key in policy_element['match']['source-addresses'].keys():
                new_str_key = "(%s,%s)" % struct_key
                policy_element['match']['source-addresses'][new_str_key] = policy_element['match']['source-addresses'][struct_key]
                del policy_element['match']['source-addresses'][struct_key]
            for struct_key in policy_element['match']['destination-addresses'].keys():
                new_str_key = "(%s,%s)" % struct_key
                policy_element['match']['destination-addresses'][new_str_key] = policy_element['match']['destination-addresses'][struct_key]
                del policy_element['match']['destination-addresses'][struct_key]
        return policy_
    elif (type_ == "address_set"):
        address_set_ = copy.deepcopy(dict_)
        for address_set_element in address_set_.keys():
            for struct_key in address_set_[address_set_element]["structure-to-addresses"].keys():
                new_str_key = "(%s,%s)" % struct_key
                address_set_[address_set_element]["structure-to-addresses"][new_str_key]= address_set_[address_set_element]["structure-to-addresses"][struct_key]
                del address_set_[address_set_element]["structure-to-addresses"][struct_key]
        return address_set_
    else:
        print "Incorrect parameters in ChangeType"

def WriteDebug (dict_name, dict_):

##########  Description  #######
    '''
    '''
#############  BODY ############

    if dict_name in debug.keys():
        if (dict_name == 'policy_index'):
            dict_ = ChangeType(dict_, 'policy')
        elif (dict_name == 'address_set_index_new' or dict_name == 'address_set_index_old'): 
            dict_ = ChangeType(dict_, 'address_set')
        if debug[dict_name]:
            dict_context = json.dumps(dict_, skipkeys=False, indent=2)
            version_file(dict_name, dict_context)
    else:
        print "If you need to debug this dict add to the dict debug in file debug.py"    

