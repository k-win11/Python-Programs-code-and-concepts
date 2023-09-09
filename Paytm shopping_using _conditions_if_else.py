# Paytm Discount offer 

print('''Offer on sele Amount more then 6000, gain 50% flate discount''')
print('Also offer on card use icici as code icici get 10% flet extra discount')
amount=float(input('enter the amount: '))
card=str('enter the icici card code: ')
if amount>=5000:
    print('total amout pay',amount*0.5)
    card=str(input('enter the card: '))
    if card=='icici':
        print('final mount is: ',amount*0.5*.9)
else:
    print('total payamout: ',amount)
print('Thanks for shopping')

    
  

