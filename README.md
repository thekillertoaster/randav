# Randav

An advanced random library for Python, extending the built-in `random` module with additional functionality.

## Features

- Different probability distributions
- Weighted random selection
- Seeding options
- Perlin and Simplex noise functions
- Random generators for various data types
- Random data sampling
- Pseudorandom number generator (PRNG) options
- Parallel and distributed random number generation
- Reproducibility

## Installation

Install `randav` using pip:

```bash
pip install git+https://github.com/thekillertoaster/randav.git
```

## Usage

Import randav and use it like the built-in random module:

```python
import randav as random

print(random.randint(1, 10))
print(random.uniform(0, 1))
# Use other custom functions and features
```

## Running Tests

To run tests, execute the following command in the project root directory:

```bash
python -m unittest discover tests
```

## License

This project is licensed under a custom license. See the [LICENSE](LICENSE) file for details.