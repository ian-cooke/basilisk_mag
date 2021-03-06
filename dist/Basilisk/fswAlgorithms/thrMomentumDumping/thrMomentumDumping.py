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
        mname = '.'.join((pkg, '_thrMomentumDumping')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_thrMomentumDumping')
    _thrMomentumDumping = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_thrMomentumDumping', [dirname(__file__)])
        except ImportError:
            import _thrMomentumDumping
            return _thrMomentumDumping
        try:
            _mod = imp.load_module('_thrMomentumDumping', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _thrMomentumDumping = swig_import_helper()
    del swig_import_helper
else:
    import _thrMomentumDumping
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
    return _thrMomentumDumping.new_doubleArray(nelements)
new_doubleArray = _thrMomentumDumping.new_doubleArray

def delete_doubleArray(ary):
    return _thrMomentumDumping.delete_doubleArray(ary)
delete_doubleArray = _thrMomentumDumping.delete_doubleArray

def doubleArray_getitem(ary, index):
    return _thrMomentumDumping.doubleArray_getitem(ary, index)
doubleArray_getitem = _thrMomentumDumping.doubleArray_getitem

def doubleArray_setitem(ary, index, value):
    return _thrMomentumDumping.doubleArray_setitem(ary, index, value)
doubleArray_setitem = _thrMomentumDumping.doubleArray_setitem

def new_longArray(nelements):
    return _thrMomentumDumping.new_longArray(nelements)
new_longArray = _thrMomentumDumping.new_longArray

def delete_longArray(ary):
    return _thrMomentumDumping.delete_longArray(ary)
delete_longArray = _thrMomentumDumping.delete_longArray

def longArray_getitem(ary, index):
    return _thrMomentumDumping.longArray_getitem(ary, index)
longArray_getitem = _thrMomentumDumping.longArray_getitem

def longArray_setitem(ary, index, value):
    return _thrMomentumDumping.longArray_setitem(ary, index, value)
longArray_setitem = _thrMomentumDumping.longArray_setitem

def new_intArray(nelements):
    return _thrMomentumDumping.new_intArray(nelements)
new_intArray = _thrMomentumDumping.new_intArray

def delete_intArray(ary):
    return _thrMomentumDumping.delete_intArray(ary)
delete_intArray = _thrMomentumDumping.delete_intArray

def intArray_getitem(ary, index):
    return _thrMomentumDumping.intArray_getitem(ary, index)
intArray_getitem = _thrMomentumDumping.intArray_getitem

def intArray_setitem(ary, index, value):
    return _thrMomentumDumping.intArray_setitem(ary, index, value)
intArray_setitem = _thrMomentumDumping.intArray_setitem

def new_shortArray(nelements):
    return _thrMomentumDumping.new_shortArray(nelements)
new_shortArray = _thrMomentumDumping.new_shortArray

def delete_shortArray(ary):
    return _thrMomentumDumping.delete_shortArray(ary)
delete_shortArray = _thrMomentumDumping.delete_shortArray

def shortArray_getitem(ary, index):
    return _thrMomentumDumping.shortArray_getitem(ary, index)
shortArray_getitem = _thrMomentumDumping.shortArray_getitem

def shortArray_setitem(ary, index, value):
    return _thrMomentumDumping.shortArray_setitem(ary, index, value)
shortArray_setitem = _thrMomentumDumping.shortArray_setitem


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


Update_thrMomentumDumping = _thrMomentumDumping.Update_thrMomentumDumping
SelfInit_thrMomentumDumping = _thrMomentumDumping.SelfInit_thrMomentumDumping
CrossInit_thrMomentumDumping = _thrMomentumDumping.CrossInit_thrMomentumDumping
Reset_thrMomentumDumping = _thrMomentumDumping.Reset_thrMomentumDumping
sizeof_thrMomentumDumpingConfig = _thrMomentumDumping.sizeof_thrMomentumDumpingConfig
class thrMomentumDumpingConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, thrMomentumDumpingConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, thrMomentumDumpingConfig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["thrDumpingCounter"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrDumpingCounter_set
    __swig_getmethods__["thrDumpingCounter"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrDumpingCounter_get
    if _newclass:
        thrDumpingCounter = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_thrDumpingCounter_get, _thrMomentumDumping.thrMomentumDumpingConfig_thrDumpingCounter_set)
    __swig_setmethods__["Delta_p"] = _thrMomentumDumping.thrMomentumDumpingConfig_Delta_p_set
    __swig_getmethods__["Delta_p"] = _thrMomentumDumping.thrMomentumDumpingConfig_Delta_p_get
    if _newclass:
        Delta_p = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_Delta_p_get, _thrMomentumDumping.thrMomentumDumpingConfig_Delta_p_set)
    __swig_setmethods__["thrOnTimeRemaining"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrOnTimeRemaining_set
    __swig_getmethods__["thrOnTimeRemaining"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrOnTimeRemaining_get
    if _newclass:
        thrOnTimeRemaining = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_thrOnTimeRemaining_get, _thrMomentumDumping.thrMomentumDumpingConfig_thrOnTimeRemaining_set)
    __swig_setmethods__["priorTime"] = _thrMomentumDumping.thrMomentumDumpingConfig_priorTime_set
    __swig_getmethods__["priorTime"] = _thrMomentumDumping.thrMomentumDumpingConfig_priorTime_get
    if _newclass:
        priorTime = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_priorTime_get, _thrMomentumDumping.thrMomentumDumpingConfig_priorTime_set)
    __swig_setmethods__["numThrusters"] = _thrMomentumDumping.thrMomentumDumpingConfig_numThrusters_set
    __swig_getmethods__["numThrusters"] = _thrMomentumDumping.thrMomentumDumpingConfig_numThrusters_get
    if _newclass:
        numThrusters = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_numThrusters_get, _thrMomentumDumping.thrMomentumDumpingConfig_numThrusters_set)
    __swig_setmethods__["thrMaxForce"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrMaxForce_set
    __swig_getmethods__["thrMaxForce"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrMaxForce_get
    if _newclass:
        thrMaxForce = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_thrMaxForce_get, _thrMomentumDumping.thrMomentumDumpingConfig_thrMaxForce_set)
    __swig_setmethods__["thrMinFireTime"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrMinFireTime_set
    __swig_getmethods__["thrMinFireTime"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrMinFireTime_get
    if _newclass:
        thrMinFireTime = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_thrMinFireTime_get, _thrMomentumDumping.thrMomentumDumpingConfig_thrMinFireTime_set)
    __swig_setmethods__["maxCounterValue"] = _thrMomentumDumping.thrMomentumDumpingConfig_maxCounterValue_set
    __swig_getmethods__["maxCounterValue"] = _thrMomentumDumping.thrMomentumDumpingConfig_maxCounterValue_get
    if _newclass:
        maxCounterValue = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_maxCounterValue_get, _thrMomentumDumping.thrMomentumDumpingConfig_maxCounterValue_set)
    __swig_setmethods__["thrusterOnTimeOutMsgName"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrusterOnTimeOutMsgName_set
    __swig_getmethods__["thrusterOnTimeOutMsgName"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrusterOnTimeOutMsgName_get
    if _newclass:
        thrusterOnTimeOutMsgName = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_thrusterOnTimeOutMsgName_get, _thrMomentumDumping.thrMomentumDumpingConfig_thrusterOnTimeOutMsgName_set)
    __swig_setmethods__["thrusterOnTimeOutMsgID"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrusterOnTimeOutMsgID_set
    __swig_getmethods__["thrusterOnTimeOutMsgID"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrusterOnTimeOutMsgID_get
    if _newclass:
        thrusterOnTimeOutMsgID = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_thrusterOnTimeOutMsgID_get, _thrMomentumDumping.thrMomentumDumpingConfig_thrusterOnTimeOutMsgID_set)
    __swig_setmethods__["thrusterImpulseInMsgName"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrusterImpulseInMsgName_set
    __swig_getmethods__["thrusterImpulseInMsgName"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrusterImpulseInMsgName_get
    if _newclass:
        thrusterImpulseInMsgName = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_thrusterImpulseInMsgName_get, _thrMomentumDumping.thrMomentumDumpingConfig_thrusterImpulseInMsgName_set)
    __swig_setmethods__["thrusterImpulseInMsgID"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrusterImpulseInMsgID_set
    __swig_getmethods__["thrusterImpulseInMsgID"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrusterImpulseInMsgID_get
    if _newclass:
        thrusterImpulseInMsgID = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_thrusterImpulseInMsgID_get, _thrMomentumDumping.thrMomentumDumpingConfig_thrusterImpulseInMsgID_set)
    __swig_setmethods__["thrusterConfInMsgName"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrusterConfInMsgName_set
    __swig_getmethods__["thrusterConfInMsgName"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrusterConfInMsgName_get
    if _newclass:
        thrusterConfInMsgName = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_thrusterConfInMsgName_get, _thrMomentumDumping.thrMomentumDumpingConfig_thrusterConfInMsgName_set)
    __swig_setmethods__["thrusterConfInMsgID"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrusterConfInMsgID_set
    __swig_getmethods__["thrusterConfInMsgID"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrusterConfInMsgID_get
    if _newclass:
        thrusterConfInMsgID = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_thrusterConfInMsgID_get, _thrMomentumDumping.thrMomentumDumpingConfig_thrusterConfInMsgID_set)
    __swig_setmethods__["thrOnTimeOut"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrOnTimeOut_set
    __swig_getmethods__["thrOnTimeOut"] = _thrMomentumDumping.thrMomentumDumpingConfig_thrOnTimeOut_get
    if _newclass:
        thrOnTimeOut = _swig_property(_thrMomentumDumping.thrMomentumDumpingConfig_thrOnTimeOut_get, _thrMomentumDumping.thrMomentumDumpingConfig_thrOnTimeOut_set)

    def __init__(self):
        this = _thrMomentumDumping.new_thrMomentumDumpingConfig()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrMomentumDumping.delete_thrMomentumDumpingConfig
    __del__ = lambda self: None
thrMomentumDumpingConfig_swigregister = _thrMomentumDumping.thrMomentumDumpingConfig_swigregister
thrMomentumDumpingConfig_swigregister(thrMomentumDumpingConfig)

class THRArrayConfigFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, THRArrayConfigFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, THRArrayConfigFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numThrusters"] = _thrMomentumDumping.THRArrayConfigFswMsg_numThrusters_set
    __swig_getmethods__["numThrusters"] = _thrMomentumDumping.THRArrayConfigFswMsg_numThrusters_get
    if _newclass:
        numThrusters = _swig_property(_thrMomentumDumping.THRArrayConfigFswMsg_numThrusters_get, _thrMomentumDumping.THRArrayConfigFswMsg_numThrusters_set)
    __swig_setmethods__["thrusters"] = _thrMomentumDumping.THRArrayConfigFswMsg_thrusters_set
    __swig_getmethods__["thrusters"] = _thrMomentumDumping.THRArrayConfigFswMsg_thrusters_get
    if _newclass:
        thrusters = _swig_property(_thrMomentumDumping.THRArrayConfigFswMsg_thrusters_get, _thrMomentumDumping.THRArrayConfigFswMsg_thrusters_set)

    def __init__(self):
        this = _thrMomentumDumping.new_THRArrayConfigFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrMomentumDumping.delete_THRArrayConfigFswMsg
    __del__ = lambda self: None
THRArrayConfigFswMsg_swigregister = _thrMomentumDumping.THRArrayConfigFswMsg_swigregister
THRArrayConfigFswMsg_swigregister(THRArrayConfigFswMsg)

class THRArrayCmdForceFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, THRArrayCmdForceFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, THRArrayCmdForceFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["thrForce"] = _thrMomentumDumping.THRArrayCmdForceFswMsg_thrForce_set
    __swig_getmethods__["thrForce"] = _thrMomentumDumping.THRArrayCmdForceFswMsg_thrForce_get
    if _newclass:
        thrForce = _swig_property(_thrMomentumDumping.THRArrayCmdForceFswMsg_thrForce_get, _thrMomentumDumping.THRArrayCmdForceFswMsg_thrForce_set)

    def __init__(self):
        this = _thrMomentumDumping.new_THRArrayCmdForceFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrMomentumDumping.delete_THRArrayCmdForceFswMsg
    __del__ = lambda self: None
THRArrayCmdForceFswMsg_swigregister = _thrMomentumDumping.THRArrayCmdForceFswMsg_swigregister
THRArrayCmdForceFswMsg_swigregister(THRArrayCmdForceFswMsg)

class THRArrayOnTimeCmdIntMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, THRArrayOnTimeCmdIntMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, THRArrayOnTimeCmdIntMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["OnTimeRequest"] = _thrMomentumDumping.THRArrayOnTimeCmdIntMsg_OnTimeRequest_set
    __swig_getmethods__["OnTimeRequest"] = _thrMomentumDumping.THRArrayOnTimeCmdIntMsg_OnTimeRequest_get
    if _newclass:
        OnTimeRequest = _swig_property(_thrMomentumDumping.THRArrayOnTimeCmdIntMsg_OnTimeRequest_get, _thrMomentumDumping.THRArrayOnTimeCmdIntMsg_OnTimeRequest_set)

    def __init__(self):
        this = _thrMomentumDumping.new_THRArrayOnTimeCmdIntMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrMomentumDumping.delete_THRArrayOnTimeCmdIntMsg
    __del__ = lambda self: None
THRArrayOnTimeCmdIntMsg_swigregister = _thrMomentumDumping.THRArrayOnTimeCmdIntMsg_swigregister
THRArrayOnTimeCmdIntMsg_swigregister(THRArrayOnTimeCmdIntMsg)

sizeof_THRArrayConfigFswMsg = _thrMomentumDumping.sizeof_THRArrayConfigFswMsg
sizeof_THRArrayCmdForceFswMsg = _thrMomentumDumping.sizeof_THRArrayCmdForceFswMsg

import sys
protectAllClasses(sys.modules[__name__])

# This file is compatible with both classic and new-style classes.


