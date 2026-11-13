from datetime import datetime

def clock():
    return datetime.now().strftime("%H:%M")

rules = {"hello":"hello i'm Echo-mini",
         "name":"i'm Kiyana and i make Echo-mini",
         "price":"10 dollors in month",
         "bye": "goodbye"
    }
for msg in ["Hello", "time", "PRICE", "pizza","bye"]:
    word = msg.strip().lower()
    if word == "bye":
        print(rules[word])
        break
    if word in rules:
        print(word, "->", rules[word])
    elif word == "time": 
        print(word, "-> hour", clock())
    else:
        print(word, "not found")