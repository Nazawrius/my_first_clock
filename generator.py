import time

src = open('my_first_clock.py', 'w')

src.write("""import time

print('Hi! This is my first clock application\\nWould you like to know current time? (y/n)')
""")

src.write("""
response = input()
local = time.localtime()
t = local[3]*3600 + local[4]*60 + local[5]

if response == 'y':""")

for i in range(86400):
	h = i//3600
	m = (i%3600)//60
	s = i%60
	src.write(f"""
	if t == {i}: print(f'Current time is {'0'*(2 - len(str(h)))+str(h)}:{'0'*(2 - len(str(m)))+str(m)}:{'0'*(2 - len(str(s)))+str(s)}')""")

src.write("""
elif response == 'n':
	print('*hanged man stickman*')
else:
	print('You speak gibberish')
""")

src.close()