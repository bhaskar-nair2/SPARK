import mysql.connector as mc
import urllib
import json as m_json
import os


config={"user":"root","password":"","host":"127.0.0.1","database":"devloping_spark"}

con=mc.connect(**config)
cur=con.cursor

class net: 
    def srch(self,que):
        query=que
        query = urllib.urlencode ( { 'q' : query } )
        response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
        json = m_json.loads ( response )
        results = json [ 'responseData' ] [ 'results' ]
        for result in results:
            #title = result['title']
            url = result['url']   # was URL in the original and that threw a name error exception
            os.startfile(url)

    def wiki(self,que):
        os.startfile("https://en.wikipedia.org/wiki/"+que.replace(' ','_'))
  
def siter(quer):
    cur.execute("select * from waste")
    #cur.execute("select distinct site from site_list where inpu like '%"+que+"%'")
    #s=cur.fetchall()
    #os.startfile("https://"+rs[0])

siter('google')
