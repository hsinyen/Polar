# Created:     19/06/2012
#getAdInfoByDate()
a='<xml><ad><name>AD_NAME</name><id>AD_ID</id><country><name>COUNTRY_NAME</name><impressions>AD_IMPRESSIONS_NUMBER</impressions><clicks>AD_CLICKS_NUMBER</clicks><cost>AD_COSTS</cost></country></ad></xml>'
b=' <xml><network><subdomain>SUBDOMAIN_NAME_HERE</subdomain><id>NETWORK_ID_HERE</id></network></xml>'
a='<xml><campaign_stats><creative_id>CREATIVE_ID_HERE</creative_id><creative_name>CREATIVE_NAME_HERE</creative_name><campaign_id>CAMPAIGN_ID_HERE</campaign_id><advertiser_id>ADVERTISER_ID_HERE</advertiser_id><advertiser_name>ADVERTISER_NAME_HERE</advertiser_name><company_name>ADVERTISERS_COMPANY_NAME</company_name><campaign_name>CAMPAIGN_NAME_HERE</campaign_name><network_id>NETWORK_ID_HERE</network_id><cost>COST_VALUE_HERE</cost><impressions>AD_IMPRESSIONS_NUMBER</impressions><clicks>AD_CLICKS_NUMBER</clicks></campaign_stats></xml>'
# start: start index of the dictionary key
# end: end index of the dictionary value
def parseResponse (code, root):

    if root=='!':  #if root is '!', it means that the dictionary is nested (see below)
        if code.find('>')==-1: #value is a simple string; not nested
            return code
        else: #value is nested
            start=1
    else:
         start=code.find (root)+len(root)+2

    res={};

    while(start<len(code) and code[start]!='/'):
        end=code.find('>',start)
        #print start,end,code
        key=code[start:end]

        #pass the value into parseResponse in case that the value is nested
        res[key]= parseResponse(code[end+1:code.find('</'+key+'>')], '!')

        start=code.find('</'+key)+len(key)+4
    return res

print parseResponse(a, 'campaign_stats')



