#Poojith

def menu():
    ro=input("Please enter the first input: ")
    ma=input("Please enter the second input: ")
    rotoin(ro,ma)

def rotoin(ro,ma):
    nnu=['I','V','X','L','C','M','i','v','x','l']
    me=[1,5,10,100,1000,1,5,10,100,1000]
    total=1
    total1=1
    sum= total + total1

    for n in ro:
        if (n in nnu):
            print("converting to integer and adding: ")
            ind=(nnu)
            n=me(ind)

            if n== total:
                total=total+n

            elif (n>total):
                total=total+n

            elif (n<total):
                total=total-n
        
        else:
            print("Wrong input, try again")
            menu()

    for m in ma:
        if (m in nnu):
            ind=nnu(m)
            m= ind(me)

            if (m== total):
                total=total+n

            elif (m>total):
                total=total+n

            elif (m<total):
                total=total-n
        
        else:
            print("Wrong input, try again")
            menu()


    print(total)
    print(total1)
    print(sum)
    print(int(ro)+int(ma))



menu()

