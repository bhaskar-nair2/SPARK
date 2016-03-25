import mysql.connector as mc
import pyttsx
#import Datamaker
import unicodedata

common=pyttsx.init()
#dat=Datamaker.logic()

config={"user":"root","password":"","host":"127.0.0.1","database":"devloping_spark"}
x=""
con=mc.connect(**config)
cur=con.cursor()

cur.execute("select * from waste")
rs=cur.fetchall()
print rs[0]
'''
for words in rs:
    print "You said {}".format(words).encode("utf-8")
    print (words.index('hello'))
    #print (str("".join(str(list(x)))))
    print(str(list(words)).encode('ascii','ignore'))
    #common.say(unicodedata.normalize('NFKD', str.join(str(words))).encode('ascii','ignore'))
    common.runAndWait()
print "bhaskar"
#for i in range(len(we)):

'''
'''
 for i in range(len(waste)):
            try:
                    st.pop(st.index(waste[i]))
            except ValueError:
                    pass
                    '''
