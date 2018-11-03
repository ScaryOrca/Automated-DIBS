#!/usr/bin/env python3

import argparse
import datetime
import requests
import urllib.request

def main():
    # command line arguments 
    parser = argparse.ArgumentParser(description="Reserve study rooms on campus at Tennessee Tech.")
    parser.add_argument("-f", "--first", help="First name", required=True)
    parser.add_argument("-l", "--last", help="Last name", required=True)
    parser.add_argument("-e", "--email", help="Email address", required=True)
    parser.add_argument("-p", "--phone", help="Phone number", required=False)
    parser.add_argument("-r", "--room", help="Room to reserve", required=True)
    args = parser.parse_args();

    # reserve room 3 days in advance
    startDate = datetime.date.today() + datetime.timedelta(days=3)
    startDate = startDate.strftime("%Y/%m/%d 16:00:00")

    # room variables
    staffAccess = "False"
    reservationLength = "2"
    langCode = "en-US"
    URL = "https://tntech.evanced.info/admin/dibs/api/reservations/post"

    print("Requesting room for 2 hours on: " + startDate)
    
    # set headers
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                    ' Chrome/36.0.1941.0 Safari/537.36'), ('Content-Type', 'application/json; charset=utf-8')]
    urllib.request.install_opener(opener)

    # set up key value pairs for the post request variables
    DATA = (
            ('firstName', args.first),
            ('lastName', args.last),
            ('emailAddress', args.email),
            ('phoneNumber', args.phone),
            ('reservationLength', reservationLength),
            ('staffAccess', staffAccess),
            ('startDate', startDate),
            ('roomid', args.room),
            ('langCode', langCode),
            )

    r = requests.post(url = URL, data = DATA)
    text = r.json()
    print("\n",text)

    parser = argparse.ArgumentParser(description="Reserve study rooms on campus at Tennessee Tech.")
    parser.add_argument("-f", "--first-name", help="First name", required=True)
    parser.add_argument("-l", "--last-name", help="Last name", required=True)
    parser.add_argument("-e", "--email", help="Email address", required=True)
    parser.add_argument("-p", "--phone", help="Phone number", required=False)
    parser.add_argument("-r", "--room", help="Room to reserve", required=True)
    args = parser.parse_args();

if __name__ == "__main__":
    main()
