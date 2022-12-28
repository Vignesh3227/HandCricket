import random
def innings(choic,check):
    ball=1
    ball2=1
    global score1
    global score2
    if choic=='bat' and check==1:
        while True:
            bat=int(input('play a shot!: '))
            cpuball=random.randint(1,6)
            print('CPU bowled:',cpuball)
            if bat!=cpuball:
                score1= score1 +  bat
                print('score after ball',ball,':',score1)
            else:
                print('You are out! Your score is:',score1)
                print('Target:',score1+1)
                break
            ball+=1  
        while True:
            cpubat=random.randint(1,6)
            bowl=int(input('Get em out!: '))
            print('CPU scored:',cpubat)
            if bowl!=cpubat:
                score2=score2+cpubat
                print('score after ball',ball2,':',score2)
                ball2=ball2+1
                if score2>score1:
                    print('CPU wins!')
                    break
                else:
                    continue
            else:
                print('You got em OUT! score is:',score2)
                if score1==score2:
                    print('Match Tied!')
                else:    
                    print('You Win!!!!! CONGRATULATIONS!!')
                break  
    elif choic=='bowl' and check==1:
        while True:
            bowl=int(input('Get em out!: '))
            cpubat=random.randint(1,6)
            print('CPU scored:',cpubat)
            if bowl!=cpubat:
                score1= score1 +  cpubat
                print('score after ball',ball,':',score1)
            else:
                print('You got em out! score is:',score1)
                print('Target:',score1+1)
                break 
            ball+=1
        ball3=0   
        while True:
            bat=int(input('play a shot!: '))
            cpuball=random.randint(1,6)   
            if bat!=cpuball:
                score2=score2+bat
                print('score after ball',ball3,':',score2)
                ball3=ball3+1
                if score2>score1:
                    print('You win!')
                    break
                else:
                    continue
            else:
                print('You got OUT! score is:',score2)
                if score1==score2:
                    print('Match Tied!')
                else:          
                    print('CPU wins!')
                break                 
    elif choic=='bowl' and check==0:
        while True:
            bat=int(input('play a shot!: '))
            cpuball=random.randint(1,6)
            print('CPU bowled:',cpuball)
            if bat!=cpuball:
                score1= score1 +  bat
                print('score after ball',ball,':',score1)
            else:
                print('You are out! Your score is:',score1)
                print('Target:',score1+1)
                break
            ball+=1  
        while True:
            cpubat=random.randint(1,6)
            bowl=int(input('Get em out!: '))
            print('CPU scored:',cpubat)
            if bowl!=cpubat:
                score2=score2+cpubat
                print('score after ball',ball2,':',score2)
                ball2=ball2+1
                if score2>score1:
                    print('CPU wins!')
                    break
                else:
                    continue
            else:
                print('You got em OUT! score is:',score2)
                if score1==score2:
                    print('Match Tied!')
                else:    
                    print('You Win!!!!! CONGRATULATIONS!!')
                break  
    elif choic=='bat' and check==0:
        while True:
            bowl=int(input('Get em out!: '))
            cpubat=random.randint(1,6)
            print('CPU scored:',cpubat)
            if bowl!=cpubat:
                score1= score1 +  cpubat
                print('score after ball',ball,':',score1)
            else:
                print('You got em out! score is:',score1)
                print('Target:',score1+1)
                break 
            ball+=1
        ball3=0   
        while True:
            bat=int(input('play a shot!: '))
            cpuball=random.randint(1,6)   
            if bat!=cpuball:
                score2=score2+bat
                print('score after ball',ball3,':',score2)
                ball3=ball3+1
                if score2>score1:
                    print('You win!')
                    break
                else:
                    continue
            else:
                print('You got OUT! score is:',score2)
                if score1==score2:
                    print('Match Tied!')
                else:    
                    print('CPU wins!')
                break                
while True:
    print('Hand Cricket Championship!')
    print(' Odd or Even ')
    toss=input()
    print('You chose',toss)
    p1=int(input('Play your turn: '))
    p3=random.randint(1,6)
    print('CPU plays:',p3)
    sum=0
    sum=p1+p3
    check=0
    choic=''
    list1=['bat','bowl']
    score1=0
    score2=0
    if toss=='Odd':
        if sum%2==0:
            print('CPU won the toss!')
        else:
            print('You won the toss!')
            check=1
    elif toss=='Even':
        if sum%2==0:
            print('You won the toss!')
            check=1
        else:
            print('CPU won the toss!')
    if check==1:
        choic=input('Choose to bat or bowl?: ')
    else:
        choic=random.choice(list1)
        print('CPU chose to',choic)
    innings(choic,check)
    continuee=input('Rematch? yes or no: ')
    if continuee=='yes':
        continue
    else:
        print('Cool then Ciao!')
        break    
                                   
