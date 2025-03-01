# 1.import MyModuleFile
""" import MyModuleFile as m
print(m.n2)
#print(MyModuleFile.data) # this will give error. because data is not iporated 
# in this file so we can't access it directly. """


# 2.import MyModuleFile
"""  from MyModuleFile import add,n1,n2,n3
print(add(90,10,40,20))
print(add(n1,n2,n3)) """

# 3. Type of tree import file
"""  from MyModuleFile import *
import MyModuleFile as m
print(add(90,10,40,20)) 
print(add(n1,n2,n3))
n1=180
print(n1)
print(m.n1)  """
