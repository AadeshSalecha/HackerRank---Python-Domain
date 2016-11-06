'''
Title     : Validating Credit Card Numbers
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re
def valid(s):
    tmp = re.findall(r'([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})(.*$)',s)
    if tmp == []:
        return False
    return len(tmp[0]) == 5 and tmp[0][4] == '' and not(re.search(r'(\d)-?\1-?\1-?\1', s)) and (len(s) == 16 or len(s) == 19)

for i in range(input()):
    print "Valid" if valid(str(raw_input())) else "Invalid"