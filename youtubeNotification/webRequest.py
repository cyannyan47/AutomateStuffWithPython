import requests

payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)

#print(r)
print(dir(r))
#print(help(r))
# r.content returns content as bytes --> need write byte
print(r.url)
postPayload = {'username': 'minh', 'password': 'testing'}
rPost = requests.post('https://httpbin.org/post', params=postPayload)
rPost_dict = rPost.json()

print(rPost_dict['form'])
#osuDir = requests.get('https://osu.ppy.sh/users/6726134')
#print(osuDir.ok)