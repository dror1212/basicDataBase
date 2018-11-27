import DB
import threading
import mutex

class securedDB:
    def __init__(self,fileName):
        self.dataBase = DB.DB(fileName)
        self.lock=threading.Lock()
        self.sem = threading.Semaphore(10)

    def write(self,key,value):
        lock.acquire()
        data = self.dataBase.write(key,value)
        lock.release()
        return data

    def read(self,key):
        lock.acquire()
        lock.release()
        sem.acquire()
        data = self.dataBase.read(key)
        sem.release()
        return data
        
            
        
        
        
        

    
    

    

    
