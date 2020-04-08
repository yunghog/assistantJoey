import datetime as t
def tellTime():
    now = t.datetime.now()
    str(now)
    return str(now.hour) + " : " + str(now.minute)
#print(tellTime())
