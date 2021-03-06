import ConfigParser
import Adafruit_BBIO.GPIO as GPIO
import importlib
import time

def gpio_handler(q_gpio):
    '''
    SETUP GPIO HERE
    '''
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')

    gpioOutSetup = Config.get('GPIO', 'out').split(',')
    gpioInSetup = Config.get('GPIO', 'in').split(',')

    for setup in gpioOutSetup:
        GPIO.setup(setup, GPIO.OUT)

    for setup in gpioInSetup:
        GPIO.setup(setup, GPIO.IN)
        
    while True:
        '''
        CHECK q_gpio for messages, execute messages accordingly
        '''
        if not q_gpio.empty()
            q_gpio_check = q_gpio.get()

            if q_gpio_check ['eventType'] == "electrical":
                queueEvent = q_gpio_check['event'].split(' ')
                queueHead = queueEvent[0]
                queueArgs = list(queueEvent)
                queueArgs.remove(queueHead) 
                print(queueHead)

                module = importlib.import_module(
                        'electrical.reactions.%s' % queueHead
                        )
                gpioFunc = getattr(module, "react_chat_%s" % queueHead)
                gpioFunc(queueArgs, GPIO)
            else:
                q_gpio.put(q_gpio_check)
                time.sleep(0.25)
