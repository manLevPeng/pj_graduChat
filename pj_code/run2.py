from flask import Flask, json, request, jsonify
app = Flask(__name__)

#서버 정상적으로 작동하는지 확인 : http://퍼블릭_IPv4_주소:5000/
@app.route("/") 
def hello():
    return "Hi, sever is runnung"

# 학시일정 홈페이지 제공 : http://퍼블릭_IPv4_주소:5000/y/schedule
@app.route('/y/schedule', methods=['POST'])
def schedule():
    body = request.get_json()
    schedule_academic = body["action"]["detailParams"]["schedule_academic"]["value"] # json파일 읽기

    answer = schedule_academic

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

# 수강신청 홈페이지 제공 : http://퍼블릭_IPv4_주소:5000/y/corseReg
##추후업데이트
@app.route('/y/corseReg', methods=['POST'])
def corseReg():
    body = request.get_json()
    schedule_academic = body["action"]["detailParams"]["schedule_academic"]["value"] # json파일 읽기

    answer = schedule_academic

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
                            "webLinkUrl": "https://hongiksugang.github.io/sugang/main"
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)