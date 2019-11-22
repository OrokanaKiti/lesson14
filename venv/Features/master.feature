#Author- Sammie E
#
#This is a gerkin Homework Asignment for L13  O w O ~
#
## platform- "Gerkin"
#
#
#Feature: "TITLE OF SCENARIO"
Feature: "Display year and month for obtaing full ssa benefits

	#outlinethingy for good equivolence classes
	Scenario Outline: ask user for <num1> & <num2>
		Given  calculator starts up
		When	user enters <num1> & <num2>
		Then	returns year <result> + month <result2> for obtaining full benefits

	Examples:
		| num1 		| num2  | result1					|	result2 					|
		|	1937	|	12	|	65	+ <num1>/12			|	<num1> + <result1>			|
		|	1938	|	1	|	65	+ <num1>/12			|	<num1> + <result1>			|
		|	1939	|	5	|	65 + 2/12	+ <num1>/12	|	<num1> + <result1>			|
		|	1940	|	5	|	65 + 4/12	+ <num1>/12	|	<num1> + <result1>			|
		|	1941	|	5	|	65 + 6/12	+ <num1>/12	|	<num1> + <result1>			|
		|	1942	|	12	|	65 + 8/12	+ <num1>/12	|	<num1> + <result1>			|
		|	1943	|	1	|	65		+ <num1>/12		|	<num1> + <result1>			|
		|	1954	|	12	|	66		+ <num1>/12		|	<num1> + <result1>			|
		|	1955	|	1	|	66 + 2/12 + <num1>/12	|	<num1> + <result1>			|
		|	1956	|	5	|	66 + 4/12+ <num1>/12	|	<num1> + <result1>			|
		|	1957	|	5	|	66 + 6/12	+ <num1>/12	|	<num1> + <result1>			|
		|	1958	|	5	|	66 + 8/12	+ <num1>/12	|	<num1> + <result1>			|
		|	1959	|	12	|	66 + 10/12+ <num1>/12	|	<num1> + <result1>			|
		|	1960	|	1	|	67		+ <num1>/12		|	<num1> + <result1>			|
#		|		|	1	|		|
#		|		|	1	|		|

	#the 13th input
	Scenario: "the extra month"
		Given	calculator starts up
		When	user enters "13" into the month option and a year
		Then	the program should at +1 to the year, then restart the month at 1

	#bad input
	Scenario: "bad input"
		Given	calculator starts up
		When	user enters something that is not a number
		Then	program should throw "Input not accepted" and offer to restart execution

	#tomuch
	Scenario: "to many numbers"
		Given	calculator starts up
		When	user enters something that is more characters than expected
		Then	program should throw "incorrect input" and offer to restart execution

	#tolittle
	Scenario: "to little numbers"
		Given	calculator starts up
		When	user enters something that is less characters than expected
		Then	program should throw "incorrect input" and offer to restart execution

	#nothing
	Scenario: "nothing entere"
		Given	calculator starts up
		When	user hits enter without inputing anything
		Then	program should throw "no input detected" and offer to restart execution

	#denialofservice
	Scenario: "deny the oldies"
		Given	calculator starts up
		When	user enters something that is before "1900" for the date born
		Then	program should throw "sorry too old" and offer to restart execution

	#denialofservice
	Scenario: "deny the oldies"
		Given	calculator starts up
		When	user enters something that is after "2019" for the date born
		Then	program should throw "Impossible for them to exsist" and offer to restart execution


