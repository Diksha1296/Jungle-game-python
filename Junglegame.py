def Happy():
    per=int(input("Do you want to play:??\n Press 1 for continue and 2 for exit:"))
    if(per==1):
        return happy()
    else:
        print(" BYE BYE!!!!\n--VISITING AGAIN")
        
    


def happy():
    a=int(input("Press 1 for  moving Left side in the Jungle \nPress 2 for  moving Right side in the Jungle:"))
    if(a==1):
        print("YOU ARE ON LEFTSIDE OF JUNGLE....\n....Again two ways.....")
        b=int(input("Choose again 1 for Right and 2 for Left:"))
        if(b==1):
            print("OHHH---CROCODILES IN RIVERS-----"
                  "!!GAME OVER !!")
            return Happy()
            
        else:
            c=int(input("Want to take Stranger help??\n Enter 1 for Help \nEnter 2 for 'No Help':"))
            if(c==1):
                print("!!WINNER-WINNER!!")
                return Happy()
            else:
                print("OOPS! You Miss the Help :<")
                print("!!!Game Over!!!")
                return Happy()

    else:
        print("---You are on Rightside of the Jungle---\n You are stuck in the middle of the jungle..." 
              "\nNow be ready to face the challenges!!")
        r1=int(input("press 1 for left and 2 for Right:"))
        if(r1==1):
            print("-----OPPS!!!you are dig into the Pathole----\n"
                  "--!!Game Over!!")
            return  Happy()
        else:
         print("Ohh!!,Lion Catches you'Bye Bye!!!"
               "--\n --!!!!!Game Over!!!!!") 
         return Happy()



print("#######---Welcome to the JUNGLE GAME----#######")
happy()