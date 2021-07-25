class PhoneNumber:
    def __init__(self, number):
        self.areacode = number[1:4]
        self.exchange = number[6:9]
        self.line = number[10:14]

    def __str__(self):
        return "(%s) %s-%s" % \
                (self.areacode, self.exchange, self.line)

    def test():
        newnumber = input("Enter phone number : ")
        phone = PhoneNumber(newnumber)
        print("The phone number is: ", phone)

    if __name__ == "__main__":
        test()




