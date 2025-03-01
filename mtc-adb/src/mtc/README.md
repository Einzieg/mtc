# ADBTouch

This module defines the `ADBTouch` class, which implements touch interactions using ADB (Android Debug Bridge).

## `ADBTouch` Class

The `ADBTouch` class inherits from the `Touch` abstract base class and provides methods for simulating touch actions on an Android device connected via ADB.

### `__init__(self, serial)`

Initializes an `ADBTouch` instance.

- `serial`: The serial number of the Android device.

### `click(self, x: int, y: int, duration: int = 100)`

Simulates a click at a specific coordinate on the device.

- `x`: The x-coordinate of the click.
- `y`: The y-coordinate of the click.
- `duration`: The duration of the click in milliseconds (default: 100ms).

### `swipe(self, points: List[Tuple[int, int]], duration: int = 500)`

Simulates a swipe gesture through a series of points on the device.

- `points`: A list of (x, y) coordinate tuples representing the swipe path.
- `duration`: The duration of the swipe in milliseconds (default: 500ms).
