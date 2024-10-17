# دریافت نمرات از کاربر
nombres = [
    float(input('Nomre dars Riazi khod ra vared konid: ')),
    float(input('Nomre dars Shimi khod ra vared konid: ')),
    float(input('Nomre dars Dini khod ra vared konid: '))
]

# دریافت تعداد واحدها از کاربر
zaribs = [
    int(input('Tedade vahed dars Riazi ra vared konid: ')),
    int(input('Tedade vahed dars Shimi ra vared konid: ')),
    int(input('Tedade vahed dars Dini ra vared konid: '))
]

# محاسبه معدل کل
moadel_kol = sum([nombres[i] * zaribs[i] for i in range(3)]) / sum(zaribs)

# نمایش معدل کل
print(f'Moadel kol: {moadel_kol:.2f}')

print(nombres[1])