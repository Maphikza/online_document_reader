import pyttsx3

text_path = 'C:/Users/stapi/Desktop/100_days_of_Code/My_text.txt'

with open(text_path, encoding="utf-8") as blog:
    text = blog.readlines()
read_text = "".join(text)


def play_article_text(input_text):
    engine = pyttsx3.init()

    engine.setProperty("rate", 195)

    voices = engine.getProperty("voices")

    engine.setProperty("voice", voices[1].id)

    engine.say(input_text)

    engine.runAndWait()


if __name__ == "__main__":
    play_article_text(read_text)
