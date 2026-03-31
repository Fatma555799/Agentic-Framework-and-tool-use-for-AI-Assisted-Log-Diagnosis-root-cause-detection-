import pandas as pd
def tool_vibration_analyzer(data):
    max_vibe = data['VibeX'].max()
    if max_vibe > 30:
        return {
            "issue": "High Vibration Detected",
            "val": max_vibe,
            "fix": "Check motor balance and propellers.",
            "wiki_link": "https://ardupilot.org/copter/docs/common-vibration-damping.html"
        }
    return None

def tool_battery_analyzer(data):
    low_volt = data['Volt'].min()
    if low_volt < 10.5:
        return {
            "issue": "Battery Voltage Critical",
            "val": low_volt,
            "fix": "Battery failsafe triggered. Check battery health.",
            "wiki_link": "https://ardupilot.org/copter/docs/common-failsafe-battery.html"
        }
    return None

class ArduLogAgent:
    def __init__(self):
        self.tools = [tool_vibration_analyzer, tool_battery_analyzer]

    def run(self, log_data):
        print("Agent is reasoning over the log data...")
        results = []
        for tool in self.tools:
            out = tool(log_data)
            if out:
                results.append(out)
        return results


mock_data = pd.DataFrame({
    'VibeX': [12, 15, 45, 20], 
    'Volt': [12.6, 12.2, 10.1, 11.0] 
})

if __name__ == "__main__":
    agent = ArduLogAgent()
    findings = agent.run(mock_data)

    print("\n--- Final Diagnosis Report ---")
    if not findings:
        print("✅ Log looks healthy!")
    for f in findings:
        print(f"⚠️ {f['issue']} (Value: {f['val']})")
        print(f"🔧 Fix: {f['fix']}")
        print(f"🔗 More info: {f['wiki_link']}\n")