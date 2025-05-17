from utils.llm_wrapper import call_openrouter

def critique_agent_actions(action_logs):
    prompt = f"""You're a meta agent. Evaluate the following agent actions for accuracy, completeness, tone, and output quality. Suggest improvements:\n\n{action_logs}"""
    messages = [{"role": "user", "content": prompt}]
    return call_openrouter(messages)