## Functional Programming, part 1:
# "C:\Users\Zhixiong Cheng\Desktop\complete_python_bootcamp\cheat sheet file"
def SumOfSquares(x, y):
	''' Compute its sum of square of all of its arguments '''
	twoTimes = x ** 2 + y ** 2
	return twoTimes # Here is our first comment!!

# Example 2: when taking strings as argument:
def mystery(first, second):
	mysteryString = first[1:] + second[1:]
	return mysteryString
#print(mystery('Hello', 'World'))

# Example 3: Collatz Problem:
def collatz(n):
	''' Takes a single number as argument and applies Collatz to it'''
	if n % 2 == 0:
		return n / 2
	return 3 * n + 1

print(collatz(3))

# Example 4: Match first function:
def matchFirst( s1, s2):
	'''Compare the first characters in s1 and s2
	and return True if they are the same,
	False if not'''
	if len(s1) == 0 or len(s2) == 0:
		return False
	return s1[0] == s2[0]

print(matchFirst('spam', 'super'))
print(matchFirst('AAGC', 'GAG'))
print(matchFirst('', 'like'))

# Example 5: Solve edit distance problem in simple case: 
def SimpleDistance(s1, s2):
	'''Takes two strings as arguments and return the edit
	distance between them if one of them is empty.
	Otherwise it returns an error string.'''
	if len(s1) == 0:
		return len(s2)
	elif len(s2) == 0:
		return len(s1)
	else:
		return "Help! We don't know what to do here!"

# Example 6: Solve edit distance problem in another case:
def distance(s1, s2):
	''' Returns the distance between twp strings,
	each of which is of length 4 '''
	EditDist = 0
	if s1[0] != s2[0]:
		EditDist = EditDist + 1
	if s1[1] != s2[1]:
		EditDist = EditDist + 1
	if s1[2] != s2[2]:
		EditDist = EditDist + 1
	if s1[3] != s2[3]:
		EditDist = EditDist + 1
	return EditDist

print(distance('spam', 'psam'))

# Example 7: recursion --- Factorial question:
def factorial_if(n):
	s = n 
	if n > 1:
		while n > 1:
			s = s * (n - 1)
			n = n - 1
		return s
	else:
		return 1

def factorial_rec(n):
	''' Recursive function for computing
	the factorial of n '''
	if n <= 1: # The base case
		return 1
	else:
		result = n * factorial_rec(n-1)
		return result

print(factorial_rec(4))

# Example 8: Solve Edit Distance problem in more complicated case:
def SimpleDistance_8(s1, s2):
	''' Takes two strings of the same length and returns the 
		numbers of positions in which differ.'''
	if len(s1) == 0 and len(s2) == 0:
		return 0 # base case
	else:
		if s1[0] == s2[0]: # recursive step, case 1
			distance = SimpleDistance_8(s1[1:], s2[1:])
		else: # step 2
			distance = 1 + SimpleDistance_8(s1[1:], s2[1:])
		return distance

print(SimpleDistance_8('satddd', 'sprlll'))

# Example 9: Reverse a String:
def reverse(string):
	''' Takes the string as an argument and returns
		its reversal.'''
	if len(string) == 0: # base case: is the string empty
		return ''
	else:
		FirstSymbol = reverse(string[1:]) + string[0] # hold on to the first sympol 
		return FirstSymbol

print(reverse('maps'))

# Example 10: Suitcase problem:
	## by using two recursion calls. Use it or Lost strategy.
def subset(capacity, items):
	''' Takes two arguments: a number representing the suitcase
		capacity and a list of positive numbers representing
		the weights of the items. The function return the 
		largest total weight of items that could be chosen
		withouth exceeding the suitcase capacity'''
	if capacity <= 0 or items == []:
		return 0
	elif items[0] > capacity:
		return subset(capacity, items[1:])
	else:
		lostIT = subset(capacity, items[1:])
		useIT = items[0] + subset(capacity-items[0], items[1:])
		return max(lostIT, useIT)

print(subset(42, [5, 10, 18, 23, 30, 45]))

# Biggest Example: Edit Distance between two Strings
def min_distance(first, second):
	''' Returns the edit distance between first and second. 
		first String -> second String. '''
	if first == '':
		return len(second) # base case 1
	elif second == '':
		return len(first) # base case 2
	elif first[0] == second[0]:
		return min_distance(first[1:], second[1:])
	else:
		substitution = 1 + min_distance(first[1:], second[1:])
		deletion = 1 + min_distance(first[1:], second)
		insertion = 1 + min_distance(first, second[1:])
		return min(substitution, deletion, insertion)

print(min_distance('alien', 'sales'))

## Functional Programming, Part 2:
# Example 1: determine a prime number or not using lambda func or list comprehension.
def divisors(n, low, high):
	''' Returns True if n has a divisor in the range from 
		low to high, otherwise returns False. '''
	if low > high:
		return False
	elif n % low == 0: # is n divisible by low?
		return True
	else:
		return divisors(n, low + 1, high)

#print(divisors(35, 2, 4))
	## we can test if n is prime by checking its divisors
def isPrime(n):
	''' For any n greater than or equal to 2,
		Returns True if n is prime. False if not. '''
	if divisors(n, 2, n-1):
		return False
	else:
		return True

# print(isPrime(35))
	## we can do this even more elegantly this way:
def isPrime(n):
	''' For any n greater than or equal to 2,
		Returns True if n is prime. False if not. '''
	return not divisors(n, 2, n-1)
	## to generate lists of primes, e.g. 2 to 100 --- slow: n^2
def listPrimes(n, limit):
	''' Returns all primes between n and limit. '''
	if n == limit:
		return []
	elif not isPrime(n):
		return [] + listPrimes(n+1, limit)
	else:
		return [n] + listPrimes(n+1, limit)

#print(listPrimes(2,100))
	## faster way: sieve of Eratosthenes

	## first need a filter function
def isNotDivisibleBy2(n):
	''' Returns True if n is not divisible by 2,
		else returns False. '''
	return not n % 2 == 0		

filter(isNotDivisibleBy2, range(3, 10))

	## the funcion above is same as Lambda function:
filter(lambda n: n % 2 != 0, range(3, 10))

	## import sys to allow too many recursions:
import sys
sys.setrecursionlimit(20000) # Allow 20000 levels of recursion.
	## define sift by using anonymous function:
def sift(toremove, numlist):
	''' Takes a number, toremove, and a list of numbers, numlist.
	Returns the list of these numbers in numlist that are not
	multiples of toremove. '''

	return filter(lambda n: n % toremove != 0, numlist)
	## We can also using sift by list-comprehension syntax:
def sift(toremove, numlist):
	return [x for x in numlist if x % toremove != 0]


def primeSieve(numberList):
	''' Returns the primes in numlist using a prime sieve algorithm.'''
	if numberList == []: # Base case
		return []
	else:
		prime = numberList[0] # The first element is prime!
		return [prime] + primeSieve(sift(prime, numberList[1:]))

print(primeSieve(range(2, 101)))

# Example 2: Mapping： functions take list as argment and 
	# return a new list in which some function is applied to 
	# every element in that list.

	## First: create a increasement list function:
def incrementList(numberList):
	''' Takses a list of numbers as an argument and returns
		a new list with each number incremented by one. '''
	if numberList == []:
		return []
	else:
		FirstNum = numberList[0] + 1 # increment 1st element
		# next increment the remaining list
		return [FirstNum] + incrementList(numberList[1:])

print(incrementList([10, 20, 30]))

	## Second: define increment and triple function, and map it:
def increment(x):
	''' Takes a number x as an argument and increment it by one. '''
	return x + 1

def triple(x):
	''' Takes a number x as an argument and triple it. '''
	return x * 3

print map(increment, [10, 20, 30])
[x + 1 for x in [10, 20 ,30]]
print map(triple, range(1,5))
[x * 3 for x in range(1, 5)]

[x ** 2 for x in range(1, 11) if x % 2 == 0]

# Example 3: Reduce: can reduce all elements in list to a single element
	## First define add function and multiply function
def add(x, y):
	''' Returns the sum of the two arguments. '''
	return x + y

def multiply(x, y):
	''' Takes two numbers and returns their product. '''
	return x * y

	## Second import functools and use reduce
from functools import * # this is only for Python 3
print reduce(add, range(1,5))
print reduce(multiply, range(1,5)) 
	## RMK: reduce takes the first 2 element from list to apply func
	## to reduce them to one element, then take that result and
	## the next element from the list and apply the func to reduce...

# Example 4: MapReduce
	## First write a function that is the composition of Map and Reduce
def add(x, y):
	''' Returns the sum of two arguments. '''
	return x + y
def multiply(x):
	''' Takes a number x as an argument and triple it. '''
	return x * 3
def mapReduce(mapfunction, reducefunction, numberList):
	''' Applies mapFunction to numberlist to construct a new list
	and then applies reduceFunction to the new list
	and returns that value.'''
	return reduce(reducefunction, map(mapfunction, numberList))
print mapReduce(multiply, add, [1,2,3,4]) 

# Example 5: Function as Result
	## First: scale function
def scale(n):
	return lambda x: x * n
f = scale(42) # f is a lambda function: lambda x: x * 42
print f(4)

def scale(n):
	def multiple(x):
		return n * x
	return multiple
	
# Example 6: Derivative Function:
def derivative(f, h):
	''' Returns a new function that is the approximation of 
	the derivative of f with respect to h. '''
	return lambda x: (f(x + h) - f(x)) / h
def square(x):
	return x ** 2

g = derivative(square, 0.0001) # get first derivative when x = 10
print g(10)
h = derivative(g, 0.0001) # get the second derivative when x = 10
print h(10)
	
	## create a function to get k-th derivatives:
def kthderivative(f, h, k):
	''' Returns a new function that is approximation of
	the k-th derivative of f with respect to h. '''
	if k == 1:
		return lambda x: (f(x + h) - f(x)) / h
	else:
		temp_func = kthderivative(f, h, k-1)
		return lambda x: (temp_func(x + h) - temp_func(x)) / h
g = kthderivative(square, 0.0001, 4)
print g(10)

# Biggest Example: RSA Cryptography
	## our object to create 'makeEncoderDecode()' function
	## it takes no arguments, constructs the RSA encryption and decryption keys
	## and returns two functions:
	## first function encryts data using the encryption key
	## seond decrypts encrypted data using decryption key

	## first create inverse function
from functools import *
def inverse(e, m):
	''' Returns the inverse of e mod m. '''
	return filter(lambda d: e*d % m == 1, range(1, m))[0]

	## last create makeEncoderDecoder function:
import random
def makeEncoderDecoder():
	''' Returns two functions: An RSA encryption function
		and an RSA decryption function. '''
	# choose 2 primes:
	p, q = random.sample(primeSieve(range(2, 10)), 2)
	n = p*q # compute n
	m = (p-1) * (q-1) # compute m
	print "Maximum number that can be encrypted is %d", %(n-1)

	# choose a random prime for e:
	e = random.choice(primeSeive(2, m))
	if m % e == 0: # if e divides m, it won't work!!
		print "Please try again"
	else:
		d = inverse(e, m) # compute d
		encoder = lambda x: (x**e) % n # encryption function
		decoder = lambda y: (y**d) % n # decryption function
		return [encoder, decoder]

# Chapter 5: Imperative Programming:
# 5.2 Get input from user:
def greeting():
	name = raw_input('What\'s your name?\n')
	print 'Nice to meet you, %s' %(name)

def plus42():
	''' takse user's input string and convert it into floating num.'''
	number = float(raw_input('Enter a number\n'))
	nplus42 = number + 42
	print number, ' + 42 = ', nplus42

# 5.3 Repeated Tasks - Loops:
artists = []
## users will enter 3 artists:
for i in range(3):
	next_artist = raw_input('Enter an artist: ')
	artists.append(next_artist)
print "Thank you! We'll work on your recommendations now. "

def factorial(n):
	''' iteration version of factorial. '''
	answerSoFar = 1
	for i in range(1, n + 1):
		answerSoFar = answerSoFar * i
	return answerSoFar

def listDoubler(aList):
	''' Returns a new list in which each element is double 
		the value of elements in the input list. '''
	doubledList = []
	for elem in aList:
		doubledList.append(elem * 2)
	return doubledList

def numMatches(userPrefs, storedUserPrefs):
	''' Returns the number of elements that match between
		the lists userPrefs and storedUserPrefs. '''
	count = 0
	for i in userPrefs:
		if i in storedUserPrefs:
			count += 1
	return count

userPrefs = ['Maroon 5', 'Lady Gaga', 'Justin Bieber']
storedUserPrefs = ['Maroon 5', 'Kelly Clarkson', 'Lady Gaga', 'Bruno Mars']

## Find the user with the best match with current user:
def findBestUser(userPrefs, allUserPrefs):
	''' Given a list of user artist preferences and a 
		list of lists representing all stored users'
		preferences, return the index of the stored
		users with the most matches to the current user. '''
	max_matches = 0
	best_index = []
	for user in allUserPrefs:
		if numMatches(userPrefs, user) > max_matches:
			max_matches = numMatches(userPrefs, user)
			best_index = allUserPrefs.index(user)
	return max_matches, best_index

allUserPrefs = [['Lady Gaga', 'Adele', 'Kelly Clarkson', 'The Dixie Chicks', 'Lady Antebellum'],
['Kelly Clarkson', 'Lady Gaga', 'Katy Perry', 'Justin Bieber', 'Lady Antebellum'],
['The Beatles', 'Maroon 5', 'Eli Young Band', 'Scotty McCreery'],
['Adele', 'Maroon 5', 'Katy Perry', 'Bruno Mars']]
userPrefs = ['Maroon 5', 'The Rolling Stones', 'The Beatles']

## while loop for infinite input of artist:
prefs = []
newPref = raw_input('''Please enter the name of an
	artist or band that you like: ''')
while newPref != '':
	prefs.append(newPref)
	newPref = raw_input("""Please enter an artist or band
that you like, or just press enter to see recommendations: """)
	## another way:
prefs = []
while True:
	newPref = raw_input("Please enter an artist or band\
that you like, or just press enter to see recommendations: ")
	if newPref:
	prefs.append(newPref)
	else:
		break
print prefs

## compare iteration and recursion:
# first iteration:
counter = 0
while counter < 10000:
	counter += 1
# Then is recursion:
def increment(value, times):
	if times <= 0:
		return value
	return increment(value + 1, times - 1)
counter = increment(0, 100)

# 5.4. References and Mutable vs. Immutable Data:
x = 43
id(x)
list1 = [x]
list2 = list1
id(list1)
id(list2) # their address are the same
id(list1[0]) # its address are same as x's
## reference sequesnce: list1 -> [x] -> x
## so when we change list[0]:
list1[0] = 42
list2[0] # this value will changed, too
id[list1]
id[list2]
## strings are immutable different from lists:
s = 'immutable' 
## there will be errors for s[0] = ' '; can only change the whole thing.

# 5.5: Mutable Data + Iteration: Sorting out Artists.
## First need to sort the list: a Simple Sorting Algorithm:
prefs = []
while True:
	newPref = raw_input('Please enter an artist or band\
that you like, or just press enter to see recommendations: ')
	if newPref:
		prefs.append(newPref)
	else:
		break
print '\nThanks for your input!'
### We need to keep format of all input: no leading white space and Title case:
standardPreds = []
for artist in prefs:
	standardPreds.append(artist.strip().title())
### Algorithm: selecting sort -- repeat selecting min remaining element and move it to next position.
def index_of_min(aList, starting_index = 0):
	newList = aList[starting_index:]
	return newList.index(min(newList)) + starting_index
#### Professor's version:
def index_of_min(aList, starting_index):
	min_elem_index = starting_index
	for i in range(len(aList)):
		if aList[min_elem_index] > aList[i]:
			min_elem_index = i
	return min_elem_index
def swap(aList, i, j):
	temp = aList[i]
	aList[i] = aList[j]
	aList[j] = temp
def selectionSort(ListToSort):
	for i in range(len(ListToSort)-1):
		index = index_of_min(ListToSort, i)
		swap(ListToSort, i, index)
	return ListToSort
### Example: list = ['Maroon 5', 'Adele', 'Lady Gaga']
## find matches between two sorted lists:
def numMatches(list1, list2):
	''' Returns the number of elements that match between two sorted list. '''
	matches = 0
	i = 0
	j = 0
	while i < len(list1) and j < len(list2):
		if list1[i] == list2[j]:
			matches += 1
			i += 1
			j += 1
		elif list1[i] < list2[j]:
			i += 1
		else:
			j += 1
	return matches

## Create function a standardlize the users' preference: (2D array)
def standardizeAll(storedPrefs):
	standardStoredPrefs = []
	for storedUsers in storedPrefs:
		standardStoredUser = []
		for artist in storedUsers:
			standardStoredUser.append(artist.strip().title())
		standardStoredPrefs.append(standardStoredUser)
	return standardStoredPrefs
	### print (standardizeAll([[' adele', 'lAdY GAGA'], ['maROON 5']]))
def standardizeAll(storedPrefs):
	''' A simpler version. '''
	for i in range(len(storedPrefs)):
		for j in range(len(storedPrefs[i])):
			standardArtist = storedPrefs[i][j].stip().title()
			storedPrefs[i][j] = standardArtist
	return storedPrefs
## Use Dictionaries to store username and preferred artist
myDict = {} # creates and empty dictionaries
myDict['April'] = ['Maroon 5', 'The Rolling Stones', 'The Beatles']
myDict.has_key('f') # Check whether a key is in a dictionaries.
myDict.keys() # Get the keys in the dictionary
def getBestUser(currUser, prefs, userMap):
	''' Get recommendations for currUser based on the users in
		Usermap (a dictionary) and the current user's preferences
		in prefs (a list). '''
	users = userMap.keys() # all user names
	bestuser = None # initialization
	bestscore = -1
	for user in users:
		score = numMatches(prefs, Usermap[user])
		if score > bestscore and currUser != user:
			bestscore = score
			bestuser = user
	return bestuser

# 5.6 Reading and Writing files
## for files: username:artist1,artist2,...,artistN
## save users' perferences into a dictionary from file
def loadUsers(fileName):
	''' Reads in a file of stored users' preferences stored
		in the file 'fileName'.
		Returns a dictionary containing a mapping of user
		names to a list of preferred artists. '''
	file = open(fileName, 'r') # w/'r', we can only read file
	userDict = {}
	for line in file: # read file line by line
		[username, bands] = line.strip().split(:)# seperate by ':'
		bandList = bands.split(',') # seperate bands
		bandList.sort() # sort bands alphabetically
		userDict[username] = bandList
	file.close()
	return userDict

## inversely, save users' preferences into a file
def saveUserPreferences(userName, prefs, userMap, fileName):
	''' Writes all of the user preferences to the file.
		Returns nothing. '''
	userMap[userName] = prefs # add all key-value pairs to dict
	file = open(fileName, 'w')
	for user in userMap: # write username:artist,.. line by line
		toSave = str(user) + ':' + ','.join(userMap[user]) + \
		"\n"
		file.write(toSave)
	file.close()
# Biggest Example: recommondation system:
PREF_FILE = 'musicrec-store.txt'
def loadUsers(fileName):
	file = open(fileName, 'r')
	userDict = {}
	for line in file:
		[userName, bands] = line.strip().split(':')
		bandList = bands.split(',')
		bandList.sort()
		userDict[userName] = bandList
	file.close()
	return userDict

def getPreferences(userName, userMap):
	''' Returns a list of the uesr's preferred artists.

        If the system already knows about the user,
        it gets the preferences out of the userMap
        dictionary and then asks the user if she has
        additional preferences.  If the user is new,
        it simply asks the user for her preferences. '''
    newPref = ""
    if userName in userMap:
    	prefs = userMap[userName]
    	print "I see you have used the system before."
    	print "Your music preferences include":
    	for artist in prefs:
    		print artist
    	print "Please enter additional aritist or band that you"
    	print "like, or just press enter"
    	newPref = raw_input('to see your recommendations: ')
    else:
    	prefs = []
    	print "I see you are a new user."
    	print "Please enter the name of an artist or band"
    	newPref = raw_input("that you like: ")
    while newPrefs:
    	prefs.append(newPrefs.strip().title())
    	print "Please enter another artist or band that you"
    	print "like, or just press enter"
    	newPref = raw_input("to see your recommendations: ")
    # Always keep the lists in sorted order for ease of comparision
    prefs.sort()
    return prefs

def getRecommendations(currUser, prefs, userMap):
	bestUser = findBestUser(currUser, prefs, userMap)
	recommendations = drop(prefs, userMap[bestUser])
	return recommendations

def findBestUser(currUser, prefs, userMap):
	users = userMap.keys()
	bestUser = None
	bestScore = -1
	for user in users:
		score = numMatches(prefs, userMap[user])
		if score > bestScore and user != currUser:
			bestUser = user
			bestScore = score
	return bestUser

def drop(list1, list2):
	list3 = []
	i = 0
	j = 0
	while j < len(list2):
		if list1[i] == list2[j] and i < len(list):
			i += 1
			j += 1
		elif list1[i] < list2[j] and i < len(list):
			i += 1
		elif list1[i] > list2[j]:
			list3.append(list2[j])
			j += 1
		else:
			list3.append(list2[j:])
			break
	list3.sort()
	return list3

def numMatches(list1, list2):
	matches = 0
	i = 0
	j = 0
	while i < len(list1) and j < len(list2):
		if list1[i] == list2[j]:
			matches += 1
			i += 1
			j += 1
		elif list1[i] < list2[j]:
			i += 1
		else:
			j += 1
	return matches

def saveUserPreferences(userName, prefs, userMap, fileName):
	userMap[userName] = prefs
	file = open(fileName, 'w')
	for user in userMap:
		toSave = str(user) + ':' + ",".join(userMap[user]) + \
		"\n"
		file.write(toSave)
	file.close()

def main():
	''' The main recommendation function. '''
	userMap = loadUsers(PREF_FILE)
	print "Welcome to the music recommender system!"

	userName = raw_input('Please enter your name: ')
	print "Welcome, ", userName

	prefs = getPreferences(userName, userMap)
	recs = getRecommendations(userName, prefs, userMap)

	# Print the user's recommendations
	if len(recs) == 0:
		print "I'm sorry but I have no recommendations\
		for your right now."
	else:
		print(userName, "based on the user that I currently")
		print("know about, I believe you might like: ")
		for artist in recs:
			print artist
		print "I hope you enjoy them! I will save your"
		print "preferred artists and have new"
		print " recommendations for your in the future!"
	saveUserPreferences(userName, prefs, userMap, PREF_FILE)

if __name__ == "__main__": main()

# Chapter 6: Fun and Games with OOPs: Object-Oriented Programs
# 6.3 Define a rational number Data Type:
class Rational:
	def __init__(self, num, denom):
		self.numerator = num # numerator is one of attribute of Rational Class
		self.denominator = denom
	def add(self, other):
		newNumerator = self.numerator * other.denominator +\
						self.denominator * other.numerator
		newDenominator = self.denominator * other.denominator
		return Rational(newNumerator, newDenominator)
	def __eq__(self, other): # Overloading
		return self.numerator * other.denominator \
		== other.numerator * self.denominator
	def __ge__(self, othter):
		return self.numerator * other.denominator \
		>= other.numerator * self.denominator
	def __str__(self):
		return str(self.numerator) + '/' + str(self.denominator)
## Example:
r1 = Rational(36, 1000)
r2 = Rational(42, 100)
r3 = r1.add(r2)
r1.numerator # 36

# 6.4 Overloading
## would like to calculate rational numbers without converting them into floating data types:
r1 = Rational(1,2)
r2 = Rational(1,2)
r1 == r1 # show False because each one is a reference to a different object,
			# in other words, those two references not in same memory location.

### after overloading, the following expression will print True:
fuelNeeded = Rational(42, 1000)
tank1 = Rational(36, 1000)
tank2 = Rational(6, 1000)
tank1 + tank2 >= fuelNeeded # print True

# 6.5 Prin an Object
## print(r3) cannot print the value of r3
## we can overloading __str__ funciton to print our numbers
print(str(r1))

# Getting Graphical with OOPs


# Logic-2 > make_bricks 

''' 
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks 
(5 inches each). Return True if it is possible to make the goal 
by choosing from the given bricks. This is a little harder than 
it looks and can be done without any loops. See also: 
Introduction to MakeBricks

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''
def make_bricks(small, big, goal):
  big_adj = big
  if big_adj == 0:
    return goal in range(0, small + 1)
  
  if big_adj > (goal // 5):
    big_adj = goal // 5
    
  if goal - (5*big_adj) in range(0, small+1) :
    return True
  else:
    return False
