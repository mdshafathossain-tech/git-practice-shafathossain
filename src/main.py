import datetime
from utils import add, subtract

name = "Shafat Hossain"
today = datetime.date.today()

print(f"Hello, my name is {name}")
print(f"Today's date is: {today}")

# Testing the new calculator functions
print(f"10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {subtract(10, 5)}")