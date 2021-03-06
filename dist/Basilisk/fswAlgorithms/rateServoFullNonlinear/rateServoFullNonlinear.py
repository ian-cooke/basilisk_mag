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
        mname = '.'.join((pkg, '_rateServoFullNonlinear')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_rateServoFullNonlinear')
    _rateServoFullNonlinear = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_rateServoFullNonlinear', [dirname(__file__)])
        except ImportError:
            import _rateServoFullNonlinear
            return _rateServoFullNonlinear
        try:
            _mod = imp.load_module('_rateServoFullNonlinear', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _rateServoFullNonlinear = swig_import_helper()
    del swig_import_helper
else:
    import _rateServoFullNonlinear
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
    return _rateServoFullNonlinear.new_doubleArray(nelements)
new_doubleArray = _rateServoFullNonlinear.new_doubleArray

def delete_doubleArray(ary):
    return _rateServoFullNonlinear.delete_doubleArray(ary)
delete_doubleArray = _rateServoFullNonlinear.delete_doubleArray

def doubleArray_getitem(ary, index):
    return _rateServoFullNonlinear.doubleArray_getitem(ary, index)
doubleArray_getitem = _rateServoFullNonlinear.doubleArray_getitem

def doubleArray_setitem(ary, index, value):
    return _rateServoFullNonlinear.doubleArray_setitem(ary, index, value)
doubleArray_setitem = _rateServoFullNonlinear.doubleArray_setitem

def new_longArray(nelements):
    return _rateServoFullNonlinear.new_longArray(nelements)
new_longArray = _rateServoFullNonlinear.new_longArray

def delete_longArray(ary):
    return _rateServoFullNonlinear.delete_longArray(ary)
delete_longArray = _rateServoFullNonlinear.delete_longArray

def longArray_getitem(ary, index):
    return _rateServoFullNonlinear.longArray_getitem(ary, index)
longArray_getitem = _rateServoFullNonlinear.longArray_getitem

def longArray_setitem(ary, index, value):
    return _rateServoFullNonlinear.longArray_setitem(ary, index, value)
longArray_setitem = _rateServoFullNonlinear.longArray_setitem

def new_intArray(nelements):
    return _rateServoFullNonlinear.new_intArray(nelements)
new_intArray = _rateServoFullNonlinear.new_intArray

def delete_intArray(ary):
    return _rateServoFullNonlinear.delete_intArray(ary)
delete_intArray = _rateServoFullNonlinear.delete_intArray

def intArray_getitem(ary, index):
    return _rateServoFullNonlinear.intArray_getitem(ary, index)
intArray_getitem = _rateServoFullNonlinear.intArray_getitem

def intArray_setitem(ary, index, value):
    return _rateServoFullNonlinear.intArray_setitem(ary, index, value)
intArray_setitem = _rateServoFullNonlinear.intArray_setitem

def new_shortArray(nelements):
    return _rateServoFullNonlinear.new_shortArray(nelements)
new_shortArray = _rateServoFullNonlinear.new_shortArray

def delete_shortArray(ary):
    return _rateServoFullNonlinear.delete_shortArray(ary)
delete_shortArray = _rateServoFullNonlinear.delete_shortArray

def shortArray_getitem(ary, index):
    return _rateServoFullNonlinear.shortArray_getitem(ary, index)
shortArray_getitem = _rateServoFullNonlinear.shortArray_getitem

def shortArray_setitem(ary, index, value):
    return _rateServoFullNonlinear.shortArray_setitem(ary, index, value)
shortArray_setitem = _rateServoFullNonlinear.shortArray_setitem


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


Update_rateServoFullNonlinear = _rateServoFullNonlinear.Update_rateServoFullNonlinear
SelfInit_rateServoFullNonlinear = _rateServoFullNonlinear.SelfInit_rateServoFullNonlinear
CrossInit_rateServoFullNonlinear = _rateServoFullNonlinear.CrossInit_rateServoFullNonlinear
Reset_rateServoFullNonlinear = _rateServoFullNonlinear.Reset_rateServoFullNonlinear
sizeof_rateServoFullNonlinearConfig = _rateServoFullNonlinear.sizeof_rateServoFullNonlinearConfig
sizeof_RWAvailabilityFswMsg = _rateServoFullNonlinear.sizeof_RWAvailabilityFswMsg
sizeof_AttGuidFswMsg = _rateServoFullNonlinear.sizeof_AttGuidFswMsg
sizeof_VehicleConfigFswMsg = _rateServoFullNonlinear.sizeof_VehicleConfigFswMsg
sizeof_RWArrayConfigFswMsg = _rateServoFullNonlinear.sizeof_RWArrayConfigFswMsg
sizeof_RWSpeedIntMsg = _rateServoFullNonlinear.sizeof_RWSpeedIntMsg
sizeof_RateCmdFswMsg = _rateServoFullNonlinear.sizeof_RateCmdFswMsg
class rateServoFullNonlinearConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rateServoFullNonlinearConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rateServoFullNonlinearConfig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["K1"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_K1_set
    __swig_getmethods__["K1"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_K1_get
    if _newclass:
        K1 = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_K1_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_K1_set)
    __swig_setmethods__["K3"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_K3_set
    __swig_getmethods__["K3"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_K3_get
    if _newclass:
        K3 = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_K3_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_K3_set)
    __swig_setmethods__["omega_max"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_omega_max_set
    __swig_getmethods__["omega_max"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_omega_max_get
    if _newclass:
        omega_max = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_omega_max_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_omega_max_set)
    __swig_setmethods__["P"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_P_set
    __swig_getmethods__["P"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_P_get
    if _newclass:
        P = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_P_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_P_set)
    __swig_setmethods__["Ki"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_Ki_set
    __swig_getmethods__["Ki"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_Ki_get
    if _newclass:
        Ki = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_Ki_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_Ki_set)
    __swig_setmethods__["integralLimit"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_integralLimit_set
    __swig_getmethods__["integralLimit"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_integralLimit_get
    if _newclass:
        integralLimit = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_integralLimit_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_integralLimit_set)
    __swig_setmethods__["priorTime"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_priorTime_set
    __swig_getmethods__["priorTime"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_priorTime_get
    if _newclass:
        priorTime = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_priorTime_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_priorTime_set)
    __swig_setmethods__["z"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_z_set
    __swig_getmethods__["z"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_z_get
    if _newclass:
        z = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_z_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_z_set)
    __swig_setmethods__["knownTorquePntB_B"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_knownTorquePntB_B_set
    __swig_getmethods__["knownTorquePntB_B"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_knownTorquePntB_B_get
    if _newclass:
        knownTorquePntB_B = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_knownTorquePntB_B_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_knownTorquePntB_B_set)
    __swig_setmethods__["ISCPntB_B"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_ISCPntB_B_set
    __swig_getmethods__["ISCPntB_B"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_ISCPntB_B_get
    if _newclass:
        ISCPntB_B = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_ISCPntB_B_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_ISCPntB_B_set)
    __swig_setmethods__["rwConfigParams"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwConfigParams_set
    __swig_getmethods__["rwConfigParams"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwConfigParams_get
    if _newclass:
        rwConfigParams = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_rwConfigParams_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwConfigParams_set)
    __swig_setmethods__["rwParamsInMsgName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwParamsInMsgName_set
    __swig_getmethods__["rwParamsInMsgName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwParamsInMsgName_get
    if _newclass:
        rwParamsInMsgName = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_rwParamsInMsgName_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwParamsInMsgName_set)
    __swig_setmethods__["rwParamsInMsgID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwParamsInMsgID_set
    __swig_getmethods__["rwParamsInMsgID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwParamsInMsgID_get
    if _newclass:
        rwParamsInMsgID = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_rwParamsInMsgID_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwParamsInMsgID_set)
    __swig_setmethods__["vehConfigInMsgName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_vehConfigInMsgName_set
    __swig_getmethods__["vehConfigInMsgName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_vehConfigInMsgName_get
    if _newclass:
        vehConfigInMsgName = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_vehConfigInMsgName_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_vehConfigInMsgName_set)
    __swig_setmethods__["vehConfigInMsgID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_vehConfigInMsgID_set
    __swig_getmethods__["vehConfigInMsgID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_vehConfigInMsgID_get
    if _newclass:
        vehConfigInMsgID = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_vehConfigInMsgID_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_vehConfigInMsgID_set)
    __swig_setmethods__["rwAvailInMsgName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwAvailInMsgName_set
    __swig_getmethods__["rwAvailInMsgName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwAvailInMsgName_get
    if _newclass:
        rwAvailInMsgName = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_rwAvailInMsgName_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwAvailInMsgName_set)
    __swig_setmethods__["rwAvailInMsgID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwAvailInMsgID_set
    __swig_getmethods__["rwAvailInMsgID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwAvailInMsgID_get
    if _newclass:
        rwAvailInMsgID = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_rwAvailInMsgID_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_rwAvailInMsgID_set)
    __swig_setmethods__["outputDataName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_outputDataName_set
    __swig_getmethods__["outputDataName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_outputDataName_get
    if _newclass:
        outputDataName = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_outputDataName_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_outputDataName_set)
    __swig_setmethods__["outputMsgID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_outputMsgID_set
    __swig_getmethods__["outputMsgID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_outputMsgID_get
    if _newclass:
        outputMsgID = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_outputMsgID_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_outputMsgID_set)
    __swig_setmethods__["inputGuidName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputGuidName_set
    __swig_getmethods__["inputGuidName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputGuidName_get
    if _newclass:
        inputGuidName = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_inputGuidName_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputGuidName_set)
    __swig_setmethods__["inputGuidID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputGuidID_set
    __swig_getmethods__["inputGuidID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputGuidID_get
    if _newclass:
        inputGuidID = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_inputGuidID_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputGuidID_set)
    __swig_setmethods__["inputRWSpeedsName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRWSpeedsName_set
    __swig_getmethods__["inputRWSpeedsName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRWSpeedsName_get
    if _newclass:
        inputRWSpeedsName = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRWSpeedsName_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRWSpeedsName_set)
    __swig_setmethods__["inputRWSpeedsID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRWSpeedsID_set
    __swig_getmethods__["inputRWSpeedsID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRWSpeedsID_get
    if _newclass:
        inputRWSpeedsID = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRWSpeedsID_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRWSpeedsID_set)
    __swig_setmethods__["inputRateSteeringName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRateSteeringName_set
    __swig_getmethods__["inputRateSteeringName"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRateSteeringName_get
    if _newclass:
        inputRateSteeringName = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRateSteeringName_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRateSteeringName_set)
    __swig_setmethods__["inputRateSteeringID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRateSteeringID_set
    __swig_getmethods__["inputRateSteeringID"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRateSteeringID_get
    if _newclass:
        inputRateSteeringID = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRateSteeringID_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_inputRateSteeringID_set)
    __swig_setmethods__["controlOut"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_controlOut_set
    __swig_getmethods__["controlOut"] = _rateServoFullNonlinear.rateServoFullNonlinearConfig_controlOut_get
    if _newclass:
        controlOut = _swig_property(_rateServoFullNonlinear.rateServoFullNonlinearConfig_controlOut_get, _rateServoFullNonlinear.rateServoFullNonlinearConfig_controlOut_set)

    def __init__(self):
        this = _rateServoFullNonlinear.new_rateServoFullNonlinearConfig()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rateServoFullNonlinear.delete_rateServoFullNonlinearConfig
    __del__ = lambda self: None
rateServoFullNonlinearConfig_swigregister = _rateServoFullNonlinear.rateServoFullNonlinearConfig_swigregister
rateServoFullNonlinearConfig_swigregister(rateServoFullNonlinearConfig)

class RWAvailabilityFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RWAvailabilityFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RWAvailabilityFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["wheelAvailability"] = _rateServoFullNonlinear.RWAvailabilityFswMsg_wheelAvailability_set
    __swig_getmethods__["wheelAvailability"] = _rateServoFullNonlinear.RWAvailabilityFswMsg_wheelAvailability_get
    if _newclass:
        wheelAvailability = _swig_property(_rateServoFullNonlinear.RWAvailabilityFswMsg_wheelAvailability_get, _rateServoFullNonlinear.RWAvailabilityFswMsg_wheelAvailability_set)

    def __init__(self):
        this = _rateServoFullNonlinear.new_RWAvailabilityFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rateServoFullNonlinear.delete_RWAvailabilityFswMsg
    __del__ = lambda self: None
RWAvailabilityFswMsg_swigregister = _rateServoFullNonlinear.RWAvailabilityFswMsg_swigregister
RWAvailabilityFswMsg_swigregister(RWAvailabilityFswMsg)

BOOL_FALSE = _rateServoFullNonlinear.BOOL_FALSE
BOOL_TRUE = _rateServoFullNonlinear.BOOL_TRUE
AVAILABLE = _rateServoFullNonlinear.AVAILABLE
UNAVAILABLE = _rateServoFullNonlinear.UNAVAILABLE
class AttGuidFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AttGuidFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AttGuidFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sigma_BR"] = _rateServoFullNonlinear.AttGuidFswMsg_sigma_BR_set
    __swig_getmethods__["sigma_BR"] = _rateServoFullNonlinear.AttGuidFswMsg_sigma_BR_get
    if _newclass:
        sigma_BR = _swig_property(_rateServoFullNonlinear.AttGuidFswMsg_sigma_BR_get, _rateServoFullNonlinear.AttGuidFswMsg_sigma_BR_set)
    __swig_setmethods__["omega_BR_B"] = _rateServoFullNonlinear.AttGuidFswMsg_omega_BR_B_set
    __swig_getmethods__["omega_BR_B"] = _rateServoFullNonlinear.AttGuidFswMsg_omega_BR_B_get
    if _newclass:
        omega_BR_B = _swig_property(_rateServoFullNonlinear.AttGuidFswMsg_omega_BR_B_get, _rateServoFullNonlinear.AttGuidFswMsg_omega_BR_B_set)
    __swig_setmethods__["omega_RN_B"] = _rateServoFullNonlinear.AttGuidFswMsg_omega_RN_B_set
    __swig_getmethods__["omega_RN_B"] = _rateServoFullNonlinear.AttGuidFswMsg_omega_RN_B_get
    if _newclass:
        omega_RN_B = _swig_property(_rateServoFullNonlinear.AttGuidFswMsg_omega_RN_B_get, _rateServoFullNonlinear.AttGuidFswMsg_omega_RN_B_set)
    __swig_setmethods__["domega_RN_B"] = _rateServoFullNonlinear.AttGuidFswMsg_domega_RN_B_set
    __swig_getmethods__["domega_RN_B"] = _rateServoFullNonlinear.AttGuidFswMsg_domega_RN_B_get
    if _newclass:
        domega_RN_B = _swig_property(_rateServoFullNonlinear.AttGuidFswMsg_domega_RN_B_get, _rateServoFullNonlinear.AttGuidFswMsg_domega_RN_B_set)
    __swig_setmethods__["PRV"] = _rateServoFullNonlinear.AttGuidFswMsg_PRV_set
    __swig_getmethods__["PRV"] = _rateServoFullNonlinear.AttGuidFswMsg_PRV_get
    if _newclass:
        PRV = _swig_property(_rateServoFullNonlinear.AttGuidFswMsg_PRV_get, _rateServoFullNonlinear.AttGuidFswMsg_PRV_set)

    def __init__(self):
        this = _rateServoFullNonlinear.new_AttGuidFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rateServoFullNonlinear.delete_AttGuidFswMsg
    __del__ = lambda self: None
AttGuidFswMsg_swigregister = _rateServoFullNonlinear.AttGuidFswMsg_swigregister
AttGuidFswMsg_swigregister(AttGuidFswMsg)

class VehicleConfigFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VehicleConfigFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VehicleConfigFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ISCPntB_B"] = _rateServoFullNonlinear.VehicleConfigFswMsg_ISCPntB_B_set
    __swig_getmethods__["ISCPntB_B"] = _rateServoFullNonlinear.VehicleConfigFswMsg_ISCPntB_B_get
    if _newclass:
        ISCPntB_B = _swig_property(_rateServoFullNonlinear.VehicleConfigFswMsg_ISCPntB_B_get, _rateServoFullNonlinear.VehicleConfigFswMsg_ISCPntB_B_set)
    __swig_setmethods__["CoM_B"] = _rateServoFullNonlinear.VehicleConfigFswMsg_CoM_B_set
    __swig_getmethods__["CoM_B"] = _rateServoFullNonlinear.VehicleConfigFswMsg_CoM_B_get
    if _newclass:
        CoM_B = _swig_property(_rateServoFullNonlinear.VehicleConfigFswMsg_CoM_B_get, _rateServoFullNonlinear.VehicleConfigFswMsg_CoM_B_set)
    __swig_setmethods__["CurrentADCSState"] = _rateServoFullNonlinear.VehicleConfigFswMsg_CurrentADCSState_set
    __swig_getmethods__["CurrentADCSState"] = _rateServoFullNonlinear.VehicleConfigFswMsg_CurrentADCSState_get
    if _newclass:
        CurrentADCSState = _swig_property(_rateServoFullNonlinear.VehicleConfigFswMsg_CurrentADCSState_get, _rateServoFullNonlinear.VehicleConfigFswMsg_CurrentADCSState_set)

    def __init__(self):
        this = _rateServoFullNonlinear.new_VehicleConfigFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rateServoFullNonlinear.delete_VehicleConfigFswMsg
    __del__ = lambda self: None
VehicleConfigFswMsg_swigregister = _rateServoFullNonlinear.VehicleConfigFswMsg_swigregister
VehicleConfigFswMsg_swigregister(VehicleConfigFswMsg)

class RWArrayConfigFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RWArrayConfigFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RWArrayConfigFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["GsMatrix_B"] = _rateServoFullNonlinear.RWArrayConfigFswMsg_GsMatrix_B_set
    __swig_getmethods__["GsMatrix_B"] = _rateServoFullNonlinear.RWArrayConfigFswMsg_GsMatrix_B_get
    if _newclass:
        GsMatrix_B = _swig_property(_rateServoFullNonlinear.RWArrayConfigFswMsg_GsMatrix_B_get, _rateServoFullNonlinear.RWArrayConfigFswMsg_GsMatrix_B_set)
    __swig_setmethods__["JsList"] = _rateServoFullNonlinear.RWArrayConfigFswMsg_JsList_set
    __swig_getmethods__["JsList"] = _rateServoFullNonlinear.RWArrayConfigFswMsg_JsList_get
    if _newclass:
        JsList = _swig_property(_rateServoFullNonlinear.RWArrayConfigFswMsg_JsList_get, _rateServoFullNonlinear.RWArrayConfigFswMsg_JsList_set)
    __swig_setmethods__["numRW"] = _rateServoFullNonlinear.RWArrayConfigFswMsg_numRW_set
    __swig_getmethods__["numRW"] = _rateServoFullNonlinear.RWArrayConfigFswMsg_numRW_get
    if _newclass:
        numRW = _swig_property(_rateServoFullNonlinear.RWArrayConfigFswMsg_numRW_get, _rateServoFullNonlinear.RWArrayConfigFswMsg_numRW_set)
    __swig_setmethods__["uMax"] = _rateServoFullNonlinear.RWArrayConfigFswMsg_uMax_set
    __swig_getmethods__["uMax"] = _rateServoFullNonlinear.RWArrayConfigFswMsg_uMax_get
    if _newclass:
        uMax = _swig_property(_rateServoFullNonlinear.RWArrayConfigFswMsg_uMax_get, _rateServoFullNonlinear.RWArrayConfigFswMsg_uMax_set)

    def __init__(self):
        this = _rateServoFullNonlinear.new_RWArrayConfigFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rateServoFullNonlinear.delete_RWArrayConfigFswMsg
    __del__ = lambda self: None
RWArrayConfigFswMsg_swigregister = _rateServoFullNonlinear.RWArrayConfigFswMsg_swigregister
RWArrayConfigFswMsg_swigregister(RWArrayConfigFswMsg)

class RateCmdFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RateCmdFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RateCmdFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["omega_BastR_B"] = _rateServoFullNonlinear.RateCmdFswMsg_omega_BastR_B_set
    __swig_getmethods__["omega_BastR_B"] = _rateServoFullNonlinear.RateCmdFswMsg_omega_BastR_B_get
    if _newclass:
        omega_BastR_B = _swig_property(_rateServoFullNonlinear.RateCmdFswMsg_omega_BastR_B_get, _rateServoFullNonlinear.RateCmdFswMsg_omega_BastR_B_set)
    __swig_setmethods__["omegap_BastR_B"] = _rateServoFullNonlinear.RateCmdFswMsg_omegap_BastR_B_set
    __swig_getmethods__["omegap_BastR_B"] = _rateServoFullNonlinear.RateCmdFswMsg_omegap_BastR_B_get
    if _newclass:
        omegap_BastR_B = _swig_property(_rateServoFullNonlinear.RateCmdFswMsg_omegap_BastR_B_get, _rateServoFullNonlinear.RateCmdFswMsg_omegap_BastR_B_set)

    def __init__(self):
        this = _rateServoFullNonlinear.new_RateCmdFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rateServoFullNonlinear.delete_RateCmdFswMsg
    __del__ = lambda self: None
RateCmdFswMsg_swigregister = _rateServoFullNonlinear.RateCmdFswMsg_swigregister
RateCmdFswMsg_swigregister(RateCmdFswMsg)

class RWSpeedIntMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RWSpeedIntMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RWSpeedIntMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["wheelSpeeds"] = _rateServoFullNonlinear.RWSpeedIntMsg_wheelSpeeds_set
    __swig_getmethods__["wheelSpeeds"] = _rateServoFullNonlinear.RWSpeedIntMsg_wheelSpeeds_get
    if _newclass:
        wheelSpeeds = _swig_property(_rateServoFullNonlinear.RWSpeedIntMsg_wheelSpeeds_get, _rateServoFullNonlinear.RWSpeedIntMsg_wheelSpeeds_set)
    __swig_setmethods__["wheelThetas"] = _rateServoFullNonlinear.RWSpeedIntMsg_wheelThetas_set
    __swig_getmethods__["wheelThetas"] = _rateServoFullNonlinear.RWSpeedIntMsg_wheelThetas_get
    if _newclass:
        wheelThetas = _swig_property(_rateServoFullNonlinear.RWSpeedIntMsg_wheelThetas_get, _rateServoFullNonlinear.RWSpeedIntMsg_wheelThetas_set)

    def __init__(self):
        this = _rateServoFullNonlinear.new_RWSpeedIntMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rateServoFullNonlinear.delete_RWSpeedIntMsg
    __del__ = lambda self: None
RWSpeedIntMsg_swigregister = _rateServoFullNonlinear.RWSpeedIntMsg_swigregister
RWSpeedIntMsg_swigregister(RWSpeedIntMsg)

class CmdTorqueBodyIntMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CmdTorqueBodyIntMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CmdTorqueBodyIntMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["torqueRequestBody"] = _rateServoFullNonlinear.CmdTorqueBodyIntMsg_torqueRequestBody_set
    __swig_getmethods__["torqueRequestBody"] = _rateServoFullNonlinear.CmdTorqueBodyIntMsg_torqueRequestBody_get
    if _newclass:
        torqueRequestBody = _swig_property(_rateServoFullNonlinear.CmdTorqueBodyIntMsg_torqueRequestBody_get, _rateServoFullNonlinear.CmdTorqueBodyIntMsg_torqueRequestBody_set)

    def __init__(self):
        this = _rateServoFullNonlinear.new_CmdTorqueBodyIntMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rateServoFullNonlinear.delete_CmdTorqueBodyIntMsg
    __del__ = lambda self: None
CmdTorqueBodyIntMsg_swigregister = _rateServoFullNonlinear.CmdTorqueBodyIntMsg_swigregister
CmdTorqueBodyIntMsg_swigregister(CmdTorqueBodyIntMsg)

sizeof_CmdTorqueBodyIntMsg = _rateServoFullNonlinear.sizeof_CmdTorqueBodyIntMsg

import sys
protectAllClasses(sys.modules[__name__])

# This file is compatible with both classic and new-style classes.


