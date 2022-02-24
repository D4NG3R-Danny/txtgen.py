#Github: D4NG3R-Danny
from pathlib import Path
import os, time, secrets
#Create Directory-Chooser/Maker for linux OS, maybe Windows
#Make Function creating file
#Make Function filing file 
yeah = ["YES","Y","yes","y","Yes"]
nope = ["No","N","n","no","NO"]

def current_dir():
    os.system("clear")
    print("You're In The Current Directory: ",end="")
    print(Path.cwd(),flush=True,end='\n')
    answer = input("Do you want to create a new Directory"+"\n"+"  in the current directory?[Y(es)]/[N(o)]"+"\n")
    if answer in nope:
        os.system("clear")
        answer = input("Then write me an absolute Path to put the Files in: ")
        create_directory(answer)
    else:
        create_directory(answer)

def create_directory(answer:str):
    os.system("clear")
    global Goal_dir 

    if answer in yeah:
        Goal_dir = str(Path.cwd())+"/uselessTXT"
        os.makedirs(Goal_dir)
        print("Created /uselessTXT in ",Goal_dir)
        time.sleep(3)
        os.system("clear")
    else:
        Goal_dir = answer+"/uselessTXT"
        os.makedirs(Goal_dir)
        print("Created /uselessTXT in ",Goal_dir)
        time.sleep(3)
        os.system("clear")


def file_creator(amount, length=20):
    for i in range(1,1+int(amount)):
        os.mknod(Goal_dir+"/"+"placeholder"+str(i)+".txt")

if "__main__" == __name__:
    try:
        current_dir()
    except FileExistsError:
        os.system("clear")
        print("Directory /uselessTXT exists already in: ",Goal_dir)
        catching = input("Do you want to put Files in this directory?[yes][no]")
        if catching in nope:
            print("It's your problem, not mine.")
            raise FileExistsError("Delete the Folder /uselessTXT")
    
    os.system("clear")
    amount = input("How many files to create?")
    os.system("clear")
    file_creator(amount)