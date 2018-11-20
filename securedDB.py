import DB
import threading
import mutex

class securedDB:
    def __init__(self,fileName):
        self.dataBase = DB.DB(fileName)
        self.lock=threading.Lock()
        self.sem = threading.Semaphore(10)
        self.writingStatus=True

    def write(self,key,value):
        lock.acquire()
        self.writingStatus=False
        self.dataBase.write(key,value)
        self.writingStatus=True
        lock.release()

    def read(self,key):
        while not self.writingStatus:
            pass
        
            
        
        
        
        

    
    

    

    
