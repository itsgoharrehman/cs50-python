# Home Federal Savings Bank

greeting = input("Hi there! How are you greeting the day at Home Federal Savings Bank? ")
greeting = greeting.lower()

if greeting.startswith("hello"):
    print("0$")
elif greeting == "h":
    print("20$")
else:
    print("100$")