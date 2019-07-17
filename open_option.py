# File Objects

# 'r' is for review or reading
# 'w' write
# 'a' appends
# 'r+' read and write
f = open('test.txt', 'r')

print(f.mode)

# when using open you must close
f.close()
