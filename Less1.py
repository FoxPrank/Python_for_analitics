# 1
fio = 'Петрова Татьяна Алексеевна'
for el in list(fio):
 print(el)

# 2
def my_usd_to_eur (usd, rate=1.17):
 try:
  eur = round(float(usd)*float(rate),2)
  return eur
 except ValueError:
  print('Ведите сумму usd и обменный курс числом, обменный курс по умолчанию = 1,17')
print(my_usd_to_eur(15.3))
