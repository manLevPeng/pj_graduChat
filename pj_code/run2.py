from flask import Flask, json, request, jsonify
app = Flask(__name__)

#서버 정상적으로 작동하는지 확인 : http://퍼블릭_IPv4_주소:5000/
@app.route("/") 
def hello():
    return "Hi, sever is runnung"

# 학시일정 홈페이지 제공 : http://퍼블릭_IPv4_주소:5000/y/Schedule
@app.route('/y/Schedule', methods=['POST'])
def Schedule():
    body = request.get_json()
    y_schedule = body["action"]["detailParams"]["y_schedule"]["value"] # json파일 읽기

    answer = y_schedule

    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
            {
                "basicCard": {
                    "thumbnail": {
                        "imageUrl": "https://github.com/manLevPeng/pj_graduChat/blob/8ad5b9a4d8b7932c880d753c01ab675b90c31562/pj_img/%ED%99%8D%EB%8C%80%EB%A1%9C%EA%B3%A0_%EB%B8%94%EB%A3%A8.jpg"
                    },
                    "buttons": [
                        {
                        "action": "webLink",
                        "label": "학사일정",
                        "webLinkUrl": "https://www.hongik.ac.kr/contents/www/cor/calendar_2.html"
                        }
                    ]
                }
            }
            ]
        }
    }
    return responseBody

# 수강신청 홈페이지 제공 : http://퍼블릭_IPv4_주소:5000/y/CorseReg
##추후업데이트
@app.route('/y/CorseReg', methods=['POST'])
def CorseReg():
    body = request.get_json()
    y_corseReg = body["action"]["detailParams"]["y_corseReg"]["value"] # json파일 읽기

    answer = y_corseReg

    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "thumbnail": {
                            "imageUrl": "https://github.com/manLevPeng/pj_graduChat/blob/8ad5b9a4d8b7932c880d753c01ab675b90c31562/pj_img/%ED%99%8D%EB%8C%80%EB%A1%9C%EA%B3%A0_%EB%B8%94%EB%9E%99.jpg"
                        },
                        "buttons": [
                            {
                            "action": "webLink",
                            "label": "수강신청 페이지",
                            "webLinkUrl": "https://sugang.hongik.ac.kr/cn1000.jsp"
                            },
                            {
                            "action": "webLink",
                            "label": "수강신청 연습 페이지",
                            "webLinkUrl": "https://hongiksugang.github.io"
                            },
                            {
                            "action": "webLink",
                            "label": "시간표",
                            "webLinkUrl": "https://sugang.hongik.ac.kr/cn50000.jsp"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return responseBody

# 학교 지도 제공 : http://퍼블릭_IPv4_주소:5000/y/Map
@app.route('/y/Map', methods=['POST'])
def Map():
    body = request.get_json()
    y_map = body["action"]["detailParams"]["y_map"]["value"] # json파일 읽기

    answer = y_map

    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "thumbnail": {
                            "imageUrl": "https://github.com/manLevPeng/pj_graduChat/blob/8ad5b9a4d8b7932c880d753c01ab675b90c31562/pj_img/%ED%99%8D%EB%8C%80%EB%A1%9C%EA%B3%A0_%EB%B8%94%EB%9E%99.jpg"
                        },
                        "buttons": [
                            {
                            "action": "webLink",
                            "label": "학교 홈페이지 지도",
                            "webLinkUrl": "https://www.hongik.ac.kr/contents/www/cor/seoulroad_1.html"
                            },
                            {
                            "action": "webLink",
                            "label": "홍그와트 지도",
                            "webLinkUrl": "https://everytime.kr/370446/v/242634440"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return responseBody
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)