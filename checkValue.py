import urllib2
for i in range (0, 100):
    if i < 10:
        print urllib2.urlopen("https://wd51nn4ogc.execute-api.us-east-1.amazonaws.com/cover_letters?id=0" + str(i)).read()
    else:
        print urllib2.urlopen("https://wd51nn4ogc.execute-api.us-east-1.amazonaws.com/cover_letters?id=" + str(i)).read()

"""
177780858994
"""
