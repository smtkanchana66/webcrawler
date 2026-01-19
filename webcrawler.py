import urllib.request, urllib.parse, urllib.error
import re 
url_lst = list()

fhand = urllib.request.urlopen('https://pahe.ink/')

for line in fhand:
    decoded_line = line.decode('utf-8', errors='ignore').strip()
    url = re.findall('https?://\\S+', decoded_line)
    print(url)
#     if url:
#         newurl = url[0]
#         url_lst.extend(url)

# print(newurl,url_lst)