#stage_01.py responsible for writing afile 
text = "input 01"

with open("artifacts01.txt", "w") as f: #creating one file named artifacts
    f.write(text) #writing into that file