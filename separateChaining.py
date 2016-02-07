class hashTable:
	
	def __init__(self,n):
		self.table = []
		self.tableSize = n
		for i in range (0,self.tableSize):
			self.table.append([])
	
	def printTable(self):
		print ("hashTable of size ", self.tableSize)
		comma = ", "
		for i in range (0,self.tableSize):
			print(i,": ", end = '')
			print (comma.join(self.table[i]))
	
	def stringLengthHash(self,key):
		hashVal = 0;
		for i in range (0, len(key)):
			hashVal = 37 * hashVal + ord(key[i])
		hashVal %= self.tableSize
		if hashVal < 0:
			hashVal += tableSize
		return hashVal

	def addToTable(self,key,hashFunc):
		hashed = hashFunc(self,key);
		if key not in self.table[hashed]:
			self.table[hashed].append(key);

k = hashTable(13)
k.addToTable("tyralyn", hashTable.stringLengthHash)
k.addToTable("tyralyn", hashTable.stringLengthHash)
k.addToTable("fuzz", hashTable.stringLengthHash)
k.addToTable("chandler", hashTable.stringLengthHash)
k.printTable()
