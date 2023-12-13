

def trivia_intro():
    total_nice_points = 0
    total_naughty_points = 0
    print("In order to help save Christmas, we first must make sure that you know all about the true meaning of Christmas!")
    print("Be sure to answer these questions to the best of your ability, for every point earned will help you rebuild the broken toy")
    print("The level you choose will determine how many points you will earn for each answer")
    print("With that in mind, please select your level")
    level = select_level()
    if level == 'easy':
        naughty, nice= easy_mode()
        total_naughty_points+= naughty
        total_nice_points+= nice
    elif level=='classic':
        naughty, nice= classic_mode()
        total_naughty_points+= naughty
        total_nice_points+= nice
    elif level == 'extreme':
        naughty, nice= extreme_mode()
        total_naughty_points+= naughty
        total_nice_points+= nice
    print('You have completed this mini game! You have earned ' + str(total_naughty_points) + ' naughty points and ' + str(total_nice_points)+ ' nice points.')

#questions for the extreme level:
movie_questions = {
    'In Home Alone, where are the McCallisters going on vacation when they leave Kevin behind?': 'paris', 
    'Which actor played six different roles in the Polar Express?': 'tom hanks',
    'What is the name of the Snowman narrator in Rudolph the Red Nose Reindeer?': 'sam',
    'What did Frosty say after he came to life?': 'happy birthday',
    'In It\'s a Wonderful Life, what does an angel get when they ring the bell': 'wings',
    'In The Nightmare Before Christmas, what does Jack call Santa Claus?': 'sandy claws',
    'In The Nightmare Before Christmas, what is the name of Jack\'s dog?':'zero',
    'In The Nightmare Before Christmas, what is Oogie Boogie made of?':'bugs',
    'In Elf, what city does Buddy travel to find his dad?': 'new york city',
    'How many reindeers does Santa Claus have?' : 'nine',
    'What is the Grinch\'s dog\'s name?': 'max' ,
    'How many ghosts are in A Christmas Carol?':'four' ,
}

#questions for the classic level:
christmas_music= {
    'What singer is nicknamed the \'Queen of Christmas\' ': 'mariah carey',
    'How many gifts are given in total in the song 12 days of Christmas': '364',
    'Who is coming for Stray Kids in their song \'Christmas Evel\' ': 'jack frost',
    'Which one of Santa\'s reindeer has the same name as another holiday mascot?' : 'cupid',
    'According to the song, what did my true love give to me on the 2nd day of Christmas?':'turtle dove',
    'What color Christmas will Elvis have?':'blue',
    'In Winter Wonderland, what do we call the snowman?': 'parson brown',
    'Whose eyes are all aglow in the Christmas Song?': 'tiny tots'   
}

#questions for easy level:
easy_questions = {
    'who has a bright red nose': 'rudolph',
    'what do you do under a mistletoe?': 'kiss',
    'what does Santa Claus come down to enter a house?': 'chimney',
    'what does Santa give to bad children instead of presents': 'coal',
    'what pulls Santa\'s sleigh?' : 'reindeer'
}

def select_level():
    while True:
        print('Here are the available levels: \nEasy \nClassic \nExtreme')
        answer = input('Type the level you\'d like to select: ')
        answer = answer.lower()
        if answer == 'easy':
            print('You have selected Easy')
            return 'easy'
        elif answer == 'classic':
            print('You have selected Classic')
            return 'classic'
        elif answer == 'extreme':
            print("You have selected Extreme")
            return 'extreme'
        else:
            print("Invalid Selection. Please try again.")

def easy_mode():
    nice_points= 0
    naughty_points = 0
    missing_toys = 0
    question_counter= 1
    for key in easy_questions.keys():
        print("Question " + str(question_counter) + ": " + key)
        user_answer = input("Enter your answer here: ")
        if user_answer.lower() == easy_questions[key].lower():
            print("\nCorrect. You have found a missing toy!\nAre you going to bring it back to the workshop, hide it, or destroy it?")
            while True:
                try:
                    print('1) Bring it back to the workshop \n2)Hide it \n3)Destroy it')
                    return_or_hide = int(input("\nEnter your selection: "))
                    if return_or_hide == 1:
                        print('You have decided to bring the missing toy back to the workshop.\n')
                        nice_points +=1
                        missing_toys +=1
                        break
                    elif return_or_hide == 2:
                        print('You have decided to hide the toy. The hiding spot isn\'t the best, but maybe they won\'t find it...\n')
                        naughty_points +=1
                        break
                    elif return_or_hide == 3:
                        print('You have destroyed the toy. Now they can never restore it!\n')
                        naughty_points +=2
                        break
                    else:
                        print('Invalid selection. Please try again\n')
                except TypeError: #catches type error
                    print('Please enter the number of your selection\n')
            question_counter +=1
                
        else:
            print("Seems you don't know the answer. Maybe you'll know the next one! \n")
            question_counter +=1
    if missing_toys == 1:
        print("You have collected: 1 missing toy.\n")
    else:
        print("You have collected: "+ str(missing_toys)+ " missing toys.\n")
    return naughty_points, nice_points

def classic_mode():
    nice_points= 0
    naughty_points = 0
    broken_toys_fixed = 0
    question_counter= 1
    for key in christmas_music.keys():
        print("Question " + str(question_counter) + ": " + key)
        user_answer = input("Enter your answer here: ")
        if user_answer.lower() == christmas_music[key].lower():
            print("\nCorrect. You have found a broken toy! \nAre you going to completely fix the toy, give it to another elf, or leave it broken")
            while True:
                try:
                    print('1) Fix it completely \n2) give it to another elf \n3)leave it')
                    return_or_hide = int(input("Enter your selection: "))
                    if return_or_hide == 1:
                        print('You have decided to bring the fix the broken toy. It is restored to its original state. The kids will love it!\n')
                        nice_points +=3
                        broken_toys_fixed +=1
                        break
                    elif return_or_hide == 2:
                        print('You give the broken toy to the head elf. Maybe they might be able to restore it...\n')
                        nice_points +=1
                        break
                    elif return_or_hide == 3:
                        print('You decided to leave it. They won\'t have time to fix it. They will be really sad they aren\'t receiving this toy...\n')
                        naughty_points +=2
                        break
                    else:
                        print('Invalid selection. Please try again\n')
                except TypeError: #catches type error
                    print('Please enter the number of your selection\n')
            question_counter +=1
        else:
            print("Seems you don't know the answer. Maybe you'll know the next one! \n")
            question_counter +=1
    if broken_toys_fixed == 1:
        print("You have fixed: 1 broken toy.\n")
    else:
        print("You have fixed: "+ str(broken_toys_fixed) + " broken toys.\n")
    return naughty_points, nice_points

def extreme_mode():
    nice_points= 0
    naughty_points = 0
    toy_piece = 0
    toys =0
    question_counter= 1
    for key in movie_questions.keys():
        print("Question " + str(question_counter) + ": " + key)
        user_answer = input("Enter your answer here: ")
        if user_answer.lower() == movie_questions[key].lower():
            print("\nCorrect. You have found a broken toy piece. \nAre you going to collect the piece or throw it away")
            while True:
                try:
                    print('1) Collect the piece \n2) Throw it away')
                    return_or_hide = int(input("Enter your selection: "))
                    if return_or_hide == 1:
                        print('You have decided to collect the broken toy piece. Hopefully you can collect enough pieces to restore the toy!\n')
                        nice_points +=4
                        toy_piece +=1
                        if toy_piece%2 == 0:
                            print('You were able to restore a toy!')
                            nice_points +=3
                            toys +=1
                        break
                    elif return_or_hide == 2:
                        print('You throw away the broken toy piece. Now they\'ll never be able to restore the toy!\n')
                        naughty_points +=4
                        break
                    else:
                        print('Invalid selection. Please try again\n')
                except TypeError: #catches type error
                    print('Please enter the number of your selection\n')
            question_counter +=1
        else:
            print("Seems you don't know the answer. Maybe you'll know the next one! \n")
            question_counter +=1
    if toy_piece == 1:
        print('You have collected one toy piece. You were unable to make any toys.')
    else:
        if toys == 1:
            print("You have collected: "+ str(toy_piece) + " toy pieces. You have made 1 toy!\n")
        else:
            print("You have collected: "+ str(toy_piece) + " toy pieces. You have made " + str(toys) + " toys!\n")
    return naughty_points, nice_points

trivia_intro()