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
        mname = '.'.join((pkg, '_thrMomentumManagement')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_thrMomentumManagement')
    _thrMomentumManagement = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_thrMomentumManagement', [dirname(__file__)])
        except ImportError:
            import _thrMomentumManagement
            return _thrMomentumManagement
        try:
            _mod = imp.load_module('_thrMomentumManagement', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _thrMomentumManagement = swig_import_helper()
    del swig_import_helper
else:
    import _thrMomentumManagement
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
    return _thrMomentumManagement.new_doubleArray(nelements)
new_doubleArray = _thrMomentumManagement.new_doubleArray

def delete_doubleArray(ary):
    return _thrMomentumManagement.delete_doubleArray(ary)
delete_doubleArray = _thrMomentumManagement.delete_doubleArray

def doubleArray_getitem(ary, index):
    return _thrMomentumManagement.doubleArray_getitem(ary, index)
doubleArray_getitem = _thrMomentumManagement.doubleArray_getitem

def doubleArray_setitem(ary, index, value):
    return _thrMomentumManagement.doubleArray_setitem(ary, index, value)
doubleArray_setitem = _thrMomentumManagement.doubleArray_setitem

def new_longArray(nelements):
    return _thrMomentumManagement.new_longArray(nelements)
new_longArray = _thrMomentumManagement.new_longArray

def delete_longArray(ary):
    return _thrMomentumManagement.delete_longArray(ary)
delete_longArray = _thrMomentumManagement.delete_longArray

def longArray_getitem(ary, index):
    return _thrMomentumManagement.longArray_getitem(ary, index)
longArray_getitem = _thrMomentumManagement.longArray_getitem

def longArray_setitem(ary, index, value):
    return _thrMomentumManagement.longArray_setitem(ary, index, value)
longArray_setitem = _thrMomentumManagement.longArray_setitem

def new_intArray(nelements):
    return _thrMomentumManagement.new_intArray(nelements)
new_intArray = _thrMomentumManagement.new_intArray

def delete_intArray(ary):
    return _thrMomentumManagement.delete_intArray(ary)
delete_intArray = _thrMomentumManagement.delete_intArray

def intArray_getitem(ary, index):
    return _thrMomentumManagement.intArray_getitem(ary, index)
intArray_getitem = _thrMomentumManagement.intArray_getitem

def intArray_setitem(ary, index, value):
    return _thrMomentumManagement.intArray_setitem(ary, index, value)
intArray_setitem = _thrMomentumManagement.intArray_setitem

def new_shortArray(nelements):
    return _thrMomentumManagement.new_shortArray(nelements)
new_shortArray = _thrMomentumManagement.new_shortArray

def delete_shortArray(ary):
    return _thrMomentumManagement.delete_shortArray(ary)
delete_shortArray = _thrMomentumManagement.delete_shortArray

def shortArray_getitem(ary, index):
    return _thrMomentumManagement.shortArray_getitem(ary, index)
shortArray_getitem = _thrMomentumManagement.shortArray_getitem

def shortArray_setitem(ary, index, value):
    return _thrMomentumManagement.shortArray_setitem(ary, index, value)
shortArray_setitem = _thrMomentumManagement.shortArray_setitem


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


Update_thrMomentumManagement = _thrMomentumManagement.Update_thrMomentumManagement
SelfInit_thrMomentumManagement = _thrMomentumManagement.SelfInit_thrMomentumManagement
CrossInit_thrMomentumManagement = _thrMomentumManagement.CrossInit_thrMomentumManagement
Reset_thrMomentumManagement = _thrMomentumManagement.Reset_thrMomentumManagement
class thrMomentumManagementConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, thrMomentumManagementConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, thrMomentumManagementConfig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["initRequest"] = _thrMomentumManagement.thrMomentumManagementConfig_initRequest_set
    __swig_getmethods__["initRequest"] = _thrMomentumManagement.thrMomentumManagementConfig_initRequest_get
    if _newclass:
        initRequest = _swig_property(_thrMomentumManagement.thrMomentumManagementConfig_initRequest_get, _thrMomentumManagement.thrMomentumManagementConfig_initRequest_set)
    __swig_setmethods__["Delta_H_B"] = _thrMomentumManagement.thrMomentumManagementConfig_Delta_H_B_set
    __swig_getmethods__["Delta_H_B"] = _thrMomentumManagement.thrMomentumManagementConfig_Delta_H_B_get
    if _newclass:
        Delta_H_B = _swig_property(_thrMomentumManagement.thrMomentumManagementConfig_Delta_H_B_get, _thrMomentumManagement.thrMomentumManagementConfig_Delta_H_B_set)
    __swig_setmethods__["rwConfigParams"] = _thrMomentumManagement.thrMomentumManagementConfig_rwConfigParams_set
    __swig_getmethods__["rwConfigParams"] = _thrMomentumManagement.thrMomentumManagementConfig_rwConfigParams_get
    if _newclass:
        rwConfigParams = _swig_property(_thrMomentumManagement.thrMomentumManagementConfig_rwConfigParams_get, _thrMomentumManagement.thrMomentumManagementConfig_rwConfigParams_set)
    __swig_setmethods__["hs_min"] = _thrMomentumManagement.thrMomentumManagementConfig_hs_min_set
    __swig_getmethods__["hs_min"] = _thrMomentumManagement.thrMomentumManagementConfig_hs_min_get
    if _newclass:
        hs_min = _swig_property(_thrMomentumManagement.thrMomentumManagementConfig_hs_min_get, _thrMomentumManagement.thrMomentumManagementConfig_hs_min_set)
    __swig_setmethods__["deltaHOutMsgName"] = _thrMomentumManagement.thrMomentumManagementConfig_deltaHOutMsgName_set
    __swig_getmethods__["deltaHOutMsgName"] = _thrMomentumManagement.thrMomentumManagementConfig_deltaHOutMsgName_get
    if _newclass:
        deltaHOutMsgName = _swig_property(_thrMomentumManagement.thrMomentumManagementConfig_deltaHOutMsgName_get, _thrMomentumManagement.thrMomentumManagementConfig_deltaHOutMsgName_set)
    __swig_setmethods__["deltaHOutMsgID"] = _thrMomentumManagement.thrMomentumManagementConfig_deltaHOutMsgID_set
    __swig_getmethods__["deltaHOutMsgID"] = _thrMomentumManagement.thrMomentumManagementConfig_deltaHOutMsgID_get
    if _newclass:
        deltaHOutMsgID = _swig_property(_thrMomentumManagement.thrMomentumManagementConfig_deltaHOutMsgID_get, _thrMomentumManagement.thrMomentumManagementConfig_deltaHOutMsgID_set)
    __swig_setmethods__["vehicleConfigDataInMsgName"] = _thrMomentumManagement.thrMomentumManagementConfig_vehicleConfigDataInMsgName_set
    __swig_getmethods__["vehicleConfigDataInMsgName"] = _thrMomentumManagement.thrMomentumManagementConfig_vehicleConfigDataInMsgName_get
    if _newclass:
        vehicleConfigDataInMsgName = _swig_property(_thrMomentumManagement.thrMomentumManagementConfig_vehicleConfigDataInMsgName_get, _thrMomentumManagement.thrMomentumManagementConfig_vehicleConfigDataInMsgName_set)
    __swig_setmethods__["vehicleConfigDataInMsgID"] = _thrMomentumManagement.thrMomentumManagementConfig_vehicleConfigDataInMsgID_set
    __swig_getmethods__["vehicleConfigDataInMsgID"] = _thrMomentumManagement.thrMomentumManagementConfig_vehicleConfigDataInMsgID_get
    if _newclass:
        vehicleConfigDataInMsgID = _swig_property(_thrMomentumManagement.thrMomentumManagementConfig_vehicleConfigDataInMsgID_get, _thrMomentumManagement.thrMomentumManagementConfig_vehicleConfigDataInMsgID_set)
    __swig_setmethods__["rwSpeedsInMsgName"] = _thrMomentumManagement.thrMomentumManagementConfig_rwSpeedsInMsgName_set
    __swig_getmethods__["rwSpeedsInMsgName"] = _thrMomentumManagement.thrMomentumManagementConfig_rwSpeedsInMsgName_get
    if _newclass:
        rwSpeedsInMsgName = _swig_property(_thrMomentumManagement.thrMomentumManagementConfig_rwSpeedsInMsgName_get, _thrMomentumManagement.thrMomentumManagementConfig_rwSpeedsInMsgName_set)
    __swig_setmethods__["rwSpeedsInMsgID"] = _thrMomentumManagement.thrMomentumManagementConfig_rwSpeedsInMsgID_set
    __swig_getmethods__["rwSpeedsInMsgID"] = _thrMomentumManagement.thrMomentumManagementConfig_rwSpeedsInMsgID_get
    if _newclass:
        rwSpeedsInMsgID = _swig_property(_thrMomentumManagement.thrMomentumManagementConfig_rwSpeedsInMsgID_get, _thrMomentumManagement.thrMomentumManagementConfig_rwSpeedsInMsgID_set)
    __swig_setmethods__["rwConfigDataInMsgName"] = _thrMomentumManagement.thrMomentumManagementConfig_rwConfigDataInMsgName_set
    __swig_getmethods__["rwConfigDataInMsgName"] = _thrMomentumManagement.thrMomentumManagementConfig_rwConfigDataInMsgName_get
    if _newclass:
        rwConfigDataInMsgName = _swig_property(_thrMomentumManagement.thrMomentumManagementConfig_rwConfigDataInMsgName_get, _thrMomentumManagement.thrMomentumManagementConfig_rwConfigDataInMsgName_set)
    __swig_setmethods__["rwConfInMsgID"] = _thrMomentumManagement.thrMomentumManagementConfig_rwConfInMsgID_set
    __swig_getmethods__["rwConfInMsgID"] = _thrMomentumManagement.thrMomentumManagementConfig_rwConfInMsgID_get
    if _newclass:
        rwConfInMsgID = _swig_property(_thrMomentumManagement.thrMomentumManagementConfig_rwConfInMsgID_get, _thrMomentumManagement.thrMomentumManagementConfig_rwConfInMsgID_set)
    __swig_setmethods__["controlOut"] = _thrMomentumManagement.thrMomentumManagementConfig_controlOut_set
    __swig_getmethods__["controlOut"] = _thrMomentumManagement.thrMomentumManagementConfig_controlOut_get
    if _newclass:
        controlOut = _swig_property(_thrMomentumManagement.thrMomentumManagementConfig_controlOut_get, _thrMomentumManagement.thrMomentumManagementConfig_controlOut_set)

    def __init__(self):
        this = _thrMomentumManagement.new_thrMomentumManagementConfig()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrMomentumManagement.delete_thrMomentumManagementConfig
    __del__ = lambda self: None
thrMomentumManagementConfig_swigregister = _thrMomentumManagement.thrMomentumManagementConfig_swigregister
thrMomentumManagementConfig_swigregister(thrMomentumManagementConfig)

sizeof_thrMomentumManagementConfig = _thrMomentumManagement.sizeof_thrMomentumManagementConfig
class VehicleConfigFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VehicleConfigFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VehicleConfigFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ISCPntB_B"] = _thrMomentumManagement.VehicleConfigFswMsg_ISCPntB_B_set
    __swig_getmethods__["ISCPntB_B"] = _thrMomentumManagement.VehicleConfigFswMsg_ISCPntB_B_get
    if _newclass:
        ISCPntB_B = _swig_property(_thrMomentumManagement.VehicleConfigFswMsg_ISCPntB_B_get, _thrMomentumManagement.VehicleConfigFswMsg_ISCPntB_B_set)
    __swig_setmethods__["CoM_B"] = _thrMomentumManagement.VehicleConfigFswMsg_CoM_B_set
    __swig_getmethods__["CoM_B"] = _thrMomentumManagement.VehicleConfigFswMsg_CoM_B_get
    if _newclass:
        CoM_B = _swig_property(_thrMomentumManagement.VehicleConfigFswMsg_CoM_B_get, _thrMomentumManagement.VehicleConfigFswMsg_CoM_B_set)
    __swig_setmethods__["CurrentADCSState"] = _thrMomentumManagement.VehicleConfigFswMsg_CurrentADCSState_set
    __swig_getmethods__["CurrentADCSState"] = _thrMomentumManagement.VehicleConfigFswMsg_CurrentADCSState_get
    if _newclass:
        CurrentADCSState = _swig_property(_thrMomentumManagement.VehicleConfigFswMsg_CurrentADCSState_get, _thrMomentumManagement.VehicleConfigFswMsg_CurrentADCSState_set)

    def __init__(self):
        this = _thrMomentumManagement.new_VehicleConfigFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrMomentumManagement.delete_VehicleConfigFswMsg
    __del__ = lambda self: None
VehicleConfigFswMsg_swigregister = _thrMomentumManagement.VehicleConfigFswMsg_swigregister
VehicleConfigFswMsg_swigregister(VehicleConfigFswMsg)

sizeof_VehicleConfigFswMsg = _thrMomentumManagement.sizeof_VehicleConfigFswMsg
class RWArrayConfigFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RWArrayConfigFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RWArrayConfigFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["GsMatrix_B"] = _thrMomentumManagement.RWArrayConfigFswMsg_GsMatrix_B_set
    __swig_getmethods__["GsMatrix_B"] = _thrMomentumManagement.RWArrayConfigFswMsg_GsMatrix_B_get
    if _newclass:
        GsMatrix_B = _swig_property(_thrMomentumManagement.RWArrayConfigFswMsg_GsMatrix_B_get, _thrMomentumManagement.RWArrayConfigFswMsg_GsMatrix_B_set)
    __swig_setmethods__["JsList"] = _thrMomentumManagement.RWArrayConfigFswMsg_JsList_set
    __swig_getmethods__["JsList"] = _thrMomentumManagement.RWArrayConfigFswMsg_JsList_get
    if _newclass:
        JsList = _swig_property(_thrMomentumManagement.RWArrayConfigFswMsg_JsList_get, _thrMomentumManagement.RWArrayConfigFswMsg_JsList_set)
    __swig_setmethods__["numRW"] = _thrMomentumManagement.RWArrayConfigFswMsg_numRW_set
    __swig_getmethods__["numRW"] = _thrMomentumManagement.RWArrayConfigFswMsg_numRW_get
    if _newclass:
        numRW = _swig_property(_thrMomentumManagement.RWArrayConfigFswMsg_numRW_get, _thrMomentumManagement.RWArrayConfigFswMsg_numRW_set)
    __swig_setmethods__["uMax"] = _thrMomentumManagement.RWArrayConfigFswMsg_uMax_set
    __swig_getmethods__["uMax"] = _thrMomentumManagement.RWArrayConfigFswMsg_uMax_get
    if _newclass:
        uMax = _swig_property(_thrMomentumManagement.RWArrayConfigFswMsg_uMax_get, _thrMomentumManagement.RWArrayConfigFswMsg_uMax_set)

    def __init__(self):
        this = _thrMomentumManagement.new_RWArrayConfigFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrMomentumManagement.delete_RWArrayConfigFswMsg
    __del__ = lambda self: None
RWArrayConfigFswMsg_swigregister = _thrMomentumManagement.RWArrayConfigFswMsg_swigregister
RWArrayConfigFswMsg_swigregister(RWArrayConfigFswMsg)

sizeof_RWArrayConfigFswMsg = _thrMomentumManagement.sizeof_RWArrayConfigFswMsg
class CmdTorqueBodyIntMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CmdTorqueBodyIntMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CmdTorqueBodyIntMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["torqueRequestBody"] = _thrMomentumManagement.CmdTorqueBodyIntMsg_torqueRequestBody_set
    __swig_getmethods__["torqueRequestBody"] = _thrMomentumManagement.CmdTorqueBodyIntMsg_torqueRequestBody_get
    if _newclass:
        torqueRequestBody = _swig_property(_thrMomentumManagement.CmdTorqueBodyIntMsg_torqueRequestBody_get, _thrMomentumManagement.CmdTorqueBodyIntMsg_torqueRequestBody_set)

    def __init__(self):
        this = _thrMomentumManagement.new_CmdTorqueBodyIntMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrMomentumManagement.delete_CmdTorqueBodyIntMsg
    __del__ = lambda self: None
CmdTorqueBodyIntMsg_swigregister = _thrMomentumManagement.CmdTorqueBodyIntMsg_swigregister
CmdTorqueBodyIntMsg_swigregister(CmdTorqueBodyIntMsg)

sizeof_CmdTorqueBodyIntMsg = _thrMomentumManagement.sizeof_CmdTorqueBodyIntMsg
class RWSpeedIntMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RWSpeedIntMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RWSpeedIntMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["wheelSpeeds"] = _thrMomentumManagement.RWSpeedIntMsg_wheelSpeeds_set
    __swig_getmethods__["wheelSpeeds"] = _thrMomentumManagement.RWSpeedIntMsg_wheelSpeeds_get
    if _newclass:
        wheelSpeeds = _swig_property(_thrMomentumManagement.RWSpeedIntMsg_wheelSpeeds_get, _thrMomentumManagement.RWSpeedIntMsg_wheelSpeeds_set)
    __swig_setmethods__["wheelThetas"] = _thrMomentumManagement.RWSpeedIntMsg_wheelThetas_set
    __swig_getmethods__["wheelThetas"] = _thrMomentumManagement.RWSpeedIntMsg_wheelThetas_get
    if _newclass:
        wheelThetas = _swig_property(_thrMomentumManagement.RWSpeedIntMsg_wheelThetas_get, _thrMomentumManagement.RWSpeedIntMsg_wheelThetas_set)

    def __init__(self):
        this = _thrMomentumManagement.new_RWSpeedIntMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrMomentumManagement.delete_RWSpeedIntMsg
    __del__ = lambda self: None
RWSpeedIntMsg_swigregister = _thrMomentumManagement.RWSpeedIntMsg_swigregister
RWSpeedIntMsg_swigregister(RWSpeedIntMsg)

sizeof_RWSpeedIntMsg = _thrMomentumManagement.sizeof_RWSpeedIntMsg

import sys
protectAllClasses(sys.modules[__name__])

# This file is compatible with both classic and new-style classes.

