
# Inserts an int into an already sorted list of numbers
def insert_in_sorted(x, sorted_list):
    # Iterates through the sorted list. i in range is used to get the correct index for inserting number when x < number in list
    for i in range(len(sorted_list)):
        if x < sorted_list[i]:
            # insert into list at i index, if x <  sorted_list[i]
            sorted_list.insert(i, x)
            return sorted_list
    # If no x < list[i] is found, then x is the largest number in the list. Append to list, then return list
    sorted_list.append(x)
    return sorted_list

# Sorts a list of numbers by calling insert in sorted function
def insertion_sort(my_list):
    
    out = [] 
    # Iterates through all numbers in list
    for n in my_list:
        # calls insert in sorted, that func mutates the out list when inserting number at correct index
        insert_in_sorted(n, out)
    
    return out

print(insert_in_sorted(2,[]))
print(insert_in_sorted(5,[0,1,3,4]))
print(insert_in_sorted(2,[0,1,2,3,4]))
print(insert_in_sorted(2,[2,2]))
print(insert_in_sorted(12,[1,1,1,1,2,2,2,2,7,7,7,7,7,12,12,12,12,12,15,15,15,15]))

test_list= [5,12,754,1,0,4,3]

print(insertion_sort(test_list))

test_list = []

print(insertion_sort(test_list))

test_list = [5,12,754,1,0,4,3]

print(insertion_sort(test_list))

test_list = [1,1,1,1,2,2,2,2,7,7,7,7,7,12,12,12,12,12,15,15,15,15]

print(insertion_sort(test_list))