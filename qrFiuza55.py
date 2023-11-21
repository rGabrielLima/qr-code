import qrcode

qrFiuza = qrcode.make(
    "https://linktr.ee/fiuza55im"
)

qrFiuza.save("qrcode.png")
qrFiuza.show()

