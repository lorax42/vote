import sys
import os
import json
import hashlib

def getOpt(fileName: str) -> list:
    options={}
    option={
        "id":0,
        "count":0
    }

    fileName=f"files/{fileName}"
    if not os.path.isfile(fileName):
        raise Exception(f"file \"{fileName}\" does not exist")

    with open(fileName) as fp:
        #id=0
        for line in fp:
            name=line.strip()

            options[name]=option
            
            #options[name]["id"]=id
            options[name]["count"]=0
            
            #id+=1
    
    return options

def hashJSON(candidates) -> str:
    h = hashlib.new('sha256') #sha256 can be replaced with diffrent algorithms
    h.update(candidates.encode()) #give a encoded string. Makes the String to the Hash 
    print(h.hexdigest()) #Prints the Hash

    return h.hexdigest()

def writeHash(hash):
    with open("files/sha256sum.txt","w") as hashFile:
        hashFile.write(hash)

def main():
    candidatesDict=getOpt(sys.argv[1])
    print(candidatesDict)
    candidates=json.dumps(candidatesDict)
    hash=hashJSON(candidates)
    writeHash(hash)

if __name__ == "__main__":
    main()
