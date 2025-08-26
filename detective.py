#Web page detective with python by Burak "paradass" Görez
import time
import requests
import argparse

class Detective:
    def __init__(self):
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

        self.hidden_pages = [
            # Root dizin
            "/admin",
            "/administrator",
            "/admin-panel",
            "/wp-admin",
            "/cms",
            "/manager",
            "/login",
            "/signin",
            "/user/login",
            "/account/login",
            "/auth",
            "/cpanel",
            "/controlpanel",
            "/dashboard",
            "/system",
            "/console",
            "/backup",
            "/backups",
            "/db",
            "/database",
            "/dump",
            "/test",
            "/dev",
            "/staging",
            "/sandbox",
            "/beta",
            "/config",
            "/settings",
            "/setup",
            "/install",
            "/phpmyadmin",
            # Alt dizin varyasyonları
            "/admin/login",
            "/admin/dashboard",
            "/admin/control",
            "/cms/admin",
            "/cms/login",
            "/user/admin",
            "/user/dashboard",
            "/account/admin",
            "/dev/admin",
            "/dev/login",
            "/staging/admin",
            "/staging/login",
            "/backup/admin",
            "/backup/database",
            "/system/admin",
            "/config/setup",
            "/settings/admin",
            "/install/setup",
            "/manager/login",
            "/manager/dashboard"
        ]

    def search(self):
        parser = argparse.ArgumentParser(description="Web page detective by paradass",add_help=False)
        parser.add_argument("-t","--target",type=str,required=True)
        args = parser.parse_args()
        target = args.target

        if target[-1] == "/":
            target = target[0:len(target)-1]

        print("\033[31mSearching..\033[0m")

        for page in self.hidden_pages:
            try:
                time.sleep(0.5)
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