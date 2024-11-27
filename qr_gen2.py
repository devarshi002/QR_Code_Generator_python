import qrcode
import re
import urllib.parse

def is_valid_phone_number(phone_number):
    """Validate phone number format (assuming it’s a 10-digit phone number)."""
    pattern = r'^\d{10}$'  # 10 digit phone number
    return re.match(pattern, phone_number)

# Taking phone number as input with validation
phone_number = input("Enter your phone number (10 digits): ").strip()
if not is_valid_phone_number(phone_number):
    print("Invalid phone number format. Please enter a 10-digit phone number.")
    exit()

# Create the UPI ID using the phone number
upi_id = f"{phone_number}@upi"

# Taking recipient name, amount, and optional note
recipient_name = input("Enter the recipient's name: ").strip() or "Recipient"
amount = input("Enter the amount (optional): ").strip()
note = input("Enter a note or message (optional): ").strip()

# URL encode the UPI ID, name, amount, and note to ensure proper formatting
recipient_name_encoded = urllib.parse.quote(recipient_name)
note_encoded = urllib.parse.quote(note)

# Define payment URLs with encoded parameters for PhonePe and Google Pay
phonepe_url = f"upi://pay?pa={upi_id}&pn={recipient_name_encoded}&am={amount}&tn={note_encoded}"
google_pay_url = f"upi://pay?pa={upi_id}&pn={recipient_name_encoded}&am={amount}&tn={note_encoded}"

# Generate QR codes for both payment options
phonepe_qr = qrcode.make(phonepe_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save QR codes to image files
phonepe_qr.save("phonepe_qr.png")
google_pay_qr.save("google_pay_qr.png")

# Display QR codes
try:
    phonepe_qr.show()
    google_pay_qr.show()
except Exception as e:
    print(f"Error displaying QR codes: {e}")

print("QR codes generated successfully!")
print("Saved as 'phonepe_qr.png' and 'google_pay_qr.png'.")
