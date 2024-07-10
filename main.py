
import StarSearch
import logger
#Just the driver code

def main():
	#Checking to see if interstellar is in theaters
	#sotre the result for the logger

	statusOfMovie = StarSearch.webScraper()
	if statusOfMovie == True:
		StarSearch.sendEmail() 
		statusOfMovie = True
		logger.logIt(statusOfMovie)
	else:
		statusOfMovie = False
		logger.logIt(statusOfMovie)
		



if __name__ == "__main__":
    main()

