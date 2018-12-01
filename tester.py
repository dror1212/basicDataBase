import securedDB
import threading

#####to be able to print the values that are returned from the threading#####

class ThreadWithReturnValue(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None
    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)
    def join(self):
        threading.Thread.join(self)
        return self._return

###############################################################################

def checkOneWriting(data,key,value):
    t2 = ThreadWithReturnValue(target=data.write, args=(key,value,))
    t2.start()
    t2.join()

def checkOneReading(data,key):
    t = ThreadWithReturnValue(target=data.read, args=(key,))
    t.start()
    t.join()
    
def canNotWriteWhileSomeOneElseReading(data,key,value):
    t = ThreadWithReturnValue(target=data.read, args=(key,))
    t2 = ThreadWithReturnValue(target=data.write, args=(key,value,))

    t.start()
    t2.start()

    t.join()
    t2.join()

def canNotReadWhileWriting(data,key,value):
    t = ThreadWithReturnValue(target=data.read, args=(key,))
    t2 = ThreadWithReturnValue(target=data.write, args=(key,value,))

    t2.start()
    t.start()
    
    t2.join()
    t.join()

def readMoreThanOne(data,key):
    t = ThreadWithReturnValue(target=data.read, args=(key,))
    t2 = ThreadWithReturnValue(target=data.read, args=(key,))
    t3 = ThreadWithReturnValue(target=data.read, args=("dfbfghd",))
    
    t3.start()
    t.start()
    t2.start()
    
    t2.join()
    t3.join()
    t.join()

def finalCheck(data,key,key2,value1,value2):
    t = ThreadWithReturnValue(target=data.read, args=(key,))
    t2 = ThreadWithReturnValue(target=data.read, args=(key,))
    t3 = ThreadWithReturnValue(target=data.read, args=(key2,))
    t4 = ThreadWithReturnValue(target=data.read, args=(key2,))
    
    t3.start()
    t.start()
    t2.start()
    t4.start()
    
    t2.join()
    t3.join()
    t.join()
    t4.join()

    t5 = ThreadWithReturnValue(target=data.write, args=(key2,value2,))

    t5.start()
    t5.join()



    t = ThreadWithReturnValue(target=data.read, args=(key,))
    t2 = ThreadWithReturnValue(target=data.read, args=(key,))
    t3 = ThreadWithReturnValue(target=data.read, args=(key2,))
    t4 = ThreadWithReturnValue(target=data.read, args=(key2,))
    
    t3.start()
    t.start()
    t2.start()
    t4.start()
    
    t2.join()
    t3.join()
    t.join()
    t4.join()

    
def main():
    data = securedDB.securedDB("dataBase.txt")
    data.clear() #clear the txt file

    print "first check:"
    checkOneWriting(data,1,"xxx") #first check
    print "\n"

    print "second check:"
    checkOneReading(data,1) #second check
    print "\n"
    
    print "check 3:"
    canNotWriteWhileSomeOneElseReading(data,"y",123) #check 3
    print "\n"
    
    print "check 4:"
    canNotReadWhileWriting(data,"y",123) #check 4
    print "\n"

    print "check 5:" #happenning faster than before because no one delay them
    readMoreThanOne(data,1) #check 5
    print "\n"

    print "check 6:" #notice that it is stopping in the middle, and than reading again, it is because someone os writing
    finalCheck(data,1,"y","sdrfsafs","abc") #check 6
    print "\n"

    
main()
