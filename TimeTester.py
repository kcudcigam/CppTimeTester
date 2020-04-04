import os
import threading
import shutil
CppFile = []
isCheck = 0
TimeL = 0
Li = 0
Ri = 0
Ti = 0
AddCode_Check = "signed main() {\n\tfreopen(\"DataSize.txt\", \"r\", stdin);\n\tfreopen(\"INPUTFILE.in\", \"w\", stdout);\n\tfakemain();\n\treturn 0;\n}"
AddCode = "signed main() {\n\tfreopen(\"INPUTFILE.in\", \"r\", stdin);\n\tfreopen(\"FILENAME.out\", \"w\", stdout);\n\tclock_t START_FILE,FINISH_FILE;\n\tSTART_FILE = clock();\n\tfakemain();\n\tFINISH_FILE = clock();\n\tfclose(stdin), fclose(stdout);\n\tfreopen(\"FILENAME.data\", \"a+\", stdout);\n\tcout << FINISH_FILE - START_FILE << endl;\n\tfclose(stdout);\n\treturn 0;\n}"
def CopyCpp():
    os.system("copy Code\\*.cpp Workshop 2>nul 1>nul")
def CheckCpp():
    global isCheck
    global CppFile
    FileName = os.listdir("Workshop")
    for FileI in FileName:
        FileNamePre = os.path.splitext(FileI)[0]
        FileNameSuf = os.path.splitext(FileI)[1]
        if(FileNameSuf == ".cpp"):
            if(FileNamePre == "check"):
                isCheck = 1
            else:
                CppFile.append(FileNamePre)
    if isCheck == 0:
        print("Error, Please Check if There's check.cpp")
        shutil.rmtree("Workshop")
        exit()
    if len(CppFile) == 0:
        print("Error, Code Not Found")
        shutil.rmtree("Workshop")
        exit()
    print("OK, Codes are Found. Prepare for the TimeTest")
    print("Your Codes' Names are: " + str(CppFile))
def CompileCpp():
    global CppFile
    if os.system("g++ -Wl,--stack,100000000 -std=c++11 Workshop\\check.cpp -o Workshop\\check.exe") == 1:
        print("Oh no! There's a Problem in your check.cpp. Please Check it again")
        shutil.rmtree("Workshop")
        exit()
    else:
        print("OK, check.cpp has been Compiled")
    CppTi = CppFile[:]
    for FileI in CppTi:
        if os.system("g++ -Wl,--stack,100000000 -std=c++11 Workshop\\" + FileI + ".cpp -o Workshop\\" + FileI + ".exe") == 1:
            print("Oh no! There's a Problem in your " + FileI + ".cpp. Please Check it again")
            CppFile.remove(FileI)
        else:
            print("OK, " + FileI + ".cpp has been Compiled")
    if len(CppFile) == 0:
        print("All the Codes Compile Error. Please Check and Try again")
        shutil.rmtree("Workshop")
        exit(0)
def AddFile():
    fo = open("Workshop\\check.cpp", "r+")
    tmp_data = fo.read()
    tmp_data = tmp_data.replace("main", "fakemain")
    fo.seek(0)
    fo.write(tmp_data + "\n" + AddCode_Check)
    fo.close()
    print("OK, check.cpp has been written")
    for FileI in CppFile:
        fo = open("Workshop\\" + FileI + ".cpp", "r+")
        tmp_data = fo.read()
        tmp_data = tmp_data.replace("main", "fakemain")
        fo.seek(0)
        fo.write("#include<time.h>\n" + tmp_data)
        fo.seek(0, 2)
        fo.write(AddCode.replace("FILENAME", FileI))
        fo.close()
        print("OK, " + FileI + ".cpp has been written")
def mytest(ci):
    #print("Workshop\\" + ci + ".exe")
    os.chdir("Workshop")
    print("Run " + ci + ".exe...", end = ' ')
    os.system(ci + ".exe")
    os.chdir("..")
    #os.system("Workshop\\" + ci + ".exe")
def TimeLimit(ci, Li):
    if __name__ == '__main__':
        t = threading.Thread(target = mytest, args = (ci, ))
        t.setDaemon(True)
        t.start()
        t.join(Li)
        if os.system("taskkill /f /t /im " + ci + ".exe 2>nul 1>nul") == 0:
            fo = open("Workshop\\" + ci + ".data", "a+")
            fo.seek(0, 2)
            fo.write(str(Li * 1000 + 200) + "\n")
            print("Time Limit Error!")
            fo.close()
        else:
            print("Success!")
def RunCode():
    mytest("check")
    print("Success!")
    for FileI in CppFile:
        TimeLimit(FileI, TimeL)
def DataRun(Datasize):
    fo = open("Workshop\\DataSize.txt", "w")
    fo.write(str(Datasize))
    fo.close()
    RunCode()
def calc(datal, datar, datat):
    for i in range(datal, datar + 1, datat):
        print("---- Data Size: " + str(i) + " ----")
        DataRun(i)
def ReadTime():
    for FileI in CppFile:
        fo = open("Workshop\\" + FileI + ".data", "r")
        for i in range(len(RunData)):
            si = int(next(fo))
            RunTime[i].append(si)
#main

os.chdir(os.path.split(os.path.realpath(__file__))[0])
if os.path.exists("Workshop"):
    shutil.rmtree("Workshop")
os.mkdir("Workshop")
CopyCpp()
CheckCpp()
AddFile()
CompileCpp()
Li = int(input("Please Enter the Minimum Data: "))
Ri = int(input("Please Enter the Maximum Data: "))
if(Li >= Ri):
    print("Error, Input Invalid. The Maximum Number Should be Bigger than the Minimum Data")
    shutil.rmtree("Workshop")
    exit()
Ti = int(input("Please Enter the Delta Data: "))
if Ti <= 0:
    print("Error, Input Invalid. The Delta Data Should be Bigger than 0")
    shutil.rmtree("Workshop")
    exit()
TimeL = int(input("Please Enter the Time Limit(s): "))
if TimeL <= 0:
    print("Error, Input Invalid. The TimeLimit Should be Bigger than 0")
    shutil.rmtree("Workshop")
    exit()

calc(Li, Ri, Ti)
RunData = list(range(Li, Ri + 1, Ti))
RunTime = [[] for i in range(len(RunData))]
ReadTime()
#print(RunTime)

import altair as alt
import pandas as pd
source = pd.DataFrame(RunTime,
                    columns=CppFile, index=pd.RangeIndex(Li, Ri + 1, Ti, name='数据规模'))
source = source.reset_index().melt('数据规模', var_name='Name', value_name='运行时间(ms)')
nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['数据规模'], empty='none')
line = alt.Chart(source).mark_line(interpolate='basis').encode(
    x='数据规模:Q',
    y='运行时间(ms):Q',
    color='Name:N'
)
selectors = alt.Chart(source).mark_point().encode(
    x='数据规模:Q',
    opacity=alt.value(0),
).add_selection(
    nearest
)
points = line.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)
text = line.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest, '运行时间(ms):Q', alt.value(' '))
)
rules = alt.Chart(source).mark_rule(color='gray').encode(
    x='数据规模:Q',
).transform_filter(
    nearest
)
result = alt.layer(
    line, selectors, points, rules, text
).properties(
    width=1200, height=600
)
result.save("result.html")
print("OK, TimeTest Success! See \'result.html\'")
shutil.rmtree("Workshop")
