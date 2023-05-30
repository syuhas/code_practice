num = int(input("Enter a number: "))

result = bin_search(seq, num, len(seq)-1, 0)



if result != -1:
    print(f"The number you entered is the {str(result + 1)}th number in the sequence.")
else:
    print("The number you entered is not present in the sequence.")