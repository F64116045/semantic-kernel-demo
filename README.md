# Semantic Kernel Demo

A working Python demo based on [[Microsoft Semantic Kernel]](https://github.com/microsoft/semantic-kernel). 

- Built with Python 3.12 and [`uv`](https://github.com/astral-sh/uv) for dependency management
- Includes a custom semantic function implemented in `lights_plugin.py`
- Compatible with OpenAI GPT-4o-mini

## Quick Start
### 1. Set up the virtual environment and install dependencies

```bash
uv venv
uv sync
```

### 2. Run 
```bash
uv run app.py
```

## Plugin Overview: `LightsPlugin`

The `LightsPlugin` is a custom semantic function plugin that manages the status of a group of lights. It simulates a smart home scenario where lights can be turned on or off using natural language prompts interpreted by the Semantic Kernel.

### Internal Data

The plugin maintains a predefined list of lights:
```python
[
    {"id": 1, "name": "Table Lamp", "is_on": False},
    {"id": 2, "name": "Porch light", "is_on": False},
    {"id": 3, "name": "Chandelier", "is_on": True},
]
```

### Exposed Semantic Functions

#### `get_lights`
- **Purpose**: Returns the current on/off status of all lights.
- **Kernel Name**: `get_lights`
- **Returns**: A list of light objects.

#### `change_state`
- **Purpose**: Changes the on/off state of a specific light by ID.
- **Kernel Name**: `change_state`
- **Parameters**:
  - `id` (int): The light's unique ID.
  - `is_on` (bool): Desired state (`true` for ON, `false` for OFF).
- **Returns**: The updated light object, or `None` if not found.

> These functions are registered via the `@kernel_function` decorator and can be called from prompts handled by the Semantic Kernel planner or chat interface.


## Development Tools

- Python 3.12+
- [`uv`](https://github.com/astral-sh/uv)
- Semantic Kernel (via PyPI)

## License

MIT (or specify another license)

