import readline

# @classmethod
def get_random_str(level=7):
	import random
	_random_str_list = 'asdfghjklqwertyuiopzxcvbnm1234567890ASDFGHJKLZXCVBNMQWERTYUIOP'
	random_str = ''
	for i in range(level):
		random_str += random.choice(_random_str_list)
	return random_str

# @classmethod
def make_rand():
	filename = "X" + get_random_str()
	make(filename)

# @classmethod
def make(filename):
	f = open(filename+".py",'w')
	for i in range(readline.get_current_history_length()):
		line = str(readline.get_history_item(i)) 
		if line == "None": continue
		f.write(line+'\n')
	f.close()
	readline.clear_history()
