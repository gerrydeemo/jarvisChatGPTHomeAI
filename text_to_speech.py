import speech_recognition as sr
from chat import wholefunc

r = sr.Recognizer()


with sr.Microphone(device_index=0, sample_rate=44100, chunk_size=512) as source:

    r.adjust_for_ambient_noise(source)

    audio = r.listen(source, phrase_time_limit=5)

try:

    text = r.recognize_google(audio)
    
except sr.UnknownValueError:
    print("Speech recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from speech recognition service; {e}")
