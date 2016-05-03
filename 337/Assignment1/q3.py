encrypText = "Ryhu vla bhduv djr, lq Ghfhpehu 1989, L zdv orrnlqj iru d 'kreeb' surjudpplqj surmhfw wkdw zrxog nhhs ph rffxslhg gxulqj wkh zhhn durxqg Fkulvwpdv. Pb riilfh ... zrxog eh forvhg, exw L kdg d krph frpsxwhu, dqg qrw pxfk hovh rq pb kdqgv. L ghflghg wr zulwh dq lqwhusuhwhu iru wkh qhz vfulswlqj odqjxdjh L kdg ehhq wklqnlqj derxw odwhob: d ghvfhqgdqw ri DEF wkdw zrxog dsshdo wr Xqla/F kdfnhuv. L fkrvh Sbwkrq dv d zrunlqj wlwoh iru wkh surmhfw, ehlqj lq d voljkwob luuhyhuhqw prrg (dqg d elj idq ri Prqwb Sbwkrq'v Ioblqj Flufxv)."
encrypList = list(encrypText)

'''
Encryption is created by going three letters forward in the alphabet or if the letter is at the end of the alphabet by spilling
over onto the front. I decrypted it by reversing this process: if the letter was not one of the first three letters I went three
letters backwards, otherwise I went 23 letters forward.
'''
let = 0
while let < len(encrypList):
    if ord(encrypList[let]) >= 68 and ord(encrypList[let]) <= 90 or ord(encrypList[let]) >= 100 and ord(encrypList[let]) <= 122:
        encrypList[let] = chr(ord(encrypList[let]) - 3)
    elif ord(encrypList[let]) >= 65 and ord(encrypList[let]) <= 67 or ord(encrypList[let]) >= 97 and ord(encrypList[let]) <= 99:
        encrypList[let] = chr(ord(encrypList[let]) + 23)
    let += 1

print "".join(encrypList)
