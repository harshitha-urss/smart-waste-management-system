# backend/rewards.py
from .database import read_users, write_users
import pandas as pd

# token rules
TOKENS = {
    'correct_segregation': 10,
    'throw_in_machine': 5,
    'daily_streak': 3,
    'rare_recycle': 8,
    'report_full': 4
}

BADGES = [
    (50, 'Eco Beginner'),
    (200, 'Eco Warrior'),
    (500, 'Eco Champion')
]

def award_tokens(user_id: str, reason: str):
    df = read_users()
    if user_id not in df['user_id'].values:
        df = pd.concat([df, pd.DataFrame([{"user_id":user_id, "mistakes":0, "points":0, "blocked":False}])], ignore_index=True)
    idx = df.index[df['user_id']==user_id][0]
    if df.at[idx, 'blocked']:
        return {'status':'blocked', 'user': df.iloc[idx].to_dict()}
    delta = TOKENS.get(reason, 0)
    df.at[idx, 'points'] = int(df.at[idx, 'points']) + int(delta)
    write_users(df)
    total = df.at[idx, 'points']
    earned = [name for (th, name) in BADGES if total >= th]
    return {'status':'ok', 'awarded': delta, 'total': total, 'badges': earned}

def penalize(user_id: str):
    df = read_users()
    if user_id not in df['user_id'].values:
        df = pd.concat([df, pd.DataFrame([{"user_id":user_id, "mistakes":0, "points":0, "blocked":False}])], ignore_index=True)
    idx = df.index[df['user_id']==user_id][0]
    df.at[idx, 'mistakes'] = int(df.at[idx, 'mistakes']) + 1
    status = 'penalized'
    if df.at[idx, 'mistakes'] >= 5:
        df.at[idx, 'blocked'] = True
        status = 'blocked'
    write_users(df)
    return {'status': status, 'record': df.iloc[idx].to_dict()}
