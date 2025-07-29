from flask import Flask, request, jsonify, render_template
import secrets

app = Flask(__name__)
api_keys = {} # <- db 가 아닌 일단 배열에 저장
user_variables = {}

def generate_api_key():
    return secrets.token_hex(16) # API 생성

@app.route('/')
def index():
    return render_template('index_test.html')  

@app.route('/generate_key', methods=['POST'])
def generate_key():
    username = request.json.get('username')
    if not username:
        return jsonify({'error': 'username required'}), 400
    key = generate_api_key()
    api_keys[username] = key 
    return jsonify({'api_key': key})

@app.route('/set_var', methods=['POST'])
def set_variable():
    data = request.json
    key = data.get('api_key')
    var_name = data.get('var_name')     # <- 변수 값 셋팅 , 애네 값 활용하는 거임
    var_value = data.get('var_value')   # <- 변수 값 셋팅 , 애네 값 활용하는 거임

    if key not in api_keys.values():
        return jsonify({'error': 'Invalid API key'}), 403

    # u 사용자 이름, k 가 키값
    # u,k 가 api_keys.items() 안에 있을때 반복    만약 k = key 가 같은 것만 u 리스트에 넣음
    username = [u for u, k in api_keys.items() if k == key][0]  # <- 리스트 0번째 값만 즉 게스트 이름
    
    # 해당 사용자 데이터를 user_variables <- 여기에 저장
    # setdefault 키가 없으면 새로 만들고, 있으면 그 값을 그대로 반환
    # 사용 이유 if문 없어도 딕셔너리 초기화 가능
    user_variables.setdefault(username, {})[var_name] = var_value
    return jsonify({'message': f'{var_name} 저장 완료'})

@app.route('/get_var', methods=['GET'])
def get_variable():
    key = request.args.get('api_key')
    var_name = request.args.get('var_name')

    if key not in api_keys.values():
        return jsonify({'error': 'Invalid API key'}), 403

    username = [u for u, k in api_keys.items() if k == key][0]
    print(f"[현재 전체 변수 상태] {user_variables}")   # 추가된 변수 플라스크 서버 터미널에서 확인용 코드
    value = user_variables.get(username, {}).get(var_name) # 유저네임하고 value 값 저장

    if value is None:
        return jsonify({'error': '변수 없음'}), 404

    return jsonify({'var_name': var_name, 'value': value})


if __name__ == '__main__':
    app.run(debug=False)
