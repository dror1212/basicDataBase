import DB
import threading
import time #add delay to the functions to show that it is really waiting

class securedDB:
    def __init__(self,fileName):
        self.dataBase = DB.DB(fileName)
        self.lock=threading.Lock()
        self.sem = threading.Semaphore(10)

    def write(self,key,value):
        self.lock.acquire()
        for i in xrange(0,10):
            self.sem.acquire()
        print "wait before releaseing to create delay" ####to check if he really waits####
        data = self.dataBase.write(key,value)
        print data
        time.sleep(2) ####to check if he really waits####
        for i in xrange(0,10):
            self.sem.release()
        self.lock.release()
        return data

    def read(self,key):
        self.lock.acquire()
        self.sem.acquire()
        self.lock.release()
        print "wait before releaseing to create delay" ####to check if he really waits####
        data = self.dataBase.read(key)
        print data
        time.sleep(1) ####to check if he really waits####
        self.sem.release()
        return data

    def update(self,key,value):
        self.lock.acquire()
        for i in xrange(0,10):
            self.sem.acquire()
        print "wait before releaseing to create delay" ####to check if he really waits####  
        data = self.dataBase.update(key,value)
        print data
        for i in xrange(0,10):
            self.sem.release()
        self.lock.release()
        return data

    def delete(self,key):
        self.lock.acquire()
        for i in xrange(0,10):
            self.sem.acquire()
        print "wait before releaseing to create delay" ####to check if he really waits####
        data = self.dataBase.delete(key)
        print data
        for i in xrange(0,10):
            self.sem.release()
        self.lock.release()
        return data

    def clear(self):
        self.dataBase.clear()
            
        
        
        
        

    
    

    

    
