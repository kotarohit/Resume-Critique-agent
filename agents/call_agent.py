import whisper
from utils.llm_wrapper import call_openrouter

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['text']

def summarize_transcript(transcript):
    prompt = f"""Summarize the following transcript. Highlight insights, objections, and action items:\n{transcript}"""
    messages = [{"role": "user", "content": prompt}]
    return call_openrouter(messages)