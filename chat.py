import random
import json
from openaipart import main
import torch
import re
from datetime import datetime,date
from light import Green,Lime,Red,Cyan,LightBlue,Blue,Pink,Purple,lightoff,lighton,setBrightnessValue
import speech_recognition as sr
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
import speech_recognition as sr


r = sr.Recognizer()




device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('pytorchpart/intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "pytorchpart/data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]
now = datetime.now()

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Jarvis"
print("Let's chat! (type 'quit' to exit)")
while True:
    with sr.Microphone(device_index=0, sample_rate=44100, chunk_size=512) as source:

        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, phrase_time_limit=5)

        try:

            speaktext = r.recognize_google(audio)
            
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from speech recognition service; {e}")
    sentence = speaktext
    savesentence = sentence
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    date_today = date.today()
    day_today = now.strftime('%A')
    current_time = now.strftime("%H:%M:%S")
    if prob.item() > 0.85:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                if random.choice(intent['responses']) == "BRIGHTNESS":
                    match = re.search(r'\d+',savesentence)
                    if match:
                        number = int(match.group())
                        setBrightnessValue(number)
                    break
                if random.choice(intent['responses']) == "COLORGREEN":
                    Green()
                    break
                if random.choice(intent['responses']) == "COLORLIME":
                    Lime()
                    break
                if random.choice(intent['responses']) == "COLORRED":
                    Red()
                    break
                if random.choice(intent['responses']) == "COLORCYAN":
                    Cyan()
                    break
                if random.choice(intent['responses']) == "COLORLIGHTBLUE":
                    LightBlue()
                    break
                if random.choice(intent['responses']) == "COLORBLUE":
                    Blue()
                    break
                if random.choice(intent['responses']) == "COLORPINK":
                    Pink()
                    break
                if random.choice(intent['responses']) == "COLORPURPLE":
                    Purple()
                    break
                if random.choice(intent['responses']) == "ON":
                    lighton()
                    break
                if random.choice(intent['responses']) == "OFF":
                    lightoff()
                    break
                if random.choice(intent['responses']) == "TIME":
                    print(f"{bot_name}: {current_time}")
                    break
                if random.choice(intent['responses']) == "DATE":
                    print(f"{bot_name}: {date_today}")
                    break
                if random.choice(intent['responses']) == "DAY":
                    print(f"{bot_name}: {day_today}")
                    break
                if random.choice(intent['responses']) == "GPT":
                    main(savesentence)
                    break
                
                else:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
                    break
    else:
        main(savesentence)
        break