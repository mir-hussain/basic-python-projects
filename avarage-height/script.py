print("Average height calculator.")

# Not using For loop

height_list = input(
    "Enter the height in cm. separate the measurements by comma. (eg. 176, 145, 164) \n").replace(" ", "").split(",")

avg = round(sum(list(map(int, height_list))) / len(height_list), 2)

print(f"The average hight is {avg} cm.")


# Using for loop

# height_list = input(
#     "Enter the height in cm. separate the measurements by comma. (eg. 176, 145, 164) \n").replace(" ", "").split(",")

# sum = 0

# for height in height_list:
#     sum += int(height)

# avg = sum / len(height_list)

# print(f"The average hight is {avg} cm.")
