# Smart Waste System — Full Production Demo (Software-only)

## Quickstart (Windows + venv)
1. venv already created and activated? If not:

2. Install deps:

3. Start server:

4. Open browser: http://127.0.0.1:8000

5. Upload image via UI to classify and award tokens.

6. Run IoT simulation in another terminal:

7. Check logs:
- `/logs`
- `/ledger`
- `/users`

## Notes
- MobileNetV2 weights will download once on first run (internet required).
- `data/users.csv` and `data/logs.csv` are created automatically.
- For production or hardware integration, replace the IoT simulator with real device HTTP/MQTT calls to `/iot`.
