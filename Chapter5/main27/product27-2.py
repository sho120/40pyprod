import requests

url = 'http://api.vworld.kr/req/address?'
params = 'service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=-false&format=json&type='

road_type = 'ROAD'
road_type2 = 'PARCEL'
address = '&address='
key = '&key='
primary_key = '발급 받은 인증키를 붙여넣으세요.'

def request_geo(road):
    page = requests.get(url+params+road_type+address+road+key+primary_key)
    json_data = page.json()
    if json_data['response']['status'] == 'OK':
        x = json_data['response']['status']['point']['x']
        y = json_data['response']['status']['point']['y']
        return x,y
    else:
        #print("else")
        x = 0
        y = 0
        return x,y

x,y = request_geo("경기도 시흥시 산기대학로 238 (정왕동, 한국산업기술대학교)")

print(f'x값: {x}')
print(f'y값: {y}')