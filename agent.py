from tools import ParserTool, RuleTool 

class SimpleLogAgent:
    def __init__(self):
        self.tools = {
            "parse_log": ParserTool(),
            "apply_rules": RuleTool(),
        }
    
    def diagnose(self, log_path: str) -> dict:
        print("Step 1: Parsing log...")
        parse_result = self.tools["parse_log"].run(log_path)
        
        print("Step 2: Applying physics rules...")
        rules_result = self.tools["apply_rules"].run(parse_result['features'], parse_result['raw_messages'])
        
        final_diagnosis = {
            "log_path": log_path,
            "root_causes": rules_result,
            "overall_confidence": max([r["confidence"] for r in rules_result], default=0) if rules_result else 30,
            "recommendation": "Check evidence links above. If inconclusive, upload to forum with this report."
        }
        
        return final_diagnosis
