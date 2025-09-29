my_sum=0
while True:
    my_input = input("Enter number or Stop : ")
    if my_input == "Stop":
        break
    if my_input.isdigit():
        my_sum += int(my_input)
    else:
        print("Please enter number or Stop")

print(my_sum) 