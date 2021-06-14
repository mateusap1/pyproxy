# pyproxy
A really simple module to help me filter working proxies

# Usage
If you want to integrate pyproxy with an existing project, you can  follow this simple steps:

* Import the Proxy module
```python3
import Proxy from proxy
```

* Create an object with it's necessary paramaters
```python3
url = "https://www.amazon.com/" # The website you want to test the proxies in
input_path = "./input.txt" # The file that contains a list of proxies you want to test
output_path = "./output.txt" # The file that will contain the working proxies

proxy = Proxy(url, input_path, output_path)
```

* Call the "get_valid_proxies" method
```python3
proxy.get_valid_proxies()
```
