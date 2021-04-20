import random
import time

print("Hangman Game")
gameStart = True
wrong = 0
def load_words(wordlist):
       wordlist = list()
       with open ("wordlist.txt", "r") as f:
            for line in f:
                wordlist.append(line.rstrip('\n'))
       return wordlist
def print_output():
    print
    print(''.join([x+" " for x in output]))

wordlist = load_words('wordlist.txt')
randword = random.choice(wordlist)
print("""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """)
output = ['_'] * len(randword)

while(gameStart):
    for i in range(1):
        print_output()
        print ("")
        letter = input("Guess a letter/word: ")
        if letter in randword:
            print("")
            print (letter, " is in the word!")
            for i, x in enumerate(randword):
                if x is letter:
                    output[i] = letter
        else:
            print("")
            print ("Incorrect,", "", letter, " is not in the word.")
            wrong += 1
    if(wrong == 1):
        print("""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    """)
    if(wrong == 2):
        print("""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    """)
    if(wrong == 3):
        print("""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    """)
    if(wrong == 4):
        print("""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    """)
    if(wrong == 5):
        print("""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    """)
    if(wrong == 6):
        print("""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    """)

    if("".join(output) == randword):
        print("You win! The word was: ", randword)
        input('Press ENTER to exit')
        f.close()
        time.sleep(15)
        gameStart = False

    if(wrong == 6):
        print("You lose! The word was: ", randword)
        input('Press ENTER to exit')
        f.close()
        time.sleep(15)
        gameStart = False