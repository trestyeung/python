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
# Generated from file `Router.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>

import Ice, IcePy, __builtin__
import Ice_BuiltinSequences_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('Router'):
    _M_Ice.Router = Ice.createTempClass()
    class Router(Ice.Object):
        '''The Ice router interface. Routers can be set either globally with
Communicator.setDefaultRouter, or with ice_router on specific
proxies.'''
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.Router:
                raise RuntimeError('Ice.Router is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Ice::Router')

        def ice_id(self, current=None):
            return '::Ice::Router'

        def ice_staticId():
            return '::Ice::Router'
        ice_staticId = staticmethod(ice_staticId)

        def getClientProxy(self, current=None):
            '''Get the router's client proxy, i.e., the proxy to use for
forwarding requests from the client to the router.

Returns:
    The router's client proxy.'''
            pass

        def getServerProxy(self, current=None):
            '''Get the router's server proxy, i.e., the proxy to use for
forwarding requests from the server to the router.

Returns:
    The router's server proxy.'''
            pass

        def addProxy(self, proxy, current=None):
            '''Add new proxy information to the router's routing table.

This operation is deprecated, and only used for old
Ice clients (older than version 3.1).

Arguments:
    proxy The proxy to add.'''
            pass

        def addProxies(self, proxies, current=None):
            '''Add new proxy information to the router's routing table.

Arguments:
    proxies The proxies to add.

Returns:
    Proxies discarded by the router.'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Router)

        __repr__ = __str__

    _M_Ice.RouterPrx = Ice.createTempClass()
    class RouterPrx(Ice.ObjectPrx):

        '''Get the router's client proxy, i.e., the proxy to use for
forwarding requests from the client to the router.

Returns:
    The router's client proxy.'''
        def getClientProxy(self, _ctx=None):
            return _M_Ice.Router._op_getClientProxy.invoke(self, ((), _ctx))

        '''Get the router's client proxy, i.e., the proxy to use for
forwarding requests from the client to the router.

Returns:
    The router's client proxy.'''
        def begin_getClientProxy(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Ice.Router._op_getClientProxy.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Get the router's client proxy, i.e., the proxy to use for
forwarding requests from the client to the router.

Returns:
    The router's client proxy.'''
        def end_getClientProxy(self, _r):
            return _M_Ice.Router._op_getClientProxy.end(self, _r)

        '''Get the router's client proxy, i.e., the proxy to use for
forwarding requests from the client to the router.

Returns:
    The router's client proxy.'''
        def getClientProxy_async(self, _cb, _ctx=None):
            return _M_Ice.Router._op_getClientProxy.invokeAsync(self, (_cb, (), _ctx))

        '''Get the router's server proxy, i.e., the proxy to use for
forwarding requests from the server to the router.

Returns:
    The router's server proxy.'''
        def getServerProxy(self, _ctx=None):
            return _M_Ice.Router._op_getServerProxy.invoke(self, ((), _ctx))

        '''Get the router's server proxy, i.e., the proxy to use for
forwarding requests from the server to the router.

Returns:
    The router's server proxy.'''
        def begin_getServerProxy(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Ice.Router._op_getServerProxy.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Get the router's server proxy, i.e., the proxy to use for
forwarding requests from the server to the router.

Returns:
    The router's server proxy.'''
        def end_getServerProxy(self, _r):
            return _M_Ice.Router._op_getServerProxy.end(self, _r)

        '''Add new proxy information to the router's routing table.

This operation is deprecated, and only used for old
Ice clients (older than version 3.1).

Arguments:
    proxy The proxy to add.'''
        def addProxy(self, proxy, _ctx=None):
            return _M_Ice.Router._op_addProxy.invoke(self, ((proxy, ), _ctx))

        '''Add new proxy information to the router's routing table.

This operation is deprecated, and only used for old
Ice clients (older than version 3.1).

Arguments:
    proxy The proxy to add.'''
        def begin_addProxy(self, proxy, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Ice.Router._op_addProxy.begin(self, ((proxy, ), _response, _ex, _sent, _ctx))

        '''Add new proxy information to the router's routing table.

This operation is deprecated, and only used for old
Ice clients (older than version 3.1).

Arguments:
    proxy The proxy to add.'''
        def end_addProxy(self, _r):
            return _M_Ice.Router._op_addProxy.end(self, _r)

        '''Add new proxy information to the router's routing table.

Arguments:
    proxies The proxies to add.

Returns:
    Proxies discarded by the router.'''
        def addProxies(self, proxies, _ctx=None):
            return _M_Ice.Router._op_addProxies.invoke(self, ((proxies, ), _ctx))

        '''Add new proxy information to the router's routing table.

Arguments:
    proxies The proxies to add.

Returns:
    Proxies discarded by the router.'''
        def begin_addProxies(self, proxies, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Ice.Router._op_addProxies.begin(self, ((proxies, ), _response, _ex, _sent, _ctx))

        '''Add new proxy information to the router's routing table.

Arguments:
    proxies The proxies to add.

Returns:
    Proxies discarded by the router.'''
        def end_addProxies(self, _r):
            return _M_Ice.Router._op_addProxies.end(self, _r)

        '''Add new proxy information to the router's routing table.

Arguments:
    proxies The proxies to add.

Returns:
    Proxies discarded by the router.'''
        def addProxies_async(self, _cb, proxies, _ctx=None):
            return _M_Ice.Router._op_addProxies.invokeAsync(self, (_cb, (proxies, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Ice.RouterPrx.ice_checkedCast(proxy, '::Ice::Router', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Ice.RouterPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Ice._t_RouterPrx = IcePy.defineProxy('::Ice::Router', RouterPrx)

    _M_Ice._t_Router = IcePy.defineClass('::Ice::Router', Router, (), True, None, (), ())
    Router._ice_type = _M_Ice._t_Router

    Router._op_getClientProxy = IcePy.Operation('getClientProxy', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), IcePy._t_ObjectPrx, ())
    Router._op_getServerProxy = IcePy.Operation('getServerProxy', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), IcePy._t_ObjectPrx, ())
    Router._op_addProxy = IcePy.Operation('addProxy', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), IcePy._t_ObjectPrx),), (), None, ())
    Router._op_addProxy.deprecate("addProxy() is deprecated, use addProxies() instead.")
    Router._op_addProxies = IcePy.Operation('addProxies', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), _M_Ice._t_ObjectProxySeq),), (), _M_Ice._t_ObjectProxySeq, ())

    _M_Ice.Router = Router
    del Router

    _M_Ice.RouterPrx = RouterPrx
    del RouterPrx

# End of module Ice
