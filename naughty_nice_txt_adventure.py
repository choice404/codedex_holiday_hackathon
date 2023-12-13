# Yazmine Hoeferlin
# GitHub username: cedar-codes
# 12/12/23
# Codedex Holiday Hackathon: Naughty or Nice Morality Tracker. Text based choose your own adventure game with
# a Christmas theme. Help save Christmas from the villain Krampus Polar bear!


# Decide on villain name
# Add 1-2 more scenes/prompts?
# What should we name the game??

# YuleQuest: Naughty or Nice Tracker

# Prompt 1: Caroling  x
# Prompt 2: Snowball   x
# Prompt 3: Feed Rudolph   x
# Prompt 4: Fixing toys
# Prompt 5: Hot chocolate for Mrs. Clause

# Naughty Route: If certain amount of naughty points, join main villain.
# Nice Route: If certain amount of nice points, convince the villain to join you and save Xmas.


class NaughtyorNiceGame:
    def __init__(self):
        self._morality_tracker = 0
        self._nice_tracker = 0
        self._naughty_tracker = 0

    def display_prompt(self, prompt_text, options):
        """Gives the prompts and options for naughty or nice"""

        print(f"{prompt_text}")
        for option_text in enumerate(options, start=1):
            print(f"{option_text}")

    def process_choice(self, choice, nice_outcome, naughty_outcome):
        """Sets values for morality trackers and stores Naughty or Nice values"""

        if choice.lower() == 'nice' or 1:       # can choose nice or 1
            print(f"You choose the nice option: {nice_outcome}")
            self._morality_tracker += 1         # adding to trackers
            self._nice_tracker += 1

        elif choice.lower() == 'naughty' or 2:
            print(f"You choose the naughty option: {naughty_outcome}")  # function to be able to modify it later
            self._morality_tracker -= 2         # can change values of tracker here
            self._naughty_tracker += 1
            self._nice_tracker -= 1

        else:
            print("Invalid choice. Please select 'Nice' or 'Naughty'.")     # for cases beyond entering 1 or 2

    def run_game(self):
        """Can modify script and prompts or add more"""

        # Prompt 1: Caroling Chaos or Cheer?
        self.display_prompt("A group of elves are caroling and spreading Yuletide cheer. You have a choice:",
                            ["You join in with the cheerful elves and sing along with them!",
                             "Bah Humbug! I'm not in the mood to sing..."])

        choice_caroling = input("What's your decision? (Nice/Naughty): ")

        self.process_choice(choice_caroling, "You join in the holiday fun!",
                            "You are feeling mischievous today and end up throwing a snowball instead!")

        # Prompt 2: Snowball Fight
        self.display_prompt("On the way back to Santa's workshop, you see some elves sledding. Do you:",
                            ["Join in and have a blast!",
                             "Listen to the evil Krampus Polar Bear and throw snowballs of exploding ice at them!?"])

        choice_snowball = input("What's your decision? (Nice/Naughty): ")

        self.process_choice(choice_snowball, "You join in the fun!",
                                "You embrace the chaos and throw an exploding ice snowball, causing a"
                                " fight among the elves.")

        # Prompt 3: Feed Rudolph
        self.display_prompt("As you continue back to Santa's workshop, Rudolph the Reindeer comes up to you.\n"
                            "Rudolph needs his favorite chocolate chip cookies before the Christmas journey, "
                            "so you head to the kitchen.",
                        ["Pick his favorite, chocolate chip.",
                            "Be sneaky and pick the oatmeal raisin!"])

        choice_caroling = input("What's your decision? (Nice/Naughty): ")

        self.process_choice(choice_caroling, "You picked Rudolph's favorite and Rudolph is beaming!",
                        "Rudolph gets sick from his allergy to raisins and has to sit Christmas "
                            "out this year!")

        # Display the morality tracker
        print("\nMorality Tracker:", self._morality_tracker)

        if self._nice_tracker > self._naughty_tracker:
            print("You have chosen the moral high road and Christmas is saved!")
        elif self._naughty_tracker > self._nice_tracker:
            print("You embrace Yuletide chaos and help the villain ruin Christmas!")
        else:
            print("You chose the moral neutral ground and are neither naughty nor nice.")


# Instantiate the game and run it
morality_tracking_game = NaughtyorNiceGame()
morality_tracking_game.run_game()
