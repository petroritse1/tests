import time


with open("C:\\Users\\USER\\Documents\\gibbresh.txt","w+") as f:
    i = 0
    while i < 100:
        d = f.read(1)
        if d == "\n":
            time.sleep(0.1)
        else:
            time.sleep(0.2)
            print(d,sep="") 
        i += 1

     