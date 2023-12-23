# PyCamelot

PyCamelot is a Python library for harmonic mixing, leveraging the Camelot wheel system to help DJs and music producers create seamless transitions between songs. It maps musical keys to their corresponding Camelot keys and calculates compatible keys for mixing.

## Features

- Map musical keys to Camelot keys.
- Find compatible keys for harmonic mixing.
- Support for both sharp and flat notations.

## Installation

To install PyCamelot, ensure you have Poetry installed and run:

```shell
poetry install
```

## Usage

```python
from pycamelot import HarmonicMixing

# Create a HarmonicMixing instance
mixer = HarmonicMixing()

# Get the Camelot key for a given musical key
camelot_key = mixer.get_camelot_key('C')  # Returns '8B'

# Get a list of compatible Camelot keys
compatible_keys = mixer.get_compatible_keys('8B')  # Returns ['8B', '9B', '7B', '8A']
```

## Development

To contribute to PyCamelot, clone the repository, and set up the project with:

```shell
poetry install
```

## Running Tests

PyCamelot uses pytest for testing. Run tests with the following command:

```shell
poetry run pytest
```

## License

PyCamelot is released under the MIT License. See the LICENSE file for more details.

## Authors

- DJ Stomp <dj@deepai.org>

We hope PyCamelot makes your DJing journey harmonious and your mixes flawless!