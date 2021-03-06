import requests
from bs4 import BeautifulSoup as bs

url = 'https://hub.ucd.ie/usis/W_HU_MENU.P_PUBLISH?p_tag=GYMBOOK'
# url = 'https://hub.ucd.ie/usis/W_HU_REPORTING.P_RUN_SQL?p_query=SW-GYMANON&p_confirmed=Y&p_parameters=A450F95C75D0F126D32D1FF64557FC5BE3608119B07310D1D9E0C20656AF60AC613D8D39CD5236FDD9B95C7FC606FF4D94E0DE7540D7ADAA8F964D46DB321598695BE40C523901A6AB2B61B8F30A1C6E1FA6F5A2BE1353FDE6EAD59DF28C3AB4E4AA22A96297609C311A753F158A47837945DFE7BB3D3EF5A3D8BFAE093B4DC6EC041E121E68CAA752BAE9DFC6D83D14C5EFDAFA243934E1F4559432346B80F3838DB9B304E4EA9DC1C3CE192154E0E637EC330A3EB5B5637930DD720E2022429508FD3E81ECA2AB85C70D0DBC00D8E4414063A45BBCF6E58F2A1706E3F3ED26FBB44AB7F8CBB856ACEBB57AA4C3A2602CA86379E3E7F94292288E6351EB27E14A673F076940CB2DE54A6749171A1B2D02BB0C72A5EC0C3EB8BD6675ED0D7D7F2B4C3F4E8F1FB3DE0EB30DDF1B17E3F4CFFF1B47FDF82CC5B02492080FE40F0C490A0DE619512CEE3C5C6463A0A3F691F76D61D5FBF5FF685EE09667D7F45C45'

req = requests.get(url)

# print(req.text)

with open('test_init.html', 'w') as f:
    f.write(req.text)



with open('test_init.html', 'r') as f:
    filE = f.read()

work = bs(filE, 'html.parser')

link = 'https://hub.ucd.ie/usis/' + work.find_all('a', text='Book')[0]['href']

# print(link)
req = requests.get(link).text
new_link = 'https://hub.ucd.ie/usis/' + bs(req, 'html.parser').find_all('form')[0]['action']
print(new_link)
student_number = 20385676

params = {
    'MEMBER_NO':student_number
}

req = requests.post(new_link, params=params)
with open('test_result.html', 'w') as f:
    filE = f.write(req.text)