from pymavlink import mavutil
import pandas as pd
import numpy as np
from typing import Dict, Any

path = "00afa36e54__log_0007_vibration_high.bin" 
def parse_bin_log(log_path: str) -> Dict[str, Any]:
    mlog = mavutil.mavlink_connection(log_path)
    messages = {
        'VIBE': [], 'BAT': [],  'EV': [], 'ATT': [],
        'EKF3': [], 'PARM': [], 'GPS': []
    }
    
    while True:
        msg = mlog.recv_match(type=list(messages.keys()), blocking=False)
        if msg is None:
            break
        msg_type = msg.get_type()
        messages[msg_type].append(msg.to_dict())
    
    dfs = {k: pd.DataFrame(v) for k, v in messages.items() if v}
    
    features = {}
    
    if 'VIBE' in dfs:
        vibe = dfs['VIBE']
        features['vibe_x_rms'] = vibe['VibeX'].mean()
        features['vibe_y_rms'] = vibe['VibeY'].mean()
        features['vibe_z_rms'] = vibe['VibeZ'].mean()
        features['clipping_total'] = vibe.get('Clip', 0).sum() if 'Clip' in vibe.columns else 0
        features['max_vibe'] = max(features['vibe_x_rms'], features['vibe_y_rms'], features['vibe_z_rms'])
    
    if 'BAT' in dfs:
        bat = dfs['BAT']
        features['batt_voltage_min'] = bat['Volt'].min()
        features['batt_current_max'] = bat['Curr'].max()
    
    vehicle = "Unknown"
    if hasattr(mlog, 'messages') and 'MSG' in mlog.messages:
        vehicle = str(mlog.messages['MSG'])

    return {
        'raw_messages': dfs,
        'features': features,
        'log_info': {
            'vehicle_type': vehicle, 
            'length': getattr(mlog, 'remaining', 0) 
        }
    }
# import json
# result = parse_bin_log(path)

# # 2. Print the Summary (The Features)
# print("\n" + "="*40)
# print("       FLIGHT LOG ANALYSIS RESULTS")
# print("="*40)

# print(f"\n[VEHICLE INFO]: {result['log_info']['vehicle_type']}")

# print("\n[EXTRACTED FEATURES]:")
# print(json.dumps(result['features'], indent=4))

# # 3. Optional: See the first few rows of the GPS or Battery table
# if 'BAT' in result['raw_messages']:
#     print("\n[BATTERY DATA PREVIEW]:")
#     print(result['raw_messages']['BAT'].head())

# print("\n" + "="*40)

