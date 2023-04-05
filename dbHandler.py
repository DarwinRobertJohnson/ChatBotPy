import sqlite3

#class that gets emotion data from the emotion db file
class happy:

    def __init__(self):
        self.con=sqlite3.connect("dbFiles/emotions")
        self.cur=self.con.cursor()

    def getHappy(self):
        return self.cur.execute("select * from happy")

class sad:

    def __init__(self):
        self.con=sqlite3.connect("dbFiles/emotions")
        self.cur=self.con.cursor()

    def getSad(self):
        return self.cur.execute("select * from sad")


Happiness=happy().getHappy()
Sadness=sad().getSad()

Happy=[]
Sad=[]

for i in Happiness:
    Happy.append(i[1])

for i in Sadness:
    Sad.append(i[1])

