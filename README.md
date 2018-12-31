# Physics

This is a python package to aid automating physics labs and various other physics calculations.

## Structure

`physics` is a python module which contains 3 submodules: `calculations`, `error`, and `units`.

`calculations` contains various physics formulas for deriving values. `error` contains various functions to aid in experimental error analysis. `units` is will be designed to enforce proper dimensional analysis in calculations.

All tests are located in `tests/` using `pytest` (TODO- add link). These can be run from the root directory using the command `python -m pytest tests/`.

## TODO

- Develop readme more
- Add more tests
- Add more conceptual calculations in `calculations.py`
- Add more error analysis tools in `error.py`
- Formalize design for `units` submodule
- Switch over lab examples to use `physics` package instead of `functions.py`
