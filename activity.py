#1st Function
def my_function():
  name = input("enter your name: ")
  return name

#2nd function
def secondFunction():
  age = int(input("enter your age: "))
  return age

def main():
  name = my_function()
  age = secondFunction()

  print("My name is:", name)
  print("I am ", age, " years old.")

main()