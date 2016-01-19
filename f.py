import requests
resp = requests.get("https://www.whitehouse.gov/the-press-office/remarks-president-barack-obama-address-joint-session-congress")
print("https://www.whitehouse.gov/the-press-office/remarks-president-barack-obama-address-joint-session-congress")
print(len(resp.text))
print(resp.text.lower().count("applause"))
import requests
resp = requests.get("https://www.whitehouse.gov/the-press-office/remarks-president-state-union-address")
print("https://www.whitehouse.gov/the-press-office/remarks-president-state-union-address")
print(len(resp.text))
print(resp.text.lower().count("applause"))
import requests
resp = requests.get("https://www.whitehouse.gov/the-press-office/2011/01/25/remarks-president-state-union-address")
print("https://www.whitehouse.gov/the-press-office/2011/01/25/remarks-president-state-union-address")
print(len(resp.text))
print(resp.text.lower().count("applause"))
import requests
resp = requests.get("https://www.whitehouse.gov/the-press-office/2013/02/12/remarks-president-state-union-address")
print("https://www.whitehouse.gov/the-press-office/2013/02/12/remarks-president-state-union-address")
print(len(resp.text))
print(resp.text.lower().count("applause"))
import requests
resp = requests.get("https://www.whitehouse.gov/the-press-office/2014/01/28/president-barack-obamas-state-union-address")
print("https://www.whitehouse.gov/the-press-office/2014/01/28/president-barack-obamas-state-union-address")
print(len(resp.text))
print(resp.text.lower().count("applause"))
import requests
resp = requests.get("https://www.whitehouse.gov/the-press-office/2015/01/20/remarks-president-state-union-address-january-20-2015")
print("https://www.whitehouse.gov/the-press-office/2015/01/20/remarks-president-state-union-address-january-20-2015")
print(len(resp.text))
print(resp.text.lower().count("applause"))
import requests
resp = requests.get("https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-%E2%80%93-prepared-delivery-state-union-address")
print("https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-%E2%80%93-prepared-delivery-state-union-address")
print(len(resp.text))
print(resp.text.lower().count("applause"))