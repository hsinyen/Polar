# Created:     19/06/2012

a='<xml><network><subdomain>SUBDOMAIN_NAME_HERE</subdomain><id>NETWORK_ID_HERE</id></network></xml>'

# start: start index of the dictionary key
# end: end index of the dictionary value
def parseResponse (code, root):
    res={};
    key=root
    start=code.find (key)+len(key)+2
    while(code[start]!='/'):
        end=code.find('>',start)

        key=code[start:end]
        res[key]= code[start+1:code.find('</'+key)]

        start=code.find('</'+key)+len(key)+4
    return res

print parseResponse(a, 'network')



