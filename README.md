# StateMachine

This library is a flexible implementation of a state machine for use in robots.

# Specification and Interface

## State


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
* __init__(states={}) - Creates a state machine object
* start() - Runs the state machine
```