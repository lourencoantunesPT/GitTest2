

# args
#import sys
#print(sys.argv[0])
#print(sys.argv[1])
#print("Ola")

# mais um comentario

#exemplo apenas para a versao 1 do curso

x=1
y=2
z=x+y
print(z)


# Arrays 

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")