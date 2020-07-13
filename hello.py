print("hello, world!")


"""This is a doc string
spanning multiple lines"""

#print("Enter your name:")
x = input("Enter Your name \n")
print("Hello, " + x)

#The for loop acts as an iterator, does not require an indexing variable
#In this example banana will not be printed because print is being skipped by the continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Simple recursion example
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)  #for variable of 5 this ends up being 5+4+3+2+1=15, then 4+3+2+1=10, etc.
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(5)
