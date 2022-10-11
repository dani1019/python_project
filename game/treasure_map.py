row1 = ['■','■','■']
row2 = ['■','■','■']
row3 = ['■','■','■']

rows = [row1 ,row2, row3]

#setting the location coordinates
col_row_num = input("where do you want to treasure? ")

#The number of col,row
col = int(col_row_num[0]) - 1
row = int(col_row_num[1]) - 1

#enter x the location that user enter the number[col,row].
rows[row][col] = 'x'

#print the result
print(f"{row1}\n{row2}\n{row3}")