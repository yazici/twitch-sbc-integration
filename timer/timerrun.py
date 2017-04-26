import ConfigParser
import importlib
import time
import json

def timer_handler(q_timer):

    time_to_sleep = 60*5
    messageIndex = 0 

    while True:
        with open ("timer/messages.json", 'r') as f:
            messages = json.load(f)

        queueEvent = { 
                'eventType': 'chat',
                'event'    : messages[messageIndex]
        }

        messageIndex += 1
        if messageIndex == len(messages): messageIndex = 0
        q_timer.put(queueEvent)
        time.sleep(time_to_sleep)
