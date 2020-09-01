from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.chrome.options import Options
import codecs
import datetime, time

# Ref https://tools.ietf.org/html/rfc6238

# Use this this secret
accountSecret = "AAAAAAAAAAAAAAAAAAAAAAAA"

try:
    import pyotp

    print( "Secret: {}".format(accountSecret))

    # Generate Timebase OTP based on accountSecret
    totp = pyotp.TOTP( accountSecret )
    token = totp.now()
    print( "Python pyotp: {}".format(token))
except Exception as e:
    print( "PYOTP-1 Exception {}".format(e))

try:
    import hmac, base64, struct, hashlib, time

    def getHOTPtoken(secret, intervalsNo):
        h = hmac.new(base64.b32decode(secret, True),
                        struct.pack(">Q", intervalsNo),
                        hashlib.sha1).digest()
        o = h[19] & 15
        return (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000

    def getTOTPtoken(secret):
        return getHOTPtoken(secret, intervalsNo=int(time.time())//30)

    token = getTOTPtoken(accountSecret)
    print( "TOTP-3: {}".format(token))
except Exception as e:
    print( "PYOTP-2 Exception {}".format(e))

print("Complete")
