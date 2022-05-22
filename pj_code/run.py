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
                    "simpleText": {
                        "text": answer + "\nhttps://www.hongik.ac.kr/contents/www/cor/calendar_2.html"
                    }
                }
            ]
        }
    }
    return responseBody

# 수강신청 홈페이지 제공 : http://퍼블릭_IPv4_주소:5000/y/corseReg
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
                    "simpleText": {
                        "text": answer + "\nhttps://sugang.hongik.ac.kr/cn1000.jsp"
                    }
                }
            ]
        }
    }
    return responseBody

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)