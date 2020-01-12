# StateMachine

This library is a flexible implementation of a state machine. It provides a safe and clean interface for making dependable execution and transition functions, and a machine to run on top of each state.

# Specification and Interface

## State

#### Public Variables

```python
self.name - The name of the state
self.exe - The execution function of the state
self.transition - The transition function of the state
```

#### Public Methods

```python
self.setName(name) - Sets the name of the state
self.setExe(f) - Sets the state execution function
self.setExeCapture(c) - Sets the closure for the execution function
self.setTransition(f) - Sets the state transition function
self.setTransitionCapture(n) - Sets the closure for the transition function
self.isValid() - (Bool) True if the state is valid, False otherwise
```


## Machine

#### Public Variables

```python
self.state - Current machine state
self.started - (Bool) True if the machine has been started, False otherwise
self.running - (Bool) True if the machine is currently running, False otherwise
self.finished - (Bool) True if the machine is finished running, False otherwise
```

#### Public Methods

```python
__init__(states={}) - Creates a state machine object
start() - Runs the state machine
```
