from pyzbar.pyzbar import decode
from PIL import Image


a=decode(Image.open('nvpan.jpg'))
# print(a)
# b=str(a[0].data)
d=a[0].data
# c=b.split(' ')
# print(a[0].data)
f=d.decode('utf-8') 
# print(f)



DOB = f[96:107]
Pan =f[120:]
print(Pan)
print(DOB)
# print(f[96:107])#DOB
# print(f[120:])#PanNumber



