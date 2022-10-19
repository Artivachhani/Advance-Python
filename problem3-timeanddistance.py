# Provide a program to calculate the time and distance based on below problem
from colorama import Fore, Back
''' Total length of rod = 100mtr

    left cockroach = c1
    right cockroach = c2

    speed = distance/time
    time = distance/speed

    c1 moves 1 meter/sec forward.  but every 10 sec. it moves 2 meters backward
    speed of c1 = 8/10 = 0.8 meter/sec.
    Total time to complete the 100 meter rod,

    T1 = 100/0.8 = 125sec. 

    c2 moves 2 meter /sec forward. but every 5 sec. it moves 1 meter backward
    speed of c2 = 9/5 meter/sec.
    Total time to complete the 100 meter rod,

    T2 = 100/(9/5) = 55.56sec.

    Relative speed = speed of c1 + speed of c2
    Time to meet = Distance(length of rod) / Relative Speed
    '''

def speed_calculate():
    length_rod = 100
    speed_c1 = 0.8
    speed_c2 = float(9/5)

    relative_speed = speed_c1 + speed_c2

    t1 = __Total_time(length_rod,speed_c1)
    t2 = __Total_time(length_rod,speed_c2)
    meeting_time = __Total_time(length_rod,relative_speed)
    distance_coverby_c1 = speed_c1 * meeting_time
    distance_coverby_c2 = speed_c2 * meeting_time
    
    #print(f'Both Cockroaches meet at {meeting_time} sec.')
    #print(f'The Left Cockroach cover {distance_coverby_c1} meter to meet The Right cockroach,')
    #print(f'The Right Cockroach cover {distance_coverby_c2} meter to meet The Left cockroach,')
    #print(f'The Left Cockroach cover {length_rod} in {t1} sec.')
    #print(f'The Right Cockroach cover {length_rod} in {t2} sec.')

    print(' =======================================================')
    print(' X ----->                                               ')
    
    print('                                                       X')
    print(' =======================================================')
    print(f'                               {length_rod} Meters in {"{:.2f}".format(t1)} Sec.')
    
    print('\n\n')
    print(' =======================================================')
    
    
    print('                                                <----- Y')
    print(' Y                                                      ')
    print(' =======================================================')
    print(f' {length_rod} Meters in {"{:.2f}".format(t2)} Sec.')

    print('\n\n')
    print(' =======================================================')
      
    print(' X----->                                        <----- Y')
    print(f' ------{"{:.2f}".format(distance_coverby_c1)} m---> X                                 ')
    print(f'                   Y <---{"{:.2f}".format(distance_coverby_c2)} m------------------------')
    print(' =======================================================')
    print(f'        Meet at {"{:.2f}".format(meeting_time)} Sec.')
    
    

    
    







def __Total_time(length_rod,speed_c):
    return float(length_rod/speed_c)


def main():
    speed_calculate()

if __name__=="__main__":
    main()
