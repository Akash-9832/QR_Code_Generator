import qrcode

features=qrcode.QRCode(version=1,box_size=30,border=3)
features.add_data('https://www.linkedin.com/in/akash-modak-it/')
features.make(fit=True)
image=features.make_image(fill_color="black",back_color="skyblue")
image.save('link.png')