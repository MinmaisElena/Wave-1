deposit = float(input("How much money is depositd?: "))
year1 = deposit*1.04
year2 = year1*1.04
year3 = year2*1.04
print("Your money in saving account are "+str(round(year1,2))+"for year 1, "+str(round(year2,2))+"for year 2, "+str(round(year3,2))+"for year 3.")