#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst




def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    sorted_list = []

    while len(list1) > 0 or len(list2) > 0: #while the length of list1 or list2 is more than- 0
        if list1 == []: #if list1 is empty
            sorted_list.append(list2.pop(0)) #pop the 1st element off of list two and add it to sorted list
        elif list2 == []:
            sorted_list.append(list1.pop(0))
        elif list1[0] < list2[0]: #if the first element in list one is less than the first element in list2
            sorted_list.append(list1.pop(0)) #add that element to sorted list
        else:
            sorted_list.append(list2.pop(0)) #otherwise add that element from list2 to sorted list

    return sorted_list

##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    # if len(lst) > 1:
    #     mid = int(len(lst)) // 2
    #     left = lst[:mid]
    #     right = lst[mid:]

    #     merge_sort(left)
    #     merge_sort(right)

    #     i = 0 #index of left side
    #     j = 0 #index of right side
    #     k = 0 #index of sorted version


    #     while i < len(left) and j < len(right):
    #         if left[i] < right[j]: #if the num on the left is less than the num on the right
    #             lst[k] = left[i] #the num at that index is rebound to the same index of the sorted version
    #             i += 1 #increment i, move on to the next index
    #             k_list.append([k])
    #         else:
    #             lst[k] = right[j] #the num at that index is rebound to the same index of the sorted version
    #             j += 1 #increment j, move on to the next index
    #             k_list.append([k])
    #         k += 1 #no matter if i or j, k needs to be incremented

    #         while i < len(left): #while i is less than the length of the left side
    #             lst[k] = left[i]
    #             i += 1
    #             k += 1
    #             k_list.append([k])

    #         while j < len(right): #while j is less than the length of the right side
    #             lst[k] = right[j]
    #             j += 1
    #             k_list.append([k])

    #walking through this example from the book really helped me understand merge sort

    if len(lst) < 2: #if the lst is empty or len(1)
        return lst #return the lst as is

    mid = int(len(lst) // 2)
    lst1 = merge_sort(lst[:mid]) #run merge_sort on the first half (left) of the lst
    lst2 = merge_sort(lst[mid:]) #run merge_sort on the second half (right) of the lst

    return merge_lists(lst1, lst2)



#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
