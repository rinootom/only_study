from flask import Flask, request, jsonify, render_template
import secrets

app = Flask(__name__)
api_keys = {}
user_variables = {}

def generate_api_key():
    return secrets.token_hex(16) # 랜덤

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
    var_name = data.get('var_name')
    var_value = data.get('var_value')

    if key not in api_keys.values():
        return jsonify({'error': 'Invalid API key'}), 403

    username = [u for u, k in api_keys.items() if k == key][0]
    user_variables.setdefault(username, {})[var_name] = var_value
    return jsonify({'message': f'{var_name} 저장 완료'})

@app.route('/get_var', methods=['GET'])
def get_variable():
    key = request.args.get('api_key')
    var_name = request.args.get('var_name')

    if key not in api_keys.values():
        return jsonify({'error': 'Invalid API key'}), 403

    username = [u for u, k in api_keys.items() if k == key][0]
    print(f"[현재 전체 변수 상태] {user_variables}")
    value = user_variables.get(username, {}).get(var_name)

    if value is None:
        return jsonify({'error': '변수 없음'}), 404

    return jsonify({'var_name': var_name, 'value': value})


if __name__ == '__main__':
    app.run(debug=False)
