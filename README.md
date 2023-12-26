
# Simple Json&Random game

A brief description of what this project does and who it's for

Why is it simple? Because only the built-in tools and only these two libraries were used to create this game
## Features
So far, there are few features, but at the moment the following functions are implemented:
1. Opening a JSON file with saving
2. Menu:
- The player chooses: to view the characteristics, buy an item or go to fight.
3. View Stats:
- The player selects the view stats option. The program outputs its characteristics in the following form:
4. Adding to the characteristics:
- When a player receives an item, its characteristics increase by the characteristics of the item.
- When a player sells an item, its characteristics are reduced by the characteristics of the item.
5. Trade:
- The merchant offers to buy items for the player or leave the store.
- If the player chooses an item, then its value will be released
- If the player does not buy the item, he returns to the interaction menu with the merchant.
- If the player buys an item, then the player's amount of money is checked.
- If there is not enough money, the merchant expels him and does not give the item.
- If there is enough money, the player buys the item. The cost of the item is deducted from his money. Subject indicators are added to the characteristics. The merchant loses an item from the shop and the amount of money increases. The item falls into the player's list.
6. The battle:
- The enemy for the battle is randomly selected. The battle takes place with the help of a d6 die roll.
- If more than 3 drops out, the player deals damage to the opponent. The player's damage is deducted from the opponent's HP. If the HP is less than or equal to 0, then the opponent dies, and the player gets an item and money.
- If the drop is less than or equal to 3, the player takes damage from the opponent. The opponent's damage is deducted from the player's HP. If the player dies, the game ends.

- Crit Damage
 
### Possible plans include a boss battle, an increase in the narrative, and the opportunity to attack the merchant


## Run Locally

Clone the project

```bash
  git clone https://github.com/JuliossJunk/simpleJsonGame.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  #its a joke there no dependencies XD
```

Start the game in command line mode

```bash
  python main.py
```


## Authors


- [@JuliossJunk](https://github.com/JuliossJunk)

