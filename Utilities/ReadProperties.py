import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password

    @staticmethod
    def getValidUsername():
        username = config.get('common info', 'valid_username')
        return username

    @staticmethod
    def getInvalidPassword():
        password = config.get('common info', 'invalid_password')
        return password

    @staticmethod
    def getInvalidUsername2():
        username = config.get('common info', 'invalid_username_2')
        return username

    @staticmethod
    def getValidPassword2():
        password = config.get('common info', 'valid_password_2')
        return password

    @staticmethod
    def getInvalidUsername3():
        username = config.get('common info', 'invalid_username_3')
        return username

    @staticmethod
    def getInvalidPassword3():
        password = config.get('common info', 'invalid_password_3')
        return password














