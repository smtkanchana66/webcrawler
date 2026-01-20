import urllib.request, urllib.parse, urllib.error
import re 
url_lst = list()
temp_url = 'https://pahe.ink/'

while True:
    fhand = urllib.request.urlopen(temp_url)
    print("This is temp url",temp_url,len(url_lst))

    for line in fhand:
        decoded_line = line.decode('utf-8', errors='ignore').strip()
        url = re.findall('https?://\\S+"', decoded_line)
        print(url)

        if url:
            if url[0] not in url_lst:            
                url_lst.extend(url)
            print(url_lst)
            
        if url_lst:
            with open("Url_list.txt", "w") as url_file:
                url_file.write(url_lst[0])
            temp_url = url_lst[0]
            print(url_lst[0])
            url_lst.remove(url_lst[0])
            print(url_lst[0])
        else:
            break

print(len(url_lst))