# Copy from Kalle Hallden
# Source from here: https://www.youtube.com/watch?v=qbW6FRbaSl0

import urllib.request, json
import smtplib
from selenium import webdriver
import time

def look_for_new_video():
  api_key = "AIzaSyDT1OLEPTv8IduWHo9hJsEf1Cokx-Bv8U0"
  channel_id = "UCqqJQ_cXSat0KIAVfIfKkVA" #J Kenji Lopez-Alt"

  base_video_url = 'https://www.youtube.com/watch?v='
  base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

  url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key, channel_id)
  #print(url)
  inp = urllib.request.urlopen(url)
  #print(inp)
  response = json.load(inp) 
  #print(response)
  #print('\n')

  vidID = response['items'][0]['id']['videoId'] # the videoID is located at this place
  #print(vidID) 
  
  conn = smtplib.SMTP('smtp.gmail.com', 587)
  conn.ehlo()
  conn.starttls()
  conn.login('saucyDevTest@gmail.com', 'jnfycnozbewpnhhn')

  video_exists = False
  with open('videoid.json', 'r') as json_file:
    try: 
      data = json.load(json_file)
    except json.decoder.JSONDecodeError:
      with open('videoid.json', 'w') as json_file:
        data = {'videoId' : vidID}
        json.dump(data, json_file)

      mailContent = 'Subject: New video from ...\n\nCheck out new video from ' +base_video_url+vidID+'\n\nSaucyDev'
      conn.sendmail('saucyDevTest+youtubeNotification@gmail.com', 'saucyDevTest@gmail.com', mailContent)
      video_exists = True

    if data['videoId'] != vidID:
      # this will prompt WSL's firefox (not working)
      # driver = webdriver.Firefox()
      # driver.get(base_video_url + vidID)
      #TODO: find how to automate sending email
      # Send email here
      mailContent = 'Subject: New video from ...\n\nCheck out new video from ' +base_video_url+vidID+'\n\nSaucyDev'
      conn.sendmail('saucyDevTest+youtubeNotification@gmail.com', 'saucyDevTest@gmail.com', mailContent)
      video_exists = True

  if video_exists:
    with open('videoid.json', 'w') as json_file:
      data = {'videoId' : vidID}
      json.dump(data, json_file)

try:
  while True:
    look_for_new_video()
    time.sleep(60)
except KeyboardInterrupt:
  print('Stopping video notification service')