class CustomException(Exception):

    def __init__(self, log):
        super().__init__(log)

        with open('log.txt', 'a') as f:
           f.write(log + '\n')


raise CustomException("Something's wrong")

