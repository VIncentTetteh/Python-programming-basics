#number = (["1", "3", "5"], ["2", "4", "6"])
#print(number.partition(' '))
def partition(number):
    if number % 2 == 0:
        return(number, None)
    else:
        return(None, number)
    
def partition_list(numbers):
    list1 = []
    list2 = []
    for number in numbers:
        left_right = partition(number)
        if left_right[0] == number:
            list1.append(number)
        else:
            list2.append(number)
    return (list1, list2)

a = partition_list([1,2,3,4,5,6,7,8,9,10])
print(a)