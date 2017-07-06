from urllib.parse import urlencode
from urllib.request import Request, urlopen
import openpyxl
import re
import math
import pygame, time
import json

row = 0
validFields = ['name', 'contact_details', 'content']
validContactFields = ['phone', 'email', 'website', 'other']
validOtherFields = ['type', 'value']
validContentFields = ['letter_body', 'challenge_checkvalue']
start = 0
end = 100
checkvalue = ""
num = ""
for row in range (start, end):
    valid = True
    noEmail = False
    noPhone = False
    # if number is < 10 we add a 0
    if row < 10:
        url = 'https://wd51nn4ogc.execute-api.us-east-1.amazonaws.com/cover_letters?id=0' + str(row)
        num = "0" + str(row)
    else:
        url = 'https://wd51nn4ogc.execute-api.us-east-1.amazonaws.com/cover_letters?id=' + str(row)
        num = str(row)
    f = urlopen(url).read()
    values = json.loads(f.decode("utf-8"))
    # First check to see if there are any keys present other than name, contact_details, and content
    if len(list(filter(lambda a: a not in validFields, list(values.keys())))) > 0:
        print ("Extra field in JSON object number " + str(row))
        valid = False
    else:
        # If these are the only three fields
        # Check if name is a string
        if 'name' in values and type(values['name']) is not str:
            print ("Invalid name in JSON object number " + str(row))
            valid = False
        # Check if there are any keys persent other than phone, email, website, and other in contact_details
        elif 'name' not in values:
            print ("Missing name in JSON object number " + str(row))
            valid = False
        if 'contact_details' in values and len(list(filter(lambda a: a not in validContactFields, list(values['contact_details'].keys())))) > 0:
            print ("Extra contact_field in JSON object number " + str(row))
            valid = False
        elif 'contact_details' not in values:
            print ("Missing contact_field in JSON object number " + str(row))
            valid = False
        else:
            # Check if phone number is valid
            if 'phone' in values['contact_details'] and values['contact_details']['phone']:
                phoneRegex = re.compile('[-0-9 +()#]*')
                match = phoneRegex.search(values['contact_details']['phone'])
                if not match or not len(values['contact_details']['phone']) < 30:
                    print ("Invalid phone number format in JSON object number " + str(row))
                    valid = False
            # If there is no phone number keep track of that
            else:
                noPhone = True
            # Check if email is valid
            if 'email' in values['contact_details'] and values['contact_details']['email']:
                emailRegex = re.compile('[_A-Za-z0-9-]+(\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*(\.[A-Za-z]{2,4})')
                match = emailRegex.search(values['contact_details']['email'])
                if not match:
                    print ("Invalid email format in JSON object number " + str(row))
                    valid = False
            # If there is no email keep track of that
            else:
                noEmail = True
            # Make sure there is either a phone or email
            if noPhone and noEmail:
                print ("JSON object number " + str(row) + " contains neither an email nor phone number")
                valid = False
            if 'website' in values['contact_details'] and values['contact_details']['website']:
                websiteRegex = re.compile('https?://[-A-Za-z_~.]*\.[-A-Za-z_~.]{2,4}')
                match = websiteRegex.search(values['contact_details']['website'])
                if not match:
                    print ("Invalid website format in JSON object number " + str(row))
                    valid = False
            # There can be more than one 'other' object in contact_details so make sure they are all valid
            if 'other' in values['contact_details']:
                for i in range(0, len(values['contact_details']['other'])):
                    if len(list(filter(lambda a: a not in validOtherFields, list(values['contact_details']['other'][i].keys())))) > 0:
                        print ("Invalid other field in JSON object number " + str(row))
                        valid = False
        # Check if there are any keys persent other than letter_value, challenge_checkvalue, and other in content
        if 'content' in values and len(list(filter(lambda a: a not in validContentFields, list(values['content'].keys())))) > 0:
            print ("Invalid content field in JSON object number " + str(row))
            valid = False
        elif 'content' not in values:
            print ("Missing content field in JSON object number " + str(row))
            valid = False
        else:
            if 'letter_body' not in values['content']:
                print ("letter_body missing in JSON object number " + str(row))
                valid = False
    if valid == False:
        checkvalue += num

print("checkvalue: " + checkvalue)



'''
for criteria in values['contact_details']:
    for key, value in criteria.iteritems():
        print (key, 'is:', value)
    print ('')
    '''

'''
THERE CAN BE NO OTHER KEYS THAN name, contact_details, content
{
    "name": "Andrew Fischl",
    "contact_details":
    {
        "phone": "(631) 707-5353",
        "email": "anfischl@gmail.com",
        "other":
        [
            {
                "type": "github",
                "value": "https://github.com/andrefisch/"
            },
            {
                "type": "LinkedIn",
                "value": "https://linkedin.com/in/andrew-fischl-1b2376118/"
            }
        ]
    },
    "content":
    {
        "letter_body": "After spending the last Olympic cycle being a full-time athlete and part-time student/freelance programmer, I am looking to transition to serious and stable full-time employment. In addition to narrowly missing the Olympic fencing team I own and run the 2nd largest fencing video portal in the world. I have a lot of experience editing and managing large amounts of videos and I am excited to help test technology that relates to a field I have so much familiarity with.",
        "challenge_checkvalue": "162329778993"
    }
}
'''

