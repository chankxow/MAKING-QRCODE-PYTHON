import qrcode # install with terminal --> pip install qrcode

qr = qrcode.QRCode(
  version=1,
  error_correction = qrcode.constants.ERROR_CORRECT_L,
  box_size=10,
  border=4,
)

link = str(input("ใส่ลิ้งที่ต้องการแปลงเป็น QRCODE : "))
NameQrcode = str(input("ชื่อไฟลที่ต้องการแปลง QRCODE (JPG) : "))
qr.add_data(link)

img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{NameQrcode}.jpg")
