import simplejson as json
#import json

#Dict(Json)선언

data = {}
data['people'] = []
data['people'].append({
    'name' : 'kim',
    'website' : 'naver.com',
    'from' : 'seoul'
})

data['people'].append({
    'name' : 'park',
    'website' : 'google.com',
    'from' : 'busan'
})

data['people'].append({
    'name' : 'lee',
    'website' : 'daum.net',
    'from' : 'incheon'
})

#print(data)

#dump vs dumps load vs loads

#Dict(Json) -> Str

e = json.dumps(data, indent=2)
#print(type(e))
#print(e)

#Str -> Dict(Json)

d = json.loads(e)
#print(type(d))
#print(d)

with open('c:/section4/member.json','w') as outfile:
    outfile.write(e)

with open('c:/section4/member.json','r') as infile:
    r = json.loads(infile.read())
    print("======")
    #print(type(r))
    #print(r)
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
