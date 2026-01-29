import sys
import utils

def main():
    
    print("HASHING APP TEST")

    if(len(sys.argv)<=1):
        print("Not enough args")
        return

    passwd = str(sys.argv[1])
    hashed_passwd = utils.encrypt(passwd)

    hashed_passwd_json = utils.buildJson(passwd, hashed_passwd)
    print("Your hashed passwd is: " + hashed_passwd)
    print(hashed_passwd_json)
    
main()