class Patterns:
    
    """
    def isPhoneNumber(text):
        if len(text) != 12:
            return False
        for i in range(0, 3):
            if not text[i].isdecimal():
                return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
        if text[7] != '-':
                return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True

    print('Is 415-555-4242 a phone number?')
    print(isPhoneNumber('415-555-4242'))
    print('Is Moshi moshi a phone number?')
    print(isPhoneNumber('Moshi moshi'))
    
    
    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print('Phone number found: ' + chunk)
    print('Done')
    """
    
    
    import re
    
    # re.compile() is for compiling the regular expression
    # \d means "a digit character"
    # phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    # mo = phoneNumRegex.search('My number is 415-555-4242.')
    # print('Phone number found: ' + mo.group())
    
    # Import the regex module with import re.
    # Create a Regex object with the re.compile() function. (Remember to use a raw string.)
    # Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
    # Call the Match object’s group() method to return a string of the actual matched text.
    
    #group will group by the parantheses
    phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    mo = phoneNumRegex.search('My number is 415-555-4242.')
    mo.group(1)
    # print(mo.group(1))
    mo.group(2)
    # print(mo.group(2))
    mo.group(0)
    # print(mo.group(0))
    mo.group()
    # print(mo.group())
    
    #NOTE: group() and group(0) are the same
    
    #If you would like to retrieve all the groups at once, 
    #use the groups() method—note the plural form for the name.
    
    mo.groups()
    # print(mo.groups())
    
    #multiple assignment trick, i.e. areaCode is group(1)
    #and mainNumber is group(2)
    areaCode, mainNumber = mo.groups() 
    print(areaCode)
    print(mainNumber)
    
    
    phoneNumRegex2 = re.compile(r'(\d{3})-(\d{3}-\d{4})-(\d{5})-(\d{6})-(\d{7})')
    mo2 = phoneNumRegex2.search('My number is 415-555-4242-12345-987600-1111123.')
    mo2.group(1)
    print(mo2.group(1))
    mo2.group(2)
    print(mo2.group(2))
    mo2.group(3)
    print(mo2.group(3))
    mo2.group(4)
    print(mo2.group(4))
    mo2.group(5)
    print(mo2.group(5))
    

    
    