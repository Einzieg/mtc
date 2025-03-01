# Touch

This module defines an abstract base class `Touch` for simulating touch interactions.

## `Touch` Class

The `Touch` class provides an interface for implementing touch-based actions, such as clicks and swipes.

### Abstract Methods

- `click(x: int, y: int, duration: int = 100)`: Simulates a click at a specific coordinate.
  - `x`: The x-coordinate of the click.
  - `y`: The y-coordinate of the click.
  - `duration`: The duration of the click in milliseconds (default: 100ms).

- `swipe(points: List[Tuple[int, int]], duration: int = 500)`: Simulates a swipe gesture through a series of points.
  - `points`: A list of (x, y) coordinate tuples representing the swipe path.
  - `duration`: The duration of the swipe in milliseconds (default: 500ms).
