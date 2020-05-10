def Test():
    print("Hello World")

def Adding(number=0,appid=0, name="", isdlc=False):
    file = open(str(number)+".txt","w+")
    file.write(str(appid)+"\n")
    file.write(name+"\n")
    file.write(str(isdlc))

    file.close()
