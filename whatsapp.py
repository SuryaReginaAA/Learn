import pywhatkit

pywhatkit.sendwhatmsg("<country code><whatsapp number>","<message>",14,30) # 14 :30 => 2:30pm time should be in 24hour format


# syntax : -
# sendwhatmsg(phone_no: str, message: str, time_hour: int, time_min: int, wait_time: int = 15, tab_close: bool = False, close_time: int = 3)