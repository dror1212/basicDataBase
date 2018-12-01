import pickle
import os

class DB:
    def __init__(self,fileName):
        self.fileName=fileName
        if not os.path.isfile(fileName) or not os.path.getsize(fileName) > 0:
            self.file=open(fileName,"w")
            pickle.dump({},self.file)
            self.file.close()
        self.file=open(fileName,"r")
        self.dic = pickle.load(self.file)
        self.file.close()

    def read(self,key):
        self.file= open(self.fileName,"r")
        self.dic = pickle.load(self.file)
        self.file.close()
        if key in self.dic:
            return self.dic[key]
        return "not exist"

    def write(self,key,value):
        if key in self.dic:
            return False
        self.dic[key]=value
        self.file=open(self.fileName,"w")
        pickle.dump(self.dic,self.file)
        self.file.close()
        return True

    def update(self,key,value):
        if key in self.dic:
            self.dic[key]=value
            self.file=open(self.fileName,"w")
            pickle.dump(self.dic,self.file)
            self.file.close()
            return True
        return False

    def delete(self,key):
        if key in self.dic:
            self.dic.pop(key)
            self.file=open(self.fileName,"w")
            pickle.dump(self.dic,self.file)
            self.file.close()
            return True
        return False

    def clear(self):
         file1 = open(self.fileName,"w")
         file1.close()
         self.__init__(self.fileName)
        
        
        
        
            
            
            
        
