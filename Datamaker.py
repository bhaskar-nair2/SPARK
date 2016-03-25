import mysql.connector as mc

conf={"user":"root","password":"","host":"127.0.0.1","database":"devloping_spark"}

con=mc.connect(**conf)
cur=con.cursor()
class improver:
    def sqlcorrect(self,tup):
        we=str(tup)
        fi=we[3:we.index("'",3)]
        return fi
        
class logic:
    def wording(self,stri):
        wor=stri.split(" ")
        logic().correct(wor)
        
    def correct(self,wo):
        cur.execute("select * from waste")
        rs=cur.fetchall()
        for words in rs:
            try:
                wo.remove(improver().sqlcorrect(words))
            except ValueError: pass
        logic().find(wo)      
    
        
    def find(self,stri):
        for stg in stri:
            print(stg)
            cur.execute("select outpu from reply where inpu like '"+stg+"';")
            rs=cur.fetchall()
        print rs
        
    #def understand():   
    #def add():
    #def rep():
    


logic().wording("hey spark wassup")

