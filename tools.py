class ParserTool:
    def run(self, log_path):
        from log_parser import parse_bin_log
        return parse_bin_log(log_path)

class RuleTool:
    def run(self, features, messages):
        from rule_engine import apply_rules
        return apply_rules(features, messages)