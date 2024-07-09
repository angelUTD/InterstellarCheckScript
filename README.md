### InterstellarCheckScript
## Description:
This is a script that scrapes the Cinemark website to check and see if Interstellar tickets are available for advance or early tickets. If the tickets are on sale then I will be sent an email with the link,
all to ensure I do not miss these tickets. will have this set-up to run every 15 minutes to make sure I do not miss these tickets!
It will take adavantage of Beautiful Soup, smtplib, os,and requests libraries.

![alt text](https://github.com/angelUTD/InterstellarCheckScript/blob/main/EmailScreenShot.png?raw=true)

## "main.py"
Its the driver code mostly here to call the need functions.

## "checkAndEmail.py" 
# "webScraper()"
This file does all the heavy lifting, it will be in charge of checking the Cinemark website to see if the movie "Interstellar" tickets are available for early access purchase. This is done by using Beautiful soup library inorder to parse through all movie titles in the coming soon tab of cinemark. Also taking advantage of the requst library in order to create a snapchat of the website. Link to cinemark page im referring to: https://www.cinemark.com/movies/events and https://www.cinemark.com/movies/coming-soon.

# "logger.py"
This file is here to create a log to keep an eye on how the script is running or if its running at all.
It will store the current time and a message of its results of whether or not the tickets were found.
