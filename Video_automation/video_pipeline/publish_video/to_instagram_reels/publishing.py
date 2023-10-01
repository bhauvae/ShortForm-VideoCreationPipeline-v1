import requests
import config
LONG_TOKEN="EAAU3L6HCOj4BO4Tnq5LFhin7f2MMrsJthykmUAbHwzwwrfvosh5adXdZA69PZCExBAij4lhKkoznZCaKZAi3sU8lvnSEh89dZARQvZCPnGQKznUkpFDHmjhRAxXMDgQeR9VpiRp0W30CJfhgS8dc6pP1iK9F2oh4XVYUN320nCbrzKeGGTXZAoCyeOzPCU3jZC2C"
graph_url = 'https://graph.facebook.com/v17.0/'
def post_reel(instagram_account_id,caption='test', media_type ='REELS',share_to_feed='true',thumb_offset='1',video_url='./final.mp4',access_token = LONG_TOKEN):
    url = graph_url + instagram_account_id + '/media'
    param = dict()
    param['access_token'] = access_token
    param['caption'] = caption
    param['media_type'] = media_type
    param['share_to_feed'] = share_to_feed
    param['thumb_offset'] = thumb_offset
    param['video_url'] = video_url
    response =  requests.post(url,params = param)
    print("\n response",response.content)
    response =response.json()
    return response

def status_of_upload(ig_container_id = '',access_token=''):
    url = graph_url + ig_container_id
    param = {}
    param['access_token'] = access_token
    param['fields'] = 'status_code'
    response = requests.get(url,params=param)
    response = response.json()
    return response

def publish_container(creation_id = '',access_token = '',instagram_account_id=''):
    url = graph_url + instagram_account_id + '/media_publish'
    param = dict()
    param['access_token'] = access_token
    param['creation_id'] = creation_id
    response = requests.post(url,params=param)
    response = response.json()
    return response


print(post_reel(instagram_account_id='17841461748508512'))

