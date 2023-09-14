class AccountHolder:
    def __init__(self):
        pass

    def getData(self):
        self.acc_number=input("Enter the Account Number : ")
        self.name=input("Enter the name : ")
        self.balance=float(input("Enter the balance : "))
        self.acc_type=input("Enter the Account type : ")

    def calculate(self):
        rate_of_interest=float(input("Enter the Rate of interest : "))
        interest= self.balance*rate_of_interest/100
        print("Interest on account balance :",interest)

# acc1=AccountHolder()
# acc1.getData()
# acc1.calculate()


    def remove_comments(line,sep="#"):
        for s in sep:
            i= line.find(s)
            if i>=0:
                line=line[:i]
            return line.rstrip()
    filename=input("Enter the name of file")
    remove_comments(filename)
    with open(filename,"r") as f:
        lines=f.readlines()
    with open(filename,"w") as f:
        for line in lines:
            f.write(remove_comments(line))
            
