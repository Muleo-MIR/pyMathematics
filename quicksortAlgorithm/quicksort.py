
#quicksort algorithm 

filename = "quicksortAlgorithm\output.txt"
list = open(filename, "r").read().split(' ')

print(list)

def quicksort (list):
    if len (list) <= 1:
        return list
    else:
        pivot = list[0]
        left = [x for x in list[1:] if x < pivot]
        right = [x for x in list[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


sorted_list = quicksort(list)
print(f'Sorted list:{sorted_list}')

