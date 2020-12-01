import random
from time import sleep
from os import system, name 

def clr():
   # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
def clear(): 
    clr()
    print("Enter your choice\n 0. Normal dice\n 1. 1 High Probability\n 2. 2 High Probability\n 3. 3 High Probability\n 4. 4 High Probability\n 5. 5 High Probability\n 6. 6 High Probability\n")


def plain():
  print(" -------")
  print("|       |")
  print("|       |")
  print("|       |")
  print(" -------")

def one():
  print(" -------")
  print("|       |")
  print("|   *   |")
  print("|       |")
  print(" -------")

def two():
  print(" -------")
  print("|     * |")  
  print("|       |")
  print("| *     |")
  print(" -------")

def three():
  print(" -------")
  print("|     * |")
  print("|   *   |")
  print("| *     |")
  print(" -------")

def four():
  print(" -------")
  print("| *   * |")
  print("|       |")
  print("| *   * |")
  print(" -------")

def five():
  print(" -------")
  print("| *   * |")
  print("|   *   |")
  print("| *   * |")
  print(" -------")

def six():
  print(" -------")
  print("| *   * |")
  print("| *   * |")
  print("| *   * |")
  print(" -------")

def start():
  for i in range(1,3):
    clear()
    one()
    sleep(0.05)
    clear()
    two()
    sleep(0.05)
    clear()
    three()
    sleep(0.05)
    clear()
    four()
    sleep(0.05)
    clear()
    five()
    sleep(0.05)
    clear()
    six()
    sleep(0.05)
    clear()



def normal():  
  x = random.randint(1,7)

  if x==1:
    one()

  if x==2:
    two()

  if x==3:
    three()

  if x==4:
    four()

  if x==5:
    five()

  if x==6:
    six()


def onem():
  x = random.choice([1,1,1,1,2,3,4,5,6])

  if x==1:
    one()

  if x==2:
    two()

  if x==3:
    three()

  if x==4:
    four()

  if x==5:
    five()

  if x==6:
    six()



def twom():
  x = random.choice([1,2,3,2,4,2,5,2,6])

  if x==1:
    one()

  if x==2:
    two()

  if x==3:
    three()

  if x==4:
    four()

  if x==5:
    five()

  if x==6:
    six()




def threem():
  x = random.choice([3,1,3,2,3,4,3,5,6])

  if x==1:
    one()

  if x==2:
    two()

  if x==3:
    three()

  if x==4:
    four()

  if x==5:
    five()

  if x==6:
    six()



def fourm():
  x = random.choice([4,1,4,3,4,2,4,5,6])

  if x==1:
    one()

  if x==2:
    two()

  if x==3:
    three()

  if x==4:
    four()

  if x==5:
    five()

  if x==6:
    six()



def fivem():
  x = random.choice([5,1,5,2,5,3,4,5,6])

  if x==1:
    one()

  if x==2:
    two()

  if x==3:
    three()

  if x==4:
    four()

  if x==5:
    five()

  if x==6:
    six()



def sixm():
  x = random.choice([6,1,6,3,6,4,5,6,2])

  if x==1:
    one()

  if x==2:
    two()
 
  if x==3:
    three()

  if x==4:
    four()

  if x==5:
    five()

  if x==6:
    six()

n='y'

while n=='y' or n=='Y':
  clr()
  ask = int(input("Enter your choice\n 0. Normal dice\n 1. 1 High Probability\n 2. 2 High Probability\n 3. 3 High Probability\n 4. 4 High Probability\n 5. 5 High Probability\n 6. 6 High Probability\n"))

  start()

  if ask==0:
    normal()
  if ask==1:
    onem()
  if ask==2:
    twom()
  if ask==3:
    threem()
  if ask==4:
    fourm()
  if ask==5:
    fivem()
  if ask==6:
    sixm()

  n=input("Again? ( Y/N ):")