class CoffeeMachine:
    def __init__( self ):
        #self.coffee_machine_contents = {"water": 400, "milk": 540, "coffee_beans": 120, "cups": 9, "money": 550}
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
    def buy( self ):
        order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        water = self.water
        milk = self.milk
        coffee_beans = self.coffee_beans
        cups = self.cups
        money = self.money
        not_enough = []
        if order == "1":
            water -= 250
            coffee_beans -= 16
            cups -= 1
            money += 4

        elif order == "2":
            water -= 350
            milk -= 75
            coffee_beans -= 20
            cups -= 1
            money += 7
        elif order == "3":
            water -= 200
            milk -= 100
            coffee_beans -= 12
            cups -= 1
            money += 6
        elif order == "back":
            return

        if water < 0:
            not_enough.append("water")
        if milk < 0:
            not_enough.append("milk")
        if coffee_beans < 0:
            not_enough.append("coffee beans")
        if cups < 0:
            not_enough.append("cups")

        if not_enough != []:
            print("Sorry, not enough", not_enough[0], end = "")
            for ingredient in not_enough[1:]:
                print(", {}".format(ingredient), end="")
            print()

        else:
            print("I have enough resources, making you a coffee!")
            self.water = water
            self.milk = milk
            self.coffee_beans = coffee_beans
            self.cups = cups
            self.money = money

    def fill( self ):
        water = int(input("Write how many ml of water you want to add:\n"))
        milk = int(input("Write how many ml of milk you want to add:\n"))
        coffee_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
        cups = int(input("Write how many disposable cups you want to add:\n"))
        self.water += water
        self.milk += milk
        self.coffee_beans += coffee_beans
        self.cups += cups

    def take( self ):
        print("I gave you ${}".format(self.money))
        self.money = 0

    def remaining( self ):
        print("The coffee machine has:")
        print(self.water, "ml of water")
        print(self.milk, "ml of milk")
        print(self.coffee_beans, "g of coffee beans")
        print(self.cups, "disposable cups")
        print("${} of money".format(self.money))


if __name__ == '__main__':
    coffee_machine = CoffeeMachine()
    while(1):
        action = input("Write an action (buy, fill, take, remaining, exit):\n")
        if action == "buy":
            coffee_machine.buy()
        elif action == "fill":
            coffee_machine.fill()
        elif action == "take":
            coffee_machine.take()
        elif action == "remaining":
            coffee_machine.remaining()
        elif action == "exit":
            break
