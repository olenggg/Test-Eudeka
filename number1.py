def result(num):
         
            if num % 3 == 0 and num % 5 == 0:
                print("Hello World")
                 
            elif num % 5 == 0:
                print("World")

            elif num % 3 == 0:
                print("Hello")
                
if __name__ == "__main__":
    num = int(input("Enter Number:"))
    print(result(num))