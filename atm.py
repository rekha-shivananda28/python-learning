balance=50000
correct_pin="8227"
print("====ATM MACHINE====")
pin=input("Enter your PIN:")
if pin ==correct_pin:
    while True:
        print("\n =====MENU====")
        print("1.Check balance")
        print("2.Deposite money")
        print("3.Withdraw money")
        print("4.Exit")
        choice=input("Enter your choice:")
        if choice=="1":
               print("Your balance is:",balance)
        elif choice=="2":
             amount=float(input("Enter deposite amount:"))
             if amount>0:
                  balance+=amount
                  print("Amount deposite successfully.")
                  print("New balance:",balance)
             else:
                  print("Invalid amount.")
        elif choice=="3":
             amount=float(input("Enter withdrawal amount:"))
             if amount<=0:
                  print("Invalid amount.")
             elif amount>balance:
                  print("Insufficient balance:",balance)
             else:
                  balance-=amount
                  print("please collect your cash.")
                  print("Remaining balance:",balance)
        elif choice=="4":
             print("Thank you for using the ATM.")
             break
        else:
             print("Invalid choice.please try again.")
    else:
         print("Incorrect PIN.")
         print("Access denied.")

             
                

            
             