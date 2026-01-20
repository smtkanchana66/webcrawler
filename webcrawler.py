import urllib.request, urllib.parse, urllib.error
import re 
url_lst = list()
temp_url = 'https://pahe.ink/'

while True:
    #fhand = urllib.request.urlopen(temp_url)
    #print("This is temp url",temp_url,len(url_lst))

    try:
        fhand = urllib.request.urlopen(temp_url)
    except urllib.error.HTTPError as e:
        print("HTTP error:", e.code, temp_url)
    except urllib.error.URLError as e:
        print("URL error:", e.reason, temp_url)
    
    #print("fhand done")

    for line in fhand:
        decoded_line = line.decode('utf-8', errors='ignore').strip()
        url = re.findall('https?://\\S+"', decoded_line)
        #print("URL FINDED", url)

        if url:
            iterate = (len(url)-1)
            # print(iterate) 
            a = True
            while a:
                if url[iterate] not in url_lst:            
                    url_lst.extend(url)
                iterate -= 1
                if url:
                    a = False
                if iterate == -1:
                    a = False

    print(url_lst)
    if url_lst:
        with open("Url_list.txt", "a") as url_file:
            url_file.write(url_lst[0] + "\n")
        #print(temp_url)                  
            temp_url = url_lst[0]
        print(temp_url)
        url_lst.remove(url_lst[0])

        #print("This is temp last", temp_url)
        
    if not url_lst:
        #print("THis break worked")
        break

print(len(url_lst))