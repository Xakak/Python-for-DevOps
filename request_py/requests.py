import requests
#if you want to run something just uncomment it using Ctrl +Shift + A


#if you want to post something
""" payloads={
    "name":"Rayan",
    "age": 16

}

response = requests.post("https://httpbin.org/post",data=payloads)
print(response.status_code)
res_json = response.json()
print(res_json)#you will find it in the form section
 """
#if you want to pass parameters using get method:
""" parameters = {
    "name":"Rayan",
    "age": 16
}

response = requests.get("https://httpbin.org/get",params=parameters)
res_json = response.json()
print(res_json)#you will find it in the args section """

#handling status codes
""" status_code = 200 #change it to 404 or 500 to see the difference
response =requests.get(f"https://httpbin.org/status/{status_code}")

if status_code == requests.codes.not_found:
    print("Not Found")
else:
    print(status_code)
 """

#some websites serve us differently based on the user-agent (default = python-requests/2.28.1) (found in header section) so we can manually change it:
""" headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get("https://httpbin.org/user-agent",headers=headers)
print(response.json())
 """
#getting images using request
""" headers = {
    "Accept":"image/jpeg"#select any type of image
}

response = requests.get("https://httpbin.org/image",headers=headers)
with open("image.jpg", "wb") as f:
    f.write(response.content)
 """

#using proxy server:
proxies = {
    "http":"139.99.237.62:80",#use any free proxy
    "https":"139.99.237.62:80"
}
response = requests.get("https://httpbin.org/get",proxies=proxies)
print(response.text)

