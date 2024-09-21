import json
import time

print('You have to update the inventory first')
# Input for Mava kulfi
n=int(input('Mava Kulfi:'))

# Input for chocolate kulfi
p=int(input('Chocolate Kulfi :'))

# Input for Jamun kulfi
q=int(input('Jamun Kulfi :'))

# Input for Gulkand kulfi
r=int(input('Gulkand Kulfi :'))

# Input for Dryfruit kulfi
s=int(input('Dryfruit Kulfi :'))

# Dictionary of total Records 
rec = {
    101: {'Name': 'Mava Kulfi', 'Price': 10, 'qt': n},
    102: {'Name': "Chocolate Kulfi", 'Price': 25, 'qt': p},
    103: {'Name': 'Jamun Kulfi', 'Price': 25, 'qt': q},
    104: {'Name': 'Gulkand Kulfi', 'Price': 25, 'qt': r},
    105: {'Name': 'Dryfruit Kulfi', 'Price': 25, 'qt': s}
}
print('--------------------Shri ganesh kulfi ----------------')
a=time.ctime()
print('               ',a,'                         ')
# Prints the total products with their keys
for key in rec.keys():
    print(key, ':', rec[key]['Name'], '\t|', 'Price:', rec[key]['Price'], '\t|', 'Quantity:', rec[key]['qt'])
print('-------------------------------------------------------')

# Inputs for Product ID and Quantity
ui_Name = str(input('Enter Coustomer Name   : '))
ui_Mail = input('Enter Mail Id  : ')
ui_Number = (input('Enter Number  : '))
ui_pr = int(input('Enter Product Id: '))
ui_qn = int(input('Enter Quantity  : '))

# Using if and else statement to check the 
if ui_pr in rec and rec[ui_pr]['qt'] >= ui_qn:
    print('-------------------------------------------------------')
    print('Name     :', rec[ui_pr]['Name'])
    print('Price    :', rec[ui_pr]['Price'])
    print('Quantity :', ui_qn)
    print('-------------------------------------------------------')
    print('Billing Amount : ', rec[ui_pr]['Price'] * ui_qn)
    
    # Update the quantity
    rec[ui_pr]['qt'] -= ui_qn
    
    print('-------------------------------------------------------')
    
    # Save updated data into a JSON file
    js = json.dumps(rec, indent=4)
    with open('rec.json', 'w') as fd:
        fd.write(js)
    sale= ui_Name+' , '+ui_Mail+' , '+ui_Number+' , '+str(rec[ui_pr]['Name'])+' , '+str(ui_qn)+' , '+str(rec[ui_pr]['Price'])+' , '+str(ui_qn*rec[ui_pr]['Price'])+' , '+time.ctime()+ '\n'
else:
    print("Invalid product ID or insufficient stock!")
fd=open('sales.csv','a')
fd.write(sale)
fd.close()
