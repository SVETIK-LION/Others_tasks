def is_palindrome(text):
    revers_text = ''.join(reversed(text))
    if text.lower() == revers_text.lower():
        return True
    else:
        return False


print(is_palindrome('ишак ищет у тещи кашИ'))
