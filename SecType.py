#!/usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:
	##Redo this to include optional arguments (kwargs) for startdate, enddate, cik(list), ticker, formslist
	python3 SecType.py **variables list
"""

def main():
	"""Retrieve a list of all available documents from the SEC website for given parameters.

	Args:
		start_date: The first date for which you want documents found

		end_date (optional): The last date for which you want documents found
			The default value for this value is the date on which the 
			application is executed
		
		ticker (optional): The ticker symbol for the company,
			this is only valid for publicly traded companies and 
			this variable can refer to a list of tickers
		
		cik (optional): This is the company's central index key,
			 a unique identifier that most accurately identifies a company
			 in the SEC database. 
			 This variable can also refer to a list of ciks
		
		forms (optional): This is the form type that should be retrieved
			it can also refer to a list of forms. 
			The default value is to retrieve all forms
	
	Raises:
		Invalid_Date: If the start_date entered is invalid this will raise
			an Invalid_Date error. This can occur if the date entered is
			in the future or has had no trading days since it occured

		No_Company_Error: If the user does not enter either a valid cik or a
			valid company ticker this error will be raised. This prevents the 
			application from trying to download data for all companies

		Invalid_CIK: If the central index key(s) entered are invalid, this
			error will be raised and the program will be terminated

		Invalid_Ticker: If the ticker(s) entered by the user are invalid, this
			error will be raised and the program will be terminated
	
	Returns:
		##A tuple of company_identifier, date, form-type, and exhibit count
		for that form and the first exhibit's download link 
		(more download links on request).
		for all the instances found within the database
	"""

	
	start = '1/23/2017'
	code = 1009976
	##Test the below ticker to see versatility of the application
	#ticker = 'UAL'
	result_object = EdgarSearch(start, code)

	for form in result_object:
		print(form)


if __name__ == "__main__":
	main()