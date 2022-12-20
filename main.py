import pandas as pd
import hashcat

file = pd.read_excel('D:\\AllProjects\\PyCharmProjects\\4_lab_algoritms\\student_v.1.06.xlsx')

email = file['email']
adress = file['Адрес']

tel_mas = []
with open('hacked.txt', 'r') as f:
    tel_mas = f.read().splitlines()

ru_alphabet1 = ['а', 'б', 'в', 'г', 'д', 'е',  'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
ru_alphabet2 = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
eng_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

output = []

for i in range(len(email)):
    tel_out = ''
    email_out = ''
    adr_out = ''
    key_out = 0

    tel_out = tel_mas[i][-11:]

    k = adress[i].split()[-1][0]
    indc = ru_alphabet1.index(k)
    key = 10 - indc

    for k in email[i]:
        if k in eng_alphabet:
            email_out += str(eng_alphabet[(eng_alphabet.index(k) + key) % 26])
        else:
            email_out += str(k)

    for j in adress[i]:
        if j in ru_alphabet1:
            adr_out += str(ru_alphabet1[(ru_alphabet1.index(j) + key) % 32])
        elif j in ru_alphabet2:
            adr_out += str(ru_alphabet2[(ru_alphabet2.index(j) + key) % 32])
        else:
            adr_out += str(j)

    output.append([tel_out, email_out, adr_out, key])

dataset = pd.DataFrame.from_dict(output)
dataset.columns = ['Телефон', 'email', 'Адрес', 'Сдвиг']
dataset.to_excel('dataset.xlsx', index=False)