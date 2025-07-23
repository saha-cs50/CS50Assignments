import matplotlib.pyplot as plt
import numpy as np


def validate(eqn):
    t = 0
    strlength = len(eqn)
    j = 0
    i = 0
    while j < strlength:
        if eqn[j] == '1' or eqn[j] == '2' or eqn[j] == "3" or eqn[j] == "4" or eqn[j] == "5" or eqn[j] == "6" or eqn[j] == "7" or eqn[j] == "8" or eqn[j] == "9"or eqn[j] == "0" or eqn[j] == "*" or eqn[j] == 'x' or eqn[j] == "+" or eqn[j] == "-" or eqn[j].isspace():
            i = i + 1
        else:
            print("INVALID SYMBOL", eqn[j])
            exit()
        j = j + 1

    k = 0
    l = 0
    while k < strlength:
        if eqn[k] == '+' or eqn[k] == '-':
            l = l + 1
        k = k + 1
    l = l + 1
    tempeqn = eqn.replace('-', '+')
    tempnospaceeqn = tempeqn.replace(" ", "")
    spliteqn = tempnospaceeqn.split("+")

    if tempnospaceeqn[0] == "+":
        print("Do not start the first term as a negative integer")
        exit()

    s = 0
    while s < len(spliteqn):
        
        termlen = len(spliteqn[s])
        b = 0
        while b < termlen:
            if spliteqn[s][b] == 'x' and b == 0:
                if termlen == b+1:
                    t = t + 1
                elif termlen > b:
                    if spliteqn[s][b] == 'x' and spliteqn[s][b+1] == '*' and spliteqn[s][b+2] == '*' and spliteqn[s][b+3].isnumeric and spliteqn[s][b+3] != 'x':
                        t = t + 1
                    else:
                        print("invalid term", spliteqn[s])
                        exit()
                
            elif spliteqn[s][b] == 'x' and spliteqn[s][b-1] == '*' and spliteqn[s][b-2].isnumeric and spliteqn[s][b-2] != '*':
                if termlen == b+1:
                    t =t + 1
                elif termlen > b:
                    if spliteqn[s][b] == 'x' and spliteqn[s][b+1] == '*' and spliteqn[s][b+2] == '*' and spliteqn[s][b+3].isnumeric:
                        t = t + 1
                    else:
                        print("invalid term", spliteqn[s])
                        exit()
            elif 'x' not in spliteqn[s] and '*' in spliteqn[s]:
                print("invalid term", spliteqn[s])
                exit()
                    
            elif spliteqn[s][b] == 'x':
                print("invalid term",spliteqn[s])
                exit()


            b = b + 1
        s = s + 1


def evaluate(equation, xval):
    x = xval
    nospaceeqn = equation.replace(" ", "")
    tempeqn = equation.replace('-', '+')
    tempnospaceeqn = tempeqn.replace(" ", "")
    spliteqn = tempnospaceeqn.split("+")
    
    s = 0
    b = 0
    p = 0
    ans1 = 1
    ans2 = 1
    ans3 = 1
    l = 0
    m = 0
    q = 0
    signs = []
    test = 0
    termlist = []
    finalans = 0

    while p < len(nospaceeqn):
        if nospaceeqn[p] == '+' or nospaceeqn[p] == '-':
            signs.append(nospaceeqn[p])
        else:
            q = q + 1
        p = p + 1
    
    while s < len(spliteqn):
        termlen = len(spliteqn[s])
        b = 0
        ans1 = 1
        ans2 = 1 
        ans3 = 1
        while b < termlen:
            if spliteqn[s][b] == 'x' and b == 0 and termlen == 1:
                ans1 = x
                #print(ans)
            elif spliteqn[s][b] == 'x' and b > 0:                
                mulnum = spliteqn[s].split("*")
                mnum = int(mulnum[0]) 
                if '**' in spliteqn[s]:
                    ans2 = mnum 
                else:
                    ans2 = mnum * x

            elif spliteqn[s][b] == '*' and spliteqn[s][b+1] == '*' and termlen > 1:
                expnum = spliteqn[s].split("**")
                enum = int(expnum[1])
                ans3 = x ** enum
            elif 'x' not in spliteqn[s]:
                ans1 = 1
                ans2 = 1
                ans3 = int(spliteqn[s])
 
            b = b + 1 
        ans = ans1 * ans2 * ans3
        termlist.append(ans)
        s = s + 1
        
    finalans = termlist[0]
    while l < len(termlist):
        if len(signs) ==  0:
            finalans = termlist[0]
        elif m == len(signs):
            break  
        elif signs[m] == '+':
            finalans = finalans + termlist[l+1] 
            m = m + 1
        elif signs[m] == '-':
            finalans = finalans - termlist[l+1]
            m = m + 1
        l = l + 1
     

    return finalans
    


print("ENTER THE VALUE OF Y IN TERMS OF X")
#rules
print("The equation cannot contain any variables other than x\nIt does not accept fractional or decimal values")
print("It does not handle division\nFirst term cannot be negative")
print("Terms that do not contain x should be in simplest form (not using exponents or multiplication); eg: 2*3 or 2**5 are not valid")
print("x cannot be a power; eg: 2 to the power x is not valid")
print("To multiply * sign must be used and number must be before x; eg: 2 * x")
print("For powers ** sign is used after the x; eg: x ** 2")

eq = input("y = ")
x = np.linspace(-100, 100, 200)

validate(eq)
y = evaluate(eq,x)

 
plt.plot(x,y)
plt.show()
exit()







