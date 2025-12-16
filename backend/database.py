# backend/database.py
import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
USERS_CSV = os.path.join(DATA_DIR, 'users.csv')
LOGS_CSV = os.path.join(DATA_DIR, 'logs.csv')

os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(USERS_CSV):
    pd.DataFrame(columns=["user_id","mistakes","points","blocked"]).to_csv(USERS_CSV, index=False)
if not os.path.exists(LOGS_CSV):
    pd.DataFrame(columns=["timestamp","user_id","item","predicted_category","status","prev_hash","hash"]).to_csv(LOGS_CSV, index=False)

def read_users():
    return pd.read_csv(USERS_CSV)

def write_users(df: pd.DataFrame):
    df.to_csv(USERS_CSV, index=False)

def append_log(row: dict):
    df = pd.read_csv(LOGS_CSV)
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df.to_csv(LOGS_CSV, index=False)

def read_logs():
    return pd.read_csv(LOGS_CSV)
