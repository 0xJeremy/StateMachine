import inspect

class State():
	def __init__(self, name=None, exe=None, exeCapture=None, transition=None, transitionCapture=None):
		self.setName(name)
		self.setExe(exe)
		self.setExeCapture(exeCapture)
		self.setTransition(transition)
		self.setTransitionCapture(transitionCapture)
		self.__validate()

	def __validate(self):
		if self.name is not None and \
		   self.exe is not None and \
		   self.transition is not None:
		   self.valid = True
		self.valid = False

	def isValid(self):
		self.__validate()
		return self.valid

	def getName(self):
		return self.name

	def setName(self, name):
		if self.name is not None:
			raise Exception("State name cannot be redefined once set")
		self.name = name

	def setExe(self, exe):
		if not inspect.ismethod(exe) and not inspect.isfunction(exe):
			raise Exception("Execution function is improperly formed")
		self.exe = exe

	def setExeCapture(self, exeCapture):
		if self.exe is None:
			raise Exception("The execution function must be defined first")
		self.exeCapture = exeCapture

	def setTransition(self, transition):
		if not inspect.ismethod(exe) and not inspect.isfunction(exe):
			raise Exception("Transition function is improperly formed")
		self.transition = transition

	def setTransitionCapture(self, transitionCapture):
		if self.transition is None:
			raise Exception("The transition function must be defined first")
		self.transitionCapture = transitionCapture
