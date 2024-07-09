import checkAndEmail
import logger
#Just the driver code

def main():
    #Checking to see if interstellar is in theaters
    #sotre the result for the logger
    statusOfMovie = checkAndEmail.webScraper()
    if statusOfMovie == True:
        checkAndEmail.sendEmail()
    logger.logIt(statusOfMovie)  


    

if __name__ == "__main__":
    main()


