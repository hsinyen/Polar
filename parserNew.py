#Last Update: July 29th

from lxml import etree

a = '<xml><network><subdomain>SUBDOMAIN_NAME_HERE</subdomain><id>NETWORK_ID_HERE</id></network></xml>'
a = '<xml><network><subdomain>SUBDOMAIN_NAME_HERE1</subdomain><id>NETWORK_ID_HERE1</id></network><network><subdomain>SUBDOMAIN_NAME_HERE3</subdomain><id>NETWORK_ID_HERE3</id></network><network><subdomain>SUBDOMAIN_NAME_HERE2</subdomain><id>NETWORK_ID_HERE2</id></network></xml>'
a = '<xml><ad><name>AD_NAME</name><id>AD_ID</id><country><name>COUNTRY_NAME</name><impressions>AD_IMPRESSIONS_NUMBER</impressions><clicks>AD_CLICKS_NUMBER</clicks><cost>AD_COSTS</cost></country></ad></xml>'

# This is a helper function for parseResponse(); it creates a dictionary for
# each appearance of the root tag
def parseRoot(child):
    res = {}
    for c in child:
        res[c.tag] = parseRoot(c) if len(c) > 0 else c.text
    return res

# This function looks for the root tag(s) and returns a list of dictionaries,
# one dictionary each root tag
def parseResponse(code, rootTag):
    root = etree.fromstring(code)
    list = [parseRoot(element) for element in root.iter (rootTag)]

    if (len (list) == 1):
        return list[0]
    return list

print parseResponse(a, 'ad')