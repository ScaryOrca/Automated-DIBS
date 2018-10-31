#!/usr/bin/env python3
import requests
import urllib.request
import datetime

# add 3 days to current day, in order to reserve the room 3 days ahead
startDate = datetime.date.today() + datetime.timedelta(days=3)
startDate = startDate.strftime("%Y/%m/%d 16:00:00")
print("Trying to reserve Volpe Library room for 2 hours on: " + startDate)

# prepare rest of data for TN TECH "DIBS" API
firstName = 'Jacob D'
lastName = 'Kennedy'
emailAddress = "jdkennedy45@students.tntech.edu"
phoneNumber = "(901) 270-6562"
staffAccess = 'False'
reservationLength = '2'
roomid = '12' # room 244 in TN Tech library
langCode = 'en-US'

# set URL that we will direct our request to
URL = "https://tntech.evanced.info/admin/dibs/api/reservations/post"

# set headers
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                    ' Chrome/36.0.1941.0 Safari/537.36'), ('Content-Type', 'application/json; charset=utf-8')]
urllib.request.install_opener(opener)

# set up key value pairs for the post request variables
DATA = (
        ('firstName', firstName),
        ('lastName', lastName),
        ('emailAddress', emailAddress),
        ('phoneNumber', phoneNumber),
        ('reservationLength', reservationLength),
        ('staffAccess', staffAccess),
        ('startDate', startDate),
        ('roomid', roomid),
        ('langCode', langCode),
        )

r = requests.post(url = URL, data = DATA)
text = r.json()
print("\n",text)