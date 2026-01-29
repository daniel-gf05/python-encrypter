from Crypto.Hash import SHA256
import json

def encrypt(passwd: str):
    m = SHA256.new()
    encodedPasswd = passwd.encode()
    m.update(encodedPasswd)
    m.digest()
    hashed_passwd = m.hexdigest()
    return hashed_passwd

def buildJson(original_passwd: str, hashed_passwd: str):
    preJson = {
        "original_passwd": original_passwd,
        "hashed_passwd": hashed_passwd
    }
    jsons = json.dumps(preJson)
    return jsons