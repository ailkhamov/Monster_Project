class monster():

    # Charecteristics
    def __init__(self, name = '', eye='', fur='', skill='', cuteness=''):
        self.name = name
        self.eye = eye
        self.fur = fur
        self.skiil = skill
        self.cuteness = cuteness

    def scare(self,option):
        if option == 'yes':
            return print("I WILL KILL YOU HAHA!... (Opponent RUN AWAY) WELL DONE! YOU ARE SO SCARY!")
        else:
            return print("BE MORE BRAVE!")
    def eat(self, option):
        if option == 'yes':
            return print("YUM YUM! YOU HAVE FULL HEALTH AGAIN")
        else:
            return print("YOU HAVE LOW HEALTH OMG...YOU'RE GOING TO DIE SOON!")
    def transfrom(self,option):
        if option == "Dragons":
            return print("You have transfored into a dragon")
        elif option == "Unicorns":
            return print("You have transformed into Unicorn")
        elif option == 'Giant Human':
            return ("You have transformed into a Giant Human")
        else:
            return ("The tranformation is not possible")





