from agents.resume_agent import rank_resumes
from agents.call_agent import transcribe_audio, summarize_transcript
from agents.self_cri_agent import critique_agent_actions

def orchestrate():
    # 1. Resume Ranking
    critiques = rank_resumes("data/resumes")
    print("\n📝 Resume Critiques:\n", critiques)

    # 2. Call Summary
    transcript = transcribe_audio("data/call_audio/sample_call.mp3")
    summary = summarize_transcript(transcript)
    print("\n📞 Call Summary:\n", summary)

    # 3. Self Evaluation
    action_log = "\n".join([f"{name}: {text}" for name, text in critiques])
    self_review = critique_agent_actions(action_log + "\n" + summary)
    print("\n🔍 Self-Critique:\n", self_review)