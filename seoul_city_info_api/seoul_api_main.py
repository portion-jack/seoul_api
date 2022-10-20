import pandas as pd
import requests
from bs4 import BeautifulSoup
import xmltodict
from __myapi__ import *

location_list=['강남 MICE 관광특구', '동대문 관광특구', '명동 관광특구', '이태원 관광특구',
               '잠실 관광특구', '종로·청계 관광특구', '홍대 관광특구', '경복궁·서촌마을', '광화문·덕수궁', '창덕궁·종묘',
               '가산디지털단지역', '강남역', '건대입구역', '고속터미널역', '교대역', '구로디지털단지역', '서울역', '선릉역',
               '신도림역', '신림역', '신촌·이대역', '역삼역', '연신내역', '용산역', '왕십리역',
               'DMC(디지털미디어시티)', '창동 신경제 중심지', '노량진', '낙산공원·이화마을', '북촌한옥마을', '가로수길',
               '성수카페거리', '수유리 먹자골목', '쌍문동 맛집거리', '압구정로데오거리', '여의도', '영등포 타임스퀘어', '인사동·익선동',
               '국립중앙박물관·용산가족공원', '남산공원', '뚝섬한강공원', '망원한강공원', '반포한강공원', '북서울꿈의숲', '서울대공원',
               '서울숲공원', '월드컵공원', '이촌한강공원', '잠실종합운동장', '잠실한강공원']

attrs = ['live_ppltn_stts','road_traffic_stts', 'prk_stts', 'sub_stts', 'bus_stn_stts', 'sbike_stts', 'weather_stts']

api_key = my_api()

response = requests.get(f"http://openapi.seoul.go.kr:8088/{api_key}/xml/citydata/1/5/{location}")


def response2df(_response,_attr):
    soup=BeautifulSoup(response.content,"lxml")
    attr_xml=soup.find('citydata').find(_attr)
    attr_dict = xmltodict.parse(str(attr_xml))[_attr]
    try:
        return pd.DataFrame(attr_dict[_attr])
    except:
        return pd.DataFrame(attr_dict)

info_by_loc= list()

"""
info_by_loc=[
    location_1=[attrs],
    location_2=[attrs],
    .
    .
    .
    location_n =[attrs]
]
"""
for location in location_list:
    _list=list()
    response = requests.get(f"http://openapi.seoul.go.kr:8088/{api_key}/xml/citydata/1/5/{location}")
    for attr in attrs:
        _list.append(response2df(response,attr))
    info_by_loc.append(_list)

