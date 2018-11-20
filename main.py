import DB

data = DB.DB("dataBase.txt")

data.clear()

print data.read("xxx")
print data.write(1,"xxx")
print data.read(1)
print data.write(2,"xxfgxcvx")
print data.read(2)
print data.read("xxfgxcvx")
print data.update(2,"dffsfdsfsdfsdfsdfsf")
print data.read(2)
print data.write(2,"sdfsdf")
print data.delete(2)
