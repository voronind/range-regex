=========================
range-regex
=========================

The nicest numeric range regular expression generator.
Another like modules generates incorrect or excessive patterns.

Installation
=========================

The recommended way to install range-regex is with `pip <http://pypi.python.org/pypi/pip>`_::

    pip install range-regex


Usage
=========================
::

    from range_regex import regex_for_range
    
    regex_for_range(12, 34)

generates ``"1[2-9]|2\d|3[0-4]"``