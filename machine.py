class Machine():
	def __init__(self, states=[], initial=None):
		self.state = None
		self.states = {}
		self.setStates(states)
		self.started = False
		self.running = False
		self.finished = False
		self.__initial = 
		self.__valid = True

	def setStates(self, states):
		if self.states != {}:
			raise Exception("Cannot reset states once initialized")
		for item in states:
			if item.getName() in self.states.keys():
				raise Exception("Redefinition of state {}".format(item.getName()))
			if not item.isValid():
				raise Exception("{} state is malformed".format(item.getName()))
			self.states[item.getName()] = item


	def setInitial(self, initial):
		if self.started:
			raise Exception("Machine initial state cannot be set once machine is started")
			return
		self.__initial = initial

	def start(self):
		self.running = True

	def pause(self):
		self.running = False