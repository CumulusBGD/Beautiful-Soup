import time
import requests

class check_link():
    def __init__(self, address):
        self.address = address

    def check(self):
        try:
            status_code = -100
            time.sleep(2)
            response = requests.get(self.address)
            status_code = response.status_code
            if status_code in [400, 404, 403, 408, 409, 501, 502, 503]:
                print(str(status_code) + "-" + response.reason + "-->" + self.address)
            else:
                print("no problem in-->" + self.address)

        except Exception as e:
            print("SIMA {} {}-{}".format(status_code, e, self.address))
            pass

url="https://www.blic.rs//"
cl=check_link(url)
cl.check()