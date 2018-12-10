import crypt
import optparse


#cryptPass is current encrypted password that needs to be decrypted
def testPass(cryptPass, dname):
    #need salt from decrypte password
    salt = cryptPass[0:2]
    dictFile = open(dname, "r")
    for word in dictFile.readlines():
        word = word.strip("\n")
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print("[*] Found Password: " +word+ "\n")
            return
    print(" [-] Password Not Found. \n")
    return


def main():
    parser = optparse.OptionParser("usage %prog "+"-f <passwordfile> -d <dictionary>")
    parser.add_option("-f", dest="pname", type="string", help="specify password file")
    parser.add_option("-d", dest = "dname", type="string", help="specify dictionary file")
    (options, args) = parser.parse_args()
    
    if (options.pname == None) | (options.dname == None):
        print(parser.usage)
        exit()
    else:
        pname = options.pname
        dname = options.dname
    
    passFile = open(pname, "r")
    for line in passFile.readlines():
        if ":" in line:
            #user is first thing in each line
            user = line.split(":")[0]
            #each new thing is split by a colon
            cryptPass = line.split(":")[1].strip(" ")
            print("[*] cracking password for: "+user)
            testPass(cryptPass, dname)


if __name__ == "__main__":
    main()
