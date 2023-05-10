#Import the constraint module
from constraint import *

#Define a function to solve Einstein's puzzle
def solve_puzzle():

    #Create a new problem instance
    einstein_puzzle = Problem()

    #Define possible values for each variable
    country = ["England", "Japan", "Norway", "Spain", "Ukraine"]
    pet_animal = ["Dog", "Fox", "Horse", "Snail", "Zebra"]
    cigar_brand = ["Chesterfield", "Kools", "LuckyStrike","OldGold","Parliament"]
    house_color = ["Blue", "Green","Ivory", "Red","Yellow" ]
    liquid = ["Coffee", "Milk", "OrangeJuice", "Tea", "Water"]

    #Add constraints to make sure that every variable takes a unique value
    einstein_puzzle.addConstraint(AllDifferentConstraint(), country)
    einstein_puzzle.addConstraint(AllDifferentConstraint(), pet_animal)
    einstein_puzzle.addConstraint(AllDifferentConstraint(), cigar_brand)
    einstein_puzzle.addConstraint(AllDifferentConstraint(), house_color)
    einstein_puzzle.addConstraint(AllDifferentConstraint(), liquid)

    #Add every variable to the problem instance with possible values
    criteria = country + pet_animal + cigar_brand + house_color + liquid
    einstein_puzzle.addVariables(criteria, [1, 2, 3, 4, 5])

    #Add the constraints that define the relationships between every variable
    einstein_puzzle.addConstraint(lambda che, fox: abs(che - fox) == 1, ("Chesterfield", "Fox"))
    einstein_puzzle.addConstraint(lambda koo, hor: abs(koo - hor) == 1, ("Kools", "Horse"))
    einstein_puzzle.addConstraint(lambda luc, ora: luc == ora, ["LuckyStrike", "OrangeJuice"])
    einstein_puzzle.addConstraint(lambda jap, par: jap == par, ["Japan", "Parliament"])
    einstein_puzzle.addConstraint(InSetConstraint([1]), ["Norway"])
    einstein_puzzle.addConstraint(InSetConstraint([3]), ["Milk"])
    einstein_puzzle.addConstraint(lambda nor, blu: abs(nor - blu) == 1, ("Norway", "Blue"))
    einstein_puzzle.addConstraint(lambda eng, red: eng == red, ["England", "Red"])
    einstein_puzzle.addConstraint(lambda spa, dog: spa == dog, ("Spain", "Dog"))
    einstein_puzzle.addConstraint(lambda cof, gre: cof == gre, ("Coffee", "Green"))
    einstein_puzzle.addConstraint(lambda ukr, tea: ukr == tea, ("Ukraine", "Tea"))
    einstein_puzzle.addConstraint(lambda gre, ivo: gre - ivo == 1, ("Green", "Ivory"))
    einstein_puzzle.addConstraint(lambda old, sna: old == sna, ("OldGold", "Snail"))
    einstein_puzzle.addConstraint(lambda koo, yel: koo == yel, ("Kools", "Yellow"))

    #Obtain the puzzle solutions
    answers = einstein_puzzle.getSolutions()

    #Print the solutions
    if len(answers) > 0:
        for home in range(1, 6):
            print(f"\nHouse {home}")
            for x in criteria:
                for s in answers:
                    if s[x] == home:
                        print(x)

#Call the function to solve the puzzle                        
solve_puzzle()