from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
latest_command = None
latest_command_y = None
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
    global latest_command, latest_command_y
    data = request.json
    latest_command = data.get('direction')
    latest_command_y = data.get('direction_y')
    print(f"[RECEIVED] Command: {latest_command} and Command_y: {latest_command_y}")
    return 'OK'

@app.route('/get_command', methods=['GET']) # 유니티에 보내는 함수
def get_command():
    global latest_command
    cmd = latest_command
    latest_command = None  # 읽었으면 비움
    return jsonify({"direction": cmd})

@app.route('/get_command_y', methods=['GET']) # 유니티에 보내는 함수
def get_command_y():
    global latest_command_y
    cmd_y = latest_command_y
    latest_command_y = None  # 읽었으면 비움
    return jsonify({"direction": cmd_y})

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    print(f"Starting Flask server...")
    print(f"Server is running at: http://{host}:{port}")
    app.run(host=host, port=port)


