#Time Delta
#by shashank21j
#Problem
#Submissions
#Leaderboard
#Discussions
#Editorial
#Timestamps are given in the format:
#
#Day dd Mon yyyy hh:mm:ss +xxxx
#
#Here +xxxx represents the time zone. See the sample below for details.
#
#Task 
#Given  timestamps, print the absolute difference (in seconds) between them.
#
#Input Format 
#The first line contains , the number of testcases. 
#Each testcase contains  lines, representing time  and time .
#
#Output Format 
#Print the absolute difference  in seconds.
#
#Constraints 
#It is guaranteed that the input contains only valid timestamps, and the year can reach up to .
#
#Sample Input
#
#2
#Sun 10 May 2015 13:54:36 -0700
#Sun 10 May 2015 13:54:36 +0000
#Sat 02 May 2015 19:54:36 +0530
#Fri 01 May 2015 13:54:36 +0000
#Sample Output
#
#25200
#88200

from datetime import tzinfo, timedelta, datetime

ZERO = timedelta(0)
HOUR = timedelta(hours=1)

class UTC(tzinfo):
    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO

utc = UTC()

class FixedOffset(tzinfo):
    def __init__(self, offset):
        self.__offset = timedelta(minutes = offset)

    def utcoffset(self, dt):
        return self.__offset

    def dst(self, dt):
        return ZERO

for i in range(input()):
    a = str(raw_input())
    naive_dt = datetime.strptime(a[:25], '%a %d %b %Y %H:%M:%S ')
    offset_str = a[25:]
    offset = int(offset_str[-4:-2])*60 + int(offset_str[-2:])
    if offset_str[0] == "-":
        offset = -offset
    dt = naive_dt.replace(tzinfo=FixedOffset(offset))


    b = str(raw_input())
    naive_dt1 = datetime.strptime(b[:25], '%a %d %b %Y %H:%M:%S ')
    offset_str = b[25:]
    offset = int(offset_str[-4:-2])*60 + int(offset_str[-2:])
    if offset_str[0] == "-":
        offset = -offset
    dt1 = naive_dt1.replace(tzinfo=FixedOffset(offset))

    print abs(int((dt-dt1).total_seconds()))

