class hashTable:
	
	def __init__(self,n):
		self.table = []
		self.tableSize = n
		for i in range (0,self.tableSize):
			self.table.append([])
	
	def printTable(self):
		comma = ", "
		for i in range (0,self.tableSize):
			print (comma.join(self.table[i]))
	
	def stringLengthHash(self, key):
		hashVal = 0;
		for i in range (0, len(key)):
			hashVal = 37 * hashVal + ord(key[i])
			print(hashVal)
		hashVal %= self.tableSize
		if hashVal < 0:
			hashVal += tableSize
		return hashVal

k = hashTable(3)
k.printTable()
print(k.stringLengthHash("i like grapes"))