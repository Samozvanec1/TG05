TOKEN = "7409932170:AAHcOW33Hdb87tHFXshCLVZZoMxalf4_JaQ"
NASA_API_KEY = "V7eG4DpH186RrBCsIruC8Tdq5CT8pbxAEalbTqR6"
THE_CAT_API_KEY = "live_6ciz59f4AMhZ1HA8Il9vcuI7Z4JDhRrEvyVo5CyWOJWXIPWHv3w7oU7ihS00bhKX"

def testing_for():
    for i in [TOKEN, NASA_API_KEY, THE_CAT_API_KEY]:
        if i == '':
            return False
    return True


if __name__ == '__main__':
   if testing_for():
       print("Все переменные настроены")
   else:
       print("Не все переменные настроены")