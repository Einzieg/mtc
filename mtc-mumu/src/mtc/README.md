# MuMuTouch

This module defines the `MuMuTouch` class, which implements touch interactions for the MuMu emulator.

## `MuMuTouch` Class

The `MuMuTouch` class inherits from the `Touch` abstract base class and provides methods for simulating touch actions on the MuMu emulator. It relies on the `mmumu` library to interact with the emulator.

### `__init__(self, instance_index: int, emulator_install_path: str = None, dll_path: str = None, display_id: int = 0)`

Initializes a `MuMuTouch` instance.

- `instance_index`: The index of the emulator instance.
- `emulator_install_path`: The installation path of the MuMu emulator (optional).
- `dll_path`: The path to the `external_renderer_ipc.dll` file (optional).
- `display_id`: The display ID (usually 0).

### `click(self, x: int, y: int, duration: int = 100)`

Simulates a click at a specific coordinate on the emulator.

- `x`: The x-coordinate of the click.
- `y`: The y-coordinate of the click.
- `duration`: The duration of the click in milliseconds (default: 100ms).

### `swipe(self, points: List[Tuple[int, int]], duration: int = 500)`

Simulates a swipe gesture through a series of points on the emulator.

- `points`: A list of (x, y) coordinate tuples representing the swipe path.
- `duration`: The duration of the swipe in milliseconds (default: 500ms).
