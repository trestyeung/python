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
import Ice_Router_ice
import Glacier2_Session_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Start of module Glacier2
__name__ = 'Glacier2'
_M_Glacier2.__doc__ = '''Glacier2 is a firewall solution for Ice. Glacier2 authenticates
and filters client requests and allows callbacks to the client in a
secure fashion. In combination with IceSSL, Glacier2 provides a
security solution that is both non-intrusive and easy to configure.'''

if not _M_Glacier2.__dict__.has_key('PermissionDeniedException'):
    _M_Glacier2.PermissionDeniedException = Ice.createTempClass()
    class PermissionDeniedException(Ice.UserException):
        '''This exception is raised if a client is denied the ability to create
a session with the router.'''
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'Glacier2::PermissionDeniedException'

    _M_Glacier2._t_PermissionDeniedException = IcePy.defineException('::Glacier2::PermissionDeniedException', PermissionDeniedException, (), None, (('reason', (), IcePy._t_string),))
    PermissionDeniedException._ice_type = _M_Glacier2._t_PermissionDeniedException

    _M_Glacier2.PermissionDeniedException = PermissionDeniedException
    del PermissionDeniedException

if not _M_Glacier2.__dict__.has_key('SessionNotExistException'):
    _M_Glacier2.SessionNotExistException = Ice.createTempClass()
    class SessionNotExistException(Ice.UserException):
        '''This exception is raised if a client tries to destroy a session
with a router, but no session exists for the client.'''
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'Glacier2::SessionNotExistException'

    _M_Glacier2._t_SessionNotExistException = IcePy.defineException('::Glacier2::SessionNotExistException', SessionNotExistException, (), None, ())
    SessionNotExistException._ice_type = _M_Glacier2._t_SessionNotExistException

    _M_Glacier2.SessionNotExistException = SessionNotExistException
    del SessionNotExistException

if not _M_Glacier2.__dict__.has_key('Router'):
    _M_Glacier2.Router = Ice.createTempClass()
    class Router(_M_Ice.Router):
        '''The Glacier2 specialization of the Ice.Router
interface.'''
        def __init__(self):
            if __builtin__.type(self) == _M_Glacier2.Router:
                raise RuntimeError('Glacier2.Router is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::Router', '::Ice::Object', '::Ice::Router')

        def ice_id(self, current=None):
            return '::Glacier2::Router'

        def ice_staticId():
            return '::Glacier2::Router'
        ice_staticId = staticmethod(ice_staticId)

        def getCategoryForClient(self, current=None):
            '''This category must be used in the identities of all of the client's
callback objects. This is necessary in order for the router to
forward callback requests to the intended client. If the Glacier2
server endpoints are not set, the returned category is an empty 
string.

Returns:
    The category.'''
            pass

        def createSession_async(self, _cb, userId, password, current=None):
            '''Create a per-client session with the router. If a
SessionManager has been installed, a proxy to a Session
object is returned to the client. Otherwise, null is returned
and only an internal session (i.e., not visible to the client)
is created.

If a session proxy is returned, it must be configured to route
through the router that created it. This will happen automatically
if the router is configured as the client's default router at the
time the session proxy is created in the client process, otherwise
the client must configure the session proxy explicitly.

Returns:
    A proxy for the newly created session, or null if no
SessionManager has been installed.

Arguments:
    userId The user id for which to check the password.

    password The password for the given user id.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.

    CannotCreateSessionException Raised if the session
cannot be created.'''
            pass

        def createSessionFromSecureConnection_async(self, _cb, current=None):
            '''Create a per-client session with the router. The user is
authenticated through the SSL certificates that have been
associated with the connection. If a SessionManager has been
installed, a proxy to a Session object is returned to the
client. Otherwise, null is returned and only an internal
session (i.e., not visible to the client) is created.

If a session proxy is returned, it must be configured to route
through the router that created it. This will happen automatically
if the router is configured as the client's default router at the
time the session proxy is created in the client process, otherwise
the client must configure the session proxy explicitly.

Returns:
    A proxy for the newly created session, or null if no
SessionManager has been installed.

Exceptions:
    PermissionDeniedException Raised if the user cannot be
authenticated or if the user is not allowed access.

    CannotCreateSessionException Raised if the session
cannot be created.'''
            pass

        def refreshSession(self, current=None):
            '''Keep the calling client's session with this router alive.

Exceptions:
    SessionNotExistException Raised if no session exists
for the calling client.'''
            pass

        def destroySession(self, current=None):
            '''Destroy the calling client's session with this router.

Exceptions:
    SessionNotExistException Raised if no session exists
for the calling client.'''
            pass

        def getSessionTimeout(self, current=None):
            '''Get the value of the session timeout. Sessions are destroyed
if they see no activity for this period of time.

Returns:
    The timeout (in seconds).'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_Glacier2._t_Router)

        __repr__ = __str__

    _M_Glacier2.RouterPrx = Ice.createTempClass()
    class RouterPrx(_M_Ice.RouterPrx):

        '''This category must be used in the identities of all of the client's
callback objects. This is necessary in order for the router to
forward callback requests to the intended client. If the Glacier2
server endpoints are not set, the returned category is an empty 
string.

Returns:
    The category.'''
        def getCategoryForClient(self, _ctx=None):
            return _M_Glacier2.Router._op_getCategoryForClient.invoke(self, ((), _ctx))

        '''This category must be used in the identities of all of the client's
callback objects. This is necessary in order for the router to
forward callback requests to the intended client. If the Glacier2
server endpoints are not set, the returned category is an empty 
string.

Returns:
    The category.'''
        def begin_getCategoryForClient(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Glacier2.Router._op_getCategoryForClient.begin(self, ((), _response, _ex, _sent, _ctx))

        '''This category must be used in the identities of all of the client's
callback objects. This is necessary in order for the router to
forward callback requests to the intended client. If the Glacier2
server endpoints are not set, the returned category is an empty 
string.

Returns:
    The category.'''
        def end_getCategoryForClient(self, _r):
            return _M_Glacier2.Router._op_getCategoryForClient.end(self, _r)

        '''Create a per-client session with the router. If a
SessionManager has been installed, a proxy to a Session
object is returned to the client. Otherwise, null is returned
and only an internal session (i.e., not visible to the client)
is created.

If a session proxy is returned, it must be configured to route
through the router that created it. This will happen automatically
if the router is configured as the client's default router at the
time the session proxy is created in the client process, otherwise
the client must configure the session proxy explicitly.

Returns:
    A proxy for the newly created session, or null if no
SessionManager has been installed.

Arguments:
    userId The user id for which to check the password.

    password The password for the given user id.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.

    CannotCreateSessionException Raised if the session
cannot be created.'''
        def createSession(self, userId, password, _ctx=None):
            return _M_Glacier2.Router._op_createSession.invoke(self, ((userId, password), _ctx))

        '''Create a per-client session with the router. If a
SessionManager has been installed, a proxy to a Session
object is returned to the client. Otherwise, null is returned
and only an internal session (i.e., not visible to the client)
is created.

If a session proxy is returned, it must be configured to route
through the router that created it. This will happen automatically
if the router is configured as the client's default router at the
time the session proxy is created in the client process, otherwise
the client must configure the session proxy explicitly.

Returns:
    A proxy for the newly created session, or null if no
SessionManager has been installed.

Arguments:
    userId The user id for which to check the password.

    password The password for the given user id.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.

    CannotCreateSessionException Raised if the session
cannot be created.'''
        def begin_createSession(self, userId, password, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Glacier2.Router._op_createSession.begin(self, ((userId, password), _response, _ex, _sent, _ctx))

        '''Create a per-client session with the router. If a
SessionManager has been installed, a proxy to a Session
object is returned to the client. Otherwise, null is returned
and only an internal session (i.e., not visible to the client)
is created.

If a session proxy is returned, it must be configured to route
through the router that created it. This will happen automatically
if the router is configured as the client's default router at the
time the session proxy is created in the client process, otherwise
the client must configure the session proxy explicitly.

Returns:
    A proxy for the newly created session, or null if no
SessionManager has been installed.

Arguments:
    userId The user id for which to check the password.

    password The password for the given user id.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.

    CannotCreateSessionException Raised if the session
cannot be created.'''
        def end_createSession(self, _r):
            return _M_Glacier2.Router._op_createSession.end(self, _r)

        '''Create a per-client session with the router. The user is
authenticated through the SSL certificates that have been
associated with the connection. If a SessionManager has been
installed, a proxy to a Session object is returned to the
client. Otherwise, null is returned and only an internal
session (i.e., not visible to the client) is created.

If a session proxy is returned, it must be configured to route
through the router that created it. This will happen automatically
if the router is configured as the client's default router at the
time the session proxy is created in the client process, otherwise
the client must configure the session proxy explicitly.

Returns:
    A proxy for the newly created session, or null if no
SessionManager has been installed.

Exceptions:
    PermissionDeniedException Raised if the user cannot be
authenticated or if the user is not allowed access.

    CannotCreateSessionException Raised if the session
cannot be created.'''
        def createSessionFromSecureConnection(self, _ctx=None):
            return _M_Glacier2.Router._op_createSessionFromSecureConnection.invoke(self, ((), _ctx))

        '''Create a per-client session with the router. The user is
authenticated through the SSL certificates that have been
associated with the connection. If a SessionManager has been
installed, a proxy to a Session object is returned to the
client. Otherwise, null is returned and only an internal
session (i.e., not visible to the client) is created.

If a session proxy is returned, it must be configured to route
through the router that created it. This will happen automatically
if the router is configured as the client's default router at the
time the session proxy is created in the client process, otherwise
the client must configure the session proxy explicitly.

Returns:
    A proxy for the newly created session, or null if no
SessionManager has been installed.

Exceptions:
    PermissionDeniedException Raised if the user cannot be
authenticated or if the user is not allowed access.

    CannotCreateSessionException Raised if the session
cannot be created.'''
        def begin_createSessionFromSecureConnection(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Glacier2.Router._op_createSessionFromSecureConnection.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Create a per-client session with the router. The user is
authenticated through the SSL certificates that have been
associated with the connection. If a SessionManager has been
installed, a proxy to a Session object is returned to the
client. Otherwise, null is returned and only an internal
session (i.e., not visible to the client) is created.

If a session proxy is returned, it must be configured to route
through the router that created it. This will happen automatically
if the router is configured as the client's default router at the
time the session proxy is created in the client process, otherwise
the client must configure the session proxy explicitly.

Returns:
    A proxy for the newly created session, or null if no
SessionManager has been installed.

Exceptions:
    PermissionDeniedException Raised if the user cannot be
authenticated or if the user is not allowed access.

    CannotCreateSessionException Raised if the session
cannot be created.'''
        def end_createSessionFromSecureConnection(self, _r):
            return _M_Glacier2.Router._op_createSessionFromSecureConnection.end(self, _r)

        '''Keep the calling client's session with this router alive.

Exceptions:
    SessionNotExistException Raised if no session exists
for the calling client.'''
        def refreshSession(self, _ctx=None):
            return _M_Glacier2.Router._op_refreshSession.invoke(self, ((), _ctx))

        '''Keep the calling client's session with this router alive.

Exceptions:
    SessionNotExistException Raised if no session exists
for the calling client.'''
        def begin_refreshSession(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Glacier2.Router._op_refreshSession.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Keep the calling client's session with this router alive.

Exceptions:
    SessionNotExistException Raised if no session exists
for the calling client.'''
        def end_refreshSession(self, _r):
            return _M_Glacier2.Router._op_refreshSession.end(self, _r)

        '''Keep the calling client's session with this router alive.

Exceptions:
    SessionNotExistException Raised if no session exists
for the calling client.'''
        def refreshSession_async(self, _cb, _ctx=None):
            return _M_Glacier2.Router._op_refreshSession.invokeAsync(self, (_cb, (), _ctx))

        '''Destroy the calling client's session with this router.

Exceptions:
    SessionNotExistException Raised if no session exists
for the calling client.'''
        def destroySession(self, _ctx=None):
            return _M_Glacier2.Router._op_destroySession.invoke(self, ((), _ctx))

        '''Destroy the calling client's session with this router.

Exceptions:
    SessionNotExistException Raised if no session exists
for the calling client.'''
        def begin_destroySession(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Glacier2.Router._op_destroySession.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Destroy the calling client's session with this router.

Exceptions:
    SessionNotExistException Raised if no session exists
for the calling client.'''
        def end_destroySession(self, _r):
            return _M_Glacier2.Router._op_destroySession.end(self, _r)

        '''Destroy the calling client's session with this router.

Exceptions:
    SessionNotExistException Raised if no session exists
for the calling client.'''
        def destroySession_async(self, _cb, _ctx=None):
            return _M_Glacier2.Router._op_destroySession.invokeAsync(self, (_cb, (), _ctx))

        '''Get the value of the session timeout. Sessions are destroyed
if they see no activity for this period of time.

Returns:
    The timeout (in seconds).'''
        def getSessionTimeout(self, _ctx=None):
            return _M_Glacier2.Router._op_getSessionTimeout.invoke(self, ((), _ctx))

        '''Get the value of the session timeout. Sessions are destroyed
if they see no activity for this period of time.

Returns:
    The timeout (in seconds).'''
        def begin_getSessionTimeout(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Glacier2.Router._op_getSessionTimeout.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Get the value of the session timeout. Sessions are destroyed
if they see no activity for this period of time.

Returns:
    The timeout (in seconds).'''
        def end_getSessionTimeout(self, _r):
            return _M_Glacier2.Router._op_getSessionTimeout.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Glacier2.RouterPrx.ice_checkedCast(proxy, '::Glacier2::Router', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Glacier2.RouterPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Glacier2._t_RouterPrx = IcePy.defineProxy('::Glacier2::Router', RouterPrx)

    _M_Glacier2._t_Router = IcePy.defineClass('::Glacier2::Router', Router, (), True, None, (_M_Ice._t_Router,), ())
    Router._ice_type = _M_Glacier2._t_Router

    Router._op_getCategoryForClient = IcePy.Operation('getCategoryForClient', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), IcePy._t_string, ())
    Router._op_createSession = IcePy.Operation('createSession', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), _M_Glacier2._t_SessionPrx, (_M_Glacier2._t_PermissionDeniedException, _M_Glacier2._t_CannotCreateSessionException))
    Router._op_createSessionFromSecureConnection = IcePy.Operation('createSessionFromSecureConnection', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (), (), _M_Glacier2._t_SessionPrx, (_M_Glacier2._t_PermissionDeniedException, _M_Glacier2._t_CannotCreateSessionException))
    Router._op_refreshSession = IcePy.Operation('refreshSession', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, (_M_Glacier2._t_SessionNotExistException,))
    Router._op_destroySession = IcePy.Operation('destroySession', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, (_M_Glacier2._t_SessionNotExistException,))
    Router._op_getSessionTimeout = IcePy.Operation('getSessionTimeout', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), IcePy._t_long, ())

    _M_Glacier2.Router = Router
    del Router

    _M_Glacier2.RouterPrx = RouterPrx
    del RouterPrx

if not _M_Glacier2.__dict__.has_key('Admin'):
    _M_Glacier2.Admin = Ice.createTempClass()
    class Admin(Ice.Object):
        '''The Glacier2 administrative interface. This must only be
accessible from inside the firewall.'''
        def __init__(self):
            if __builtin__.type(self) == _M_Glacier2.Admin:
                raise RuntimeError('Glacier2.Admin is an abstract class')

        def ice_ids(self, current=None):
            return ('::Glacier2::Admin', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Glacier2::Admin'

        def ice_staticId():
            return '::Glacier2::Admin'
        ice_staticId = staticmethod(ice_staticId)

        def shutdown(self, current=None):
            '''Shut down the Glacier2 router.'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_Glacier2._t_Admin)

        __repr__ = __str__

    _M_Glacier2.AdminPrx = Ice.createTempClass()
    class AdminPrx(Ice.ObjectPrx):

        '''Shut down the Glacier2 router.'''
        def shutdown(self, _ctx=None):
            return _M_Glacier2.Admin._op_shutdown.invoke(self, ((), _ctx))

        '''Shut down the Glacier2 router.'''
        def begin_shutdown(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Glacier2.Admin._op_shutdown.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Shut down the Glacier2 router.'''
        def end_shutdown(self, _r):
            return _M_Glacier2.Admin._op_shutdown.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Glacier2.AdminPrx.ice_checkedCast(proxy, '::Glacier2::Admin', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Glacier2.AdminPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Glacier2._t_AdminPrx = IcePy.defineProxy('::Glacier2::Admin', AdminPrx)

    _M_Glacier2._t_Admin = IcePy.defineClass('::Glacier2::Admin', Admin, (), True, None, (), ())
    Admin._ice_type = _M_Glacier2._t_Admin

    Admin._op_shutdown = IcePy.Operation('shutdown', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, ())

    _M_Glacier2.Admin = Admin
    del Admin

    _M_Glacier2.AdminPrx = AdminPrx
    del AdminPrx

# End of module Glacier2
