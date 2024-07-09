### InterstellarCheckScript
##Description:
#This is a script that scrapes the Cinemark website to check and see if Interstellar tickets are available for advance or early tickets. If the tickets are on sale then I will be sent an email with the link,
all to ensure I do not miss these tickets. will have this set-up to run every 15 minutes to make sure I do not miss these tickets!
It will take adavantage of Beautiful Soup, smtplib, os,and requests libraries.

## "main.py"
Its the driver code mostly here to call the need functions.

## "checkAndEmail.py" 
#This file does all the heavy lifting, it will be in charge of checking the Cinemark website to see if the movie "Interstellar" tickets are available for early access purchase. It is also in charge of creating a connection to the users gmail account for the purpose of sending myself an email to inform me that tickets are on sale. The email will also contain the link to purchase these tickets.

