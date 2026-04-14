import random

mode = input("Do you want to guess the states or capitals? ")

def quiz(a):
    states_to_capitals = ["Alabama:Montgomery", "Alaska:Juneau", "Arizona:Phoenix", "Arkansas:Little Rock", "California:Sacramento", "Colorado:Denver", "Connecticut:Hartford", "Delaware:Dover", "Florida:Tallahassee", "Georgia:Atlanta", "Hawaii:Honolulu", "Idaho:Boise", "Illinois:Springfield", ""]
    correct = 0
    if a == "capitals":
        random.shuffle(states_to_capitals)
        for item in states_to_capitals:
            entry = item.split(":")
            state = entry[0]
            capital = entry[1]
            answer = input(f"What is the capital of {state}? ")
            if answer.title() == capital:
                print("Correct!")
                correct += 1
            else:
                print("Incorrect")
            

quiz(mode)