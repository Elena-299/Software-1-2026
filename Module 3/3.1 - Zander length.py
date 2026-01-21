length= float(input("Enter the length of the Zander caught: "))
if length < 42:
    print("The size is insufficient, you have to put the fish back into the lake!")
    remainder = 42 - length
    print(f"The Zander was {remainder:.3f}cm under the approved size limit.")
else:
    print("Congratulations on your catch!")
