
from authlib.client import OAuth1Session

import requests

urlprexix = method + host + port

request_token_url = 'http://192,168.37.14:8080/oauth/request_token' 
request_token = session.fetch_request_token(request_token_url)

request_token_url = '/jira/plugins/servlet/oauth/request-token'
access_token_url = '/jira/plugins/servlet/oauth/access-token'
authorize_url = '/jira/plugins/servlet/oauth/authorize'

data_url = 'http://localhost:8090/jira/rest/api/2/issue/BULK-1'

resp = requests.get('https://jira.hyperledger.org/rest/api/2/issue/CAC-1')
