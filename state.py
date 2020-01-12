class State():
	def __init__(self, name=None, exe=None, exeCapture=None, transition=None, transitionCapture=None):
		self.name = name
		self.exe = exe
		self.transition = transition
		self.valid = self.__valid()

	def __valid(self):
		if self.name is not None and \
		   self.exe is not None and \
		   self.transition is not None:
		   return True
		return False

	def isValid(self):
		return self.valid

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name
	def setExe(self, exe):
		self.exe = exe
	def setExeCapture(self, exeCapture):
		if self.exe is None:
			raise Exception("The execution function must be defined first")
		self.exeCapture = exeCapture
	def setTransition(self, transition):
		self.transition = transition
	def setTransitionCapture(self, transitionCapture):
		if self.transition is None:
			raise Exception("The transition function must be defined first")
		self.transitionCapture = transitionCapture
