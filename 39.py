import Sort 

List = list(map(int, filter(None, input("Enter numbers: ").split(" "))))

C1 = int(input("Enter 1 for bubble sort and 2 for selection sort: "))

sorting_instance = Sort.Sorting(List)

if C1 == 1:
    sorted_list = sorting_instance.bubble_sort() 
    print(f"Your sorted list is: {sorted_list}")
elif C1 == 2:
    sorted_list = sorting_instance.selection_sort()  
    print(f"Your sorted list is: {sorted_list}")