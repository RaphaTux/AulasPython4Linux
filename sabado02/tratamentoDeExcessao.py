#!/usr/bin/python3.5

while True:

    try:
        n1 = int( input( '1º num ' ))
        n2 = int( input( '2º num ' ))
    except ValueError as v :
        print(v)
        break

    try:
        r = n1/n2
    except ZeroDivisionError as e:
        print(e)
    else:
        print(r)
    finally:
        print( 'fim ' )

#exit()
#try:
#    print(5/0)
#except ZeroDivisionError as e 
#    print(e)