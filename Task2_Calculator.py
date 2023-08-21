
class Operations:
         def __init__(self) :
                 self.operation_count =0

         def increment_operation_count(self):
                 self.operation_count +=1
                 return self.operation_count

         def Addition(self ,a,b):
                 return(a+b)

         def Multiplication(self,a,b):
                  return(a*b)

         def Subtraction(self,a,b):
                  return(a-b)

         def  Division(self,a,b):
                 if b!=0:
                         return(a/b)
                 else: 
                         return "Undefined!!!"
    
         def Modulus(self,a,b):
                if b!=0:
                         return(a%b)
                else: 
                         return "Undefined!!!"

         def Exponential(self,a,b):
                return (a**b)


def main():
      print("<<<<<|---CALCULATOR---|>>>>>\n")
      print("------|...OPERATIONS...|-----")
      print("1 : ADDITION(+)")
      print("2 : MULTIPLICATION(*)")
      print("3 : SUBTRACTION(-)")
      print("4 : DIVISION(/)")
      print("5 : MODULUS(%)")
      print("6 : EXPONENTIAL(**)\n")
       
      oper = Operations()
      while True:
                  choice=input("Which Operation do you want to perform..? ")
                  if choice in('1' ,'2' ,'3' ,'4' ,'5' ,'6'):
                          x=int(input("Enter the first number :"))
                          y=int(input("Enter the second number :"))

                          if choice == '1':
                                  print(f"<-----ADDITION IS----->: {oper.Addition(x,y)}\n")
 
                          elif choice == '2':
                                  print(f"<-----MULTIPLICATION IS-----> : {oper.Multiplication(x,y)}\n")

                          elif choice == '3':
                                 print(f"<-----SUBTRACTION IS-----> : {oper.Subtraction(x,y)}\n")

                          elif choice == '4':
                                 print(f"<-----DIVISION IS-----> : {oper.Division(x,y)}\n")

                          elif choice == '5':
                                 print(f"<-----MODULUS IS-----> : {oper.Modulus(x,y)}\n")

                          elif choice == '6':
                                 print(f"<-----{x} power {y} is-----> : {oper.Exponential(x,y)}\n")   
                  else :
                             print("INVALID CHOICE!!!!\n")
                             continue
                  
                  #Total Operations Performed Count  
                  total_count=oper.increment_operation_count()
 
                  status = input("Do you want to perform another operation? Y/N: ")
                  while status.lower() not in ('y', 'n'):
                          print("Invalid Choice. Please choose Y/N....\n")
                          status = input("Do you want to perform another operation? Y/N: ")
        
                  if status.lower() == 'n':
                         print("EXIT!!!!\n")
                         break
          
      print(f".....| Total Operations performed |.... : {total_count}\n")

if __name__=="__main__":
     main()
 