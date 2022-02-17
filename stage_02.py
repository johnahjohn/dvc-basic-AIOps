#stage_02.py responsible for reading that file

with open("artifacts01.txt", "r") as f: #it open this artifacts file and read  the txt
    text = f.read() #read and store it into some text

print(text) #print the content of that txt
print("end of stage-02")