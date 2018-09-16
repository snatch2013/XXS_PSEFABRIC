import re
import cidr_to_netmask

'''
The list of templates for pan
'''

######## vlan ###########


######## svi ###########


######## address  ###########

def pan_create_address (name, ipv4_prefix, vlan, vrf, interface):
    network, netmask, gate = cidr_to_netmask.cidr_to_netmask(ipv4_prefix)
    config_txt = '''
set shared address %s ip-netwask %s/%s
''' % (name, network, netmask)
    return config_txt

def pan_delete_address (name, ipv4_prefix, vlan, vrf, interface):
    network, netmask, gate = cidr_to_netmask.cidr_to_netmask(ipv4_prefix)
    config_txt = '''
delete shared address %s    
''' % name
    return config_txt

######## address-set  ##########

def pan_create_address_set (name,addresses):
    config_addresses = ''
    for address_element in addresses:
        if ( config_addresses == ''):
            config_addresses = '%s' % address_element
        else:
            config_addresses = config_addresses + ' ' + '%s' % address_element

    config_addresses = '[ ' + config_addresses + ' ]'

    config_txt = '''
set shared address-group %s static %s
''' % (name, config_addresses)
    return config_txt

def pan_delete_address_set (name,addresses):
    config_addresses = ''
    for address_element in addresses:
        if ( config_addresses == ''):
            config_addresses = '%s' % address_element
        else:
            config_addresses = config_addresses + ' ' + '%s' % address_element

    config_addresses = '[ ' + config_addresses + ' ]'

    config_txt = '''
delete shared address-group %s
''' % name
    return config_txt


######### application (services) ###########

def pan_create_application (name, prot, ports):
    if (prot == '6'):
        prot_ = 'tcp'
    elif (prot == '17'):
        prot_ = 'udp'
    elif (prot == '1'):
        prot_ = 'icmp'
    else:
        prot_ = prot
    if 'lower-port' in ports:
        ports_range = '%s-%s' % (ports['lower-port'], ports['upper-port'])
    else:
        ports_range = ''
    config_txt = '''
set shared services %s protocol %s port %s
''' % ( name, prot_, ports_range)

    return config_txt

def pan_delete_application (name, prot, ports):
    config_txt = '''
delete shared services %s''' % name
    return config_txt


######### application-set (services)  ###########

def pan_create_application_set (name, application):

    config_applications = ''

    for application_element in application:
        if re.match(config_applications, ''):
            config_applications = '%s' % application_element
        else:
            config_applications =  config_applications + ' ' + '%s' % application_element

    config_applications = '[ ' + config_applications + ' ]'


    config_txt='''
set shared service-group %s member %s
''' % (name, config_applications)

    return config_txt

def pan_delete_application_set (name, application):

    config_applications = '''
delete shared service-group %s
''' % name
    return config_txt

######### access ###########

def pan_create_access (name, source_address_set_list, destination_address_set_list, application_set_list, action ):
    config_access = ''

    for source_address_set_element in source_address_set_list:
        if re.match(config_match_source, ''):
            config_match_source = '%s' % source_address_set_element['address-set-name']
        else:
            config_match_source = config_match_source + ' %s' % source_address_set_element['address-set-name']

    config_match_source = '[ ' + config_match_source + ' ]'

    for destination_address_set_element in destination_address_set_list:
        if re.match(config_match_destination, ''):
            config_match_destination = '%s' % destination_address_set_element['address-set-name']
        else:
            config_match_destination = config_match_destination + ' %s' % destination_address_set_element['address-set-name']

    config_match_destination = '[ ' + config_match_destination + ' ]'

    for application_element in application_list['application-set']:
        if re.match(config_match_application, ''):
            config_match_application = ' %s' % application_element
        else:
            config_match_application = config_match_application + ' %s' % application_element

    config_match_application = '[ ' + config_match_application + ' ]'

    config_txt = '''
ip access-list extended all_vlans_out
%s''' % config_access

    return config_txt
