def Test():
    print("Hello World")

def Adding(workpath, number=0,appid=0, name="", isdlc=False):
    file = open(str(number)+".txt","w+")
    file.write(str(appid))
    file.close()
