import re
line1 = '(75, 180)'
lines = '''(75, 182)
(+90.0, -147.45)
(77.11112223331, 149.99999999)
(+90, +180)
(90, 180)
(-90.00000, -180.0000)
(75, 280)
(+190.0, -147.45)
(77.11112223331, 249.99999999)
(+90, +180.2)
(90., 180.)
(-090.00000, -180.0000)'''

text = '''
t: 
string (X, V) is considered valid if the following criteria are me 
The string starts with a (, has a comma after X and ends with a 
here is no space between the opening parenthesis and the first chara 
here is no space between the comma and the last character of X. 
here is one space between the comma and the first character of 
here is no space between V and the closing parenthesis. 
X and Y are decimal numbers and may be preceded by a Siq 

there are no leading zeros. 
No other characters are allowed In or 

coordinates     results  Reasoning
(90, 180)       Valid
(+90, +180)     Valid
 (90, 180)      Invalid  Preceding space
(90.0, 180.1)   Invalid  Y is out of bounds
(85S, 95W)      Invalid  Extraneous characters

'''

#myre = re.compile('(\+?-?\d*\.?\d*), (\+?-?\d*\.?\d*)')

#p = re.compile('([+-]*\d*[\.]*\d*), ([+-]*\d*[\.]*\d*)')
#t = int(input())
myre = re.compile('(\+?-?\d*\.?\d*), (\+?-?\d*\.?\d*)')

for inputline in lines.split('\n'):
    try:
        re_check = re.findall(myre, inputline)
        re_str = re_check[0]
        x = re_str[0]
        y = re_str[1]
        if(x[0] == '+' or x[0] == '-'):
            x = x[1:]
        if(y[0] == '+' or y[0] == '-'):
            y = y[1:]
        if(x[len(x)-1] == '.' or y[len(y)-1] == '.'):
            print("Invalid")
            continue
        if((len(x) > 1 and x[0] == '0' and x[1] != '.') or (len(y) > 1 and y[0] == '0' and y[1] != '.')):
            print("Invalid")
            continue
        x = float(x)
        y = float(y)
        if(x >= -90.0 and x <= 90.0 and y >= -180.0 and y <= 180.0):
            print("Valid")
        else:
            print("Invalid")
    except:
        print("Invalid")
