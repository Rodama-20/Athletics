# CJAJB Athletics

[![Test CJAJB Athletics](https://github.com/Rodama-20/Athletics/actions/workflows/test.yml/badge.svg)](https://github.com/Rodama-20/Athletics/actions/workflows/test.yml)

`cjajb_athletics` computes athletics points for CJAJB meetings using the Swiss Athletics FSA 2010 scoring formulas.

## Installation

```bash
pip install cjajb-athletics
```

For local development:

```bash
pip install -e .
```

## Usage

Running performances are expressed in seconds:

```python
from cjajb_athletics import run

run.flat_100_men(10.0)
# 1195

run.flat_100_men("10.0")
# 1195
```

Technical performances are expressed in metres:

```python
from cjajb_athletics import technic

technic.long_jump_men(8.0)
# 1102
```

NumPy arrays and regular Python sequences are supported and are evaluated vectorially:

```python
import numpy as np
from cjajb_athletics import run

run.flat_100_men(np.array([10.0, 9.98, 22.0]))
# array([1195, 1199,    0])

run.flat_100_men([10.0, 22.0])
# array([1195,    0])
```

Scalar inputs return a Python `int`; array-like inputs return a NumPy integer array. Scores are limited to the official range from 0 to 1200 points. Negative, non-finite, and out-of-domain numeric performances score 0 points.

## Modules

- `cjajb_athletics.run`: flat races and hurdles for men and women.
- `cjajb_athletics.technic`: jumps and throws for men and women.

Formula parameters are based on the Swiss Athletics FSA 2010 scoring tables.

## Development

Run the test suite with:

```bash
pytest
```
