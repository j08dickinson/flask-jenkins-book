Feature: Check-in and out book
	Scenario: Store book in library
		Given Book "The Lord of the Rings" by "J.R.R. Tolkien" with ISBN number "0395974682"
		When I store the book in the library
		Then I am able to retreive the book by ISBN number
