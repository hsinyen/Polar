# Created:     19/06/2012

a='<xml><ad><name>AD_NAME</name><id>AD_ID</id><country><name>COUNTRY_NAME</name><impressions>AD_IMPRESSIONS_NUMBER</impressions><clicks>AD_CLICKS_NUMBER</clicks><cost>AD_COSTS</cost></country></ad></xml>'
b=' <xml><network><subdomain>SUBDOMAIN_NAME_HERE</subdomain><id>NETWORK_ID_HERE</id></network></xml>'
a='<xml><campaign_stats><creative_id>CREATIVE_ID_HERE</creative_id><creative_name>CREATIVE_NAME_HERE</creative_name><campaign_id>CAMPAIGN_ID_HERE</campaign_id><advertiser_id>ADVERTISER_ID_HERE</advertiser_id><advertiser_name>ADVERTISER_NAME_HERE</advertiser_name><company_name>ADVERTISERS_COMPANY_NAME</company_name><campaign_name>CAMPAIGN_NAME_HERE</campaign_name><network_id>NETWORK_ID_HERE</network_id><cost>COST_VALUE_HERE</cost><impressions>AD_IMPRESSIONS_NUMBER</impressions><clicks>AD_CLICKS_NUMBER</clicks></campaign_stats></xml>'
a='<xml><inventory><date>DATE</date><zones><zone><id>ZONE_ID</id><name>ZONE_NAME</name><impressions>IMPRESSIONS_NUMBER_FOR_THE_ZONE</impressions></zone></zones><total_impressions>TOTAL_IMPRESSIONS_NUMBER</total_impressions></inventory></xml>'
a='<xml><network><subdomain>SUBDOMAIN_NAME_HERE1</subdomain><id>NETWORK_ID_HERE1</id></network><network><subdomain>SUBDOMAIN_NAME_HERE3</subdomain><id>NETWORK_ID_HERE3</id></network><network><subdomain>SUBDOMAIN_NAME_HERE2</subdomain><id>NETWORK_ID_HERE2</id></network></xml>'
# start: start index of the dictionary key
# end: end index of the dictionary value


def parseResponse(code, root):

    # If root is '!', it means that the dictionary is nested (see below):
    if root == '!':
        # If the value does not contain any '<', it means that it's a single
        # string and not nested
        if code.find('>') == -1:
            return code
        else:
            start=1
    else:
         list = code.split('</' + root + '>')
         if (len(list) > 2):
            dictList = []
            for i in range(len(list) - 1):
                dictList.append(parseResponse (list [i] , root))

            return dictList

         start = code.find('<', code.find(root)) + 1

    res = {};

    while(start != 0 and code[start] != '/'):
        end = code.find('>', start)
        key = code[start:end]

        # Pass the value into parseResponse() in case that the value is nested
        res[key] = parseResponse(code[end+1:code.find('</' + key + '>')], '!')

        start = code.find('<', code.find('</' + key) + 1) + 1
    return res

print parseResponse(a, 'network')



