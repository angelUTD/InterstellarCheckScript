import checkAndEmail
import logger


def main():
    #Checking to see if interstellar is in theaters
    statusOfMovie = checkAndEmail.webScraper()
    if statusOfMovie == True:
        checkAndEmail.sendEmail()
    logger.logIt(statusOfMovie)  


    

if __name__ == "__main__":
    main()


