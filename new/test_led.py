from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 전역 상태
light_state = {
    "is_on": True,
    "color": {"r": 255, "g": 255, "b": 255}
}

@app.route('/')
def index():
    return render_template('index_led.html')

# ON/OFF 상태 설정
@app.route('/toggle', methods=['POST'])
def toggle_light():
    global light_state
    data = request.json
    if 'on' in data:
        light_state["is_on"] = bool(data["on"])
        print("[TOGGLE] LED 상태:", light_state["is_on"])
        return jsonify({"success": True, "on": light_state["is_on"]})
    return jsonify({"success": False, "error": "Missing 'on' parameter"}), 400

# RGB 색상 설정
@app.route('/set_color', methods=['POST'])
def set_color():
    global light_state
    data = request.json
    if all(k in data for k in ('r', 'g', 'b')):
        light_state["color"] = {
            "r": int(data.get("r", 255)),
            "g": int(data.get("g", 255)),
            "b": int(data.get("b", 255))
        }
        print("[SET_COLOR] LED 색상:", light_state["color"])
        return jsonify({"success": True, "color": light_state["color"]})
    return jsonify({"success": False, "error": "Missing RGB parameters"}), 400

# 상태 조회 (Unity 쪽에서 사용)
@app.route('/get_light', methods=['GET'])
def get_light():
    return jsonify(light_state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
