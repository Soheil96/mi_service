from .models import Warranty, Message


def num_to_letter(num):
    result = ""
    while num:
        digit = num % 10
        num = int(num / 10)
        result += chr(ord('A') + int(digit))
    return result


def get_warranty_number(month):
    mod = 1000000007
    prime = 1205123
    cnt = Warranty.objects.count() + 1
    code = cnt * prime % mod
    while code < 1000000000:
        code *= 10
    SN = chr(ord('A') + int(month)) + str(code) + num_to_letter(code)
    return SN
