import qrcode

#taking upi id as a input

upi_id = input("Enter your upi Id: ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment url based on the upi id and the payemnt app
#you can modify these urls based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr code for each payment 
phonepe_qr = qrcode.make(phonepe_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the qr code to image file (optional)
phonepe_qr.save('phonepe_qr.png')
google_pay_qr.save('google_pay_qr.png')

#Display the qr codes (you may need to install pil/ pillow library)

phonepe_qr.show()
google_pay_qr.show()