from typing import Dict

from streamlit import empty
import log_parser
def apply_rules(features: Dict, messages: Dict) -> list:
    diagnoses = []
    # Rule 1: High Vibration
    if features.get('max_vibe', 0) > 30:
        diagnoses.append({
            "issue": "High Vibration",
            "severity": "High",
            "confidence": 85,
            "evidence": f"VIBE max = {features['max_vibe']:.1f} m/s² (threshold >30)",
            "suggested_fix": "Check vibration damping, motor balance, props. See: https://ardupilot.org/copter/docs/common-measuring-vibration.html"
        })
    
    # Rule 2: Battery Low
    if features.get('batt_voltage_min', 0) < 10.0:  
        diagnoses.append({
            "issue": "Battery Voltage Low / Brownout risk",
            "severity": "Critical",
            "confidence": 90,
            "evidence": f"Min voltage = {features['batt_voltage_min']:.2f}V",
            "suggested_fix": "Check battery, connectors, power module. Adjust BATT_LOW_VOLT."
        })
    if diagnoses == []:
        diagnoses.append({
            "issue": "No major issues detected",
            "severity": "None",
            "confidence": 95,
            "evidence": "All features within normal ranges.",
            "suggested_fix": "None needed. Log looks healthy."
        })
    return diagnoses
result = log_parser.parse_bin_log("00afa36e54__log_0007_vibration_high.bin")
diagnoses = apply_rules(result['features'],result['raw_messages'])
print(diagnoses)