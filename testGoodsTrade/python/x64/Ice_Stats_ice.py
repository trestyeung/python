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
# Generated from file `Stats.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>

import Ice, IcePy, __builtin__

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('Stats'):
    _M_Ice.Stats = Ice.createTempClass()
    class Stats(object):
        '''An interface Ice uses to report statistics, such as how much data
is sent or received. Applications must provide their own Stats
by implementing this interface and installing it in a communicator.'''
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.Stats:
                raise RuntimeError('Ice.Stats is an abstract class')

        def bytesSent(self, protocol, num):
            '''Callback to report that data has been sent.

Arguments:
    protocol The protocol over which data has been sent (for
example "tcp", "udp", or "ssl").

    num How many bytes have been sent.'''
            pass

        def bytesReceived(self, protocol, num):
            '''Callback to report that data has been received.

Arguments:
    protocol The protocol over which data has been received
(for example "tcp", "udp", or "ssl").

    num How many bytes have been received.'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Stats)

        __repr__ = __str__

    _M_Ice._t_Stats = IcePy.defineClass('::Ice::Stats', Stats, (), True, None, (), ())
    Stats._ice_type = _M_Ice._t_Stats

    _M_Ice.Stats = Stats
    del Stats

# End of module Ice
