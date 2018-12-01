import DB
import threading

class securedDB:
    def __init__(self,fileName):
        self.dataBase = DB.DB(fileName)
        self.lock=threading.Lock()
        self.sem = threading.Semaphore(10)

    def write(self,key,value):
        self.lock.acquire()
        for i in xrange(0,10):
            self.sem.acquire()
        data = self.dataBase.write(key,value)
        for i in xrange(0,10):
            self.sem.release()
        self.lock.release()
        return data

    def read(self,key):
        self.sem.acquire()
        data = self.dataBase.read(key)
        self.sem.release()
        return data

    def update(self,key,value):
        self.lock.acquire()
        for i in xrange(0,10):
            self.sem.acquire()
        data = self.dataBase.update(key,value)
        for i in xrange(0,10):
            self.sem.release()
        self.lock.release()
        return data

    def delete(self,key):
        self.lock.acquire()
        for i in xrange(0,10):
            self.sem.acquire()
        data = self.dataBase.delete(key)
        for i in xrange(0,10):
            self.sem.release()
        self.lock.release()
        return data
            
        
        
        
        

    
    

    

    
