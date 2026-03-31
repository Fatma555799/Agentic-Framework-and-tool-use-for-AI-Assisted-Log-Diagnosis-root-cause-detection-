from agent import SimpleLogAgent
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python demo.py path/to/your/log.bin")
        sys.exit(1)
    
    log_path = sys.argv[1]
    agent = SimpleLogAgent()
    
    print("ArduPilot AI Log Diagnosis Agent (Demo)")
    print("="*60)
    result = agent.diagnose(log_path)
    
    print("\nDiagnosis Result:")
    for cause in result["root_causes"]:
        print(f"\n Issue: {cause['issue']}")
        print(f"   Severity: {cause['severity']}")
        print(f"   Confidence: {cause['confidence']}%")
        print(f"   Evidence: {cause['evidence']}")
        print(f"   Fix: {cause['suggested_fix']}")
    
    print(f"\nOverall Confidence: {result['overall_confidence']}%")