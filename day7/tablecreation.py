from prettytable import PrettyTable
mytable = PrettyTable(["Student Name","Class","Section","Percentage"])

mytable.add_row(["Leonard","TE","A","90%"])
mytable.add_row(["Penny","TE","A","85%"])
mytable.add_row(["Howard","TE","A","46%"])
mytable.add_row(["Carry","TE","B","56%"])
mytable.add_row(["Sheldon","SE","A","90%"])
mytable.add_row(["Amy","SE","A","95%"])
mytable.add_row(["FID","TE","A","86%"])

print(mytable)


#...................