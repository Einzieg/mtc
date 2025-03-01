# MiniTouch

This module defines the `MiniTouch` class, which implements touch interactions using the MiniTouch service on an Android device.

## `MiniTouch` Class

The `MiniTouch` class inherits from the `Touch` abstract base class and provides methods for simulating touch actions on an Android device connected via ADB. It communicates with a MiniTouch service running on the device.

### `__init__(self, serial)`

Initializes a `MiniTouch` instance.

- `serial`: The serial number of the Android device.

### `start(self)`

Starts the MiniTouch service on the device and connects to it.

### `stop(self)`

Stops the MiniTouch service and disconnects from it.

### `click(self, x: int, y: int, duration: int = 100)`

Simulates a click at a specific coordinate on the device.

- `x`: The x-coordinate of the click.
- `y`: The y-coordinate of the click.
- `duration`: The duration of the click in milliseconds (default: 100ms).

### `swipe(self, points: list, duration: int = 300)`

Simulates a swipe gesture through a series of points on the device.

- `points`: A list of (x, y) coordinate tuples representing the swipe path.
- `duration`: The duration of the swipe in milliseconds (default: 300ms).
