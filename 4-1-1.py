import sys
import io
import requests
import urllib.request as req
from bs4 import BeautifulSoup
import os.path
import pickle #객체 또는 텍스트를 직렬화, 역직렬화


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#파일 이름과 데이터 (변수선언)

bfilename = "c:/section4/test.bin"
tfilename = "c:/section4/test.txt"

data1 = 77
data2 = "hello, world!"
data3 = ['car','apple','house']

#바이너리 쓰기
with open(bfilename, 'wb') as f:
    pickle.dump(data1,f) #dump -> 객체를 바이너리 / dumps ->문자열을 직렬화
    pickle.dump(data2,f)
    pickle.dump(data3,f)

#텍스트 쓰기
with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3)) # car apple house 변환!

#바이너리 읽기 - class 그대로 //

with open(bfilename, 'rb') as f:
    b = pickle.load(f)
    print(type(b), 'Binary Read  | ',b )
    b = pickle.load(f)
    print(type(b), 'Binary Read2 | ',b )
    b = pickle.load(f)
    print(type(b), 'Binary Read3| ',b )

#텍스트 읽기

with open(tfilename, 'rt') as f:
    for i, line in enumerate(f,1):
        print(type(line), 'Text Read' + str(i) + '|' + line, end='')
