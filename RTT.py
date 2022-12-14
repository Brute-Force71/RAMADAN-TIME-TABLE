import os
import sys
import time
import shutil


columns = shutil.get_terminal_size().columns

path = "/data/data/com.termux/files/usr/"
home = "/data/data/com.termux/files/home/"

def psb(z):
    for l in z + "\n":
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.02)

#PackageSetup
def package_setup():
    if not os.path.exists(path+"lib/python3.10/site-packages/ramadan"):
        os.system("cp -r ramadan "+path+"lib/python3.10/site-packages")

#SetupShortCut
def shortcut():
    if not os.path.exists(path+"bin/ramadan"):
        os.system("cd $PREFIX/bin/ && echo '#!/bin/bash\ncd "+path+"lib/python3.10/site-packages/ramadan && python main.py $1 $2 && cd' > ramadan && chmod +x ramadan > /dev/null 2>&1")

#SaveDistrict
def save_dist(data):
    file = open(path+"lib/python3.10/site-packages/ramadan/.district", "w")
    file.write(data)
    file.close()

#SetupBanner
def banner():
    logo()
    name = input("\n    \033[92m[\033[37m*\033[92m] Enter Your Name: \033[37m")
    while (name == ""):
        psb("\n    \033[92m[\033[91m!\033[92m] Please Enter Your Name!")
        name = input("\n    \033[92m[\033[37m*\033[92m] Enter Your Name: \033[37m")
    
    if os.path.exists(home+".bashrc"):
        opn = open(home+".bashrc", "r").read()
        if not ("ramadan --banner" in opn):
            fsh = ""
            if ("fish" in opn):
                fsh = "\nfish"
                opn = opn.replace("fish", "").replace("&& fish", "").replace("&& fish &&", "").replace("fish &&", "")
            os.system("mv "+home+".bashrc "+home+".bashrctemp  > /dev/null 2>&1")
            if (opn == "") or (opn == " ") or (opn == "\n") or (opn == " \n") or (opn == "\n "):
                opn = "clear && figlet "+name+" | lolcat\n"
            file = open(home+".bashrc", "w")
            file.write(opn+"ramadan --banner"+fsh)
            file.close()
            time.sleep(1)
            psb("\n    \033[92m[\033[37m*\033[92m] Banner Added Successfully..!!\033[37m\n")
        else:
            psb("\n    \033[92m[\033[91m!\033[92m] Banner Is Already Added To Your Termux!\033[37m\n")
    else:
        file = open(home+".bashrc", "w")
        file.write("clear && figlet "+name+" | lolcat && ramadan --banner")
        file.close()
        time.sleep(1)
        psb("\n    \033[92m[\033[37m*\033[92m] Banner Added Successfully..!!\033[37m\n")

#RemoveBanner
def remove_banner():
    if os.path.exists(home+".bashrc"):
        opn = open(home+".bashrc", "r").read()
        if ("ramadan --banner" in opn):
            rmv = input("\n    \033[92m[\033[37m*\033[92m] Are You Sure You Want To Remove Ramadan Banner? [y/n]: \033[37m").lower()
            while not (rmv in ["y", "n", ""]):
                psb("\n    \033[92m[\033[91m!\033[92m] Please Enter Only y or n!")
                rmv = input("\n    \033[92m[\033[37m*\033[92m] Are You Sure You Want To Remove Ramadan Banner? [y/n]: \033[37m").lower()
            if (rmv == "y") or (rmv == ""):
                os.system("rm "+home+".bashrc  > /dev/null 2>&1")
                os.system("mv "+home+".bashrctemp "+home+".bashrc > /dev/null 2>&1")
                time.sleep(1)
                psb("\n    \033[92m[\033[37m*\033[92m] Banner Removed Successfully!")
                psb("    \033[92m[\033[37m*\033[92m] Please Close Your Termux and Reopen It!\033[37m\n")
            else:
                psb("\n    \033[92m[\033[37m*\033[92m] Banner Remove Process Canceled!\033[37m\n")
        else:
            psb("\n    \033[92m[\033[91m!\033[92m] You Have not Added Ramadan Time Table Banner Yet!!\033[37m\n")
    else:
        psb("\n    \033[92m[\033[91m!\033[92m] You Have not Added Ramadan Time Table Banner Yet!!\033[37m\n")

#ResetRamadanTimeSettings
def reset():
    if os.path.exists(path+"lib/python3.10/site-packages/ramadan/.district"):
        rmv = input("\n    \033[92m[\033[37m*\033[92m] Are You Sure You Want To Reset Ramadan Time Table Settings? [y/n]: \033[37m").lower()
        while not (rmv in ["y", "n", ""]):
            psb("\n    \033[92m[\033[91m!\033[92m] Please Enter Only y or n!")
            rmv = input("\n    \033[92m[\033[37m*\033[92m] Are You Sure You Want To Reset Ramadan Time Table Settings? [y/n]: \033[37m").lower()
        if (rmv == "y") or (rmv == ""):
            os.system("rm "+path+"lib/python3.10/site-packages/ramadan/.district > /dev/null 2>&1")
            time.sleep(1)
            if os.path.exists(home+".bashrc"):
                opn = open(home+".bashrc", "r").read()
                if ("ramadan --banner" in opn):
                    os.system("rm "+home+".bashrc  > /dev/null 2>&1")
                    os.system("mv "+home+".bashrctemp "+home+".bashrc > /dev/null 2>&1")
                    time.sleep(1)
            os.system("rm "+path+"bin/ramadan > /dev/null 2>&1")
            os.system("rm -rf "+path+"lib/python3.10/site-packages/ramadan > /dev/null 2>&1")
            psb("\n    \033[92m[\033[37m*\033[92m] Time Table Settings Reset Successful!\033[37m\n")
        else:
            psb("\n    \033[92m[\033[37m*\033[92m] Time Table Settings Reset Canceld!\033[37m\n")
    else:
        psb("\n    \033[92m[\033[91m!\033[92m] You Have Not Setup Your Ramadan Time Table Yet!!\033[37m\n")

#SetupRamadanTimeTable
def setup():
    logo()
    psb("\n    \033[92m[\033[37m*\033[92m] Choose Your District:\n")
    opn = open("district_list.txt", "r").readlines()
    num = 0
    red = 0
    for d in opn:
        if (num == 32):
            break
        num1 = num
        num2 = num + 32
        if (red == 0):
            nshow = str(num1 + 1)
            dist = opn[num1].replace("\n", "").title()
            if (len(nshow) == 1):
                nshow = "0"+nshow
            print("    \033[92m[\033[37m"+nshow+"\033[92m] "+dist, end = "")
            red = 1
            if (len(dist) <= 6):
                print("\t\t", end = "")
            elif (len(dist) < 15):
                print("\t", end = "")
        else:
            nshow = str(num2 + 1)
            dist = opn[num2].replace("\n", "").title()
            if (len(nshow) == 1):
                nshow = "0"+nshow
            print("\033[92m[\033[37m"+nshow+"\033[92m] "+dist)
            red = 0
            num = num + 1
    op = input("\n    \033[92m[\033[37m*\033[92m] Enter Your Choice:> \033[37m")
    
    while not (op in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64"]):
        psb("\n    \033[92m[\033[91m!\033[92m] Please Choose a Correct Option!")
        op = input("\n    \033[92m[\033[37m*\033[92m] Enter Your Choice:> \033[37m")
    package_setup()
    user_dist = opn[int(op) - 1]
    save_dist(user_dist)
    shortcut()
    
    psb("\n    \033[92m[\033[37m*\033[92m] District \033[37m"+user_dist.replace("\n", "").title()+" \033[92mSelected Successfully..!!")
    time.sleep(1)
    lb = input("\n    \033[92m[\033[37m*\033[92m] Do You Want To Set Ramadan Time Table as Banner? [y/n]: \033[37m").lower()
    while not (lb in ["y", "n", ""]):
        psb("\n    \033[92m[\033[91m!\033[92m] Please Enter Only y or n!")
        lb = input("\n    \033[92m[\033[37m*\033[92m] Do You Want To Set It as Banner? [y/n]: \033[37m").lower()
    if (lb == "y") or (lb == ""):
        banner()
    psb("\n    \033[92m[\033[37m*\033[92m] Ramadan Settings Setup Successfull!")
    psb("    \033[92m[\033[37m*\033[92m] Type \033[37mramadan\033[92m On Terminal To See Ramadan Time Table!!")
    psb("    \033[92m[\033[37m*\033[92m] Please Make Sure That, You Have an Internet Connection In The Days, \033[37mApril 3 & 4")
    psb("    \033[92m[\033[37m*\033[92m] Close Your Termux and Start Again...\n")
    psb("\033[92m[\033[37m???\033[92m] Ramadan Mobarak! \033[92m[\033[37m???\033[92m]".center(columns + 30))
    print("\033[37m")

#ExitTool
def logout():
    psb("\n    \033[94m[\033[92m*\033[94m]\033[92m Thanks For Using Our Tool")
    psb("    \033[94m[\033[92m*\033[94m]\033[92m For More Tools, Visit: \n")
    print("\033[93m[ \033[92mhttps://github.com/Toxic-Noob/ \033[93m]\033[37m\n".center(columns + 20))
    sys.exit()

#Logo
def logo():
    os.system("clear")
    print("\033[94m??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????".center(columns+5))
    print("\033[94m??? \033[92m?????????            ???        ?????????   ???      \033[94m  ???".center(columns+15))
    print("\033[94m??? \033[92m?????????????????????????????????????????????????????????????????????????????? ??????????????? ??? ????????????\033[94m???".center(columns+15))
    print("\033[94m??? \033[92m?????? ??????????????? ??????????????? ??????????????? ???  ??? ????????? ??? ?????? ????????????\033[94m???".center(columns+15))
    print("\033[94m??? \033[92m??? ?????????????????? ????????????????????????????????? ???  ?????? ????????? ??? ????????????  \033[94m???".center(columns+15))
    print("\033[94m???                              \033[94m          ???".center(columns+9))
    print("\033[94m??? \033[95mAuthor : NAIM HASSAN                     \033[94m???".center(columns+15))
    print("??? \033[95mTool   : Ramadan Time-Table Setup      \033[94m???".center(columns+9))
    print("??? \033[95mGitHub : https://github.com/Brute-force71  \033[94m???".center(columns+9))
    print("??? \033[95mCoder  : HunterSl4d3                   \033[94m???".center(columns+9))
    print("\033[94m??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????".center(columns+5))

#MainMenu
def main():
    logo()
    psb("\n    \033[92m[\033[37m*\033[92m] Choose Your Option:")
    
    print("\n    \033[92m[\033[37m01\033[92m] Setup Ramadan Time Table")
    print("    \033[92m[\033[37m02\033[92m] Use Ramadan Times With Banner")
    print("    \033[92m[\033[37m03\033[92m] Remove Ramadan Time Table Banner")
    print("    \033[92m[\033[37m04\033[92m] Reset Ramadan Time Settings")
    print("    \033[92m[\033[37m##\033[92m] Exit")
    
    op = input("\n    \033[92m[\033[37m*\033[92m] Enter Your Choice:> \033[37m").replace("0", "").replace("##", "#")
    while not (op in ["1", "2", "3", "4", "#"]):
        psb("\n    \033[92m[\033[91m!\033[92m] Please Choose a Correct Option!")
        op = input("\n    \033[92m[\033[37m*\033[92m] Enter Your Choice:> \033[37m").replace("0", "").replace("##", "#")
    
    if (op == "1"):
        setup()
    elif (op == "2"):
        banner()
    elif (op == "3"):
        remove_banner()
    elif (op == "4"):
        reset()
    elif (op == "#"):
        logout()


##MainProcess##
if __name__ == "__main__":
    main()
