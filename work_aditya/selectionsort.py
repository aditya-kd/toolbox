#lex_auth_0127667356693872643343
def swap(num_list, first_index, second_index):
    #Remove pass and copy the code written earlier for this function
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp

def find_next_min(num_list,start_index):
    #Remove pass and copy the code written earlier for this function
    mini=min(num_list[start_index::])
    return num_list.index(mini)

def selection_sort(num_list):
    #Remove pass and implement the selection sort algorithm to sort the elements of num_list in ascending order
    for i in range(len(num_list)):
        index=find_next_min(num_list, i)
        swap(num_list, index, i)
        
#Pass different values to the function and test your program
num_list=[8,2,19,34,23, 67, 91]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)