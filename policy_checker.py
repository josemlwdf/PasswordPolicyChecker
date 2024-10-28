#!/usr/bin/env python3

import sys
from string import *
import os


policies = {
    "lower" : False,
    "upper" : False,
    "digits" : False,
    "chars" : False,
    "length" : 0
}


"""
check for the different policies applicable to the passwords based on an example password
"""
def check_policies_enabled(policy_template):
    global policies

    print("[!] Creating password policy from [{}].".format(policy_template))

    policies["length"] = len(policy_template)
    print("[!] Minimum {} characters.".format(len(policy_template)))
    for chr in policy_template:
        if chr in ascii_lowercase:            
            if not policies["lower"]: 
                print("[!] Required lowercases.")
            policies["lower"] = True
        elif chr in ascii_uppercase:
            if not policies["upper"]:
                print("[!] Required UPPERCASE.")
            policies["upper"] = True
        elif chr in digits:
            if not policies["digits"]:
                print("[!] Required d1g1ts.")
            policies["digits"] = True
        elif chr in punctuation:
            if not policies["chars"]:
                print("[!] Required ch@rs.")
            policies["chars"] = True
        else:
            print("[-] The template contains invalid characters")
            exit()
    print("[+] Policy Created.")


"""
check if some string is a password policy compliant
"""
def check_policy_compliant(password):
    if (len(password) < policies["length"]): return False

    lower = False
    upper = False
    digit = False
    chars = False

    for chr in password:
        if (policies["lower"] and chr in ascii_lowercase):
            lower = True
        elif (policies["upper"] and chr in ascii_uppercase):
            upper = True
        elif (policies["digits"] and chr in digits):
            digit = True
        elif policies["chars"] and chr in punctuation:
            chars = True

    if (policies["lower"] and not lower):
        return False
    elif (policies["upper"] and not upper):
        return False
    elif (policies["digits"] and not digit):
        return False
    elif (policies["chars"] and not chars):
        return False
    else:
        return True

"""
opens file and recover passwords from a given wordlist, if is not a file,
use the passed arg as username value (useful when user is recovered using OSINT)
"""
def parse_passwords_wordlist():
    pfname = sys.argv[2]
    if (os.path.isfile(pfname)):        
            # open the file, this is our passwords wordlist
        with open(pfname, "rb") as fh:
            # read file line by line
            print("[!] Checking passwords and showing the Policy Compliants.")
            for passw in fh:
                try:
                    passw = bytes.decode(passw, encoding="utf-8")
                except:
                    continue
                parse_passwords(passw)
            fh.close()
        # if it is not a file, use it as password
    else:
        print("[!] Using {} as the only password".format(pfname))
        parse_passwords(pfname)


"""
helps to parse passwords from the wordlist file
"""
def parse_passwords(fline):
    password = fline.replace("\n", "")
    if ((password != " ") and (password != "")):
        password = password.strip()
    
    if not check_policy_compliant(password): return

    save_to_file(password)


def save_to_file(data_line):
    with open("policy_compliant.txt", "at") as fh:
        fh.write(data_line + "\n")
        fh.close()


def usage():
    print("[!] Usage: python3 {} /path/to/users_wordlist /path/to/pass_wordlist http://www.example.com/login.php P@ssw0rd_P0l1cy_Ex@mpl3".format(sys.argv[0]))
    print("[!] Password Policy is optional. We need to pass a template for the Policy checker")
    exit()


def main():
    if (len(sys.argv) > 2):
        try:
            policy_template = sys.argv[1]
            check_policies_enabled(policy_template)
        except:
            print("[!] Not password policy entered.")
            usage()

        # if the argument provided as passwords wordlist path is a file, get the passwords from it
        parse_passwords_wordlist()

    else:
        print("[!] Usage: python3 {} P@ssw0rd_P0l1cy_Ex@mpl3 /path/to/pass_wordlist".format(sys.argv[0]))
        print("[!] We need to pass a template for the Policy checker")
        exit()


main()
