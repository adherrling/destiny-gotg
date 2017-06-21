#!/usr/bin/python

import json
import requests

def getClanUserJSONs(path, header, clanId)
    def retrieveClanUserJSON():
        morePages = True
        pageCounter = 1
        #clanId = ''
        #with open('./Tokens/clanId.txt','r') as f:
        #    clanId = f.readline().strip()
        while morePages:
            clan_url = "https://bungie.net/Platform/Group/"+clanId+"/Members/?lc=en&fmt=true&currentPage="+str(pageCounter)+"&platformType=2"
            print "Connecting to Bungie: " + clan_url
            print "Fetching page " + str(pageCounter) + " of users."
            res = requests.get(clan_url, header)
            data = res.json()
            error_stat = data['ErrorStatus']
            print "Error Stats: " + error_stat
            #Stores each page of clan user responses as a different .json
            with open(path+'clanUsersPage'+str(pageCounter)+'.json','w') as f:
                json.dump(data,f)
            hasMore = res.json()['Response']['hasMore']
            morePages = hasMore
            pageCounter+=1

if __name__ == "__main__":
    path = '../Clan/'
    #getClanUserJSONs()