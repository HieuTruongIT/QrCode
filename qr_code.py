import qrcode

# dữ liệu mã hóa thành qr code 
data = "..."


# Tạo đối tượng QRCode
qr = qrcode.QRCode(
    version=1,  # Độ lớn của mã QR (1 là nhỏ nhất, 40 là lớn nhất)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Mức độ sửa lỗi (L: thấp, M: trung bình, Q: cao, H: rất cao)
    box_size=10,  # Kích thước mỗi ô vuông trong mã QR
    border=4,  # Độ dày biên của mã QR
)

# Thêm dữ liệu vào mã QR
qr.add_data(data)
qr.make(fit=True)

# Tạo ảnh mã QR
img = qr.make_image(fill='black', back_color='white')

# Lưu mã QR vào file
img.save("qrcode_example.png")

# Hiển thị mã QR
img.show()
