#!/usr/bin/python -tt


# class myClass:
#     "a simple example class"
#     i = 12345
#     def f(self):
#         return 'hello world'

# x = myClass()

# print x.i
# print x.f()

# ==========

# sample_list = list('sachin')
# print sample_list

# f = open('namu','w')
# # f.write('\n'.join(sample_list))

# for item in sample_list:
#     f.write("%s\n" % item)

f = open('examples.txt','r')    
for line in f.readlines():
    print line

f.close()
