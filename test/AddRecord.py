import requests

if __name__ == '__main__':
    url = "http://127.0.0.1:5000/record/withimage"

    querystring = {"title": "testing3", "description": "this%20is%20a%20testing%20example.", "phone": "12345678901",
                   "mail": "test@test.com", "source": "test"}

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"picture\"; filename=\"sun.png\"\r\nContent-Type: image/png\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"picture\"; filename=\"sun1.png\"\r\nContent-Type: image/png\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'User-Agent': "PostmanRuntime/7.19.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "78ba0677-dcaf-4f1e-97f1-e52d234cb7f2,4a2bfad3-f70e-4651-8acd-4621c7c89db7",
        'Host': "127.0.0.1:5000",
        'Content-Type': "multipart/form-data; boundary=--------------------------776591742965009802777155",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "6052619",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)
