from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv, dotenv_values 


def  webScraper():
    url = 'https://www.cinemark.com/movies/coming-soon'
    movie = "Instellar"
    movie2 = "Interstellar Early access"

    comingSoonPage = requests.get(url)
    soup = BeautifulSoup(comingSoonPage.text, "html.parser")

    quotes = soup.find_all('div', class_='title')
    for i in quotes:
        if i.contents[0] == f"{movie}" or i.contents[0] == f"{movie2}":
            return True
            print("Tickets are out fool get them asap!!!!!")


def sendEmail():
    dotenv_path = os.path.join(os.path.dirname(__file__), 'resources', '.env')
    load_dotenv(dotenv_path)
    key = os.getenv("CINEMA_PASSKEY")
    email = os.getenv("EMAIL")

    subject = "The Movie Lords has blessed you with goodnews"
    message = "Interstellar Tickets are now on sale so go get that done! Dont even bother asking your self what you know what dumbass! \n https://www.cinemark.com/theatres/tx-dallas/cinemark-dallas-xd-and-imax"

    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(email, key)
    server.sendmail(email, email, text)
    print("Email has been sent for this test")
