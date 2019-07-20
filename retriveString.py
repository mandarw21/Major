from connection import MongoConnection
import base64

a=[]
collect=MongoConnection.getConnection()
dits=collect.find({},{"Image" : 1})
i=0
for dit in dits: 
    
    a.append(dit['Image'])    
    imgdata = base64.b64decode(a[i])
    filename = str(i)+'.png'  
    with open('/home/krypton/Documents/RetrivedImages/'+filename, 'wb') as f:
        f.write(imgdata)
    i=i+1
print(str(i)+" Images saved")

collect=MongoConnection.getConnection()
x=collect.delete_many({})
