
import random


def bin_search(seq, num, hi, low):

    if hi >= low:

        mid = (hi + low) // 2
        print(f"{mid + 1} is the new middle location")

        if seq[mid] == num:
            return mid
        
        elif seq[mid] > num:
            return bin_search(seq, num, mid - 1, low)
        
        else:
            return bin_search(seq, num, hi, mid + 1)
        
    else:
        return -1








seq = []

for i in range(0, 99):
    
    if i > 0:
        newrand = random.randint(-100, 100)
        
        while newrand in seq:
            newrand = random.randint(-100, 100) 


        seq.append(newrand)
                

    else:
        x = random.randint(-100, 100)
        seq.append(x)
    
    
        

num = int(input("Enter a number: "))

result = bin_search(seq, num, len(seq)-1, 0)

seq.sort()
print(seq)

if result != -1:
    print(f"The number you entered is the {str(result + 1)}th number in the sequence.")
else:
    print("The number you entered is not present in the sequence.")

