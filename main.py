from  tkinter import *
import pyjokes
from googletrans import Translator
import httpcore

def generate_joke():
    try:
        translator = Translator()
        joke = pyjokes.get_joke()
        text["height"] = 1
        text["text"] = translator.translate(joke,dest=f"{lang.get()}").text
    except ValueError:
        text["height"] = 1
        text["text"] = f"Ошыбыка язык :{lang.get()} введен неправильно"
    except httpcore._exceptions.ConnectError:
        try:
            joke_ofline = pyjokes.get_joke(language=lang.get())
            text["height"] = 2
            text["text"] = f"нету интерата шутка на {lang.get()}\n{joke_ofline}"
        except pyjokes.pyjokes.LanguageNotFoundError:
            ofline_languages = ["en","de","es","gl","eu","it"]
            text["height"] = 2
            text["text"] = f"Ошыбка офлайн язык не найден\n{ofline_languages}"
root = Tk()
root["bg"] = "white"
root.title("JokesOfIt by _sineD_0")

lang = StringVar()
lang.set("ru")

h1 = Label(text="JokesOfIt",bg="white",font="Bold").pack()
text = Label(text="Ваша шутка будет тут",bg="white",height=1)
choose_lang = OptionMenu(root,lang, "ru","uk","en","lt","de","pl","es","gl","eu","it").pack()
input_lang = Entry(textvariable=lang,bg="white").pack()
text.pack()
btn = Button(text="Сгенерировать шутку",command=generate_joke).pack()

root.mainloop()