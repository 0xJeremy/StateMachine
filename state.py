class State():
	def __init__(self, name=None, exe=None, transition=None):
		self.name = name
		self.exe = exe
		self.transition = transition

	def __valid():
		if self.name is not None and \
		   self.exe is not None and \
		   self.transition is not None:
		   return True
		return False

	def setName(name):
		self.name = name
	def setExe(exe):
		self.exe = exe
	def setTransition(transition):
		self.transition = transition