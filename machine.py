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
		self.__uniqueHistory = []
		self.__history = []

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
		if self.started:
			raise Exception("Machine cannot be started more than once")
		self.stated = True
		self.running = True
		self.state = self.states[initial]
		self.__run()

	def __run(self):
		while self.running:
			self.state.__run(self)
			self.__history.append(self.state)
			if self.__uniqueHistory[-1] is not self.state.getName():
				self.__uniqueHistory.append(self.state)
			transition = self.state.__runTransition(self)
			if transition is not None:
				if transition is not in self.states.keys():
					raise Exception("State {} returned invalid transition ({})".format(self.state.getName(), transition))
				self.state = self.states[transition]

	def pause(self):
		if not self.started:
			raise Exception("Machine cannot pause because it has not been started")
		self.running = False

	def unpause(self):
		if not self.started:
			raise Exception("Machine cannot unpause because it has not been started")
		self.running = True
		self.__run()
