# collections :: counter, namedtuple OrderedDict, DefaultDict, deque

from collections import Counter, namedtuple, OrderedDict

# Counter
a = "Test String aaaaaaaaabbbbbbbbbcccccccccddddddddd"
my_counter = Counter(a)

# most common x element into list of tuples
print(my_counter.most_common(2))

# namedtuple
point = namedtuple("point", "x,y")
pt = point(1, -4)
print(pt)
print("x = ", pt.x)
print("y = ", pt.y)

# namedtuple
point = namedtuple("point", "x,y")
pt = point(1, -4)
print(pt)
print("x = ", pt.x)
print("y = ", pt.y)

# OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1

print(ordered_dict)

# OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1

print(ordered_dict)