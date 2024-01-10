from pathlib import Path
import openai

speech_file_path = Path(__file__).parent / "speech.mp3"
response = openai.Audio.Speech.create(
  model="tts-1",
  voice="alloy",
  input="The quick brown fox jumped over the lazy dog."
)
response.stream_to_file(speech_file_path)