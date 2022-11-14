# Print out the last name of the second employee.
d = {"employees": [{"firstName": "John", "LastName": "Doe"},
                   {"firstName": "Anna", "LastName": "Smith"},
                   {"firstName": "Peter", "LastName": "Jones"}],
     "owners": [{"firstName": "Jack", "LastName": "Petter"},
                {"firstName": "Jessy", "LastName": "Petter"}]}
print(d['employees'][1]['LastName'])