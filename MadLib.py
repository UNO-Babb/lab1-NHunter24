#MadLib.py
#Name: Nick Hunter
#Date: 9/1/24
#Assignment: MadLib

def main():
  print("MyBizzareStory")
  #Ask user for words
  verb1 = input("Enter a verb: ")
  noun1 = input("Enter an animal: ")
  noun2 = input("Enter a noun: ")
  name1 = input("Enter a name: ")
  adj1 = input("Enter an adjective: ")
  food1 = input("Enter a food: ")
  print("I was" , verb1 , "with my" , noun1 , "when I heard a" , adj1 , "noise." , "I went to the other room and saw" , name1 , "fighting my" , noun1 , "and" , verb1 , "my" , food1 + ".")
  #Print the story with the user supplied words.



#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
