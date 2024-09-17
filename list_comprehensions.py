if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    """
    # THIS CODE CORRESPONDS TO BELOW CODE
    for index in range(x + 1):
        for index_other in range(y + 1):
            for index_another in range(z + 1):
                if index + index_other + index_another != n:
                    empty_list.append([index, index_other, index_another])
    """
            
    print([[index, index_other, index_another] for index in range(x + 1) \
    for index_other in range(y + 1) for index_another in range(z + 1) \
    if index + index_other + index_another != n])