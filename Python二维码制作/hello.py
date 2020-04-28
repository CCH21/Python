#!/usr/bin/env python3

import qrcode

qr = qrcode.QRCode(
    version=1,     # 值为1-40的整数，控制二维码的大小，如果想让程序自动确定，将值设置为None并使用fit参数即可
    error_correction=qrcode.constants.ERROR_CORRECT_L,     # 大约7%或更少的错误能被纠正（默认M，可选L,M,H）
    box_size=10,     # 控制二维码中每个小格子包含的像素数
    border=4,     # 控制边框（二维码与图片边界的距离）包含的格子数，默认为4，是相关标准规定的最小值
)
qr.add_data('Hello, QRCode!')
qr.make(fit=True)
img = qr.make_image()
img.save('hello.png')
