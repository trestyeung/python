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
# Generated from file `IceBox.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>

import Ice, IcePy, __builtin__
import Ice_BuiltinSequences_ice
import Ice_CommunicatorF_ice
import Ice_PropertiesF_ice
import Ice_SliceChecksumDict_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module IceBox
_M_IceBox = Ice.openModule('IceBox')
__name__ = 'IceBox'
_M_IceBox.__doc__ = '''IceBox is an application server specifically for Ice
applications. IceBox can easily run and administer Ice services
that are dynamically loaded as a DLL, shared library, or Java
class.'''

if not _M_IceBox.__dict__.has_key('FailureException'):
    _M_IceBox.FailureException = Ice.createTempClass()
    class FailureException(Ice.LocalException):
        '''This exception is a general failure notification. It is thrown
for errors such as a service encountering an error during
initialization, or the service manager being unable
to load a service executable.'''
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceBox::FailureException'

    _M_IceBox._t_FailureException = IcePy.defineException('::IceBox::FailureException', FailureException, (), None, (('reason', (), IcePy._t_string),))
    FailureException._ice_type = _M_IceBox._t_FailureException

    _M_IceBox.FailureException = FailureException
    del FailureException

if not _M_IceBox.__dict__.has_key('AlreadyStartedException'):
    _M_IceBox.AlreadyStartedException = Ice.createTempClass()
    class AlreadyStartedException(Ice.UserException):
        '''This exception is thrown if an attempt is made to start an
already-started service.'''
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceBox::AlreadyStartedException'

    _M_IceBox._t_AlreadyStartedException = IcePy.defineException('::IceBox::AlreadyStartedException', AlreadyStartedException, (), None, ())
    AlreadyStartedException._ice_type = _M_IceBox._t_AlreadyStartedException

    _M_IceBox.AlreadyStartedException = AlreadyStartedException
    del AlreadyStartedException

if not _M_IceBox.__dict__.has_key('AlreadyStoppedException'):
    _M_IceBox.AlreadyStoppedException = Ice.createTempClass()
    class AlreadyStoppedException(Ice.UserException):
        '''This exception is thrown if an attempt is made to stop an
already-stopped service.'''
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceBox::AlreadyStoppedException'

    _M_IceBox._t_AlreadyStoppedException = IcePy.defineException('::IceBox::AlreadyStoppedException', AlreadyStoppedException, (), None, ())
    AlreadyStoppedException._ice_type = _M_IceBox._t_AlreadyStoppedException

    _M_IceBox.AlreadyStoppedException = AlreadyStoppedException
    del AlreadyStoppedException

if not _M_IceBox.__dict__.has_key('NoSuchServiceException'):
    _M_IceBox.NoSuchServiceException = Ice.createTempClass()
    class NoSuchServiceException(Ice.UserException):
        '''This exception is thrown if a service name does not refer
to an existing service.'''
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceBox::NoSuchServiceException'

    _M_IceBox._t_NoSuchServiceException = IcePy.defineException('::IceBox::NoSuchServiceException', NoSuchServiceException, (), None, ())
    NoSuchServiceException._ice_type = _M_IceBox._t_NoSuchServiceException

    _M_IceBox.NoSuchServiceException = NoSuchServiceException
    del NoSuchServiceException

if not _M_IceBox.__dict__.has_key('Service'):
    _M_IceBox.Service = Ice.createTempClass()
    class Service(object):
        '''An application service managed by a ServiceManager.'''
        def __init__(self):
            if __builtin__.type(self) == _M_IceBox.Service:
                raise RuntimeError('IceBox.Service is an abstract class')

        def start(self, name, communicator, args):
            '''Start the service. The given communicator is created by the
ServiceManager for use by the service. This communicator may
also be used by other services, depending on the service
configuration.

The ServiceManager owns this communicator, and is
responsible for destroying it.

Arguments:
    name The service's name, as determined by the
configuration.

    communicator A communicator for use by the service.

    args The service arguments that were not converted into
properties.

Exceptions:
    FailureException Raised if start failed.'''
            pass

        def stop(self):
            '''Stop the service.'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_IceBox._t_Service)

        __repr__ = __str__

    _M_IceBox._t_Service = IcePy.defineClass('::IceBox::Service', Service, (), True, None, (), ())
    Service._ice_type = _M_IceBox._t_Service

    _M_IceBox.Service = Service
    del Service

if not _M_IceBox.__dict__.has_key('ServiceObserver'):
    _M_IceBox.ServiceObserver = Ice.createTempClass()
    class ServiceObserver(Ice.Object):
        '''An Observer interface implemented by admin clients
interested in the status of services'''
        def __init__(self):
            if __builtin__.type(self) == _M_IceBox.ServiceObserver:
                raise RuntimeError('IceBox.ServiceObserver is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceBox::ServiceObserver')

        def ice_id(self, current=None):
            return '::IceBox::ServiceObserver'

        def ice_staticId():
            return '::IceBox::ServiceObserver'
        ice_staticId = staticmethod(ice_staticId)

        def servicesStarted(self, services, current=None):
            pass

        def servicesStopped(self, services, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_IceBox._t_ServiceObserver)

        __repr__ = __str__

    _M_IceBox.ServiceObserverPrx = Ice.createTempClass()
    class ServiceObserverPrx(Ice.ObjectPrx):

        def servicesStarted(self, services, _ctx=None):
            return _M_IceBox.ServiceObserver._op_servicesStarted.invoke(self, ((services, ), _ctx))

        def begin_servicesStarted(self, services, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceBox.ServiceObserver._op_servicesStarted.begin(self, ((services, ), _response, _ex, _sent, _ctx))

        def end_servicesStarted(self, _r):
            return _M_IceBox.ServiceObserver._op_servicesStarted.end(self, _r)

        def servicesStarted_async(self, _cb, services, _ctx=None):
            return _M_IceBox.ServiceObserver._op_servicesStarted.invokeAsync(self, (_cb, (services, ), _ctx))

        def servicesStopped(self, services, _ctx=None):
            return _M_IceBox.ServiceObserver._op_servicesStopped.invoke(self, ((services, ), _ctx))

        def begin_servicesStopped(self, services, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceBox.ServiceObserver._op_servicesStopped.begin(self, ((services, ), _response, _ex, _sent, _ctx))

        def end_servicesStopped(self, _r):
            return _M_IceBox.ServiceObserver._op_servicesStopped.end(self, _r)

        def servicesStopped_async(self, _cb, services, _ctx=None):
            return _M_IceBox.ServiceObserver._op_servicesStopped.invokeAsync(self, (_cb, (services, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceBox.ServiceObserverPrx.ice_checkedCast(proxy, '::IceBox::ServiceObserver', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceBox.ServiceObserverPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceBox._t_ServiceObserverPrx = IcePy.defineProxy('::IceBox::ServiceObserver', ServiceObserverPrx)

    _M_IceBox._t_ServiceObserver = IcePy.defineClass('::IceBox::ServiceObserver', ServiceObserver, (), True, None, (), ())
    ServiceObserver._ice_type = _M_IceBox._t_ServiceObserver

    ServiceObserver._op_servicesStarted = IcePy.Operation('servicesStarted', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_Ice._t_StringSeq),), (), None, ())
    ServiceObserver._op_servicesStopped = IcePy.Operation('servicesStopped', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_Ice._t_StringSeq),), (), None, ())

    _M_IceBox.ServiceObserver = ServiceObserver
    del ServiceObserver

    _M_IceBox.ServiceObserverPrx = ServiceObserverPrx
    del ServiceObserverPrx

if not _M_IceBox.__dict__.has_key('ServiceManager'):
    _M_IceBox.ServiceManager = Ice.createTempClass()
    class ServiceManager(Ice.Object):
        '''Administers a set of Service instances.'''
        def __init__(self):
            if __builtin__.type(self) == _M_IceBox.ServiceManager:
                raise RuntimeError('IceBox.ServiceManager is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceBox::ServiceManager')

        def ice_id(self, current=None):
            return '::IceBox::ServiceManager'

        def ice_staticId():
            return '::IceBox::ServiceManager'
        ice_staticId = staticmethod(ice_staticId)

        def getSliceChecksums(self, current=None):
            '''Returns the checksums for the IceBox Slice definitions.

Returns:
    A dictionary mapping Slice type ids to their checksums.'''
            pass

        def startService(self, service, current=None):
            '''Start an individual service.

Arguments:
    service The service name.'''
            pass

        def stopService(self, service, current=None):
            '''Stop an individual service.

Arguments:
    service The service name.'''
            pass

        def addObserver(self, observer, current=None):
            '''Registers a new observer with the ServiceManager.

Arguments:
    observer The new observer'''
            pass

        def shutdown(self, current=None):
            '''Shut down all services. This causes Service#stop to be
invoked on all configured services.'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_IceBox._t_ServiceManager)

        __repr__ = __str__

    _M_IceBox.ServiceManagerPrx = Ice.createTempClass()
    class ServiceManagerPrx(Ice.ObjectPrx):

        '''Returns the checksums for the IceBox Slice definitions.

Returns:
    A dictionary mapping Slice type ids to their checksums.'''
        def getSliceChecksums(self, _ctx=None):
            return _M_IceBox.ServiceManager._op_getSliceChecksums.invoke(self, ((), _ctx))

        '''Returns the checksums for the IceBox Slice definitions.

Returns:
    A dictionary mapping Slice type ids to their checksums.'''
        def begin_getSliceChecksums(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceBox.ServiceManager._op_getSliceChecksums.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Returns the checksums for the IceBox Slice definitions.

Returns:
    A dictionary mapping Slice type ids to their checksums.'''
        def end_getSliceChecksums(self, _r):
            return _M_IceBox.ServiceManager._op_getSliceChecksums.end(self, _r)

        '''Start an individual service.

Arguments:
    service The service name.'''
        def startService(self, service, _ctx=None):
            return _M_IceBox.ServiceManager._op_startService.invoke(self, ((service, ), _ctx))

        '''Start an individual service.

Arguments:
    service The service name.'''
        def begin_startService(self, service, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceBox.ServiceManager._op_startService.begin(self, ((service, ), _response, _ex, _sent, _ctx))

        '''Start an individual service.

Arguments:
    service The service name.'''
        def end_startService(self, _r):
            return _M_IceBox.ServiceManager._op_startService.end(self, _r)

        '''Start an individual service.

Arguments:
    service The service name.'''
        def startService_async(self, _cb, service, _ctx=None):
            return _M_IceBox.ServiceManager._op_startService.invokeAsync(self, (_cb, (service, ), _ctx))

        '''Stop an individual service.

Arguments:
    service The service name.'''
        def stopService(self, service, _ctx=None):
            return _M_IceBox.ServiceManager._op_stopService.invoke(self, ((service, ), _ctx))

        '''Stop an individual service.

Arguments:
    service The service name.'''
        def begin_stopService(self, service, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceBox.ServiceManager._op_stopService.begin(self, ((service, ), _response, _ex, _sent, _ctx))

        '''Stop an individual service.

Arguments:
    service The service name.'''
        def end_stopService(self, _r):
            return _M_IceBox.ServiceManager._op_stopService.end(self, _r)

        '''Stop an individual service.

Arguments:
    service The service name.'''
        def stopService_async(self, _cb, service, _ctx=None):
            return _M_IceBox.ServiceManager._op_stopService.invokeAsync(self, (_cb, (service, ), _ctx))

        '''Registers a new observer with the ServiceManager.

Arguments:
    observer The new observer'''
        def addObserver(self, observer, _ctx=None):
            return _M_IceBox.ServiceManager._op_addObserver.invoke(self, ((observer, ), _ctx))

        '''Registers a new observer with the ServiceManager.

Arguments:
    observer The new observer'''
        def begin_addObserver(self, observer, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceBox.ServiceManager._op_addObserver.begin(self, ((observer, ), _response, _ex, _sent, _ctx))

        '''Registers a new observer with the ServiceManager.

Arguments:
    observer The new observer'''
        def end_addObserver(self, _r):
            return _M_IceBox.ServiceManager._op_addObserver.end(self, _r)

        '''Registers a new observer with the ServiceManager.

Arguments:
    observer The new observer'''
        def addObserver_async(self, _cb, observer, _ctx=None):
            return _M_IceBox.ServiceManager._op_addObserver.invokeAsync(self, (_cb, (observer, ), _ctx))

        '''Shut down all services. This causes Service#stop to be
invoked on all configured services.'''
        def shutdown(self, _ctx=None):
            return _M_IceBox.ServiceManager._op_shutdown.invoke(self, ((), _ctx))

        '''Shut down all services. This causes Service#stop to be
invoked on all configured services.'''
        def begin_shutdown(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceBox.ServiceManager._op_shutdown.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Shut down all services. This causes Service#stop to be
invoked on all configured services.'''
        def end_shutdown(self, _r):
            return _M_IceBox.ServiceManager._op_shutdown.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceBox.ServiceManagerPrx.ice_checkedCast(proxy, '::IceBox::ServiceManager', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceBox.ServiceManagerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceBox._t_ServiceManagerPrx = IcePy.defineProxy('::IceBox::ServiceManager', ServiceManagerPrx)

    _M_IceBox._t_ServiceManager = IcePy.defineClass('::IceBox::ServiceManager', ServiceManager, (), True, None, (), ())
    ServiceManager._ice_type = _M_IceBox._t_ServiceManager

    ServiceManager._op_getSliceChecksums = IcePy.Operation('getSliceChecksums', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_Ice._t_SliceChecksumDict, ())
    ServiceManager._op_startService = IcePy.Operation('startService', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), None, (_M_IceBox._t_AlreadyStartedException, _M_IceBox._t_NoSuchServiceException))
    ServiceManager._op_stopService = IcePy.Operation('stopService', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), None, (_M_IceBox._t_AlreadyStoppedException, _M_IceBox._t_NoSuchServiceException))
    ServiceManager._op_addObserver = IcePy.Operation('addObserver', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_IceBox._t_ServiceObserverPrx),), (), None, ())
    ServiceManager._op_shutdown = IcePy.Operation('shutdown', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), None, ())

    _M_IceBox.ServiceManager = ServiceManager
    del ServiceManager

    _M_IceBox.ServiceManagerPrx = ServiceManagerPrx
    del ServiceManagerPrx

# End of module IceBox
