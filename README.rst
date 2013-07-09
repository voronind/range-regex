Python numeric range regular expression generator
=========================

Another like packages generates incorrect or excessive patterns.

Installation
=========================
::

    pip install range-regex

or

::

    git clone git://github.com/dimka665/range-regex.git

Usage
=========================
::

    from range_regex import regex_for_range
    from range_regex import bounded_regex_for_range

    regex_for_range(12, 34)
    bounded_regex_for_range(12, 34)

generates

    "1[2-9]|2\d|3[0-4]"
    "\b(1[2-9]|2\d|3[0-4])\b"

