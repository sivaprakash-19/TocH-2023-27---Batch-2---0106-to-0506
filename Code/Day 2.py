class Node : 
    def __init__(self, data):
        self.data = data
        self.next = None


def getInput() :
    data = int(input("Enter head data : ")) 
    if data == -1 :
        return None
    head = Node(data)
    tail = head 
    while True :
        data = int(input("Enter node data : ")) 
        if data == -1 :
            return head
        node = Node(data) 
        tail.next = node 
        tail = node

def printList(head) :
    if head is None :
        return 
    print(head.data , end = "->")
    printList(head.next)

def removeNode(head, val) :
    current = head 
    prev = None 
    while current : 
        if current.data == val :
            if prev is None : 
                return head.next
            else :
                prev.next = current.next
                return head
        prev = current
        current = current.next
    return head

head = getInput()
head = removeNode(head, 20)
printList(head)
# temp = head
# while temp : 
#     print(temp.data, end = "->")
#     temp = temp.next





'''
class User :
    count = 1
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.balance = 1000
        self.accountNumber = User.count
        User.count += 1
    
    def printUser(self) :
        print("-----------")
        print("Name : ", self.name)
        print("Account Number : ", self.accountNumber)
        print("Balance : ", self.balance)
        print("-----------")

    def credit(self, amount) :
        self.balance += amount

    def debit(self, amount) :
        # Get pin of user -> 3 times 
        currentPin = int(input("Enter pin : "))
        c = 3 
        while currentPin != self.pin :
            print("Pin is incorrect! Enter pin again ", end = "")
            if(c == 0) :
                print("Limit reached! Try later!!") 
                return
            currentPin = int(input())
            c -= 1
        # Minimum balance -> 1000 
        if self.balance - amount >= 1000 :
            self.balance -= amount
        else :
            print("Insufficient balance! Try again")

u = User("Abc", 8021) 
u.printUser() 
u.credit(1000)
u.debit(500)
u.printUser()
# u1 = User("Def", 7992)
# u1.printUser()

'''

'''
def factorial(n) : 
    if n == 1 :
        return n
    smallAns = factorial(n - 1) 
    return n * smallAns

print(factorial(4))
'''