import sys
import os.path

# mypyc depends on a copy of mypy installed as package-data that won't
# live in the normal python path (to avoid potential conflicts with an
# installed mypy). In order to make sure we find it, we perform
# sys.path shenanigans here when mypyc is first imported.
base_path = os.path.dirname(__file__)
mypy_path = os.path.abspath(os.path.join(base_path,'..',  'external', 'mypy'))
sys.path.insert(0, mypy_path)

# print(__file__)
# print(sys.path[0])

# Make sure that we can find mypy and that it is the *right* mypy.  If
# mypy was imported before mypyc was, our path manipulations might
# have been too late, and this assert will catch the problem.
import mypy

found = mypy.__file__
expect = os.path.join(mypy_path, 'mypy', '__init__.py'),
assert found ==  expect, f"Found a mypy at {found!r} rather than at {expect!r}"
