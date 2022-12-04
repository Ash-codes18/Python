import os
os.system("pip install colorama")
os.system("cls")
import colorama,os
from colorama import Fore,Style,Back

########################       CACLUCULATION      ##########################################3

def mul(val,unit):
    out=val*unit
    print(Fore.GREEN)
    print("    >>>>",Style.RESET_ALL,val,Fore.BLUE + l2[a-1],Style.RESET_ALL,"=","%.4f"%out,Fore.BLUE + l2[b-1],Style.RESET_ALL)
    return

############################    LISTS   ########################################################

l1=["1) INR-Indian Rupee","2) USD-US dollar", "3) CAD-Canadian dollar","4) CNY-Chinese yuan","5) RUB-Russia’s Rubal","6) EUR-Euro"]
l2=["INR","USD", "CAD","CNY","RUB","EUR"]

#############################    LOOP     ##############################################################

while True:
    print('''                   ____                          _            
                  / ___|___  _ ____   _____ _ __| |_ ___ _ __ 
                 | |   / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
                 | |__| (_) | | | \ V /  __/ |  | ||  __/ |   
                  \____\___/|_| |_|\_/ \___|_|   \__\___|_|   
                                                                  ''')
    print("The avilable options are:")
    print()
    for i in l1:
        print("     ",i)
    print()
    

############################  WRONG INPUT FOR "FROM__"   ##############################

    print(Fore.GREEN)
    a=int(input("From __ (choose above options): "))

    if a<=len(l1):
        a=int(a)
    else:
        print("     >>>>>",Fore.RED + "Enter vaild input",Style.RESET_ALL)
        print("                 Press",Fore.CYAN + '\033[1m' + 'ENTER' + '\033[0m',Style.RESET_ALL, "For Next Conversion")
        al=input()
        os.system("clear")
        continue
    
    print("    >>>>",Fore.BLUE + l2[a-1]+" is selected")
    print(Style.RESET_ALL)
    c=(l2[a-1])
    
############################  WRONG INPUT FOR "TO__"   ##############################

    print(Fore.GREEN)
    b=int(input("{} To __ (choose above options): ".format(c)))

    if b<=len(l1):
        b=b
    else:
        print("     >>>>>",Fore.RED + "Enter vaild input",Style.RESET_ALL)
        print("                 Press",Fore.CYAN + '\033[1m' + 'ENTER' + '\033[0m',Style.RESET_ALL, "For Next Conversion")
        al=input()
        os.system("clear")
        continue

    print("     >>>>",Fore.BLUE + l2[b-1]+" is selected")
    print()
    print(Fore.GREEN)
    c=(l2[a-1],l2[b-1])
    val=eval(input("Value for conversion %s to %s: "%c))
    print(Style.RESET_ALL)

   
    if a==b:
        mul(val,1)
############################   INR TO OTHERS   ########################################################       

    elif a==1 and b==2:
        mul(val,0.012114432)
    elif a==2 and b==1:
        mul(val,82.524641)
    
    elif a==1 and b==3:
        mul(val,0.16543757)
    elif a==3 and b==1:
        mul(val,60.436276)

    elif a==1 and b==4:
        mul(val,0.87739056)
    elif a==4 and b==1:
        mul(val,11.394784)

    elif a==1 and b==5:
        mul(val,0.74818389)
    elif a==5 and b==1:
        mul(val,1.3381059)

    elif a==1 and b==6:
        mul(val,0.012290295)
    elif a==6 and b==1:
        mul(val,81.345962)

################################  USD TO OTHER   ###################################################################
    
    elif a==2 and b==3:
        mul(val,1.3665878)
    elif a==3 and b==2:
        mul(val,0.73171013)

    elif a==2 and b==4:
        mul(val,7.2434067)
    elif a==4 and b==2:
        mul(val,0.13805389)

    elif a==2 and b==5:
        mul(val,61.833713)
    elif a==5 and b==2:
        mul(val,0.016144115)
    
    elif a==2 and b==6:
        mul(val,1.0146885)
    elif a==6 and b==2:
        mul(val,0.98540154)

##################################   CAD TO OTHER  ################################################################

    elif a==3 and b==4:
        mul(val,5.3043698)
    elif a==4 and b==3:
        mul(val,0.18862945)

    elif a==3 and b==5:
        mul(val,45.194092)
    elif a==5 and b==3:
        mul(val,0.2214124)

    elif a==3 and b==6:
        mul(val,0.7430328)
    elif a==6 and b==3:
        mul(val,1.3457804)

################################### CNY TO OTHERS#######################################################

    elif a==4 and b==5:
        mul(val,8.5226981)
    elif a==5 and b==4:
        mul(val,0.11741431)
    
    elif a==4 and b==6:
        mul(val,0.14008219)
    elif a==6 and b==4:
        mul(val,7.1391185)
    
##################################   RUB TO OTHERS ##############################################################

    elif a==5 and b==6:
        mul(val,0.016447669)
    elif a==6 and b==5:
        mul(val,60.925618)
    print()
    print()
    print("                 Press",Fore.CYAN + '\033[1m' + 'ENTER' + '\033[0m',Style.RESET_ALL, "For Next Conversion")
    al=input()
    os.system("cls")
