import qrcode

file_path = r'Chapter3\\main4\\qrcodeUrl.txt'
with open(file_path, 'rt', encoding='UTF8') as f :
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = 'Chapter3\\main4\\'+qr_data + '.png'
        qr_img.save(save_path)