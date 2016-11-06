'''
Title     : HTML Parser - Part 2
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print ">>> Multi-line Comment"
            print data
        else:
            print ">>> Single-line Comment"
            print data
        
    def handle_data(self, data):
        set_b = True
        if len(data) == 1:
            set_b = False
        if set_b:           
            print ">>> Data"
            print data
 
html = ""       
for i in range(int(raw_input())):
    html += raw_input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
