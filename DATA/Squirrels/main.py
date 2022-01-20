"""
Comb dataset and extract total number of squirrels depending on their colour
"""
import pandas

data = pandas.read_csv('Central-Park-Squirrel-Census-Squirrel-Data.csv')
gray_squirrels = len(data[data['Primary Fur Color'] == "Gray"])
cinammon_squirrels = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrels = len(data[data['Primary Fur Color'] == "Black"])

dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinammon_squirrels, black_squirrels]
}

df = pandas.DataFrame(dict)
df.to_csv("squirrels.csv")
