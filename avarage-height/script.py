print("Average height calculator.")

height_string = input(
    "Enter the height in cm. separate the measurements by comma. (eg. 176, 145, 164) \n")

height_list = height_string.replace(" ", "").split(",")

avg = round(sum(list(map(int, height_list))) / len(height_list), 2)

print(f"The average hight is {avg} cm.")
