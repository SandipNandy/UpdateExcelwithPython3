from openpyxl import Workbook
import time

book = Workbook()
sheet = book.active
for i in range(1, 19):
        sheet['F'+str(i)] = 'Y'


#now = time.strftime("%x")
#sheet['A3'] = now

book.save("cashapp 14C PROD SANITY excel.xlsx")
#book.save("BOOK3.xlsx")