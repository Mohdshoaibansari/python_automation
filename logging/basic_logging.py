import logging


class loger:

    def __init__(self, x, y):
        self.x=x
        self.y=y
        logging.basicConfig(level=logging.INFO)



object= logging(3,4)
# object.out()
print(object.x)


