from distutils.command.upload import upload
import time,requests,random,os,base64,hashlib,string
from itertools import cycle
from urllib3 import connection
from json import loads
from threading import Thread

with open("string.lvl", mode="r", encoding="utf-8") as lvlstringfile:
    lvlString = lvlstringfile.read()

def randstring(length):
    chars = string.ascii_letters
    from os import urandom
    return "".join(chars[c % len(chars)] for c in urandom(length))

def comment_chk(*,username,comment,levelid,percentage,type):
        part_1 = username + comment + levelid + str(percentage) + type + "xPT6iUrtws0J"
        return base64.b64encode(xor(hashlib.sha1(part_1.encode()).hexdigest(),"29481").encode()).decode()
def xor(data, key):
        return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
def gjp_encrypt(data):
        return base64.b64encode(xor(data,"37526").encode()).decode()
def gjp_decrypt(data):
        return xor(base64.b64decode(data.encode()).decode(),"37526")
def generate_chk(values: [int, str] = [], key: str = "", salt: str = "") -> str:
    values.append(salt)

    string = ("").join(map(str, values))

    hashed = hashlib.sha1(string.encode()).hexdigest()
    xored = xor(hashed, key)
    final = base64.urlsafe_b64encode(xored.encode()).decode()

    return final
def generate_upload_seed(data: str, chars: int = 50) -> str:
    if len(data) < chars:
        return data
    step = len(data) // chars
    return data[::step][:chars]
def uploadGJComment(name,accountid,passw,comment,perc,level):
    print("[Information]  Uploading comment...")                                                                                                                      
    gjp = gjp_encrypt(passw)
    c = base64.b64encode(comment.encode()).decode()
    chk = comment_chk(username=name,comment=c,levelid=str(level),percentage=perc,type="0")
    data={
        "secret":"Wmfd2893gb7",
        "accountID":accountid,
        "gjp":gjp,
        "userName":name,
        "comment":comment,
        "levelID":level,
        "percent":perc,
        "chk":chk
    }
    return requests.post("https://alladminnew.7m.pl/database/uploadGJComment21.php",data=data,headers={"User-Agent": ""}).text

def getGJCreatorPoint(name,accountid,passw):
    print("[Information]  Uploading level...") 
    data = {
        "gameVersion": 21,
        "accountID": accountid,
        "gjp": gjp_encrypt(passw),
        "userName": name,
        "levelID": 0,
        "levelName": "CP Farming "+randstring(5),
        "levelDesc": base64.b64encode("A level used to get Creator Points.".encode()).decode(),
        "levelVersion": 2147483647,
        "levelLength": 4,
        "audioTrack": 0,
        "auto": 0,
        "password": 2147483647,
        "original": 2147483647,
        "twoPlayer": 1,
        "songID": 1337,
        "objects": 2147483647,
        "coins": 0,
        "requestedStars": 2147483647,
        "unlisted": 1,
        "ldm": 1,
        "levelString": lvlString,
        "seed2": generate_chk(key="41274", values=[generate_upload_seed(lvlString)], salt="xI25fpAapCQg"),
        "secret": "Wmfd2893gb7"
    }
    lvlid = requests.post("https://alladminnew.7m.pl/database/uploadGJLevel21.php", data=data, headers={"User-Agent":""}).text
    print("[Information]  Level uploaded ("+lvlid+")")
    response1 = uploadGJComment(username,accid,password,"!rate easy 2147483647",percentage,str(lvlid))
    print("[Information]  Comment posted ("+response1+")")
    response2 = uploadGJComment(username,accid,password,"!epic",percentage,str(lvlid))
    print("[Information]  Comment posted ("+response2+")")

with open("string.lvl", mode="r", encoding="utf-8") as lvlStringFile:
    lvlString = lvlStringFile.read()

username="username"
accid="69420"
password="password"
percentage="2147483647"

while True:
    getGJCreatorPoint(username,accid,password)
    time.sleep(5)
