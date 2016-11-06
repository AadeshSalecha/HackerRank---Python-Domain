'''
Title     : HTML Parser - Part 1
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for i in attrs:
            print '-> ' + str(i[0]) + ' > ' + str(i[1])
            
    def handle_endtag(self, tag):
        print "End   :", tag

    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for i in attrs:
            print '-> ' + str(i[0]) + ' > ' + str(i[1])

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed('\n'.join([str(raw_input()) for i in range(input())]))