#Provide a program for the calculator from terminal
''' In python there is eval() function to solve mathematical expression.
So here is my version to solve maths expression...
limitation : nested bracket does not support by this program'''


def parsestring(s):
    originalexp = s
    s = s.replace(' ','') # remove blank space
    s = s +';' # it works as end of string
    stack = []
    #to check if there is bracket or not
    
    for i in range(0,len(s)):
        bleft , bright = find_bracket(s)  
        if bleft == -1 or bright == -1:
            break
        temp = s[bleft+1:bright]+';' #get the temporary string which is inside the bracket
        if eval_string(temp,stack):  #take it as one string it returns false if there is alphabate in string
            s = s[:bleft]+str(stack[0])+s[bright+1:]  #join its result in original string eg. 2+(3+5) = 2+8
        else:
            return
        
        stack = []

    if eval_string(s,stack):
        print(f'{originalexp} = {stack[0]}')


def find_bracket(s):
    startpoint = 0
    p = s.find('(',startpoint,-1)
    if p != -1:
        q = s.find(')',p+1,-1)
        return p,q
    else:
        return p, -1
'''This function evaluate string and join digit
and make one number and append it to the stack
according to the priority rule it evaluates formula
'''
def eval_string(s,stack):
    result = 0
    temp = ''
    flag = True
    for i in range(0,len(s)):
        if s[i].isdigit() or s[i]=='.':
            temp = temp+s[i]
        elif s[i].isalpha():
            print("Invalid Expression")
            flag = False
            break
            
        else:
            if temp != "" :
                if temp.find('.') != -1:
                    t = float(temp)
                else:
                    t = int(temp)
                stack.append(t)
                temp = ""
            if i>4 and s[i-2]=='.' and s[i-4] == '*' or s[i-4] == '/' :
                eval_expression(stack)
                
            
            if i>2 and s[i-2] == '*' or s[i-2] == '/' or s[i] == ';':
                
                eval_expression(stack)
            if s[i] != ';':              
                stack.append(s[i])
    return flag
#it pop out digit and operator and perform maths operation
def eval_expression(stack):
    while len(stack)!=1:
        v1 = stack.pop()
        exp = stack.pop()
        v2 = stack.pop()
        if exp == '+':
            result = v1+v2
            stack.append(result)
        elif exp == '-':
            result = v2-v1
            stack.append(result)
        elif exp == '*':
            result = v1 * v2
            stack.append(result)
        elif exp == '/':
            result = v2/v1
            stack.append(result)
        else:
            print("invalid expression")

def main():
    s = input("Enter Your Expression :")
    parsestring(s)

if __name__ == '__main__':
    main()
