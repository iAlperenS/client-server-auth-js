import logging, os, uuid
from flask import Flask, jsonify, request
import subprocess
import requests
import time

app = Flask(__name__)

# HWID doğrulama durumu
hwid_status = {"status": "invalid"}

def get_hwid():
    hwid = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return hwid

def validate_hwid(hwid):
    # HWID check
    site = requests.get('example.com') your web
    if hwid in site.text:
        return "valid"
    else:
        return "invalid"

@app.route('/set_hwid_status', methods=['POST']) # Checking hwid status valid or invalid
def set_hwid_status():
    global hwid_status
    hwid = get_hwid()
    hwid_status['status'] = validate_hwid(hwid) # return valid or invalid
    return jsonify(hwid_status) # json

@app.route('/get_hwid_status', methods=['GET'])
def get_hwid_status():
    return jsonify(hwid_status)

if __name__ == '__main__':
    # Flask log seviyesini ayarlayın
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)  # Log

    app.run(host='0.0.0.0', port=5000)
    os.system("cls")
    print(" * Server side dont close this tab")
    print(" * github.com/iAlperenS")
