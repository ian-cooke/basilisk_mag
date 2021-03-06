# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_thrFiringRemainder')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_thrFiringRemainder')
    _thrFiringRemainder = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_thrFiringRemainder', [dirname(__file__)])
        except ImportError:
            import _thrFiringRemainder
            return _thrFiringRemainder
        try:
            _mod = imp.load_module('_thrFiringRemainder', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _thrFiringRemainder = swig_import_helper()
    del swig_import_helper
else:
    import _thrFiringRemainder
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def new_doubleArray(nelements):
    return _thrFiringRemainder.new_doubleArray(nelements)
new_doubleArray = _thrFiringRemainder.new_doubleArray

def delete_doubleArray(ary):
    return _thrFiringRemainder.delete_doubleArray(ary)
delete_doubleArray = _thrFiringRemainder.delete_doubleArray

def doubleArray_getitem(ary, index):
    return _thrFiringRemainder.doubleArray_getitem(ary, index)
doubleArray_getitem = _thrFiringRemainder.doubleArray_getitem

def doubleArray_setitem(ary, index, value):
    return _thrFiringRemainder.doubleArray_setitem(ary, index, value)
doubleArray_setitem = _thrFiringRemainder.doubleArray_setitem

def new_longArray(nelements):
    return _thrFiringRemainder.new_longArray(nelements)
new_longArray = _thrFiringRemainder.new_longArray

def delete_longArray(ary):
    return _thrFiringRemainder.delete_longArray(ary)
delete_longArray = _thrFiringRemainder.delete_longArray

def longArray_getitem(ary, index):
    return _thrFiringRemainder.longArray_getitem(ary, index)
longArray_getitem = _thrFiringRemainder.longArray_getitem

def longArray_setitem(ary, index, value):
    return _thrFiringRemainder.longArray_setitem(ary, index, value)
longArray_setitem = _thrFiringRemainder.longArray_setitem

def new_intArray(nelements):
    return _thrFiringRemainder.new_intArray(nelements)
new_intArray = _thrFiringRemainder.new_intArray

def delete_intArray(ary):
    return _thrFiringRemainder.delete_intArray(ary)
delete_intArray = _thrFiringRemainder.delete_intArray

def intArray_getitem(ary, index):
    return _thrFiringRemainder.intArray_getitem(ary, index)
intArray_getitem = _thrFiringRemainder.intArray_getitem

def intArray_setitem(ary, index, value):
    return _thrFiringRemainder.intArray_setitem(ary, index, value)
intArray_setitem = _thrFiringRemainder.intArray_setitem

def new_shortArray(nelements):
    return _thrFiringRemainder.new_shortArray(nelements)
new_shortArray = _thrFiringRemainder.new_shortArray

def delete_shortArray(ary):
    return _thrFiringRemainder.delete_shortArray(ary)
delete_shortArray = _thrFiringRemainder.delete_shortArray

def shortArray_getitem(ary, index):
    return _thrFiringRemainder.shortArray_getitem(ary, index)
shortArray_getitem = _thrFiringRemainder.shortArray_getitem

def shortArray_setitem(ary, index, value):
    return _thrFiringRemainder.shortArray_setitem(ary, index, value)
shortArray_setitem = _thrFiringRemainder.shortArray_setitem


def getStructSize(self):
    try:
        return eval('sizeof_' + repr(self).split(';')[0].split('.')[-1])
    except (NameError) as e:
        typeString = 'sizeof_' + repr(self).split(';')[0].split('.')[-1]
        raise NameError(e.message + '\nYou tried to get this size macro: ' + typeString + 
            '\n It appears to be undefined.  \nYou need to run the SWIG GEN_SIZEOF' +  
            ' SWIG macro against the class/struct in your SWIG file if you want to ' + 
            ' make this call.\n')


def protectSetAttr(self, name, value):
    if(hasattr(self, name) or name == 'this'):
        object.__setattr__(self, name, value)
    else:
        raise ValueError('You tried to add this variable: ' + name + '\n' + 
            'To this class: ' + str(self))

def protectAllClasses(moduleType):
    import inspect
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for member in clsmembers:
        try:
            exec(str(member[0]) + '.__setattr__ = protectSetAttr')
            exec(str(member[0]) + '.getStructSize = getStructSize') 
        except (AttributeError, TypeError) as e:
            pass


Update_thrFiringRemainder = _thrFiringRemainder.Update_thrFiringRemainder
SelfInit_thrFiringRemainder = _thrFiringRemainder.SelfInit_thrFiringRemainder
CrossInit_thrFiringRemainder = _thrFiringRemainder.CrossInit_thrFiringRemainder
Reset_thrFiringRemainder = _thrFiringRemainder.Reset_thrFiringRemainder
sizeof_thrFiringRemainderConfig = _thrFiringRemainder.sizeof_thrFiringRemainderConfig
class thrFiringRemainderConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, thrFiringRemainderConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, thrFiringRemainderConfig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["pulseRemainder"] = _thrFiringRemainder.thrFiringRemainderConfig_pulseRemainder_set
    __swig_getmethods__["pulseRemainder"] = _thrFiringRemainder.thrFiringRemainderConfig_pulseRemainder_get
    if _newclass:
        pulseRemainder = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_pulseRemainder_get, _thrFiringRemainder.thrFiringRemainderConfig_pulseRemainder_set)
    __swig_setmethods__["thrMinFireTime"] = _thrFiringRemainder.thrFiringRemainderConfig_thrMinFireTime_set
    __swig_getmethods__["thrMinFireTime"] = _thrFiringRemainder.thrFiringRemainderConfig_thrMinFireTime_get
    if _newclass:
        thrMinFireTime = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_thrMinFireTime_get, _thrFiringRemainder.thrFiringRemainderConfig_thrMinFireTime_set)
    __swig_setmethods__["numThrusters"] = _thrFiringRemainder.thrFiringRemainderConfig_numThrusters_set
    __swig_getmethods__["numThrusters"] = _thrFiringRemainder.thrFiringRemainderConfig_numThrusters_get
    if _newclass:
        numThrusters = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_numThrusters_get, _thrFiringRemainder.thrFiringRemainderConfig_numThrusters_set)
    __swig_setmethods__["maxThrust"] = _thrFiringRemainder.thrFiringRemainderConfig_maxThrust_set
    __swig_getmethods__["maxThrust"] = _thrFiringRemainder.thrFiringRemainderConfig_maxThrust_get
    if _newclass:
        maxThrust = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_maxThrust_get, _thrFiringRemainder.thrFiringRemainderConfig_maxThrust_set)
    __swig_setmethods__["baseThrustState"] = _thrFiringRemainder.thrFiringRemainderConfig_baseThrustState_set
    __swig_getmethods__["baseThrustState"] = _thrFiringRemainder.thrFiringRemainderConfig_baseThrustState_get
    if _newclass:
        baseThrustState = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_baseThrustState_get, _thrFiringRemainder.thrFiringRemainderConfig_baseThrustState_set)
    __swig_setmethods__["prevCallTime"] = _thrFiringRemainder.thrFiringRemainderConfig_prevCallTime_set
    __swig_getmethods__["prevCallTime"] = _thrFiringRemainder.thrFiringRemainderConfig_prevCallTime_get
    if _newclass:
        prevCallTime = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_prevCallTime_get, _thrFiringRemainder.thrFiringRemainderConfig_prevCallTime_set)
    __swig_setmethods__["thrForceInMsgName"] = _thrFiringRemainder.thrFiringRemainderConfig_thrForceInMsgName_set
    __swig_getmethods__["thrForceInMsgName"] = _thrFiringRemainder.thrFiringRemainderConfig_thrForceInMsgName_get
    if _newclass:
        thrForceInMsgName = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_thrForceInMsgName_get, _thrFiringRemainder.thrFiringRemainderConfig_thrForceInMsgName_set)
    __swig_setmethods__["thrForceInMsgID"] = _thrFiringRemainder.thrFiringRemainderConfig_thrForceInMsgID_set
    __swig_getmethods__["thrForceInMsgID"] = _thrFiringRemainder.thrFiringRemainderConfig_thrForceInMsgID_get
    if _newclass:
        thrForceInMsgID = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_thrForceInMsgID_get, _thrFiringRemainder.thrFiringRemainderConfig_thrForceInMsgID_set)
    __swig_setmethods__["onTimeOutMsgName"] = _thrFiringRemainder.thrFiringRemainderConfig_onTimeOutMsgName_set
    __swig_getmethods__["onTimeOutMsgName"] = _thrFiringRemainder.thrFiringRemainderConfig_onTimeOutMsgName_get
    if _newclass:
        onTimeOutMsgName = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_onTimeOutMsgName_get, _thrFiringRemainder.thrFiringRemainderConfig_onTimeOutMsgName_set)
    __swig_setmethods__["onTimeOutMsgID"] = _thrFiringRemainder.thrFiringRemainderConfig_onTimeOutMsgID_set
    __swig_getmethods__["onTimeOutMsgID"] = _thrFiringRemainder.thrFiringRemainderConfig_onTimeOutMsgID_get
    if _newclass:
        onTimeOutMsgID = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_onTimeOutMsgID_get, _thrFiringRemainder.thrFiringRemainderConfig_onTimeOutMsgID_set)
    __swig_setmethods__["thrConfInMsgName"] = _thrFiringRemainder.thrFiringRemainderConfig_thrConfInMsgName_set
    __swig_getmethods__["thrConfInMsgName"] = _thrFiringRemainder.thrFiringRemainderConfig_thrConfInMsgName_get
    if _newclass:
        thrConfInMsgName = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_thrConfInMsgName_get, _thrFiringRemainder.thrFiringRemainderConfig_thrConfInMsgName_set)
    __swig_setmethods__["thrConfInMsgID"] = _thrFiringRemainder.thrFiringRemainderConfig_thrConfInMsgID_set
    __swig_getmethods__["thrConfInMsgID"] = _thrFiringRemainder.thrFiringRemainderConfig_thrConfInMsgID_get
    if _newclass:
        thrConfInMsgID = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_thrConfInMsgID_get, _thrFiringRemainder.thrFiringRemainderConfig_thrConfInMsgID_set)
    __swig_setmethods__["thrForceIn"] = _thrFiringRemainder.thrFiringRemainderConfig_thrForceIn_set
    __swig_getmethods__["thrForceIn"] = _thrFiringRemainder.thrFiringRemainderConfig_thrForceIn_get
    if _newclass:
        thrForceIn = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_thrForceIn_get, _thrFiringRemainder.thrFiringRemainderConfig_thrForceIn_set)
    __swig_setmethods__["thrOnTimeOut"] = _thrFiringRemainder.thrFiringRemainderConfig_thrOnTimeOut_set
    __swig_getmethods__["thrOnTimeOut"] = _thrFiringRemainder.thrFiringRemainderConfig_thrOnTimeOut_get
    if _newclass:
        thrOnTimeOut = _swig_property(_thrFiringRemainder.thrFiringRemainderConfig_thrOnTimeOut_get, _thrFiringRemainder.thrFiringRemainderConfig_thrOnTimeOut_set)

    def __init__(self):
        this = _thrFiringRemainder.new_thrFiringRemainderConfig()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrFiringRemainder.delete_thrFiringRemainderConfig
    __del__ = lambda self: None
thrFiringRemainderConfig_swigregister = _thrFiringRemainder.thrFiringRemainderConfig_swigregister
thrFiringRemainderConfig_swigregister(thrFiringRemainderConfig)

class THRArrayConfigFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, THRArrayConfigFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, THRArrayConfigFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numThrusters"] = _thrFiringRemainder.THRArrayConfigFswMsg_numThrusters_set
    __swig_getmethods__["numThrusters"] = _thrFiringRemainder.THRArrayConfigFswMsg_numThrusters_get
    if _newclass:
        numThrusters = _swig_property(_thrFiringRemainder.THRArrayConfigFswMsg_numThrusters_get, _thrFiringRemainder.THRArrayConfigFswMsg_numThrusters_set)
    __swig_setmethods__["thrusters"] = _thrFiringRemainder.THRArrayConfigFswMsg_thrusters_set
    __swig_getmethods__["thrusters"] = _thrFiringRemainder.THRArrayConfigFswMsg_thrusters_get
    if _newclass:
        thrusters = _swig_property(_thrFiringRemainder.THRArrayConfigFswMsg_thrusters_get, _thrFiringRemainder.THRArrayConfigFswMsg_thrusters_set)

    def __init__(self):
        this = _thrFiringRemainder.new_THRArrayConfigFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrFiringRemainder.delete_THRArrayConfigFswMsg
    __del__ = lambda self: None
THRArrayConfigFswMsg_swigregister = _thrFiringRemainder.THRArrayConfigFswMsg_swigregister
THRArrayConfigFswMsg_swigregister(THRArrayConfigFswMsg)

sizeof_THRArrayConfigFswMsg = _thrFiringRemainder.sizeof_THRArrayConfigFswMsg
class THRArrayCmdForceFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, THRArrayCmdForceFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, THRArrayCmdForceFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["thrForce"] = _thrFiringRemainder.THRArrayCmdForceFswMsg_thrForce_set
    __swig_getmethods__["thrForce"] = _thrFiringRemainder.THRArrayCmdForceFswMsg_thrForce_get
    if _newclass:
        thrForce = _swig_property(_thrFiringRemainder.THRArrayCmdForceFswMsg_thrForce_get, _thrFiringRemainder.THRArrayCmdForceFswMsg_thrForce_set)

    def __init__(self):
        this = _thrFiringRemainder.new_THRArrayCmdForceFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrFiringRemainder.delete_THRArrayCmdForceFswMsg
    __del__ = lambda self: None
THRArrayCmdForceFswMsg_swigregister = _thrFiringRemainder.THRArrayCmdForceFswMsg_swigregister
THRArrayCmdForceFswMsg_swigregister(THRArrayCmdForceFswMsg)

sizeof_THRArrayCmdForceFswMsg = _thrFiringRemainder.sizeof_THRArrayCmdForceFswMsg
class THRArrayOnTimeCmdIntMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, THRArrayOnTimeCmdIntMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, THRArrayOnTimeCmdIntMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["OnTimeRequest"] = _thrFiringRemainder.THRArrayOnTimeCmdIntMsg_OnTimeRequest_set
    __swig_getmethods__["OnTimeRequest"] = _thrFiringRemainder.THRArrayOnTimeCmdIntMsg_OnTimeRequest_get
    if _newclass:
        OnTimeRequest = _swig_property(_thrFiringRemainder.THRArrayOnTimeCmdIntMsg_OnTimeRequest_get, _thrFiringRemainder.THRArrayOnTimeCmdIntMsg_OnTimeRequest_set)

    def __init__(self):
        this = _thrFiringRemainder.new_THRArrayOnTimeCmdIntMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrFiringRemainder.delete_THRArrayOnTimeCmdIntMsg
    __del__ = lambda self: None
THRArrayOnTimeCmdIntMsg_swigregister = _thrFiringRemainder.THRArrayOnTimeCmdIntMsg_swigregister
THRArrayOnTimeCmdIntMsg_swigregister(THRArrayOnTimeCmdIntMsg)


import sys
protectAllClasses(sys.modules[__name__])

# This file is compatible with both classic and new-style classes.


