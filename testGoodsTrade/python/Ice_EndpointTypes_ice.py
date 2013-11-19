# **********************************************************************
#
# Copyright (c) 2003-2010 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.4.1

# <auto-generated>
#
# Generated from file `EndpointTypes.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>

import Ice, IcePy, __builtin__

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('EndpointSelectionType'):
    _M_Ice.EndpointSelectionType = Ice.createTempClass()
    class EndpointSelectionType(object):
        '''Determines the order in which the Ice run time uses the endpoints
in a proxy when establishing a connection.'''

        def __init__(self, val):
            assert(val >= 0 and val < 2)
            self.value = val

        def __str__(self):
            return self._names[self.value]

        __repr__ = __str__

        def __hash__(self):
            return self.value

        def __lt__(self, other):
            if isinstance(other, _M_Ice.EndpointSelectionType):
                return self.value < other.value;
            elif other == None:
                return False
            return NotImplemented

        def __le__(self, other):
            if isinstance(other, _M_Ice.EndpointSelectionType):
                return self.value <= other.value;
            elif other == None:
                return False
            return NotImplemented

        def __eq__(self, other):
            if isinstance(other, _M_Ice.EndpointSelectionType):
                return self.value == other.value;
            elif other == None:
                return False
            return NotImplemented

        def __ne__(self, other):
            if isinstance(other, _M_Ice.EndpointSelectionType):
                return self.value != other.value;
            elif other == None:
                return False
            return NotImplemented

        def __gt__(self, other):
            if isinstance(other, _M_Ice.EndpointSelectionType):
                return self.value > other.value;
            elif other == None:
                return False
            return NotImplemented

        def __ge__(self, other):
            if isinstance(other, _M_Ice.EndpointSelectionType):
                return self.value >= other.value;
            elif other == None:
                return False
            return NotImplemented

        _names = ('Random', 'Ordered')

    EndpointSelectionType.Random = EndpointSelectionType(0)
    EndpointSelectionType.Ordered = EndpointSelectionType(1)

    _M_Ice._t_EndpointSelectionType = IcePy.defineEnum('::Ice::EndpointSelectionType', EndpointSelectionType, (), (EndpointSelectionType.Random, EndpointSelectionType.Ordered))

    _M_Ice.EndpointSelectionType = EndpointSelectionType
    del EndpointSelectionType

# End of module Ice
