import random
import sys
import os
import time
import math
class LogicalInt():
#Defines mathematical operations
    def add(x,y):
        return x + y
    def subtract(x,y):
        return x - y
    def multiply(x,y):
        return x * y
    def divide(x,y):
        return x / y
    def square(x):
        return x ** 2
    def sqroot(x):
        math.sqrt(x)
#Determines if they would like to manipulate numbers with mathematical operations
    def maths_help(self):
        self.maths_help = input("Would you like to manipulate some numbers?\n")
    def process_maths_help(self):
        if self.maths_help in ChatbotInt.yes:
            while True:
                new_maths_help = None
                print("1.Add two numbers in the form of x + y")
                print("2.Subtract one number from another in the form of x - y")
                print("3.Multiply two numbers in the form of x * y")
                print("4.Divide one number by another in the form of x / y")
                print("5.Square a number in the form of x ^ 2")
                print("6.Square root a number in the form of √x")
                decision = int(input("Enter the number for the operation you would like to carry out:"))
                if decision == 1:
                    x = int(input("Please enter x:\n"))
                    y = int(input("Please enter y:\n"))      
                    print(x," + ",y," = ",LogicalInt.add(x,y))
                    new_maths_help = input("World you like to maipulate some more numbers?\n y/n:")
                    if new_maths_help == 'y':
                        continue
                    else:
                        break

                elif decision == 2:
                    x = int(input("Please enter x:\n"))
                    y = int(input("Please enter y:\n"))  
                    print(x," - ",y," = ",LogicalInt.subtract(x,y))
                    new_maths_help = input("World you like to maipulate some more numbers? y/n:")
                    if new_maths_help == 'y':
                        continue
                    else:
                        break

                elif decision == 3:
                    x = int(input("Please enter x:\n"))
                    y = int(input("Please enter y:\n"))  
                    print(x," x ",y," = ",LogicalInt.multiply(x,y))
                    new_maths_help = input("World you like to maipulate some more numbers? y/n:")
                    if new_maths_help == 'y':
                        continue
                    else:
                        break

                elif decision == 4:
                    x = int(input("Please enter x:\n"))
                    y = int(input("Please enter y:\n"))  
                    print(x," / ",y," = ",LogicalInt.divide(x,y))
                    new_maths_help = input("World you like to maipulate some more numbers? y/n:")
                    if new_maths_help == 'y':
                        continue
                    else:
                        break

                elif decision == 5:
                    x = int(input("Please enter x:\n"))
                    y = int(input("Please enter y:\n"))  
                    print(x," ^ 2 = ",LogicalInt.square(x))
                    new_maths_help = input("World you like to maipulate some more numbers? y/n:")
                    if new_maths_help == 'y':
                        continue
                    else:
                        break

                elif decision == 6:
                    x = int(input("Please enter x:\n"))
                    y = int(input("Please enter y:\n"))  
                    print("√",x," = ",LogicalInt.sqroot(x))
                    new_maths_help = input("World you like to maipulate some more numbers? y/n:")
                    if new_maths_help == 'y':
                        continue
                    else:
                        break

                else:
                    print("Invalid input")
                    new_maths_help = "y"
        elif self.maths_help in ChatbotInt.no:
            ChatbotInt.reply = ChatbotInt.decline
            return ChatbotInt.reply
            print(ChatbotInt.reply)
            restart = input("Restart? y/n:")
        

class ChatbotInt():
  '''
  This class provides...
  '''
  greeting_type = ["hello", "hi", "hey", "hiya", "whatsup", "sup"]
  unknown = "Sorry, I didn't get what you just said!"
  response = None
  reply = None
  yes = ["yes", "yeah", "y", "yup"]
  no = ["no", "nope", "nah", "n"]
  decline = "OK, How can i help you?\n >>"
  restart = None
  
  def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

  def listen(self):
    self.intent = input("Say hi to Chatbot \n >>")

  def process_intent(self):
    if self.intent in ChatbotInt.greeting_type:
      ChatbotInt.response = random.choice(ChatbotInt.greeting_type)
    else:
      ChatbotInt.response = ChatbotInt.unknown

  def get_response(self):
    return ChatbotInt.response

  def get_reply(self):
    return ChatbotInt.reply
# Create another class for mathematical stuff e.g LogicalInterface()
# This class could provides methods such as addition, subtraction, etc.

# Create another class called ChatbotInterface()

# Create a main file def main():
# if __name__ == "__main__":
#     main()
#        main
#         ||
#   ChatbotInterface
#         ||
#   LogicalInterface

def main():
    restart = None
    while restart != 'n':      
        bot = ChatbotInt()
        logic = LogicalInt()
        bot.listen()
        bot.process_intent()
        response = bot.get_response()
        print(response)
        logic.maths_help()
        logic.process_maths_help()

        while True:
            restart = input("Restart? y/n:")
            if restart in ('y','n'):
                break
        if restart == 'y':
            continue
        if restart == 'n':
            print("End")
            time.sleep(5)
            break

      
if __name__ == "__main__":
  main()
