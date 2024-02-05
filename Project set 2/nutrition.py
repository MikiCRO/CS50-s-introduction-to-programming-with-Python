fruits = {"Apple": "52", "Banana": "96" , "Grapes":"69", "Orange":"62"
          , "Strawberry":"29", "Watermelon":"30", "Blueberries":"57", "Pineapple":"50"
          , "Mango":"60", "Avocado":"160", "Peach":"59", "Pear":"57", "Kiwi":"42"
          , "Raspberry":"53", "Lemon":"29", "Lime":"30", "Cantaloupe":"34", "Blackberries":"43"
          , "Papaya":"43", "Cranberries":"46"}

d =input("Item: ").lower()

for key,val in fruits.items():
    if(key.lower()==d):
      print(f"Calories: {val}")