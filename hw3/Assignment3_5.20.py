def display_table(lst):
    print("\t",end="")
    for a in range(len(lst[0])):
        print(a+1,end="\t")
    print()

    for a in range(len(lst)):
        print(a+1,end="\t")
        for col in lst[a]:
            print(col,end="\t")
        print()
# Testing
display_table([[34,98,23,35],[62,34,255,91],[3,4,9,5]])
