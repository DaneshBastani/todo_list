#The Project is to create a simple TO-DO List to store items and delete when required
# To add element to a list
l=[]
def User_Input():
    user = input('Enter the items t be added to the To-Do List\n')
    l.append(user)
    print(l)

    #Add Extra Element
    Add=input('Do You Want To add other Items\n')
    if Add=='yes':
        User_Input()
    elif Add=='no':
        print(l)


def remover():
        Remove =input('Enter the Item you want to remove or press Exit to End\n')
        
     #To Remove a Specific ELement from List
        if Remove in l:
                l.remove(Remove)
                print(l)
                remover()  
        elif Remove not in l and Remove!= 'exit':
            print('Check_Again')
            remover()                   
        elif Remove =='exit':
            exit()


User_Input()
remover()