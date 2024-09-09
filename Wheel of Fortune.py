'''
Author: Syed Qadri
Date: November 27, 2023
Program: Wheel of Fortune Program Assignment
ICS3U1-1; Bulhao
'''

while True:
    #Import
    import random, string, math, time

    #Create Catagories
    categories=['MOVIE', 'CELEBRITIES', 'FOOD', 'COUNTRY', 'ANIMAL']

    #Expand Catagories
    movies=['HARRY POTTER', 'INCEPTION', 'THE AVENGERS', 'THE GODFATHER', 'TITANIC']
    celebrities=['JOHNNY DEPP', 'LEONARDO DICAPRIO', 'TAYLOR SWIFT', 'BRAD PITT', 'KIM KARDASHIAN']
    foods=['PIZZA', 'BURGERS', 'ROAST BEEF', 'RAMEN', 'PANCAKES']
    countries=['CANADA', 'PAKISTAN', 'KAZAKHSTAN', 'URUGUAY', 'UNITED ARAB EMIRATES']
    animals=['KANGAROO', 'LION', 'TIGER', 'ZEBRA', 'SNAKE']

    #Create Variables
    cash = 0
    guesses=[]
    vowels=("A", "E", "I", "O", "U")

    #Assign Wheel Prizes
    outcomes=("BANKRUPT", 150, 200, 250, 300, 400, 450, 500, 600, 700, 750, 800, 900, 1000)

    #Select Catagroy
    category=categories[random.randint(0,4)]

    #Select Secret Word
    if category=='MOVIE':
        secret_word=movies[random.randint(0,4)]

    elif category=='CELEBRITIES':
        secret_word=celebrities[random.randint(0, 4)]

    elif category=='FOOD':
        secret_word=foods[random.randint(0, 4)]

    elif category=='COUNTRY':
        secret_word=countries[random.randint(0, 4)]

    else:
        secret_word=animals[random.randint(0, 4)]

    #Hide Secret Word
    def hide():
        global display
        display = "" #create new variable
        for char in secret_word:
            if char.isalpha() and char.upper() not in guesses: #Switch from letter to dashes
                display+="-"
            else:
                display+=char #Switch from dashes to letters
        return display

    #Spin The Wheel
    def choice1():
        print('--------------------------------------------------')
        global prize
        prize=random.choice(outcomes) #User spins for a random outcome
        global cash
        if prize!="BANKRUPT": #They Spin Bankrupt
            print(f"You landed on ${prize}!")
        else: #They spin a cash value
            print("You landed on BANKRUPT! You lose all your money.")
            play_again()
            return prize
        letter()

    #Guess a Letter (consonant)
    def letter():
        global cash
        global prize
        consonant=input("\nEnter a letter: ").upper() #User guesses a consonant
        Llength=len(consonant)
        #Check if input matches all verifications
        if consonant not in vowels and consonant.isalpha() and Llength==1 and consonant not in guesses:
            guesses.append(consonant) #add letter to guesses
            count=secret_word.upper().count(consonant) #Count how many times letter occurs in secret word
            if count==0: #If the letter is not in the secret word
                cash += prize
                print(f'Sorry...the letter {consonant} is not in the word!\nYou have ${cash}!')
                time.sleep(1)
                menu()
            else: #If the letter is in the word
                winnings = count*prize
                print(f"\nThere are {count} {consonant}'s in the secret word. You win ${winnings}!")
                cash += winnings
                print(f'\nBank: ${cash}')
                time.sleep(1)
                menu() #Reset to Menu
        elif consonant in vowels: #If the letter guessed is a vowel
            print("You must enter a consonant! Please try again...")
            time.sleep(1)
            letter()
        elif consonant in guesses: #If the letter has already been guessed
            print(f'You have already guessed the letter {consonant}. Please try again.')
            time.sleep(1)
            letter()
        else: #If user inputs a number or more than one letter
            print("Invalid Input. Please enter a letter.")
            time.sleep(1)
            letter()

    #User Chooses To Buy A Vowel
    def choice2():
        global cash
        cost = 250 #Variable Price
        # Verify if user can purchase a vowel
        if cash >= cost:
            vowel = input("Enter a vowel: ").upper() #User inputs a variable they would like to purchase
            if vowel.isalpha() and vowel in vowels and vowel not in guesses: #Verify all requirements
                if cash>=cost:
                    cash-=cost
                    guesses.append(vowel)
                    count=secret_word.upper().count(vowel)
                    print(f"\nThere are {count} {vowel}'s in the secret word. That cost you ${cost}!")
                    print(f"You have ${cash} left!")
                    time.sleep(1)
                    menu()
            elif vowel in guesses:  # If the vowel was already baught
                print(f'You have already purchased this vowel. Please try again.')
                time.sleep(1)
                choice2()
            else:  # User is slow and did not enter a vowel even though they are buying a vowel
                print("You must enter a vowel! Please try again...")
                time.sleep(1)
                choice2()
        else: #User is a brokie
                print("You do not have enough money to buy a vowel.")
                time.sleep(1)
                menu()

    #User choses to guess the word
    def choice3():
        global play
        solve=input("Enter the secret word: ").upper()
        if solve==secret_word.upper():
            print(f"Congratulations...{secret_word} is correct!\nYou're going home with ${cash}!")
            time.sleep(1)
            play_again()
        else:
            print(f"Sorry...{solve} is incorrect!")
            print(f"The secret word was {secret_word}.")
            time.sleep(1)
            play == "off"

    #Play Again
    def play_again():
        print("")
        play=input("Would You Like to Play Again? (Y or N): ").upper()
        if play=="Y":
            print("")
        elif play=="N":
            print("Thanks for playing Wheel of Fortune! Goodbye.")
            time.sleep(2)
            quit()
        else:
            print('Invalid Input. Enter either "Y" for Yes or "N" for No.')
            play_again()

    #Create Menu
    def menu():
        print(f'\nCATEGORY:             {category}') #Display Category
        print(f'SECRET WORD:          {hide()}') #Display Secret Word
        #Verify
        try: #User Makes Choice
            choice=int(input('\n1 - Spin The Wheel\n2 - Buy A Vowel\n3 - Solve the Word\n\nEnter Your Selection: '))
            if choice==1: #User chose to spin the wheel
                choice1()
            elif choice==2: #User chose to buy a vowel
                choice2()
            elif choice==3: #User chose to guess the word
                choice3()
            else:
                print('Invalid selection! Please enter a number between 1 and 3!') #Input was not in range
                time.sleep(1)
                menu()
        except ValueError: #Input was not a number
            print('Invalid Input! Please enter a number!')
            time.sleep(2)
            menu()

    #Start Program
    menu()