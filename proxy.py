import requests
import concurrent.futures


class Proxy(object):

    def __init__(self, url: str, input_path: str, output_path: str):
        self.__url = url
        self.input_path = input_path
        self.output_path = output_path

        self.__timeout = 3
        self.format_url()
    
    def format_url(self):
        self.__url = self.__url.replace("https", "http")
    
    def change_url(self, new_url: str):
        self.__url = new_url
        self.format_url()

    def test_proxy(self, proxy: str):
        proxies = {
            "http": proxy
        }

        try:
            r = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=self.__timeout)
        except requests.RequestException:
            return False
        
        if r.status_code == 200:
            try:
                if r.json()["origin"] == proxy.split(":")[0]:
                    try:
                        r = requests.get(self.__url, proxies=proxies, timeout=self.__timeout)
                    except requests.RequestException as e:
                        return False
                    
                    if r.status_code == 200:
                        return True
            except Exception:
                return False
        
        return False
    
    def get_valid_proxies(self) -> None:
        with open(self.input_path, "r") as f:
            proxies = f.read().splitlines()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            function = lambda proxy : proxy if self.test_proxy(proxy) else None
            good_proxies = executor.map(function, proxies)

        with open(self.output_path, "w") as f:
            for proxy in good_proxies:
                if proxy is None:
                    continue
                else:
                    f.write(proxy + "\n")
