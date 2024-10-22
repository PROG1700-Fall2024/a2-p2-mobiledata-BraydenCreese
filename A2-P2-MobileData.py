#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #: W0491583 
#Student Name: Brayden Creese

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # getting user input and checking for invalid inputs
    while True:
        try:
            dataAmount = float(input("Enter data usage (mb): "))
            break
        except ValueError:
            print("Invalid Input! Please enter a valid number for data usage.")


    # cacls for data rates / user input
    if dataAmount <= 200:
        totalCost = 20.00 # <--- flat rate for 200mb
    elif dataAmount <= 500:
        totalCost = dataAmount * 0.105 # <--- over 200-500 rate per mb
    elif dataAmount <= 1000:
        totalCost = dataAmount * 0.110  # <--- over 500-1Gb(1000) per mb
    else:
        totalCost = 118.00 # <--- flat rate over 1Gb


    # print out results to user
    print(f"\nTotal chrage is ${totalCost:.2f}")

    # YOUR CODE ENDS HERE

main()