import requests
from info import CLIENT_ID,CLIENT_SECRET,SHORT_TOKEN
client_id = CLIENT_ID
client_secret = CLIENT_SECRET
redirect_url = 'your_redirect_url'
access_url = 'https://www.facebook.com/v13.0/dialog/oauth?response_type=token&display=popup&client_id=your_client_id&redirect_uri=your_redirect_uri&auth_type=rerequest&scope=user_location%2Cuser_photos%2Cuser_friends%2Cuser_gender%2Cpages_show_list%2Cinstagram_basic%2Cinstagram_manage_comments%2Cinstagram_manage_insights%2Cpages_read_engagement%2Cpublic_profile'
graph_url = 'https://graph.facebook.com/v15.0/'

def func_get_url():
    print('\n access code url',access_url)
    code = input("\n enter the url")
    code = code.rsplit('access_token=')[1]
    code = code.rsplit('&data_access_expiration')[0]
    return code

def func_get_long_lived_access_token(access_token = ''):
    url = graph_url + 'oauth/access_token'
    param = dict()
    param['grant_type'] = 'fb_exchange_token'
    param['client_id'] = client_id
    param['client_secret'] = client_secret
    param['fb_exchange_token'] = access_token
    response = requests.get(url = url,params=param)
    print("\n response",response)
    response =response.json()
    print("\n response",response)
    long_lived_access_tokken = response['access_token']
    return long_lived_access_tokken
  
access_code = SHORT_TOKEN
long_lived_access_token = func_get_long_lived_access_token(access_token=access_code)
print(long_lived_access_token)