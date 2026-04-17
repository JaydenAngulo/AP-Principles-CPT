import random

mode = str(input("Do you want to guess the states or capitals?: ")).lower()

def quiz(a):
    states_and_capitals = ["Alabama:Montgomery", "Alaska:Juneau", "Arizona:Phoenix", "Arkansas:Little Rock", "California:Sacramento", "Colorado:Denver", "Connecticut:Hartford", "Delaware:Dover", "Florida:Tallahassee", "Georgia:Atlanta", "Hawaii:Honolulu", "Idaho:Boise", "Illinois:Springfield", "Indiana:Indianapolis", "Iowa:Des Moines", "Kansas:Topeka", "Kentucky:Frankfort", "Louisiana:Baton Rouge", "Maine:Augusta", "Maryland:Annapolis", "Massachusetts:Boston", "Michigan:Lansing", "Minnesota:Saint Paul", "Mississippi:Jackson", "Missouri:Jefferson City", "Montana:Helena", "Nebraska:Lincoln", "Nevada:Carson City", "New Hampshire:Concord", "New Jersey:Trenton", "New Mexico:Santa Fe", "New York:Albany", "North Carolina:Raleigh", "North Dakota:Bismarck", "Ohio:Columbus", "Oklahoma:Oklahoma City", "Oregon:Salem", "Pennsylvania:Harrisburg", "Rhode Island:Providence", "South Carolina:Columbia", "South Dakota:Pierre", "Tennessee:Nashville", "Texas:Austin", "Utah:Salt Lake City", "Vermont:Montpelier", "Virginia:Richmond", "Washington:Olympia", "West Virginia:Charleston", "Wisconsin:Madison", "Wyoming:Cheyenne"]
    correct = 0
    amount_of_questions = int(input("How many questions do you want?: "))
    while amount_of_questions <= 0 or amount_of_questions > 50:
        amount_of_questions = int(input("Please choose a positive number: "))

    if a.lower() == "capitals":
        random.shuffle(states_and_capitals)
        for item in states_and_capitals:
            entry = item.split(":")
            state = entry[0]
            capital = entry[1]
            answer = input(f"What is the capital of {state}?: ")
            if answer.title() == capital:
                print("Correct!")
                correct += 1
            else:
                print("Incorrect")
        print(f"You got {correct} out of {len(states_and_capitals)} questions correct!")
        
    if a.lower() == "states":
        random.shuffle(states_and_capitals)
        for item in states_and_capitals:
            entry = item.split(":")
            state = entry[0]
            capital = entry[1]
            answer = input(f"Which states' capital is {capital}?: ")
            if answer.title() == state:
                print("Correct!")
                correct += 1
            else:
                print("Incorrect")
        print(f"You got {correct} out of {len(states_and_capitals)} questions correct!")

while mode != "states" and mode != "capitals":
    mode = str(input("Your answer has to be either 'states' or 'capitals': ")).lower()

quiz(mode)