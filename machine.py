class Machine():
	def __init__(self, states={}, initial=None):
		self.state = None
		self.states = {}
		self.transitions = None
		self.started = False
		self.running = False
		self.finished = False
		self.__initial = initial


	def setInitial(initial):
		if self.started:
			raise Exception("Machine initial state cannot be set once machine is started")
			return
		self.__initial = initial

	def start():
		self.running = True

	def pause():
		self.running = False