import simplejson as json
#import json

#Dict(Json)선언

data = {}
data['people'] = []
data['people'].append({
    'name' : 'kim',
    'website' : 'naver.com',
    'from' : 'seoul',
    'grade' : [84,65,87,99]
})

data['people'].append({
    'name' : 'park',
    'website' : 'google.com',
    'from' : 'busan',
    'grade' : [88,66,97,96]
})

data['people'].append({
    'name' : 'lee',
    'website' : 'daum.net',
    'from' : 'incheon',
    'grade' : [94,75,88,99]
})

#json 파일쓰기 (dump)

with open('c:/section4/member.json','w') as outfile:
    json.dump(data, outfile)

#print(data)
