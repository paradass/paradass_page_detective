#Web page detective with python by Burak "paradass" Görez
import time
import requests
import argparse

class Detective:
    def __init__(self):
        self.hidden_pages = []

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/117.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;"
            "q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }

    def search(self):
        parser = argparse.ArgumentParser(description="Web page detective by paradass",add_help=False)
        parser.add_argument("-t","--target",type=str,required=True)
        parser.add_argument("-w","--wordlist",type=str,required=False,default="wordlist.txt")
        args = parser.parse_args()
        target = args.target
        wl = args.wordlist
        
        if target[-1] == "/":
            target = target[0:len(target)-1]

        try:
            file = open(wl,"r")
            print("\033[31mSearching..\033[0m")
        except:
            print("\033[31mWordlist file error!\033[0m")
            return
    
        for page in file.readlines():
            try:
                time.sleep(0.5)
                page = page.replace("\n","")
                for i in range(2):
                    if i == 1:
                        page += "/"
                    response = requests.get(target+page,timeout=1,headers=self.headers)
                    if response.status_code == 200:
                        print(f"\033[32m{target+page}\033[0m")
                    else:
                        print(target+page)
            except:
                pass

detective = Detective()
detective.search()