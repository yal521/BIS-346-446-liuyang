def display_table(lst):
    print("\t",end="")
    for i in range(len(lst[0])):
        print(i+1,end="\t")
    print()

    for i in range(len(lst)):
        print(i+1,end="\t")
        for col in lst[i]:
            print(col,end="\t")
        print()
# Testing
display_table([[23,62,93,31],[72,14,575,61],[2,6,13,5]])
