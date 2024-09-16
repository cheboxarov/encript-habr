from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import hashlib


def md5_hash(data):
    # Создаем объект MD5 хэш-функции
    hash_obj = hashlib.md5()
    # Обновляем хэш-объект данными
    hash_obj.update(data.encode('utf-8'))
    # Получаем хэш в виде шестнадцатеричной строки
    return hash_obj.hexdigest()


def decrypt(encrypted_data, key):
    # Проверяем длину ключа и подгоняем до 16 байт (128 бит)
    key = key.ljust(16)[:16]  # Adjust key length to 16 bytes

    # Разделение зашифрованных данных и IV
    encoded_ciphertext, encoded_iv = encrypted_data.split(':')

    # Декодирование данных и IV из Base64
    ciphertext = base64.b64decode(encoded_ciphertext)
    iv = base64.b64decode(encoded_iv)

    # Создание объекта шифрования AES в режиме CBC
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)

    # Расшифрование данных
    padded_data = cipher.decrypt(ciphertext)

    # Удаление дополнения
    data = unpad(padded_data, AES.block_size).decode('utf-8')

    return data


# Пример использования
print(md5_hash("4.3.79")[8:-8])

# Обеспечиваем, что ключ имеет правильную длину и преобразуем его в байты
key = md5_hash("4.3.79")[8:16]  # This generates a 8-byte key
key = key.ljust(16)[:16]  # Adjust key length to 16 bytes

# Пример вызова функции decrypt
try:
    decrypted_message = decrypt(
        "hml5XUAn0gXKHKGiQqI6xh7ahwQbbJd5Ofr4Xa6R+pY1YtWFXo92e8CuMNYdoRDozpEQIjWCtsLYYtNItp373n5NYf0sAPO2wgXu5iEUa1dRDcNPJPcxUEQKuar9u1BADqMqlswRKlnGY7DIPPrsH0bjMMu10G2H8wWmCkbrnkDvkiUVhODCXDq4ULxPZwFvfqeyMhEl3Y7Hdsqbi3QVLIHVVjdBVM4jeBYomIXwQm8TV2SCviHufHRVkwf51VJFuUHyqgJ0GjwWYh/VYPjGwlpm6xh0zazBvVKNEzcrAblnHmRK0qLGnB8/pRdGZb/GTOpgdTjaRD5fs26kbSKUT4k8waCOl4EL0D4WGjEzJmH3bfKZHSH17Skq8D58OJTXgkDdwRnj4BsQVXvbBdu8bPOrveAau0xptK3+QoTV/pVXmCly7/OyLz7nyQrYqUSRKP+hTXpmHzoip+E/T02LClBUDRsavsvo94WJ7Yyxdy88/TOxjuzA2PhCtid7nYxQzM71QmEVN66EfZAc+NRqNKA/imfBMG+xZrIJ4/RztdQnwV7AD6cLZIgCivat0+JgMTrGUeSmDlygivw34btQu2iUvJxoo+2pu56JfS/aowYRSMCophRBdm4YO3oBeBUqRxagrIdMSddkD0A0zf4xwl+0MnOtGcF5deP5ERjFak5gleajwfWjFTZh3xli97KkTxiUQDRQa1pCkA5mL/OWp7pb+fn4ySZcimzH/HIy9gRuCAQsVzokp5nTJqvRVitbbm9z6LhXo1YKJDnvBme/w0JXFpFj0pBCdFkm+dlE5jZswLxaPkJW7kUZRm4b4vBLwOM1XQGZ4S5b5mwJc3mHWf1HsVOIME0b/jlnIO6mqrJPdzlvKvWjTVsDVLHMIpV7lrZzX/jc/Qp6joc7sbN6sNdzl5ihJkFlS5E2BNz8sCXlrKUxd2D181qkYnBw8nepWjbDdRvieXXtOEGxpgcTGZQn6Tak+/i9+0M85vGsE/rEqoX4RPr2fwQPJG9WlXRfmGSOGiu4pN4DOKAehcNx1FggZh/kmfsL8z7+HcoQ1N08xvNhKOMRb0iSR+BFvVWFCl0Jo/PN/8yGQOFjc1ogZ2e48dRioPSxpBOGdNa9QX4ca6ejY3pY1h3a59aie3whKkwyOA+/qSJxLg1y//mwQ19sbD9mVJHHJQQfdpqgYJB33b/xpW2i2hfsqILuXMRV5oaNv3t/M+Akp6UrzNApTdcRSJWyEKywsp9Hx19XX0jMMEWcL69ZyMLekGialsM3fYjk3cBsQr/5CChnPU+hGZiUKQggF8OCFzxlmEIPvrNsbl/Ig5jKlUREmkfH0La3OszqoU42AjL98mN8tv9KwJGFbctYbJs2clBnebGd5gru1WTAfn2seo6zEjKoIZZcjMV44jXwRkhGI6BfMNPfyof+uz04XjRxKCgwoi4aXlirj/4H8Zh/YKYlP1QFqktfUGvO8Lb7njIkH5QzD2xGh91dh7ZPJ50kjT986Sf78mmdZZWYax/JZwnGOOWnL0zR7Q3bAoefcv6gVf/Am4NibolVfuYR1l73QsWcz8WoST0EFra/ws+atIX+OI9Ohbcbbe6k4lp2G4v7rkT3+zv29ruuBKlIMnfT7zH46UVHuPTFZmOjx8lirV8Bi2Yffm14B6F90gHQX6YdmCgZjduCWoQQBR+7IhS1z4C0p0WLXr0IjUQmd6Sqbn81ZGDEeLocp9veDHDsgUj8AQVCdeaQHavGDfElW8gqo/X9fR9h3G0uLQdvEjVwagI0VP7exOO+TzB+SDZHbzxLyga9NBpCV63mD2nluxkkl/GnrtrvL+JmR6kX/OkdNyRUwFc5QPxA8iyw9jwa30ovAmHyN+lG1hqKzQHczemjFlXjmNcCVXALED28Wpn0+qjQiTMFEiQB2y0k2zUhul2cIinsjpLqq9YqSJUOMNYigz6bE3/3v1os7crToSmevJFY176D9hHZ2hrbKRyEjT/o7AXpSiSgWpT0zfllJIQeZIAZjICJeOjc41+4MjyZtz2mD7+ChE+0snH7JHRuWHznL1WB2+rXtcHEDS1QwKhVzE0tzdV7eSuZPO2Yvj9khfeMQ3SxsT+9kUTELOhv7/klBcSkwLulYOOP0QqhgpT1+W6pfWYbaj+JirSZUFF04w2UdqQOK89CiMG+YxTfKWhCDgv7YhBk5iWppLMMtiiq8eK1Jflll/8LZoiDRploXUM2Z+qM9M1Y/NiSbAWeKyhUnA0S8jdQO5PtM7SsZPqN8EsvnpYp+uSoVu0wnQAA3EynEr+qjJWWpElzp2hWB4PApCbk5gyO3Q==:y9rRwVfmGOV764zsapHBUg==",
        key
    )
    print(decrypted_message)
except ValueError as e:
    print(f"Error: {e}")
