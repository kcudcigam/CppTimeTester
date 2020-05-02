import os
import threading
import shutil
CppFile = []
TestFile = []
isCheck = 0
id = 0
TimeL = 0.0
Li = 0
Ri = 0
Ti = 0
AddCode_Check = "signed main() {\n\tfreopen(\"DataSize.txt\", \"r\", stdin);\n\tfreopen(\"INPUTFILE.in\", \"w\", stdout);\n\tfakemain();\n\treturn 0;\n}"
AddCode = "signed main() {\n\tfreopen(\"INPUTFILE.in\", \"r\", stdin);\n\tfreopen(\"FILENAME.out\", \"w\", stdout);\n\tclock_t START_FILE,FINISH_FILE;\n\tSTART_FILE = clock();\n\tfakemain();\n\tFINISH_FILE = clock();\n\tfclose(stdin), fclose(stdout);\n\tfreopen(\"FILENAME.data\", \"a+\", stdout);\n\tstd::cout << FINISH_FILE - START_FILE << endl;\n\tfclose(stdout);\n\treturn 0;\n}"
def CopyCpp():
    os.system("copy Code\\*.cpp .WORKSHOP 2>nul 1>nul")
def CheckCpp():
    global isCheck
    global CppFile
    global id
    global TestFile
    FileName = os.listdir(".WORKSHOP")
    for FileI in FileName:
        FileNamePre = os.path.splitext(FileI)[0]
        FileNameSuf = os.path.splitext(FileI)[1]
        if(FileNameSuf == ".cpp"):
            if(FileNamePre == "check"):
                isCheck = 1
            else:
                CppFile.append(FileNamePre)
                id = id + 1
                os.rename(".WORKSHOP//" + FileI, ".WORKSHOP//" + "FILE_" + str(id) + ".cpp")
                TestFile.append("FILE_" + str(id))
    if isCheck == 0:
        print("\033[31mError\033[37m, Please Check if There's check.cpp")
        shutil.rmtree(".WORKSHOP")
        exit()
    if len(CppFile) == 0:
        print("\033[31mError\033[37m, Code Not Found")
        shutil.rmtree(".WORKSHOP")
        exit()
    print("OK, Codes are Found. Prepare for the TimeTest")
    print("Your Codes' Names are: " + str(CppFile))
def CompileCpp():
    global CppFile
    if os.system("g++ -w -Wl,--stack,100000000 -std=c++11 .WORKSHOP\\check.cpp -o .WORKSHOP\\check.exe") == 1:
        print("Oh no! There's a Problem in your check.cpp. Please Check it again")
        shutil.rmtree(".WORKSHOP")
        exit()
    else:
        print("OK, check.cpp has been Compiled")
    CppTi = TestFile[:]
    pi = -1
    for FileI in CppTi:
        pi = pi + 1
        if os.system("g++ -w -Wl,--stack,100000000 -std=c++11 .WORKSHOP\\" + FileI + ".cpp -o .WORKSHOP\\" + FileI + ".exe") == 1:
            print("Oh no! There's a Problem in your " + CppFile[pi] + ".cpp. Please Check it again")
            TestFile.remove(FileI)
            CppFile.pop(pi)
            pi = pi - 1
        else:
            print("OK, " + CppFile[pi] + ".cpp has been Compiled")
    if len(CppFile) == 0:
        print("\033[31mAll the Codes Compile Error\033[37m. Please Check and Try again")
        shutil.rmtree(".WORKSHOP")
        exit(0)
def AddFile():
    fo = open(".WORKSHOP\\check.cpp", "r+")
    tmp_data = fo.read()
    tmp_data = tmp_data.replace("main", "fakemain")
    fo.seek(0)
    fo.write(tmp_data + "\n" + AddCode_Check)
    fo.close()
    print("OK, check.cpp has been written")
    pi = -1
    for FileI in TestFile:
        pi = pi + 1
        fo = open(".WORKSHOP\\" + FileI + ".cpp", "r+")
        tmp_data = fo.read()
        tmp_data = tmp_data.replace("main", "fakemain")
        fo.seek(0)
        fo.write("#include<time.h>\n#include<bits/stdc++.h>\n" + tmp_data)
        fo.seek(0, 2)
        fo.write(AddCode.replace("FILENAME", FileI))
        fo.close()
        print("OK, " + CppFile[pi] + ".cpp has been written")
def mytest(ci):
    #print(".WORKSHOP\\" + ci + ".exe")
    os.system(ci + ".exe")
    #os.system(".WORKSHOP\\" + ci + ".exe")
def TimeLimit(ci, Li):
    if __name__ == '__main__':
        os.chdir(".WORKSHOP")
        t = threading.Thread(target = mytest, args = (ci, ))
        t.setDaemon(True)
        t.start()
        t.join(Li)
        if os.system("taskkill /f /t /im " + ci + ".exe 2>nul 1>nul") == 0:
            fo = open(ci + ".data", "a+")
            fo.seek(0, 2)
            fo.write(str(int(Li * 1000 + 200)) + "\n")
            print("\033[34mTime Limit Error!\033[37m")
            fo.close()
        else:
            print("\033[32mSuccess!\033[37m")
        os.chdir("..")
def RunCode():
    os.chdir(".WORKSHOP")
    mytest("check")
    os.chdir("..")
    print("\033[32mData Created Success!\033[37m")
    pi = -1
    for FileI in TestFile:
        pi = pi + 1
        print("Run " + CppFile[pi] + ".exe...", end = ' ')
        TimeLimit(FileI, TimeL)
def DataRun(Datasize):
    fo = open(".WORKSHOP\\DataSize.txt", "w")
    fo.write(str(Datasize))
    fo.close()
    RunCode()
def calc(datal, datar, datat):
    for i in range(datal, datar + 1, datat):
        print("--- Data Size: " + str(i) + " ---")
        DataRun(i)
def ReadTime():
    for FileI in TestFile:
        fo = open(".WORKSHOP\\" + FileI + ".data", "r")
        for i in range(len(RunData)):
            si = int(next(fo))
            RunTime[i].append(si)
#main
os.chdir(os.path.split(os.path.realpath(__file__))[0])
if os.path.exists(".WORKSHOP"):
    shutil.rmtree(".WORKSHOP")
os.mkdir(".WORKSHOP")
CopyCpp()
CheckCpp()
AddFile()
CompileCpp()
Li = int(input("Please Enter the Minimum Data:\n"))
Ri = int(input("Please Enter the Maximum Data:\n"))
if(Li >= Ri):
    print("\033[31mError\033[37m, Input Invalid. The Maximum Number Should be Bigger than the Minimum Data")
    shutil.rmtree(".WORKSHOP")
    exit()
Ti = int(input("Please Enter the Delta Data:\n"))
if Ti <= 0:
    print("\033[31mError\033[37m, Input Invalid. The Delta Data Should be Bigger than 0")
    shutil.rmtree(".WORKSHOP")
    exit()
TimeL = float(input("Please Enter the Time Limit(s):\n"))
if TimeL <= 0:
    print("\033[31mError\033[37m, Input Invalid. The TimeLimit Should be Bigger than 0")
    shutil.rmtree(".WORKSHOP")
    exit()

calc(Li, Ri, Ti)
RunData = list(range(Li, Ri + 1, Ti))
RunTime = [[] for i in range(len(RunData))]
ReadTime()
#print(RunTime)

import altair as alt
import pandas as pd
#alt.themes.enable('fivethirtyeight')
#alt.themes.enable('dark')
source = pd.DataFrame(RunTime,
                    columns=CppFile, index=pd.RangeIndex(Li, Ri + 1, Ti, name='数据规模'))
source = source.reset_index().melt('数据规模', var_name='Name', value_name='运行时间(ms)')
nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['数据规模'], empty='none')

#if you want the line rounded, please add " interpolate='basis' " in "mark.line()"
#like "line = alt.Chart(source).mark_line(interpolate='monotone').encode("
line = alt.Chart(source).mark_line(interpolate='monotone').encode(
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
shutil.rmtree(".WORKSHOP")
