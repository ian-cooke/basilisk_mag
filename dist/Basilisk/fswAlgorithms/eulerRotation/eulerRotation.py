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
        mname = '.'.join((pkg, '_eulerRotation')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_eulerRotation')
    _eulerRotation = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_eulerRotation', [dirname(__file__)])
        except ImportError:
            import _eulerRotation
            return _eulerRotation
        try:
            _mod = imp.load_module('_eulerRotation', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _eulerRotation = swig_import_helper()
    del swig_import_helper
else:
    import _eulerRotation
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
    return _eulerRotation.new_doubleArray(nelements)
new_doubleArray = _eulerRotation.new_doubleArray

def delete_doubleArray(ary):
    return _eulerRotation.delete_doubleArray(ary)
delete_doubleArray = _eulerRotation.delete_doubleArray

def doubleArray_getitem(ary, index):
    return _eulerRotation.doubleArray_getitem(ary, index)
doubleArray_getitem = _eulerRotation.doubleArray_getitem

def doubleArray_setitem(ary, index, value):
    return _eulerRotation.doubleArray_setitem(ary, index, value)
doubleArray_setitem = _eulerRotation.doubleArray_setitem

def new_longArray(nelements):
    return _eulerRotation.new_longArray(nelements)
new_longArray = _eulerRotation.new_longArray

def delete_longArray(ary):
    return _eulerRotation.delete_longArray(ary)
delete_longArray = _eulerRotation.delete_longArray

def longArray_getitem(ary, index):
    return _eulerRotation.longArray_getitem(ary, index)
longArray_getitem = _eulerRotation.longArray_getitem

def longArray_setitem(ary, index, value):
    return _eulerRotation.longArray_setitem(ary, index, value)
longArray_setitem = _eulerRotation.longArray_setitem

def new_intArray(nelements):
    return _eulerRotation.new_intArray(nelements)
new_intArray = _eulerRotation.new_intArray

def delete_intArray(ary):
    return _eulerRotation.delete_intArray(ary)
delete_intArray = _eulerRotation.delete_intArray

def intArray_getitem(ary, index):
    return _eulerRotation.intArray_getitem(ary, index)
intArray_getitem = _eulerRotation.intArray_getitem

def intArray_setitem(ary, index, value):
    return _eulerRotation.intArray_setitem(ary, index, value)
intArray_setitem = _eulerRotation.intArray_setitem

def new_shortArray(nelements):
    return _eulerRotation.new_shortArray(nelements)
new_shortArray = _eulerRotation.new_shortArray

def delete_shortArray(ary):
    return _eulerRotation.delete_shortArray(ary)
delete_shortArray = _eulerRotation.delete_shortArray

def shortArray_getitem(ary, index):
    return _eulerRotation.shortArray_getitem(ary, index)
shortArray_getitem = _eulerRotation.shortArray_getitem

def shortArray_setitem(ary, index, value):
    return _eulerRotation.shortArray_setitem(ary, index, value)
shortArray_setitem = _eulerRotation.shortArray_setitem


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


Update_eulerRotation = _eulerRotation.Update_eulerRotation
SelfInit_eulerRotation = _eulerRotation.SelfInit_eulerRotation
CrossInit_eulerRotation = _eulerRotation.CrossInit_eulerRotation
Reset_eulerRotation = _eulerRotation.Reset_eulerRotation
sizeof_eulerRotationConfig = _eulerRotation.sizeof_eulerRotationConfig
sizeof_AttRefFswMsg = _eulerRotation.sizeof_AttRefFswMsg
sizeof_AttStateFswMsg = _eulerRotation.sizeof_AttStateFswMsg
class eulerRotationConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, eulerRotationConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, eulerRotationConfig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["angleSet"] = _eulerRotation.eulerRotationConfig_angleSet_set
    __swig_getmethods__["angleSet"] = _eulerRotation.eulerRotationConfig_angleSet_get
    if _newclass:
        angleSet = _swig_property(_eulerRotation.eulerRotationConfig_angleSet_get, _eulerRotation.eulerRotationConfig_angleSet_set)
    __swig_setmethods__["angleRates"] = _eulerRotation.eulerRotationConfig_angleRates_set
    __swig_getmethods__["angleRates"] = _eulerRotation.eulerRotationConfig_angleRates_get
    if _newclass:
        angleRates = _swig_property(_eulerRotation.eulerRotationConfig_angleRates_get, _eulerRotation.eulerRotationConfig_angleRates_set)
    __swig_setmethods__["cmdSet"] = _eulerRotation.eulerRotationConfig_cmdSet_set
    __swig_getmethods__["cmdSet"] = _eulerRotation.eulerRotationConfig_cmdSet_get
    if _newclass:
        cmdSet = _swig_property(_eulerRotation.eulerRotationConfig_cmdSet_get, _eulerRotation.eulerRotationConfig_cmdSet_set)
    __swig_setmethods__["cmdRates"] = _eulerRotation.eulerRotationConfig_cmdRates_set
    __swig_getmethods__["cmdRates"] = _eulerRotation.eulerRotationConfig_cmdRates_get
    if _newclass:
        cmdRates = _swig_property(_eulerRotation.eulerRotationConfig_cmdRates_get, _eulerRotation.eulerRotationConfig_cmdRates_set)
    __swig_setmethods__["priorCmdSet"] = _eulerRotation.eulerRotationConfig_priorCmdSet_set
    __swig_getmethods__["priorCmdSet"] = _eulerRotation.eulerRotationConfig_priorCmdSet_get
    if _newclass:
        priorCmdSet = _swig_property(_eulerRotation.eulerRotationConfig_priorCmdSet_get, _eulerRotation.eulerRotationConfig_priorCmdSet_set)
    __swig_setmethods__["priorCmdRates"] = _eulerRotation.eulerRotationConfig_priorCmdRates_set
    __swig_getmethods__["priorCmdRates"] = _eulerRotation.eulerRotationConfig_priorCmdRates_get
    if _newclass:
        priorCmdRates = _swig_property(_eulerRotation.eulerRotationConfig_priorCmdRates_get, _eulerRotation.eulerRotationConfig_priorCmdRates_set)
    __swig_setmethods__["priorTime"] = _eulerRotation.eulerRotationConfig_priorTime_set
    __swig_getmethods__["priorTime"] = _eulerRotation.eulerRotationConfig_priorTime_get
    if _newclass:
        priorTime = _swig_property(_eulerRotation.eulerRotationConfig_priorTime_get, _eulerRotation.eulerRotationConfig_priorTime_set)
    __swig_setmethods__["dt"] = _eulerRotation.eulerRotationConfig_dt_set
    __swig_getmethods__["dt"] = _eulerRotation.eulerRotationConfig_dt_get
    if _newclass:
        dt = _swig_property(_eulerRotation.eulerRotationConfig_dt_get, _eulerRotation.eulerRotationConfig_dt_set)
    __swig_setmethods__["attRefOutMsgName"] = _eulerRotation.eulerRotationConfig_attRefOutMsgName_set
    __swig_getmethods__["attRefOutMsgName"] = _eulerRotation.eulerRotationConfig_attRefOutMsgName_get
    if _newclass:
        attRefOutMsgName = _swig_property(_eulerRotation.eulerRotationConfig_attRefOutMsgName_get, _eulerRotation.eulerRotationConfig_attRefOutMsgName_set)
    __swig_setmethods__["attRefOutMsgID"] = _eulerRotation.eulerRotationConfig_attRefOutMsgID_set
    __swig_getmethods__["attRefOutMsgID"] = _eulerRotation.eulerRotationConfig_attRefOutMsgID_get
    if _newclass:
        attRefOutMsgID = _swig_property(_eulerRotation.eulerRotationConfig_attRefOutMsgID_get, _eulerRotation.eulerRotationConfig_attRefOutMsgID_set)
    __swig_setmethods__["attitudeOutMsgName"] = _eulerRotation.eulerRotationConfig_attitudeOutMsgName_set
    __swig_getmethods__["attitudeOutMsgName"] = _eulerRotation.eulerRotationConfig_attitudeOutMsgName_get
    if _newclass:
        attitudeOutMsgName = _swig_property(_eulerRotation.eulerRotationConfig_attitudeOutMsgName_get, _eulerRotation.eulerRotationConfig_attitudeOutMsgName_set)
    __swig_setmethods__["attitudeOutMsgID"] = _eulerRotation.eulerRotationConfig_attitudeOutMsgID_set
    __swig_getmethods__["attitudeOutMsgID"] = _eulerRotation.eulerRotationConfig_attitudeOutMsgID_get
    if _newclass:
        attitudeOutMsgID = _swig_property(_eulerRotation.eulerRotationConfig_attitudeOutMsgID_get, _eulerRotation.eulerRotationConfig_attitudeOutMsgID_set)
    __swig_setmethods__["attRefInMsgName"] = _eulerRotation.eulerRotationConfig_attRefInMsgName_set
    __swig_getmethods__["attRefInMsgName"] = _eulerRotation.eulerRotationConfig_attRefInMsgName_get
    if _newclass:
        attRefInMsgName = _swig_property(_eulerRotation.eulerRotationConfig_attRefInMsgName_get, _eulerRotation.eulerRotationConfig_attRefInMsgName_set)
    __swig_setmethods__["attRefInMsgID"] = _eulerRotation.eulerRotationConfig_attRefInMsgID_set
    __swig_getmethods__["attRefInMsgID"] = _eulerRotation.eulerRotationConfig_attRefInMsgID_get
    if _newclass:
        attRefInMsgID = _swig_property(_eulerRotation.eulerRotationConfig_attRefInMsgID_get, _eulerRotation.eulerRotationConfig_attRefInMsgID_set)
    __swig_setmethods__["desiredAttInMsgName"] = _eulerRotation.eulerRotationConfig_desiredAttInMsgName_set
    __swig_getmethods__["desiredAttInMsgName"] = _eulerRotation.eulerRotationConfig_desiredAttInMsgName_get
    if _newclass:
        desiredAttInMsgName = _swig_property(_eulerRotation.eulerRotationConfig_desiredAttInMsgName_get, _eulerRotation.eulerRotationConfig_desiredAttInMsgName_set)
    __swig_setmethods__["desiredAttInMsgID"] = _eulerRotation.eulerRotationConfig_desiredAttInMsgID_set
    __swig_getmethods__["desiredAttInMsgID"] = _eulerRotation.eulerRotationConfig_desiredAttInMsgID_get
    if _newclass:
        desiredAttInMsgID = _swig_property(_eulerRotation.eulerRotationConfig_desiredAttInMsgID_get, _eulerRotation.eulerRotationConfig_desiredAttInMsgID_set)
    __swig_setmethods__["attRefOut"] = _eulerRotation.eulerRotationConfig_attRefOut_set
    __swig_getmethods__["attRefOut"] = _eulerRotation.eulerRotationConfig_attRefOut_get
    if _newclass:
        attRefOut = _swig_property(_eulerRotation.eulerRotationConfig_attRefOut_get, _eulerRotation.eulerRotationConfig_attRefOut_set)
    __swig_setmethods__["attStateOut"] = _eulerRotation.eulerRotationConfig_attStateOut_set
    __swig_getmethods__["attStateOut"] = _eulerRotation.eulerRotationConfig_attStateOut_get
    if _newclass:
        attStateOut = _swig_property(_eulerRotation.eulerRotationConfig_attStateOut_get, _eulerRotation.eulerRotationConfig_attStateOut_set)

    def __init__(self):
        this = _eulerRotation.new_eulerRotationConfig()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _eulerRotation.delete_eulerRotationConfig
    __del__ = lambda self: None
eulerRotationConfig_swigregister = _eulerRotation.eulerRotationConfig_swigregister
eulerRotationConfig_swigregister(eulerRotationConfig)


def writeOutputMessages(ConfigData, callTime, moduleID):
    return _eulerRotation.writeOutputMessages(ConfigData, callTime, moduleID)
writeOutputMessages = _eulerRotation.writeOutputMessages

def checkRasterCommands(ConfigData):
    return _eulerRotation.checkRasterCommands(ConfigData)
checkRasterCommands = _eulerRotation.checkRasterCommands

def computeTimeStep(ConfigData, callTime):
    return _eulerRotation.computeTimeStep(ConfigData, callTime)
computeTimeStep = _eulerRotation.computeTimeStep

def computeEuler321_Binv_derivative(angleSet, angleRates, B_inv_deriv):
    return _eulerRotation.computeEuler321_Binv_derivative(angleSet, angleRates, B_inv_deriv)
computeEuler321_Binv_derivative = _eulerRotation.computeEuler321_Binv_derivative

def computeEulerRotationReference(ConfigData, sigma_R0N, omega_R0N_N, domega_R0N_N):
    return _eulerRotation.computeEulerRotationReference(ConfigData, sigma_R0N, omega_R0N_N, domega_R0N_N)
computeEulerRotationReference = _eulerRotation.computeEulerRotationReference
class AttRefFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AttRefFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AttRefFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sigma_RN"] = _eulerRotation.AttRefFswMsg_sigma_RN_set
    __swig_getmethods__["sigma_RN"] = _eulerRotation.AttRefFswMsg_sigma_RN_get
    if _newclass:
        sigma_RN = _swig_property(_eulerRotation.AttRefFswMsg_sigma_RN_get, _eulerRotation.AttRefFswMsg_sigma_RN_set)
    __swig_setmethods__["omega_RN_N"] = _eulerRotation.AttRefFswMsg_omega_RN_N_set
    __swig_getmethods__["omega_RN_N"] = _eulerRotation.AttRefFswMsg_omega_RN_N_get
    if _newclass:
        omega_RN_N = _swig_property(_eulerRotation.AttRefFswMsg_omega_RN_N_get, _eulerRotation.AttRefFswMsg_omega_RN_N_set)
    __swig_setmethods__["domega_RN_N"] = _eulerRotation.AttRefFswMsg_domega_RN_N_set
    __swig_getmethods__["domega_RN_N"] = _eulerRotation.AttRefFswMsg_domega_RN_N_get
    if _newclass:
        domega_RN_N = _swig_property(_eulerRotation.AttRefFswMsg_domega_RN_N_get, _eulerRotation.AttRefFswMsg_domega_RN_N_set)

    def __init__(self):
        this = _eulerRotation.new_AttRefFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _eulerRotation.delete_AttRefFswMsg
    __del__ = lambda self: None
AttRefFswMsg_swigregister = _eulerRotation.AttRefFswMsg_swigregister
AttRefFswMsg_swigregister(AttRefFswMsg)

class AttStateFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AttStateFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AttStateFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["state"] = _eulerRotation.AttStateFswMsg_state_set
    __swig_getmethods__["state"] = _eulerRotation.AttStateFswMsg_state_get
    if _newclass:
        state = _swig_property(_eulerRotation.AttStateFswMsg_state_get, _eulerRotation.AttStateFswMsg_state_set)
    __swig_setmethods__["rate"] = _eulerRotation.AttStateFswMsg_rate_set
    __swig_getmethods__["rate"] = _eulerRotation.AttStateFswMsg_rate_get
    if _newclass:
        rate = _swig_property(_eulerRotation.AttStateFswMsg_rate_get, _eulerRotation.AttStateFswMsg_rate_set)

    def __init__(self):
        this = _eulerRotation.new_AttStateFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _eulerRotation.delete_AttStateFswMsg
    __del__ = lambda self: None
AttStateFswMsg_swigregister = _eulerRotation.AttStateFswMsg_swigregister
AttStateFswMsg_swigregister(AttStateFswMsg)


import sys
protectAllClasses(sys.modules[__name__])

# This file is compatible with both classic and new-style classes.

