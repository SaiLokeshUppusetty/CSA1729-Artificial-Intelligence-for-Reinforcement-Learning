takes(murali_krishna, csa123).
takes(mahesh_babu, uba027).
takes(murali_krishna, dsa456).
takes(rohit_sharma, his264).

classmates(X, Y):- takes(X, Z), takes(Y, Z).
