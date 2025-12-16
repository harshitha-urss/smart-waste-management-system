# iot_simulator/simulate_bin_open.py
import requests, time

API = 'http://127.0.0.1:8000/iot'

def simulate(device_id='sim01', binname='wet'):
    payload = {
        'device_id': device_id,
        'timestamp': time.time(),
        'action': f'OPEN_BIN_{binname.upper()}',
        'meta': {'bin': binname}
    }
    r = requests.post(API, json=payload)
    try:
        print(r.json())
    except:
        print('response', r.text)

if __name__ == '__main__':
    for i in range(3):
        simulate(device_id='sim01', binname='wet')
        time.sleep(1)
