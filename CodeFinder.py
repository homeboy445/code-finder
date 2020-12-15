import os
from time import sleep #for debugging use time.sleep(time(in ms))

try:
    print("Welcome to the code finder!")
    print("please specify the file path for the code you want to search")
    print("in the present directory only!")
    fpath=input("Enter here(format->(folder/file)):")

    data_to_be_matched=open(os.path.join(os.getcwd(),fpath),'r',encoding='utf-8').read()

    def is_py(file):
        s=''
        go=0
        for f in file:
            if(go==1):
                s+=f
            if(f=='.'):
                go=1
        return s=='py'

    def list_files(dir):
        r = []
        for root, dirs, files in os.walk(dir):
            for name in files:
                r.append(os.path.join(root, name))
        return r

    def _isfile(dir):
        cnt=0
        for i in dir:
            if(i=='/'):
                cnt+=1
        if(cnt==1):
            return True
        return False

    def is_disjoint(dir):
        if os.path.isfile(dir):
            dir_t=os.getcwd()
            dir_l=dir[len(dir_t):]
            if(_isfile(dir_l)):
                return dir_l[1:]
            return dir_l

    def nwlinefree(data):
        nwl=[]
        s=''
        for i in range(len(data)):
            if(data[i]!='\n'):
                s+=data[i].strip()
            else:
                nwl.append(s)
                s=''
        return nwl

    data=list_files(os.getcwd())
    file_data={}
    for d in data: #It could also be used to find specific types of files in a folder!
        if(is_py(d)):
            disj=is_disjoint(d)
            file=open(os.path.join(os.getcwd(),d),'r',encoding='utf-8')
            file_data[d]=nwlinefree(file.read())

    def Match_Count(source,target):
        if(len(source)!=len(target)):
            return 0
        cnt=0
        for i in range(len(source)):
            if(source[i]==target[i]):
                cnt+=1
        return cnt

    data_to_be_matched=nwlinefree(data_to_be_matched)
    poss_file={}

    for item in file_data:
        for k in file_data[item]:
            for mnt in data_to_be_matched:
                cnt=Match_Count(k,mnt)
            if(cnt==0):
                continue
            poss_file[cnt]=item

    def FileNameParser(name):
        s=''
        for i in range(len(name)-1,0,-1):
            if name[i]=='/':
                return s[::-1]
            s+=name[i]

    print("Results...")

    if not len(poss_file.keys()):
        print("No Match Found!")
    else:
        print(len(poss_file.keys()),' Match found!')
        for k in reversed(sorted(poss_file.keys())):
            print("File name:",FileNameParser(poss_file[k]))
            print("File path:",poss_file[k])
except:
    print("Oops! Looks like something is not right!")