# class outside:
#     dove = "pigeon"
# rak = outside()
# print(rak.dove)

# class person:
#     def __init__(self, name, age):
#       self.name = name
#       self.age = age
# coke = person(23, "favour")
# print(coke.name)
# print(coke.age)

def announce(f):
  def wrapper():
      print("i am the first")
      f()
      print("i am printed because of the f")
  return wrapper
@announce
def hello():
  print("hello world")
  
hello()