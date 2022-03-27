import os
print("Please Bir Partion Adi Giriniz\n")
print("-----------------------------\n")
print("Exampling:D or C or F")
GetPartion=input("-----------------------\nPartitonName:")
try:
    NameDirectory=os.getcwd()
    CreateUrl=NameDirectory+"\\Kod1.txt"
    OpeningFile=open(CreateUrl,"r+")
    ReadingFile=OpeningFile.readlines()
    CreatingCommand="select volume  "+GetPartion+"\n"
    ReadingFile.insert(1,CreatingCommand)
    OpeningFile.seek(0)
    for loop in ReadingFile:
        OpeningFile.write(loop)   
except IOError:
    print("There is IOError")
finally:
    OpeningFile.close()   
os.system("Kod2.bat")
