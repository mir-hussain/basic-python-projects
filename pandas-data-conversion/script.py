import pandas

data = pandas.read_csv("data.csv")
black_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_count = len(data[data["Primary Fur Color"] == "Gray"])


data_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [black_count, cinnamon_count, gray_count]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
