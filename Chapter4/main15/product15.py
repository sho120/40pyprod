import requests
import json

slack_webhook_url="https://hooks.slack.com/services/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"

def sendSlackWebhook(strText):
    headers ={
    "Content-type":"application/json"
    }

    data = {
        "text" : strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        return "ok"
    else:
        return "error"

print(sendSlackWebhook("안녕하세요. 파이썬에서 보낸 메세지입니다."))