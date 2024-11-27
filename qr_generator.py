import qrcode
import re

def is_valid_upi(upi_id):
    """Validate the UPI ID format."""
    pattern = r'^[\w.-]+@[\w.-]+$'
    return re.match(pattern, upi_id)

# Taking UPI ID as input with validation
upi_id = input("Enter your UPI ID (e.g., example@upi): ").strip()
if not is_valid_upi(upi_id):
    print("Invalid UPI ID format. Please try again.")
    exit()

# Taking recipient name, amount, and optional note
recipient_name = input("Enter the recipient's name: ").strip() or "Recipient"
amount = input("Enter the amount (optional): ").strip()
note = input("Enter a note or message (optional): ").strip()

# Define payment URLs
phonepe_url = f"upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&tn={note}"
google_pay_url = f"upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&tn={note}"

# Generate QR codes
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
