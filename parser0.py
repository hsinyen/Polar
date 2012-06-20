# Created:     19/06/2012

a='<xml><network><subdomain>SUBDOMAIN_NAME_HERE</subdomain><id>NETWORK_ID_HERE</id></network></xml>'
a='<xml><inventory><date>DATE</date><zones><zone><id>ZONE_ID</id><name>ZONE_NAME</name><impressions>IMPRESSIONS_NUMBER_FOR_THE_ZONE</impressions></zone></zones><total_impressions>TOTAL_IMPRESSIONS_NUMBER</total_impressions></inventory></xml>'
# start: start index of the dictionary key
# end: end index of the dictionary value
def parseResponse (code, root):
    res={};
    start=code.find (root)+len(root)+2
    while(code[start]!='/'):
        end=code.find('>',start)

        key=code[start:end]
        res[key]= code[end+1:code.find('</'+key)]

        start=code.find('</'+key)+len(key)+4
    return res

print parseResponse(a, 'inventory')



