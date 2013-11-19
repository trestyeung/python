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
# Generated from file `Exception.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>

import Ice, IcePy, __builtin__
import Ice_Identity_ice
import Ice_BuiltinSequences_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module IceGrid
_M_IceGrid = Ice.openModule('IceGrid')
__name__ = 'IceGrid'

if not _M_IceGrid.__dict__.has_key('ApplicationNotExistException'):
    _M_IceGrid.ApplicationNotExistException = Ice.createTempClass()
    class ApplicationNotExistException(Ice.UserException):
        '''This exception is raised if an application does not exist.'''
        def __init__(self, name=''):
            self.name = name

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::ApplicationNotExistException'

    _M_IceGrid._t_ApplicationNotExistException = IcePy.defineException('::IceGrid::ApplicationNotExistException', ApplicationNotExistException, (), None, (('name', (), IcePy._t_string),))
    ApplicationNotExistException._ice_type = _M_IceGrid._t_ApplicationNotExistException

    _M_IceGrid.ApplicationNotExistException = ApplicationNotExistException
    del ApplicationNotExistException

if not _M_IceGrid.__dict__.has_key('ServerNotExistException'):
    _M_IceGrid.ServerNotExistException = Ice.createTempClass()
    class ServerNotExistException(Ice.UserException):
        '''This exception is raised if a server does not exist.'''
        def __init__(self, id=''):
            self.id = id

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::ServerNotExistException'

    _M_IceGrid._t_ServerNotExistException = IcePy.defineException('::IceGrid::ServerNotExistException', ServerNotExistException, (), None, (('id', (), IcePy._t_string),))
    ServerNotExistException._ice_type = _M_IceGrid._t_ServerNotExistException

    _M_IceGrid.ServerNotExistException = ServerNotExistException
    del ServerNotExistException

if not _M_IceGrid.__dict__.has_key('ServerStartException'):
    _M_IceGrid.ServerStartException = Ice.createTempClass()
    class ServerStartException(Ice.UserException):
        '''This exception is raised if a server failed to start.'''
        def __init__(self, id='', reason=''):
            self.id = id
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::ServerStartException'

    _M_IceGrid._t_ServerStartException = IcePy.defineException('::IceGrid::ServerStartException', ServerStartException, (), None, (
        ('id', (), IcePy._t_string),
        ('reason', (), IcePy._t_string)
    ))
    ServerStartException._ice_type = _M_IceGrid._t_ServerStartException

    _M_IceGrid.ServerStartException = ServerStartException
    del ServerStartException

if not _M_IceGrid.__dict__.has_key('ServerStopException'):
    _M_IceGrid.ServerStopException = Ice.createTempClass()
    class ServerStopException(Ice.UserException):
        '''This exception is raised if a server failed to stop.'''
        def __init__(self, id='', reason=''):
            self.id = id
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::ServerStopException'

    _M_IceGrid._t_ServerStopException = IcePy.defineException('::IceGrid::ServerStopException', ServerStopException, (), None, (
        ('id', (), IcePy._t_string),
        ('reason', (), IcePy._t_string)
    ))
    ServerStopException._ice_type = _M_IceGrid._t_ServerStopException

    _M_IceGrid.ServerStopException = ServerStopException
    del ServerStopException

if not _M_IceGrid.__dict__.has_key('AdapterNotExistException'):
    _M_IceGrid.AdapterNotExistException = Ice.createTempClass()
    class AdapterNotExistException(Ice.UserException):
        '''This exception is raised if an adapter does not exist.'''
        def __init__(self, id=''):
            self.id = id

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::AdapterNotExistException'

    _M_IceGrid._t_AdapterNotExistException = IcePy.defineException('::IceGrid::AdapterNotExistException', AdapterNotExistException, (), None, (('id', (), IcePy._t_string),))
    AdapterNotExistException._ice_type = _M_IceGrid._t_AdapterNotExistException

    _M_IceGrid.AdapterNotExistException = AdapterNotExistException
    del AdapterNotExistException

if not _M_IceGrid.__dict__.has_key('ObjectExistsException'):
    _M_IceGrid.ObjectExistsException = Ice.createTempClass()
    class ObjectExistsException(Ice.UserException):
        '''This exception is raised if an object already exists.'''
        def __init__(self, id=Ice._struct_marker):
            if id is Ice._struct_marker:
                self.id = _M_Ice.Identity()
            else:
                self.id = id

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::ObjectExistsException'

    _M_IceGrid._t_ObjectExistsException = IcePy.defineException('::IceGrid::ObjectExistsException', ObjectExistsException, (), None, (('id', (), _M_Ice._t_Identity),))
    ObjectExistsException._ice_type = _M_IceGrid._t_ObjectExistsException

    _M_IceGrid.ObjectExistsException = ObjectExistsException
    del ObjectExistsException

if not _M_IceGrid.__dict__.has_key('ObjectNotRegisteredException'):
    _M_IceGrid.ObjectNotRegisteredException = Ice.createTempClass()
    class ObjectNotRegisteredException(Ice.UserException):
        '''This exception is raised if an object is not registered.'''
        def __init__(self, id=Ice._struct_marker):
            if id is Ice._struct_marker:
                self.id = _M_Ice.Identity()
            else:
                self.id = id

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::ObjectNotRegisteredException'

    _M_IceGrid._t_ObjectNotRegisteredException = IcePy.defineException('::IceGrid::ObjectNotRegisteredException', ObjectNotRegisteredException, (), None, (('id', (), _M_Ice._t_Identity),))
    ObjectNotRegisteredException._ice_type = _M_IceGrid._t_ObjectNotRegisteredException

    _M_IceGrid.ObjectNotRegisteredException = ObjectNotRegisteredException
    del ObjectNotRegisteredException

if not _M_IceGrid.__dict__.has_key('NodeNotExistException'):
    _M_IceGrid.NodeNotExistException = Ice.createTempClass()
    class NodeNotExistException(Ice.UserException):
        '''This exception is raised if a node does not exist.'''
        def __init__(self, name=''):
            self.name = name

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::NodeNotExistException'

    _M_IceGrid._t_NodeNotExistException = IcePy.defineException('::IceGrid::NodeNotExistException', NodeNotExistException, (), None, (('name', (), IcePy._t_string),))
    NodeNotExistException._ice_type = _M_IceGrid._t_NodeNotExistException

    _M_IceGrid.NodeNotExistException = NodeNotExistException
    del NodeNotExistException

if not _M_IceGrid.__dict__.has_key('RegistryNotExistException'):
    _M_IceGrid.RegistryNotExistException = Ice.createTempClass()
    class RegistryNotExistException(Ice.UserException):
        '''This exception is raised if a registry does not exist.'''
        def __init__(self, name=''):
            self.name = name

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::RegistryNotExistException'

    _M_IceGrid._t_RegistryNotExistException = IcePy.defineException('::IceGrid::RegistryNotExistException', RegistryNotExistException, (), None, (('name', (), IcePy._t_string),))
    RegistryNotExistException._ice_type = _M_IceGrid._t_RegistryNotExistException

    _M_IceGrid.RegistryNotExistException = RegistryNotExistException
    del RegistryNotExistException

if not _M_IceGrid.__dict__.has_key('DeploymentException'):
    _M_IceGrid.DeploymentException = Ice.createTempClass()
    class DeploymentException(Ice.UserException):
        '''An exception for deployment errors.'''
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::DeploymentException'

    _M_IceGrid._t_DeploymentException = IcePy.defineException('::IceGrid::DeploymentException', DeploymentException, (), None, (('reason', (), IcePy._t_string),))
    DeploymentException._ice_type = _M_IceGrid._t_DeploymentException

    _M_IceGrid.DeploymentException = DeploymentException
    del DeploymentException

if not _M_IceGrid.__dict__.has_key('NodeUnreachableException'):
    _M_IceGrid.NodeUnreachableException = Ice.createTempClass()
    class NodeUnreachableException(Ice.UserException):
        '''This exception is raised if a node could not be reached.'''
        def __init__(self, name='', reason=''):
            self.name = name
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::NodeUnreachableException'

    _M_IceGrid._t_NodeUnreachableException = IcePy.defineException('::IceGrid::NodeUnreachableException', NodeUnreachableException, (), None, (
        ('name', (), IcePy._t_string),
        ('reason', (), IcePy._t_string)
    ))
    NodeUnreachableException._ice_type = _M_IceGrid._t_NodeUnreachableException

    _M_IceGrid.NodeUnreachableException = NodeUnreachableException
    del NodeUnreachableException

if not _M_IceGrid.__dict__.has_key('ServerUnreachableException'):
    _M_IceGrid.ServerUnreachableException = Ice.createTempClass()
    class ServerUnreachableException(Ice.UserException):
        '''This exception is raised if a server could not be reached.'''
        def __init__(self, name='', reason=''):
            self.name = name
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::ServerUnreachableException'

    _M_IceGrid._t_ServerUnreachableException = IcePy.defineException('::IceGrid::ServerUnreachableException', ServerUnreachableException, (), None, (
        ('name', (), IcePy._t_string),
        ('reason', (), IcePy._t_string)
    ))
    ServerUnreachableException._ice_type = _M_IceGrid._t_ServerUnreachableException

    _M_IceGrid.ServerUnreachableException = ServerUnreachableException
    del ServerUnreachableException

if not _M_IceGrid.__dict__.has_key('RegistryUnreachableException'):
    _M_IceGrid.RegistryUnreachableException = Ice.createTempClass()
    class RegistryUnreachableException(Ice.UserException):
        '''This exception is raised if a registry could not be reached.'''
        def __init__(self, name='', reason=''):
            self.name = name
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::RegistryUnreachableException'

    _M_IceGrid._t_RegistryUnreachableException = IcePy.defineException('::IceGrid::RegistryUnreachableException', RegistryUnreachableException, (), None, (
        ('name', (), IcePy._t_string),
        ('reason', (), IcePy._t_string)
    ))
    RegistryUnreachableException._ice_type = _M_IceGrid._t_RegistryUnreachableException

    _M_IceGrid.RegistryUnreachableException = RegistryUnreachableException
    del RegistryUnreachableException

if not _M_IceGrid.__dict__.has_key('BadSignalException'):
    _M_IceGrid.BadSignalException = Ice.createTempClass()
    class BadSignalException(Ice.UserException):
        '''This exception is raised if an unknown signal was sent to
to a server.'''
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::BadSignalException'

    _M_IceGrid._t_BadSignalException = IcePy.defineException('::IceGrid::BadSignalException', BadSignalException, (), None, (('reason', (), IcePy._t_string),))
    BadSignalException._ice_type = _M_IceGrid._t_BadSignalException

    _M_IceGrid.BadSignalException = BadSignalException
    del BadSignalException

if not _M_IceGrid.__dict__.has_key('PatchException'):
    _M_IceGrid.PatchException = Ice.createTempClass()
    class PatchException(Ice.UserException):
        '''This exception is raised if a patch failed.'''
        def __init__(self, reasons=None):
            self.reasons = reasons

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::PatchException'

    _M_IceGrid._t_PatchException = IcePy.defineException('::IceGrid::PatchException', PatchException, (), None, (('reasons', (), _M_Ice._t_StringSeq),))
    PatchException._ice_type = _M_IceGrid._t_PatchException

    _M_IceGrid.PatchException = PatchException
    del PatchException

if not _M_IceGrid.__dict__.has_key('AccessDeniedException'):
    _M_IceGrid.AccessDeniedException = Ice.createTempClass()
    class AccessDeniedException(Ice.UserException):
        '''This exception is raised if a registry lock wasn't
acquired or is already held by a session.'''
        def __init__(self, lockUserId=''):
            self.lockUserId = lockUserId

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::AccessDeniedException'

    _M_IceGrid._t_AccessDeniedException = IcePy.defineException('::IceGrid::AccessDeniedException', AccessDeniedException, (), None, (('lockUserId', (), IcePy._t_string),))
    AccessDeniedException._ice_type = _M_IceGrid._t_AccessDeniedException

    _M_IceGrid.AccessDeniedException = AccessDeniedException
    del AccessDeniedException

if not _M_IceGrid.__dict__.has_key('AllocationException'):
    _M_IceGrid.AllocationException = Ice.createTempClass()
    class AllocationException(Ice.UserException):
        '''This exception is raised if the allocation of an object failed.'''
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::AllocationException'

    _M_IceGrid._t_AllocationException = IcePy.defineException('::IceGrid::AllocationException', AllocationException, (), None, (('reason', (), IcePy._t_string),))
    AllocationException._ice_type = _M_IceGrid._t_AllocationException

    _M_IceGrid.AllocationException = AllocationException
    del AllocationException

if not _M_IceGrid.__dict__.has_key('AllocationTimeoutException'):
    _M_IceGrid.AllocationTimeoutException = Ice.createTempClass()
    class AllocationTimeoutException(_M_IceGrid.AllocationException):
        '''This exception is raised if the request to allocate an object times
out.'''
        def __init__(self, reason=''):
            _M_IceGrid.AllocationException.__init__(self, reason)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::AllocationTimeoutException'

    _M_IceGrid._t_AllocationTimeoutException = IcePy.defineException('::IceGrid::AllocationTimeoutException', AllocationTimeoutException, (), _M_IceGrid._t_AllocationException, ())
    AllocationTimeoutException._ice_type = _M_IceGrid._t_AllocationTimeoutException

    _M_IceGrid.AllocationTimeoutException = AllocationTimeoutException
    del AllocationTimeoutException

if not _M_IceGrid.__dict__.has_key('PermissionDeniedException'):
    _M_IceGrid.PermissionDeniedException = Ice.createTempClass()
    class PermissionDeniedException(Ice.UserException):
        '''This exception is raised if a client is denied the ability to create
a session with IceGrid.'''
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::PermissionDeniedException'

    _M_IceGrid._t_PermissionDeniedException = IcePy.defineException('::IceGrid::PermissionDeniedException', PermissionDeniedException, (), None, (('reason', (), IcePy._t_string),))
    PermissionDeniedException._ice_type = _M_IceGrid._t_PermissionDeniedException

    _M_IceGrid.PermissionDeniedException = PermissionDeniedException
    del PermissionDeniedException

if not _M_IceGrid.__dict__.has_key('ObserverAlreadyRegisteredException'):
    _M_IceGrid.ObserverAlreadyRegisteredException = Ice.createTempClass()
    class ObserverAlreadyRegisteredException(Ice.UserException):
        '''This exception is raised if an observer is already registered with
the registry.'''
        def __init__(self, id=Ice._struct_marker):
            if id is Ice._struct_marker:
                self.id = _M_Ice.Identity()
            else:
                self.id = id

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::ObserverAlreadyRegisteredException'

    _M_IceGrid._t_ObserverAlreadyRegisteredException = IcePy.defineException('::IceGrid::ObserverAlreadyRegisteredException', ObserverAlreadyRegisteredException, (), None, (('id', (), _M_Ice._t_Identity),))
    ObserverAlreadyRegisteredException._ice_type = _M_IceGrid._t_ObserverAlreadyRegisteredException

    _M_IceGrid.ObserverAlreadyRegisteredException = ObserverAlreadyRegisteredException
    del ObserverAlreadyRegisteredException

if not _M_IceGrid.__dict__.has_key('FileNotAvailableException'):
    _M_IceGrid.FileNotAvailableException = Ice.createTempClass()
    class FileNotAvailableException(Ice.UserException):
        '''This exception is raised if a file is not available.'''
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::FileNotAvailableException'

    _M_IceGrid._t_FileNotAvailableException = IcePy.defineException('::IceGrid::FileNotAvailableException', FileNotAvailableException, (), None, (('reason', (), IcePy._t_string),))
    FileNotAvailableException._ice_type = _M_IceGrid._t_FileNotAvailableException

    _M_IceGrid.FileNotAvailableException = FileNotAvailableException
    del FileNotAvailableException

# End of module IceGrid
