#!/usr/bin/python3
"""Alta3 Research - tracking ISS updated output"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    # strip off the attachment (JSON) and read it
    # the problem here, is that it will read out as a string
    helmet = groundctrl.read()

    helmetson = json.loads(helmet.decode("utf-8"))

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)
    for x in people:
        print(x["name"] + " on the " + x["craft"])

if __name__ == "__main__":
    main()
