import os
from time import sleep #for debugging use time.sleep(time(in ms))

try:
    print("Welcome to the code finder!")
    print("Find excerpts from java , cpp or py codes easily")
    print("please specify the file path for the code you want to search")
    print("in the present directory only!")
    print("Please append your file/folder with the present working directory")
    print("pwd:",os.getcwd())
    print("Note:this finder will list all the files which have more than zero lines")
    print("matching!")
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
        return s=='py' or s=='cpp' or s=='java'

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
    for d in data:
        if(is_py(d)):
            disj=is_disjoint(d)
            file=open(os.path.join(os.getcwd(),d),'r',encoding='utf-8')
            file_data[d]=nwlinefree(file.read())

    def ComputeLpsArray(lps,pat):
        i=1
        ln=0
        while(i<len(pat)):
            if(pat[i]==pat[ln]):
                ln+=1
                lps[i]=ln
                i+=1
            else:
                if ln!=0:
                    ln=lps[ln-1]
                else:
                    lps[i]=0
                    i+=1
        return lps

    def Match_Strings(txt,pat):
        try:
            if txt==None or pat==None:
                return False
            if(len(pat)==len(txt)):
                return pat==txt
            if(len(txt)<len(pat)):
                txt,pat=pat,txt
            i=0
            j=0
            lps=[0]*len(pat)
            lps=ComputeLpsArray(lps,pat)
            while(i<len(txt)):
                if(txt[i]==pat[j]):
                    i+=1
                    j+=1
                if(j==len(pat)):
                    return True
                elif i<len(txt) and txt[i]!=pat[j]:
                    if j!=0:
                        j=lps[j-1]
                    else:
                        i+=1
            return False
        except:
            return False

    def FileNameParser(name):
        s=''
        for i in range(len(name)-1,0,-1):
            if name[i]=='/':
                return s[::-1]
            s+=name[i]

    data_to_be_matched=nwlinefree(data_to_be_matched+'\n')

    poss_file=set()
    for item in file_data:
        for k in file_data[item]:
            for mnt in data_to_be_matched:
                if Match_Strings(k,mnt) and FileNameParser(item)!="CodeFinder.py":
                    poss_file.add(item)

    print("Results...")
    Result={}
    if not len(poss_file):
        print("No Match Found!")
    else:
        print("{} Match(s) found!".format(len(poss_file)))
        for k in poss_file:
            print("File Name:",FileNameParser(k))
            print("File path:",k)
except Exception as e:
    print("Oops! Looks like something is not right!")
    print("seems like:",e)