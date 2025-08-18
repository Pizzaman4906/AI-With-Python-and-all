from textblob import TextBlob
import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()
print(f"{Fore.MAGENTA}Welcome to AI Sentiment / Mood detector!")
name = input(f"{Fore.YELLOW}What is your name? \n")
print(f"{Fore.YELLOW}Nice to meet to you, {name}! \n Lets find out the sentiment of your sentences")
print(f"{Fore.BLUE}Type 'exit' to quit. \n ")

while True:
    sentence = input("Your sentence: ")
    if sentence.lower() == "exit":
        print(f"{Fore.YELLOW}Goodbye!, {name}!")
        break
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        print(f"{Fore.GREEN}Positive statement detected! :D ")
    elif sentiment < 0:
        print(f"{Fore.RED}Negative statement detected! :( ")
    else:
        print(f"{Fore.BLUE}Neutral statement detected! :| ")
        