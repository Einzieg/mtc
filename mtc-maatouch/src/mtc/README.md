# MaaTouch

This module defines the `MaaTouch` class, which implements touch interactions using a method similar to scrcpy and has an interface similar to minitouch.

## `MaaTouch` Class

The `MaaTouch` class inherits from the `Touch` abstract base class and provides methods for simulating touch actions on an Android device. It communicates with a MaaTouch service running on the device.

### `__init__(self, serial)`

Initializes a `MaaTouch` instance.

- `serial`: The serial number of the Android device.

### `send(self, content)`

Sends a message to the MaaTouch service and returns the response.

- `content`: The message to send.

### `click(self, x: int, y: int, duration: int = 100)`

Simulates a click at a specific coordinate on the device.

- `x`: The x-coordinate of the click.
- `y`: The y-coordinate of the click.
- `duration`: The duration of the click in milliseconds (default: 100ms).

### `swipe(self, points: list, duration: int = 500)`

Simulates a swipe gesture through a series of points on the device.

- `points`: A list of (x, y) coordinate tuples representing the swipe path.
- `duration`: The duration of the swipe in milliseconds (default: 500ms).
