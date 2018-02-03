from random import randint
import time


def merge_lists(listA,listB):
    # This function 'zips' two sorted lists
    result=[]

    while len(listA)>0 and len(listB)>0:
        if listA[0]<listB[0]:
            result.append(listA[0])
            # Remove first element from listA
            # when all numbers are used up, listA will be empty, triggering end of loop
            listA.pop(0)
        else:
            result.append(listB[0])
            listB.pop(0)

    # One of these lists will be empty, and 'everything else' gets added to the end
    result=result+listA+listB

    return result

def merge_sort(sort_list):
    # Ending condition checked first
    if len(sort_list)<2: #0 or 1
        return sort_list

    # Split list in half
    midpoint=int(len(sort_list)/2)
    listA=sort_list[:midpoint] # Excludes midpoint
    listB=sort_list[midpoint:] # Includes midpoint

    # Sort each half
    listA=merge_sort(listA)
    listB=merge_sort(listB)

    # Assume function worked, so listA and listB are sorted and can be merged
    return merge_lists(listA,listB)


def swap_sort(sort_list):
    result = sort_list[:] # See section on pointers in Args and Kwargs

    for i in range(len(result)):
        for j in range(i,len(result)):
            if result[j] < result[i]:
                tmp = result[i]
                result[i] = result[j]
                result[j] = tmp

    return result


def speed_test(list_length):
    print("Testing a length of %i..."%list_length)
    rand_list = [randint(0,list_length) for i in range(list_length)]

    then = time.time()
    merge_sort(rand_list)
    now = time.time()
    merge_sort_time = now - then
    print("Merge Sort took %g seconds"%merge_sort_time)

    then=time.time()
    swap_sort(rand_list)
    now=time.time()
    swap_sort_time = now - then
    print("Swap Sort took %g seconds"%swap_sort_time)
    print()


speed_test(10)
speed_test(1000)
speed_test(10000)

print("Brace yourself, this is a long one...")
speed_test(100000)