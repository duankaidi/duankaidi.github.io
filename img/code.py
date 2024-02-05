import requests
import time
import pprint

cnt = 0
lx = 0
id = 900
mem = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
}
while id < 1000:
  response = requests.get("https://t.mwm.moe/fj",headers=headers)
  # fail_cnt = 0
  # while response.status_code != 200:
  #   fail_cnt = fail_cnt + 1
  #   print("fail to get images! x {} times ".format(fail_cnt))
  #   print("status code: {}".format(response.status_code))
  #   time.sleep(30)
  #   response = requests.get("https://sex.nyan.xyz/api/v2/img")
  cnt = cnt + 1
  if cnt == 10:
    time.sleep(4)
    cnt = 0
  con = response.content
  if con in mem.keys():
    lx = lx + 14
    if lx == 10:
      break
  else:
    lx = 0
    mem[con] = 1
    id = id + 1
    with open(str(id) + ".jpeg", "wb+") as f:
      f.write(con)
    print("{}.jpeg".format(id))
