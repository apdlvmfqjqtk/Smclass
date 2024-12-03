import requests

def search_bus_schedule(api_key, start_station_id, end_station_id, lang=0, output='json', station_class=None):
    # API 엔드포인트 URL
    url = "https://api.odsay.com/v1/api/searchInterBusSchedule"
    
    # 요청 파라미터 설정
    params = {
        'apiKey': api_key,  # 발급된 API 키
        'startStationID': start_station_id,  # 출발 터미널 ID
        'endStationID': end_station_id,  # 도착 터미널 ID
        'lang': 0,  # 언어 설정 (기본: 국문 0, 영문 1, 등)
        'output': output,  # 출력 형식 (기본: json, xml 가능)
    }
    
    if station_class:
        params['stationClass'] = station_class  # 정류장 종류 (선택적 파라미터)

    # API 요청 보내기
    response = requests.get(url, params=params)

    # 응답 확인
    if response.status_code == 200:
        # JSON 데이터 반환
        data = response.json()
        return data
    else:
        # 에러 코드 출력
        print(f"Error {response.status_code}: {response.text}")
        return None

# API 키와 터미널 ID 예시 (여기서 API 키는 실제 발급 받은 키로 교체해야 합니다)
api_key = "xxxxxxxxxxx"  # 실제 발급된 API 키로 변경
start_station_id = 4000314  # 출발 터미널 ID (예시)
end_station_id = 4000030  # 도착 터미널 ID (예시)

# 버스 운행정보 검색
bus_info = search_bus_schedule(api_key, start_station_id, end_station_id, lang=1, output='json')

if bus_info:
    # 결과 출력 (간단히 결과의 일부만 출력)
    for result in bus_info['result']:
        print(f"출발 터미널: {result['startStationName']}")
        print(f"도착 터미널: {result['endStationName']}")
        print(f"첫차 시간: {result['firstTime']}")
        print(f"막차 시간: {result['lastTime']}")
        print(f"운행 정보:")
        
        for schedule in result['schedule']:
            print(f"- 버스타입: {schedule['busClass']} | 출발시간: {schedule['departureTime']} | 소요시간: {schedule['wasteTime']}분 | 요금: {schedule['fare']}원")
        print("="*50)
