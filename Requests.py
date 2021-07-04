import requests
import time

url = input('Enter Url Target : ')

print("Getting Webpage Data For",'"'+url+'"')
x = requests.get(url)

status = x.status_code

code = x.apparent_encoding

arrivalOfResponse = x.elapsed

print("Webpage satus :",status)
time.sleep(1)
print("Delay",arrivalOfResponse)
time.sleep(1)
print("Apparent Encoding",'"' + code + '"')
lol = '"' + code + '"'
time.sleep(1)
print('Extracting html data...')
time.sleep(1.5)
try:
    y = x.text

    f = open('getHtml.html', "w")
    f.write(y)
    print('Html data sucsesfully written in the targeted file [sucsess]')
    f.close()

except UnicodeEncodeError:
    try:
        z = str(x.content, lol)

        e = open('getHtml.html', "w")
        e.write(z)
        print('Html data sucsesfully written in the targeted file [UnicodeEncodeError]')
        e.close()
    
    except:
        p = str(x.content)
        print("Something went wrong..",'HTML data will be written in the "Error file"')

        g = open('Error.txt', "w")
        g.write(p)
        g.close()

        print('Printing out the Html Data...')
        time.sleep(1.5)
        print(p)
