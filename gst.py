cost=int(input("Enter the cost :"))
CGST=int(input("Enter the CGST :"))
SGST=int(input("Enter the SGST :"))
aoc = 9/100*cost
aos = 9/100*cost
Total_cost = cost+ aoc+ aos
print("CGST on cost =", aoc)
print("SGST on cost =", aos)
print("Total cost = ",Total_cost)
