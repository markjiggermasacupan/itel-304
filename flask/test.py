#named indexes
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age =36)
#named indexes
txt2 = "A {0}, ate my {1}".format("dog","homework")
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John", 36)

print(txt1, txt2, txt3)
