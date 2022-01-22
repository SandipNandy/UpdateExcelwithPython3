from openpyxl import Workbook
import time

book = Workbook()
sheet = book.active
for i in range(1, 19):
        sheet['F'+str(i)] = 'Y'


#now = time.strftime("%x")
#sheet['A3'] = now

book.save("Excel1.xlsx")
#book.save("BOOK3.xlsx")
