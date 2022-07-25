import requests


payload={}
headers = {
  'cookie': '<auth_token>'
}


## Currently, calling the URL serially
for i in range(5001, 5200):
    url = "https://sumancentraluseuap-{port}-1.master.instances.azureml-test.ms".format(port=i)
    print(url)
    response = requests.request("GET", url, headers=headers, data=payload)
    print("fetched the url on port - ",i)
    # print(response.text)
