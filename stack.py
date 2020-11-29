print("Thanita")

stack = []

def insert(*num):
  for i in num:
   stack.insert(0, i)


def pop():
 del stack[0]


def peep():
 print(stack[0])


def length():
 len(stack)


def all_elem():
  print(stack)


insert(1,2,3,4,5,6,7,8,9,10)
all_elem()




