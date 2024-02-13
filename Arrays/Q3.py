# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
def get_list(num):
    odd_list = []
    for i in range(0,num):
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list 

num = int(input("enter a number:"))
print(get_list(num))