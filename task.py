# Counters in python 
from collections import Counter
a = "Ali" , "Ahmad" , "Asad" , "Ahmad" , "Akram" , "Ali"
my_counter = Counter(a)
print(my_counter)


# OrderedDict
from collections import OrderedDict
ordered_dict = {}
ordered_dict["c"] = 3
ordered_dict["b"] = 2
ordered_dict["a"] = 1
ordered_dict["d"] = 4
print(ordered_dict)


# Defaultdict in python
from collections import defaultdict
d = {}
d["a"] = 1
d["b"] =2
print(d["a"]) # if we put here another key like as c it show keyError.

# ChainMap in python 
from collections import ChainMap
d1 = {"a": 1}
d2 = {"b": 2}
chain = ChainMap(d2 , d1)
print(list(chain.keys()))
print(list(chain.values()))


# NamedTuple in python
from collections import namedtuple
Point = namedtuple("Point", "x,y")
a = Point(1, -2)
print(a.x , a.y)


# DeQue in python 
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(1)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)
d.extend([4,5,6])
print(d)
d.rotate(1)
print(d)



# Heap in python 
import heapq
lst = [2,5,8,9]
heapq.heapify(lst)
print("Original Heap is :" , list(lst))
heapq.heappush(lst,4)
print("After heap pushing : " , list(lst))


# Collections.UserDict in python 
from collections import UserDict
class custdict(UserDict):
    def pop(self, s=None):
        return False
mydict = custdict({"a":4, "b":6})
mydict.pop("b")     
print(mydict)


# Collections.UserList
from collections import UserList
class MyList(UserList):
    def pop(self,s=None):
       return False
L = MyList ([2,4,3,1])
print(L)


# Collections.UserString
from collections import UserString
class Mystr(UserString):
    def Lower(self,s=None):
        return False
s = Mystr("hello !")
print(s.capitalize())
print(s.upper())
