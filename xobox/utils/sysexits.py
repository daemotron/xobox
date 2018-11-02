# -*- coding: utf-8 -*-

"""
    xobox.utils.sysexits
    ~~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2018 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


try:
    from os import EX_OK
except ImportError:
    EX_OK = 0

try:
    from os import EX_USAGE
except ImportError:
    EX_USAGE = 64

try:
    from os import EX_DATAERR
except ImportError:
    EX_DATAERR = 65

try:
    from os import EX_NOINPUT
except ImportError:
    EX_NOINPUT = 66

try:
    from os import EX_NOUSER
except ImportError:
    EX_NOUSER = 67

try:
    from os import EX_NOHOST
except ImportError:
    EX_NOHOST = 68

try:
    from os import EX_UNAVAILABLE
except ImportError:
    EX_UNAVAILABLE = 69

try:
    from os import EX_SOFTWARE
except ImportError:
    EX_SOFTWARE = 70

try:
    from os import EX_OSERR
except ImportError:
    EX_OSERR = 71

try:
    from os import EX_OSFILE
except ImportError:
    EX_OSFILE = 72

try:
    from os import EX_CANTCREAT
except ImportError:
    EX_CANTCREAT = 73

try:
    from os import EX_IOERR
except ImportError:
    EX_IOERR = 74

try:
    from os import EX_TEMPFAIL
except ImportError:
    EX_TEMPFAIL = 75

try:
    from os import EX_PROTOCOL
except ImportError:
    EX_PROTOCOL = 76

try:
    from os import EX_NOPERM
except ImportError:
    EX_NOPERM = 77

try:
    from os import EX_CONFIG
except ImportError:
    EX_CONFIG = 78
