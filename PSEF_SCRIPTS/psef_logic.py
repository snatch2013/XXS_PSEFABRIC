'''
This is essential element of the demultiplexer layes of Psefabric Dataflow Model and one of the key elements of the psefabric concept.
The python dictionaries created here are used in multiplexer.py.
The matter is that depending on the values of the structural elements (for networks in this realization) we have to program a specific set of commands for different MOs.
And we need some algorithm for that. So these dictionaries describe this logic.

We need to program logic for the adding/removal of addresses, address-sets, applications, application-sets, policies. So we have:

def mult_dict_address()
def mult_dict_address_set()
def mult_dict_application()
def mult_dict_application_set()
def mult_dict_policy()
'''

import copy
import host_to_type

def mult_dict_address():

##########  Description  #######
    '''
    key 'DC' meens any dc.
    key 'no_vlan' corresponds vlan = 0
    key 'vlan' meens any vlan not equal 0
    '''
#############  BODY ############

    mult = {}
    mult[('DC', 'no_vlan')]=[]
    mult[('DC', 'no_vlan')].append({})
    mult[('DC', 'no_vlan')][0]['eq_addr'] = 'OSS_AA'
    mult[('DC', 'no_vlan')][0]['cmd'] = {}
    mult[('DC', 'no_vlan')][0]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][0]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][0]['cmd']['ad'].append('ptemplates.pan_create_address')
    mult[('DC', 'no_vlan')][0]['cmd']['rm'].append('ptemplates.pan_delete_address')

    mult[('DC', 'no_vlan')].append({})
    mult[('DC', 'no_vlan')][1]['eq_addr'] = 'OSS_INTERNET'
    mult[('DC', 'no_vlan')][1]['cmd'] = {}
    mult[('DC', 'no_vlan')][1]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][1]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][1]['cmd']['rm'].append('ptemplates.pan_delete_address')
    mult[('DC', 'no_vlan')][1]['cmd']['ad'].append('ptemplates.pan_create_address')

    mult[('DC', 'no_vlan')].append({})
    mult[('DC', 'no_vlan')][2]['eq_addr'] = 'INTERNAL_AA'
    mult[('DC', 'no_vlan')][2]['cmd'] = {}
    mult[('DC', 'no_vlan')][2]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][2]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][2]['cmd']['rm'].append('ptemplates.pan_delete_address')
    mult[('DC', 'no_vlan')][2]['cmd']['ad'].append('ptemplates.pan_create_address')

    mult[('DC', 'no_vlan')].append({})
    mult[('DC', 'no_vlan')][3]['eq_addr'] = 'EXTERNAL_AA'
    mult[('DC', 'no_vlan')][3]['cmd'] = {}
    mult[('DC', 'no_vlan')][3]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][3]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][3]['cmd']['rm'].append('ptemplates.pan_delete_address')
    mult[('DC', 'no_vlan')][3]['cmd']['ad'].append('ptemplates.pan_create_address')

    mult[('DC', 'no_vlan')].append({})
    mult[('DC', 'no_vlan')][4]['eq_addr'] = 'CORPO_INTERNET'
    mult[('DC', 'no_vlan')][4]['cmd'] = {}
    mult[('DC', 'no_vlan')][4]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][4]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][4]['cmd']['rm'].append('ptemplates.pan_delete_address')
    mult[('DC', 'no_vlan')][4]['cmd']['ad'].append('ptemplates.pan_create_address')

    return (mult)

def mult_dict_address_set():

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    mult.append({})
    mult[0]['eq_addr'] = 'OSS_AA'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['rm'].append('ptemplates.pan_delete_address_set')
    mult[0]['cmd']['ad'].append('ptemplates.pan_create_address_set')

    mult.append({})
    mult[1]['eq_addr'] = 'OSS_INTERNET'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['rm'].append('ptemplates.pan_delete_address_set')
    mult[1]['cmd']['ad'].append('ptemplates.pan_create_address_set')

    mult.append({})
    mult[2]['eq_addr'] = 'INTERNAL_AA'
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []
    mult[2]['cmd']['rm'].append('ptemplates.pan_delete_address_set')
    mult[2]['cmd']['ad'].append('ptemplates.pan_create_address_set')

    mult.append({})
    mult[3]['eq_addr'] = 'EXTERNAL_AA'
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []
    mult[3]['cmd']['rm'].append('ptemplates.pan_delete_address_set')
    mult[3]['cmd']['ad'].append('ptemplates.pan_create_address_set')

    mult.append({})
    mult[4]['eq_addr'] = 'CORPO_INTERNET'
    mult[4]['cmd'] = {}
    mult[4]['cmd']['ad'] = []
    mult[4]['cmd']['rm'] = []
    mult[4]['cmd']['rm'].append('ptemplates.pan_delete_address_set')
    mult[4]['cmd']['ad'].append('ptemplates.pan_create_address_set')

    return (mult)

def mult_dict_application(): 

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    mult.append({})
    mult[0]['eq_addr'] = 'OSS_AA'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'].append('ptemplates.pan_delete_application')
    mult[0]['cmd']['ad'].append('ptemplates.pan_create_application')
    
    mult.append({}) 
    mult[1]['eq_addr'] = 'OSS_INTERNET'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['rm'].append('ptemplates.pan_delete_application')
    mult[1]['cmd']['ad'].append('ptemplates.pan_create_application')

    mult.append({})
    mult[2]['eq_addr'] = 'INTERNAL_AA'
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []
    mult[2]['cmd']['rm'].append('ptemplates.pan_delete_application')
    mult[2]['cmd']['ad'].append('ptemplates.pan_create_application')

    mult.append({})
    mult[3]['eq_addr'] = 'EXTERNAL_AA'
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []
    mult[3]['cmd']['rm'].append('ptemplates.pan_delete_application')
    mult[3]['cmd']['ad'].append('ptemplates.pan_create_application')

    mult.append({})
    mult[4]['eq_addr'] = 'CORPO_INTERNET'
    mult[4]['cmd'] = {}
    mult[4]['cmd']['ad'] = []
    mult[4]['cmd']['rm'] = []
    mult[4]['cmd']['rm'].append('ptemplates.pan_delete_application')
    mult[4]['cmd']['ad'].append('ptemplates.pan_create_application')

    return (mult)

def mult_dict_application_set():

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    mult.append({})
    mult[0]['eq_addr'] = 'OSS_AA'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'].append('ptemplates.pan_delete_application_set')
    mult[0]['cmd']['ad'].append('ptemplates.pan_create_application_set')

    mult.append({})
    mult[1]['eq_addr'] = 'OSS_INTERNET'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['rm'].append('ptemplates.pan_delete_application_set')
    mult[1]['cmd']['ad'].append('ptemplates.pan_create_application_set')

    mult.append({})
    mult[2]['eq_addr'] = 'INTERNAL_AA'
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []
    mult[2]['cmd']['rm'].append('ptemplates.pan_delete_application_set')
    mult[2]['cmd']['ad'].append('ptemplates.pan_create_application_set')

    mult.append({})
    mult[3]['eq_addr'] = 'EXTERNAL_AA'
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []
    mult[3]['cmd']['rm'].append('ptemplates.pan_delete_application_set')
    mult[3]['cmd']['ad'].append('ptemplates.pan_create_application_set')

    mult.append({})
    mult[4]['eq_addr'] = 'CORPO_INTERNET'
    mult[4]['cmd'] = {}
    mult[4]['cmd']['ad'] = []
    mult[4]['cmd']['rm'] = []
    mult[4]['cmd']['rm'].append('ptemplates.pan_delete_application_set')
    mult[4]['cmd']['ad'].append('ptemplates.pan_create_application_set')

    return (mult)

def mult_dict_policy():

##########  Description  #######
    '''
 same_dc - src and dst datacenters are the same
 diff_dc - src and dst datacenters are differenet
 same_vrf - src and dst vrf are the same
 diff_vrf - src and dstsrc and dst datacenters are the same
    '''
#############  BODY ############

    mult = {}
    mult[('diff_vrf','OSS_AA', 'OSS_AA')]=[]
    mult[('diff_vrf','OSS_AA', 'OSS_AA')].append({})
    mult[('diff_vrf','OSS_AA', 'OSS_AA')][0]['eq_addr'] = 'oss'
    mult[('diff_vrf','OSS_AA', 'OSS_AA')][0]['cmd'] = {}
    mult[('diff_vrf','OSS_AA', 'OSS_AA')][0]['cmd']['ad'] = []
    mult[('diff_vrf','OSS_AA', 'OSS_AA')][0]['cmd']['rm'] = []
    mult[('diff_vrf','OSS_AA', 'OSS_AA')][0]['cmd']['rm'].append('ptemplates.pan_delete_policy')
    mult[('diff_vrf','OSS_AA', 'OSS_AA')][0]['cmd']['ad'].append('ptemplates.pan_delete_policy_all-app_dst-oss-transit')
    mult[('diff_vrf','OSS_AA', 'OSS_AA')][0]['cmd']['ad'].append('ptemplates.pan_delete_policy_src-oss-transit')
    mult[('diff_vrf','OSS_AA', 'OSS_AA')][0]['cmd']['ad'].append('ptemplates.pan_create_policy')
    mult[('diff_vrf','OSS_AA', 'OSS_AA')][0]['cmd']['ad'].append('ptemplates.pan_create_policy_all-app_dst-oss-transit')
    mult[('diff_vrf','OSS_AA', 'OSS_AA')][0]['cmd']['ad'].append('ptemplates.pan_create_policy_src-oss-transit')

    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')]=[]
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')].append({})
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')][0]['eq_addr'] = 'OSS_AA'
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')][0]['cmd'] = {}
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')][0]['cmd']['ad'] = []
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')][0]['cmd']['rm'] = []
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')][0]['cmd']['rm'].append('ptemplates.pan_delete_policy_all-app_dst-inter-area')
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')][0]['cmd']['ad'].append('ptemplates.pan_create_policy_all-app_dst-inter-area')
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')].append({})
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')][1]['eq_addr'] = 'corpo_int'
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')][1]['cmd'] = {}
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')][1]['cmd']['ad'] = []
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')][1]['cmd']['rm'] = []
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')][1]['cmd']['rm'].append('ptemplates.pan_delete_policy_src-inter-area')
    mult[('diff_vrf','OSS_AA', 'INTERNAL_AA')][1]['cmd']['ad'].append('ptemplates.pan_create_policy_src-inter-area')

    return mult

