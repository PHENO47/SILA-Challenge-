import random
import time
from fake_useragent import UserAgent

ua = UserAgent()

def random_user_agent():
    return ua.random

def random_delay(a=2, b=5):
    time.sleep(random.uniform(a, b))