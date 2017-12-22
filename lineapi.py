import requests
from flask import json


def test():
    REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
    ENTER_ACCESS_TOKEN='v3oZwFKJaEfqGTzIMf1MsCbjoiSrEVsjE9cY/wuTwsw22dTm7XHy/V4PFVpJtT5y3Q48MHqiYUxszYkucnJxcEe+0fRNpogYM+QoTNHmDSLgEqcWeLsT3RfMNkswz5AwpFZIskp8mPkpnZo67cj5LAdB04t89/1O/w1cDnyilFU='

    def post_text(reply_token, text):
        header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {" + ENTER_ACCESS_TOKEN + "}"
        }
        payload = {
            "replyToken": reply_token,
            "messages": [
                {
                    "type": "text",
                    "text": text
                }
            ]
        }
        requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))

if __name__ == '__main__':
    test()