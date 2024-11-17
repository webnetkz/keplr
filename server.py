import uuid
from flask import Flask, request, jsonify
import subprocess
import json
import threading

app = Flask(__name__)

db = {}

STATUS_WIP = "wip"
STATUS_SUCCESS = "success"
STATUS_FAILED = "failed"

@app.route('/status/<uuid>', methods=['GET'])
def handle_get(uuid):
    if uuid in db:
        task = db[uuid]
        return jsonify({"status": task['status'], "message": task.get('message', '')})
    else:
        return jsonify({"status": STATUS_FAILED, "message": "UUID not found in the database"}), 404

@app.route('/start', methods=['POST'])
def handle_post():
    data = request.get_json()

    new_uuid = str(uuid.uuid4())

    db[new_uuid] = {
        "status": STATUS_WIP,
        "data": data,
        "message": "Registration in progress"
    }

    def run_task(uuid, data):
        json_data = json.dumps(data)
        process = subprocess.Popen(
            ['python', 'main.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout, stderr = process.communicate(input=json_data.encode('utf-8'))

        if stderr:
            print(f"Error: {stderr.decode('utf-8')}")
            db[uuid]['status'] = STATUS_FAILED
            db[uuid]['message'] = "Transaction failed"
        else:
            print(f"Success: {stdout.decode('utf-8')}")
            db[uuid]['status'] = STATUS_SUCCESS
            db[uuid]['message'] = stdout.decode('utf-8')

    threading.Thread(target=run_task, args=(new_uuid, data)).start()

    return jsonify({"uuid": new_uuid})


if __name__ == '__main__':
    app.run(debug=True)
