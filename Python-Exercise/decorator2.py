def setBold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def setItalic(func):
    def wrapper():
        return '<i>' + func() + '</i>'
    return wrapper

def setUnderline(func):
    def wrapper():
        return '<u>' + func() + '</u>'
    return wrapper

def tag():
    return 'Hello world!'

print (setBold(setItalic(setUnderline(tag)))()) 
