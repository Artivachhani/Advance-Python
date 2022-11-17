'''It print * prints leftjust **** right just **** left just top *  right just    *
                              ***              ***               **              **
                              **                **               ***            ***
                              *                  *               ****          ****'''




def leftjust(n):
    for i in range(n,0,-1):
        s = ''
        for j in range(i,0,-1):
            s= s+'*'
        fill = ' '    
        print(s.ljust(n,fill),end = '')
        print('\r')

def rightjust(n):
    for i in range(n,0,-1):
        s = ''
        for j in range(i,0,-1):
            s= s+'*'
        fill = ' '    
        print(s.rjust(n,fill),end = '')
        print('\r')

def leftjust1(n):
    for i in range(0,n):
        s = ''
        for j in range(0,i+1):
            s= s+'*'
        fill = ' '    
        print(s.ljust(n,fill),end = '')
        print('\r')

def rightjust1(n):
    for i in range(0,n):
        s = ''
        for j in range(0,i+1):
            s= s+'*'
        fill = ' '    
        print(s.rjust(n,fill),end = '')
        print('\r')       


def parda(n):
    for i in range(n,0,-1):
        s = ''
        for j in range(i,0,-1):
            s= s+'*'
        fill = ' '    
        print(s.ljust(n,fill),end = '')
        print(s.rjust(n,fill))


def reverseparda(n):
    for i in range(0,n):
        s = ''
        for j in range(0,i+1):
            s= s+'*'
        fill = ' '    
        print(s.ljust(n,fill),end = '')
        print(s.rjust(n,fill))
        

   
def diamond(n):
    for i in range(n,0,-1):
        s = ''
        for j in range(i,0,-1):
            s= s+'*'
        fill = ' '    
        print(s.ljust(n,fill),end = '')
        print(s.rjust(n,fill))

    for i in range(1,n):
        s = ''
        for j in range(0,i+1):
            s= s+'*'
        fill = ' '    
        print(s.ljust(n,fill),end = '')
        print(s.rjust(n,fill))

def pyramid(n):
    fill = ' '
    s = ' *'
    print(s.center((n*2),fill))
    for i in range(0,n):
        s = ''
        for j in range(0,i+1):
            s= s+'*'
            
        print(s.rjust(n,fill),end = '')
        print(s.ljust(n,fill))


def main():
    n = input("Enter number of star: ")
    if n.isdigit():
        n = int(n)
    else:
        print("Enter Proper number")

    print("Left justify triangle :")
    leftjust(n)
    print("\nRight justify triangle :")
    rightjust(n)
    print("\nLeft justify triangle (Top to Bottom) :")
    leftjust1(n)
    print("\nRight justify triangle (Top to Bottom) :")
    rightjust1(n)
    print("\nPyramid : ")
    pyramid(n)
    print("\nDiamond :")
    diamond (n)
    print("\nFountain :")
    reverseparda(n)
    print("\n")
    parda(n)

if __name__ == '__main__':
    main()
