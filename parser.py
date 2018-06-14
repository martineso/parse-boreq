import base64
from urllib import unquote

def decode(encoded):
  return base64.b64decode(encoded)

def print_boresp (resp):
  boresp = ''

  boresp += 'Transaction type: ' + resp[:2] + "\n"
  boresp += format_borica_date(resp[2:16]) + "\n"
  boresp += 'Amount: ' + get_price(resp[16:28]) + "\n"
  boresp += 'Terminal id: ' + resp[28:36] + "\n"
  boresp += 'Order id: ' + resp[36:51] + "\n"
  boresp += 'Order description : ' + resp[51:176] + "\n"
  boresp += 'Lang: ' + resp[176:178] + "\n"
  boresp += 'Version: ' + resp[178:181] + "\n"
  boresp += 'Currency: ' + resp[181:184]
  print boresp

def format_borica_date (date_str):
  return "Processed at " + date_str[-6:-4] + ':' + date_str[-4:-2] + ":" + date_str[-2:]

def get_price (price):
  price = float(price) / 100
  return str(price)

#raw_query = 'MTAyMDE4MDYxNDExMzY1OTAwMDAwMDAwMDAwMTc5MDAwMDQxNTAwMDAwMDAwMDAyNDg30uXx8u7i7iDv6%2BD54O3lICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBCRzEuMkJHTio0NDQ0NDQgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBKdUvOodSIrxM%2BgUYqrk9tVmh3De6MefrSgdNdhcdkfr%2FIFLdMuVhKI2yKZ0hseHu%2Fs%2F%2FJ36ZOppOCZ9pbhFzu9z%2FxNuIQw6LRqooCfDklxuCM%2BqY%2Fk%2B4iwBwHLpPS8yE1o36IT20wD5FInL4O5fscrceKrFQncyiUkdgOfKkOcg%3D%3D'

raw_query = raw_input()
unquoted = unquote(raw_query)
data = decode(unquoted)

data = data.decode('cp1251')
print_boresp(data)
