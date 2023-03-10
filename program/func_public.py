
from pprint import pprint
from constants import RESOLUTION
from func_util import get_ISO_time
import pandas as pd 
import numpy as np
import time

# Get relevant time form ISO time from and TO 
ISO_TIMES = get_ISO_time()

pprint(ISO_TIMES)


# Construct market prices 
def construct_market_prices(client):
    pass
