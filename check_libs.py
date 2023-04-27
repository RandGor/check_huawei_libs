import requests
import threading

def getLink(ver):
    return 'https://developer.huawei.com/repo/com/huawei/ohos/hap/'+ver+'/hap-'+ver+'.pom'
    
def check_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(url)

threads = []
for i in range(2000,4000):
    a = str(i).zfill(4)
    url = getLink(a[0]+'.'+a[1]+'.'+a[2]+'.'+a[3])

    thread = threading.Thread(target=check_response, args=(url,))
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()
    
input("END")