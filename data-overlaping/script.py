

with open("file1.txt") as file:
    list1 = file.readlines()

with open("file2.txt") as file:
    list2 = file.readlines()


result = [int(num) for num in list2 if num not in list1]

print(result)
