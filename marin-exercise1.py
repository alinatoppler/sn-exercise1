# Marin Balabanov, May 7, 2019
# Mood Checker

print("Hi there!")
print("We'd love to know how you are feeling.")
print(" ")
mood = input("Please enter your mood. Are you happy, nervous, sad, excited or relaxed? (Please use lower case). ")

if mood == "happy":
    print("Whoohoo! So great to hear that you are", mood)

elif mood == "sad":
    print("Oh no... I am so sorry that you are", mood)

elif mood == "nervous":
    print("Everything will be fine, relax. No need to be", mood)
    print("Take a deep breath...")

elif mood == "relaxed":
    print("This is awesome. So glad that you are", mood)

elif mood == "excited":
    print("How cool is that! We are verrrry excited that you are", mood)

else:
    print("I don't recognize this mood. I guess we'll have to work on your responses.")

