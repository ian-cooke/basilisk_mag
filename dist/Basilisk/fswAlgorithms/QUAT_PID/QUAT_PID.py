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
        mname = '.'.join((pkg, '_QUAT_PID')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_QUAT_PID')
    _QUAT_PID = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_QUAT_PID', [dirname(__file__)])
        except ImportError:
            import _QUAT_PID
            return _QUAT_PID
        try:
            _mod = imp.load_module('_QUAT_PID', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _QUAT_PID = swig_import_helper()
    del swig_import_helper
else:
    import _QUAT_PID
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
    return _QUAT_PID.new_doubleArray(nelements)
new_doubleArray = _QUAT_PID.new_doubleArray

def delete_doubleArray(ary):
    return _QUAT_PID.delete_doubleArray(ary)
delete_doubleArray = _QUAT_PID.delete_doubleArray

def doubleArray_getitem(ary, index):
    return _QUAT_PID.doubleArray_getitem(ary, index)
doubleArray_getitem = _QUAT_PID.doubleArray_getitem

def doubleArray_setitem(ary, index, value):
    return _QUAT_PID.doubleArray_setitem(ary, index, value)
doubleArray_setitem = _QUAT_PID.doubleArray_setitem

def new_longArray(nelements):
    return _QUAT_PID.new_longArray(nelements)
new_longArray = _QUAT_PID.new_longArray

def delete_longArray(ary):
    return _QUAT_PID.delete_longArray(ary)
delete_longArray = _QUAT_PID.delete_longArray

def longArray_getitem(ary, index):
    return _QUAT_PID.longArray_getitem(ary, index)
longArray_getitem = _QUAT_PID.longArray_getitem

def longArray_setitem(ary, index, value):
    return _QUAT_PID.longArray_setitem(ary, index, value)
longArray_setitem = _QUAT_PID.longArray_setitem

def new_intArray(nelements):
    return _QUAT_PID.new_intArray(nelements)
new_intArray = _QUAT_PID.new_intArray

def delete_intArray(ary):
    return _QUAT_PID.delete_intArray(ary)
delete_intArray = _QUAT_PID.delete_intArray

def intArray_getitem(ary, index):
    return _QUAT_PID.intArray_getitem(ary, index)
intArray_getitem = _QUAT_PID.intArray_getitem

def intArray_setitem(ary, index, value):
    return _QUAT_PID.intArray_setitem(ary, index, value)
intArray_setitem = _QUAT_PID.intArray_setitem

def new_shortArray(nelements):
    return _QUAT_PID.new_shortArray(nelements)
new_shortArray = _QUAT_PID.new_shortArray

def delete_shortArray(ary):
    return _QUAT_PID.delete_shortArray(ary)
delete_shortArray = _QUAT_PID.delete_shortArray

def shortArray_getitem(ary, index):
    return _QUAT_PID.shortArray_getitem(ary, index)
shortArray_getitem = _QUAT_PID.shortArray_getitem

def shortArray_setitem(ary, index, value):
    return _QUAT_PID.shortArray_setitem(ary, index, value)
shortArray_setitem = _QUAT_PID.shortArray_setitem


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


Update_QUAT_PID = _QUAT_PID.Update_QUAT_PID
SelfInit_QUAT_PID = _QUAT_PID.SelfInit_QUAT_PID
CrossInit_QUAT_PID = _QUAT_PID.CrossInit_QUAT_PID
Reset_QUAT_PID = _QUAT_PID.Reset_QUAT_PID
sizeof_QUAT_PIDConfig = _QUAT_PID.sizeof_QUAT_PIDConfig
sizeof_AttGuidFswMsg = _QUAT_PID.sizeof_AttGuidFswMsg
sizeof_VehicleConfigFswMsg = _QUAT_PID.sizeof_VehicleConfigFswMsg
sizeof_RWArrayConfigFswMsg = _QUAT_PID.sizeof_RWArrayConfigFswMsg
sizeof_RWSpeedIntMsg = _QUAT_PID.sizeof_RWSpeedIntMsg
class QUAT_PIDConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, QUAT_PIDConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, QUAT_PIDConfig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["K"] = _QUAT_PID.QUAT_PIDConfig_K_set
    __swig_getmethods__["K"] = _QUAT_PID.QUAT_PIDConfig_K_get
    if _newclass:
        K = _swig_property(_QUAT_PID.QUAT_PIDConfig_K_get, _QUAT_PID.QUAT_PIDConfig_K_set)
    __swig_setmethods__["P"] = _QUAT_PID.QUAT_PIDConfig_P_set
    __swig_getmethods__["P"] = _QUAT_PID.QUAT_PIDConfig_P_get
    if _newclass:
        P = _swig_property(_QUAT_PID.QUAT_PIDConfig_P_get, _QUAT_PID.QUAT_PIDConfig_P_set)
    __swig_setmethods__["K_I"] = _QUAT_PID.QUAT_PIDConfig_K_I_set
    __swig_getmethods__["K_I"] = _QUAT_PID.QUAT_PIDConfig_K_I_get
    if _newclass:
        K_I = _swig_property(_QUAT_PID.QUAT_PIDConfig_K_I_get, _QUAT_PID.QUAT_PIDConfig_K_I_set)
    __swig_setmethods__["ISCPntB_B"] = _QUAT_PID.QUAT_PIDConfig_ISCPntB_B_set
    __swig_getmethods__["ISCPntB_B"] = _QUAT_PID.QUAT_PIDConfig_ISCPntB_B_get
    if _newclass:
        ISCPntB_B = _swig_property(_QUAT_PID.QUAT_PIDConfig_ISCPntB_B_get, _QUAT_PID.QUAT_PIDConfig_ISCPntB_B_set)
    __swig_setmethods__["rwConfigParams"] = _QUAT_PID.QUAT_PIDConfig_rwConfigParams_set
    __swig_getmethods__["rwConfigParams"] = _QUAT_PID.QUAT_PIDConfig_rwConfigParams_get
    if _newclass:
        rwConfigParams = _swig_property(_QUAT_PID.QUAT_PIDConfig_rwConfigParams_get, _QUAT_PID.QUAT_PIDConfig_rwConfigParams_set)
    __swig_setmethods__["priorTime"] = _QUAT_PID.QUAT_PIDConfig_priorTime_set
    __swig_getmethods__["priorTime"] = _QUAT_PID.QUAT_PIDConfig_priorTime_get
    if _newclass:
        priorTime = _swig_property(_QUAT_PID.QUAT_PIDConfig_priorTime_get, _QUAT_PID.QUAT_PIDConfig_priorTime_set)
    __swig_setmethods__["rwParamsInMsgName"] = _QUAT_PID.QUAT_PIDConfig_rwParamsInMsgName_set
    __swig_getmethods__["rwParamsInMsgName"] = _QUAT_PID.QUAT_PIDConfig_rwParamsInMsgName_get
    if _newclass:
        rwParamsInMsgName = _swig_property(_QUAT_PID.QUAT_PIDConfig_rwParamsInMsgName_get, _QUAT_PID.QUAT_PIDConfig_rwParamsInMsgName_set)
    __swig_setmethods__["rwParamsInMsgID"] = _QUAT_PID.QUAT_PIDConfig_rwParamsInMsgID_set
    __swig_getmethods__["rwParamsInMsgID"] = _QUAT_PID.QUAT_PIDConfig_rwParamsInMsgID_get
    if _newclass:
        rwParamsInMsgID = _swig_property(_QUAT_PID.QUAT_PIDConfig_rwParamsInMsgID_get, _QUAT_PID.QUAT_PIDConfig_rwParamsInMsgID_set)
    __swig_setmethods__["vehConfigInMsgName"] = _QUAT_PID.QUAT_PIDConfig_vehConfigInMsgName_set
    __swig_getmethods__["vehConfigInMsgName"] = _QUAT_PID.QUAT_PIDConfig_vehConfigInMsgName_get
    if _newclass:
        vehConfigInMsgName = _swig_property(_QUAT_PID.QUAT_PIDConfig_vehConfigInMsgName_get, _QUAT_PID.QUAT_PIDConfig_vehConfigInMsgName_set)
    __swig_setmethods__["vehConfigInMsgID"] = _QUAT_PID.QUAT_PIDConfig_vehConfigInMsgID_set
    __swig_getmethods__["vehConfigInMsgID"] = _QUAT_PID.QUAT_PIDConfig_vehConfigInMsgID_get
    if _newclass:
        vehConfigInMsgID = _swig_property(_QUAT_PID.QUAT_PIDConfig_vehConfigInMsgID_get, _QUAT_PID.QUAT_PIDConfig_vehConfigInMsgID_set)
    __swig_setmethods__["rwAvailInMsgName"] = _QUAT_PID.QUAT_PIDConfig_rwAvailInMsgName_set
    __swig_getmethods__["rwAvailInMsgName"] = _QUAT_PID.QUAT_PIDConfig_rwAvailInMsgName_get
    if _newclass:
        rwAvailInMsgName = _swig_property(_QUAT_PID.QUAT_PIDConfig_rwAvailInMsgName_get, _QUAT_PID.QUAT_PIDConfig_rwAvailInMsgName_set)
    __swig_setmethods__["rwAvailInMsgID"] = _QUAT_PID.QUAT_PIDConfig_rwAvailInMsgID_set
    __swig_getmethods__["rwAvailInMsgID"] = _QUAT_PID.QUAT_PIDConfig_rwAvailInMsgID_get
    if _newclass:
        rwAvailInMsgID = _swig_property(_QUAT_PID.QUAT_PIDConfig_rwAvailInMsgID_get, _QUAT_PID.QUAT_PIDConfig_rwAvailInMsgID_set)
    __swig_setmethods__["outputErrorName"] = _QUAT_PID.QUAT_PIDConfig_outputErrorName_set
    __swig_getmethods__["outputErrorName"] = _QUAT_PID.QUAT_PIDConfig_outputErrorName_get
    if _newclass:
        outputErrorName = _swig_property(_QUAT_PID.QUAT_PIDConfig_outputErrorName_get, _QUAT_PID.QUAT_PIDConfig_outputErrorName_set)
    __swig_setmethods__["outputDataName"] = _QUAT_PID.QUAT_PIDConfig_outputDataName_set
    __swig_getmethods__["outputDataName"] = _QUAT_PID.QUAT_PIDConfig_outputDataName_get
    if _newclass:
        outputDataName = _swig_property(_QUAT_PID.QUAT_PIDConfig_outputDataName_get, _QUAT_PID.QUAT_PIDConfig_outputDataName_set)
    __swig_setmethods__["inputGuidName"] = _QUAT_PID.QUAT_PIDConfig_inputGuidName_set
    __swig_getmethods__["inputGuidName"] = _QUAT_PID.QUAT_PIDConfig_inputGuidName_get
    if _newclass:
        inputGuidName = _swig_property(_QUAT_PID.QUAT_PIDConfig_inputGuidName_get, _QUAT_PID.QUAT_PIDConfig_inputGuidName_set)
    __swig_setmethods__["inputAttName"] = _QUAT_PID.QUAT_PIDConfig_inputAttName_set
    __swig_getmethods__["inputAttName"] = _QUAT_PID.QUAT_PIDConfig_inputAttName_get
    if _newclass:
        inputAttName = _swig_property(_QUAT_PID.QUAT_PIDConfig_inputAttName_get, _QUAT_PID.QUAT_PIDConfig_inputAttName_set)
    __swig_setmethods__["inputRatesName"] = _QUAT_PID.QUAT_PIDConfig_inputRatesName_set
    __swig_getmethods__["inputRatesName"] = _QUAT_PID.QUAT_PIDConfig_inputRatesName_get
    if _newclass:
        inputRatesName = _swig_property(_QUAT_PID.QUAT_PIDConfig_inputRatesName_get, _QUAT_PID.QUAT_PIDConfig_inputRatesName_set)
    __swig_setmethods__["inputSunName"] = _QUAT_PID.QUAT_PIDConfig_inputSunName_set
    __swig_getmethods__["inputSunName"] = _QUAT_PID.QUAT_PIDConfig_inputSunName_get
    if _newclass:
        inputSunName = _swig_property(_QUAT_PID.QUAT_PIDConfig_inputSunName_get, _QUAT_PID.QUAT_PIDConfig_inputSunName_set)
    __swig_setmethods__["inputRWSpeedsName"] = _QUAT_PID.QUAT_PIDConfig_inputRWSpeedsName_set
    __swig_getmethods__["inputRWSpeedsName"] = _QUAT_PID.QUAT_PIDConfig_inputRWSpeedsName_get
    if _newclass:
        inputRWSpeedsName = _swig_property(_QUAT_PID.QUAT_PIDConfig_inputRWSpeedsName_get, _QUAT_PID.QUAT_PIDConfig_inputRWSpeedsName_set)
    __swig_setmethods__["inputRWSpeedsID"] = _QUAT_PID.QUAT_PIDConfig_inputRWSpeedsID_set
    __swig_getmethods__["inputRWSpeedsID"] = _QUAT_PID.QUAT_PIDConfig_inputRWSpeedsID_get
    if _newclass:
        inputRWSpeedsID = _swig_property(_QUAT_PID.QUAT_PIDConfig_inputRWSpeedsID_get, _QUAT_PID.QUAT_PIDConfig_inputRWSpeedsID_set)
    __swig_setmethods__["outputMsgID"] = _QUAT_PID.QUAT_PIDConfig_outputMsgID_set
    __swig_getmethods__["outputMsgID"] = _QUAT_PID.QUAT_PIDConfig_outputMsgID_get
    if _newclass:
        outputMsgID = _swig_property(_QUAT_PID.QUAT_PIDConfig_outputMsgID_get, _QUAT_PID.QUAT_PIDConfig_outputMsgID_set)
    __swig_setmethods__["outputErrorID"] = _QUAT_PID.QUAT_PIDConfig_outputErrorID_set
    __swig_getmethods__["outputErrorID"] = _QUAT_PID.QUAT_PIDConfig_outputErrorID_get
    if _newclass:
        outputErrorID = _swig_property(_QUAT_PID.QUAT_PIDConfig_outputErrorID_get, _QUAT_PID.QUAT_PIDConfig_outputErrorID_set)
    __swig_setmethods__["inputGuidID"] = _QUAT_PID.QUAT_PIDConfig_inputGuidID_set
    __swig_getmethods__["inputGuidID"] = _QUAT_PID.QUAT_PIDConfig_inputGuidID_get
    if _newclass:
        inputGuidID = _swig_property(_QUAT_PID.QUAT_PIDConfig_inputGuidID_get, _QUAT_PID.QUAT_PIDConfig_inputGuidID_set)
    __swig_setmethods__["inputAttID"] = _QUAT_PID.QUAT_PIDConfig_inputAttID_set
    __swig_getmethods__["inputAttID"] = _QUAT_PID.QUAT_PIDConfig_inputAttID_get
    if _newclass:
        inputAttID = _swig_property(_QUAT_PID.QUAT_PIDConfig_inputAttID_get, _QUAT_PID.QUAT_PIDConfig_inputAttID_set)
    __swig_setmethods__["inputRatesID"] = _QUAT_PID.QUAT_PIDConfig_inputRatesID_set
    __swig_getmethods__["inputRatesID"] = _QUAT_PID.QUAT_PIDConfig_inputRatesID_get
    if _newclass:
        inputRatesID = _swig_property(_QUAT_PID.QUAT_PIDConfig_inputRatesID_get, _QUAT_PID.QUAT_PIDConfig_inputRatesID_set)
    __swig_setmethods__["inputSunID"] = _QUAT_PID.QUAT_PIDConfig_inputSunID_set
    __swig_getmethods__["inputSunID"] = _QUAT_PID.QUAT_PIDConfig_inputSunID_get
    if _newclass:
        inputSunID = _swig_property(_QUAT_PID.QUAT_PIDConfig_inputSunID_get, _QUAT_PID.QUAT_PIDConfig_inputSunID_set)
    __swig_setmethods__["controlOut"] = _QUAT_PID.QUAT_PIDConfig_controlOut_set
    __swig_getmethods__["controlOut"] = _QUAT_PID.QUAT_PIDConfig_controlOut_get
    if _newclass:
        controlOut = _swig_property(_QUAT_PID.QUAT_PIDConfig_controlOut_get, _QUAT_PID.QUAT_PIDConfig_controlOut_set)
    __swig_setmethods__["controlError"] = _QUAT_PID.QUAT_PIDConfig_controlError_set
    __swig_getmethods__["controlError"] = _QUAT_PID.QUAT_PIDConfig_controlError_get
    if _newclass:
        controlError = _swig_property(_QUAT_PID.QUAT_PIDConfig_controlError_get, _QUAT_PID.QUAT_PIDConfig_controlError_set)

    def __init__(self):
        this = _QUAT_PID.new_QUAT_PIDConfig()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _QUAT_PID.delete_QUAT_PIDConfig
    __del__ = lambda self: None
QUAT_PIDConfig_swigregister = _QUAT_PID.QUAT_PIDConfig_swigregister
QUAT_PIDConfig_swigregister(QUAT_PIDConfig)


def ctl_pid(q_BR, omega_BN, omega_RN, omega_BR, domega_RN, ctl_gain, I_RW_values, rw_spin_rates, GsValues, JsValues, out_u):
    return _QUAT_PID.ctl_pid(q_BR, omega_BN, omega_RN, omega_BR, domega_RN, ctl_gain, I_RW_values, rw_spin_rates, GsValues, JsValues, out_u)
ctl_pid = _QUAT_PID.ctl_pid

def calc_q_error(q_bn, q_rn, q_br):
    return _QUAT_PID.calc_q_error(q_bn, q_rn, q_br)
calc_q_error = _QUAT_PID.calc_q_error

def q_2_dcm(q, dcm):
    return _QUAT_PID.q_2_dcm(q, dcm)
q_2_dcm = _QUAT_PID.q_2_dcm

def dcm_2_q(dcm, q):
    return _QUAT_PID.dcm_2_q(dcm, q)
dcm_2_q = _QUAT_PID.dcm_2_q
class AttGuidFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AttGuidFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AttGuidFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sigma_BR"] = _QUAT_PID.AttGuidFswMsg_sigma_BR_set
    __swig_getmethods__["sigma_BR"] = _QUAT_PID.AttGuidFswMsg_sigma_BR_get
    if _newclass:
        sigma_BR = _swig_property(_QUAT_PID.AttGuidFswMsg_sigma_BR_get, _QUAT_PID.AttGuidFswMsg_sigma_BR_set)
    __swig_setmethods__["omega_BR_B"] = _QUAT_PID.AttGuidFswMsg_omega_BR_B_set
    __swig_getmethods__["omega_BR_B"] = _QUAT_PID.AttGuidFswMsg_omega_BR_B_get
    if _newclass:
        omega_BR_B = _swig_property(_QUAT_PID.AttGuidFswMsg_omega_BR_B_get, _QUAT_PID.AttGuidFswMsg_omega_BR_B_set)
    __swig_setmethods__["omega_RN_B"] = _QUAT_PID.AttGuidFswMsg_omega_RN_B_set
    __swig_getmethods__["omega_RN_B"] = _QUAT_PID.AttGuidFswMsg_omega_RN_B_get
    if _newclass:
        omega_RN_B = _swig_property(_QUAT_PID.AttGuidFswMsg_omega_RN_B_get, _QUAT_PID.AttGuidFswMsg_omega_RN_B_set)
    __swig_setmethods__["domega_RN_B"] = _QUAT_PID.AttGuidFswMsg_domega_RN_B_set
    __swig_getmethods__["domega_RN_B"] = _QUAT_PID.AttGuidFswMsg_domega_RN_B_get
    if _newclass:
        domega_RN_B = _swig_property(_QUAT_PID.AttGuidFswMsg_domega_RN_B_get, _QUAT_PID.AttGuidFswMsg_domega_RN_B_set)
    __swig_setmethods__["PRV"] = _QUAT_PID.AttGuidFswMsg_PRV_set
    __swig_getmethods__["PRV"] = _QUAT_PID.AttGuidFswMsg_PRV_get
    if _newclass:
        PRV = _swig_property(_QUAT_PID.AttGuidFswMsg_PRV_get, _QUAT_PID.AttGuidFswMsg_PRV_set)

    def __init__(self):
        this = _QUAT_PID.new_AttGuidFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _QUAT_PID.delete_AttGuidFswMsg
    __del__ = lambda self: None
AttGuidFswMsg_swigregister = _QUAT_PID.AttGuidFswMsg_swigregister
AttGuidFswMsg_swigregister(AttGuidFswMsg)

class VehicleConfigFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VehicleConfigFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VehicleConfigFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ISCPntB_B"] = _QUAT_PID.VehicleConfigFswMsg_ISCPntB_B_set
    __swig_getmethods__["ISCPntB_B"] = _QUAT_PID.VehicleConfigFswMsg_ISCPntB_B_get
    if _newclass:
        ISCPntB_B = _swig_property(_QUAT_PID.VehicleConfigFswMsg_ISCPntB_B_get, _QUAT_PID.VehicleConfigFswMsg_ISCPntB_B_set)
    __swig_setmethods__["CoM_B"] = _QUAT_PID.VehicleConfigFswMsg_CoM_B_set
    __swig_getmethods__["CoM_B"] = _QUAT_PID.VehicleConfigFswMsg_CoM_B_get
    if _newclass:
        CoM_B = _swig_property(_QUAT_PID.VehicleConfigFswMsg_CoM_B_get, _QUAT_PID.VehicleConfigFswMsg_CoM_B_set)
    __swig_setmethods__["CurrentADCSState"] = _QUAT_PID.VehicleConfigFswMsg_CurrentADCSState_set
    __swig_getmethods__["CurrentADCSState"] = _QUAT_PID.VehicleConfigFswMsg_CurrentADCSState_get
    if _newclass:
        CurrentADCSState = _swig_property(_QUAT_PID.VehicleConfigFswMsg_CurrentADCSState_get, _QUAT_PID.VehicleConfigFswMsg_CurrentADCSState_set)

    def __init__(self):
        this = _QUAT_PID.new_VehicleConfigFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _QUAT_PID.delete_VehicleConfigFswMsg
    __del__ = lambda self: None
VehicleConfigFswMsg_swigregister = _QUAT_PID.VehicleConfigFswMsg_swigregister
VehicleConfigFswMsg_swigregister(VehicleConfigFswMsg)

class RWArrayConfigFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RWArrayConfigFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RWArrayConfigFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["GsMatrix_B"] = _QUAT_PID.RWArrayConfigFswMsg_GsMatrix_B_set
    __swig_getmethods__["GsMatrix_B"] = _QUAT_PID.RWArrayConfigFswMsg_GsMatrix_B_get
    if _newclass:
        GsMatrix_B = _swig_property(_QUAT_PID.RWArrayConfigFswMsg_GsMatrix_B_get, _QUAT_PID.RWArrayConfigFswMsg_GsMatrix_B_set)
    __swig_setmethods__["JsList"] = _QUAT_PID.RWArrayConfigFswMsg_JsList_set
    __swig_getmethods__["JsList"] = _QUAT_PID.RWArrayConfigFswMsg_JsList_get
    if _newclass:
        JsList = _swig_property(_QUAT_PID.RWArrayConfigFswMsg_JsList_get, _QUAT_PID.RWArrayConfigFswMsg_JsList_set)
    __swig_setmethods__["numRW"] = _QUAT_PID.RWArrayConfigFswMsg_numRW_set
    __swig_getmethods__["numRW"] = _QUAT_PID.RWArrayConfigFswMsg_numRW_get
    if _newclass:
        numRW = _swig_property(_QUAT_PID.RWArrayConfigFswMsg_numRW_get, _QUAT_PID.RWArrayConfigFswMsg_numRW_set)
    __swig_setmethods__["uMax"] = _QUAT_PID.RWArrayConfigFswMsg_uMax_set
    __swig_getmethods__["uMax"] = _QUAT_PID.RWArrayConfigFswMsg_uMax_get
    if _newclass:
        uMax = _swig_property(_QUAT_PID.RWArrayConfigFswMsg_uMax_get, _QUAT_PID.RWArrayConfigFswMsg_uMax_set)

    def __init__(self):
        this = _QUAT_PID.new_RWArrayConfigFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _QUAT_PID.delete_RWArrayConfigFswMsg
    __del__ = lambda self: None
RWArrayConfigFswMsg_swigregister = _QUAT_PID.RWArrayConfigFswMsg_swigregister
RWArrayConfigFswMsg_swigregister(RWArrayConfigFswMsg)

class RWSpeedIntMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RWSpeedIntMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RWSpeedIntMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["wheelSpeeds"] = _QUAT_PID.RWSpeedIntMsg_wheelSpeeds_set
    __swig_getmethods__["wheelSpeeds"] = _QUAT_PID.RWSpeedIntMsg_wheelSpeeds_get
    if _newclass:
        wheelSpeeds = _swig_property(_QUAT_PID.RWSpeedIntMsg_wheelSpeeds_get, _QUAT_PID.RWSpeedIntMsg_wheelSpeeds_set)
    __swig_setmethods__["wheelThetas"] = _QUAT_PID.RWSpeedIntMsg_wheelThetas_set
    __swig_getmethods__["wheelThetas"] = _QUAT_PID.RWSpeedIntMsg_wheelThetas_get
    if _newclass:
        wheelThetas = _swig_property(_QUAT_PID.RWSpeedIntMsg_wheelThetas_get, _QUAT_PID.RWSpeedIntMsg_wheelThetas_set)

    def __init__(self):
        this = _QUAT_PID.new_RWSpeedIntMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _QUAT_PID.delete_RWSpeedIntMsg
    __del__ = lambda self: None
RWSpeedIntMsg_swigregister = _QUAT_PID.RWSpeedIntMsg_swigregister
RWSpeedIntMsg_swigregister(RWSpeedIntMsg)

class CmdTorqueBodyIntMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CmdTorqueBodyIntMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CmdTorqueBodyIntMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["torqueRequestBody"] = _QUAT_PID.CmdTorqueBodyIntMsg_torqueRequestBody_set
    __swig_getmethods__["torqueRequestBody"] = _QUAT_PID.CmdTorqueBodyIntMsg_torqueRequestBody_get
    if _newclass:
        torqueRequestBody = _swig_property(_QUAT_PID.CmdTorqueBodyIntMsg_torqueRequestBody_get, _QUAT_PID.CmdTorqueBodyIntMsg_torqueRequestBody_set)

    def __init__(self):
        this = _QUAT_PID.new_CmdTorqueBodyIntMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _QUAT_PID.delete_CmdTorqueBodyIntMsg
    __del__ = lambda self: None
CmdTorqueBodyIntMsg_swigregister = _QUAT_PID.CmdTorqueBodyIntMsg_swigregister
CmdTorqueBodyIntMsg_swigregister(CmdTorqueBodyIntMsg)

sizeof_CmdTorqueBodyIntMsg = _QUAT_PID.sizeof_CmdTorqueBodyIntMsg
class QuatGuidFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, QuatGuidFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, QuatGuidFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sigma_BR"] = _QUAT_PID.QuatGuidFswMsg_sigma_BR_set
    __swig_getmethods__["sigma_BR"] = _QUAT_PID.QuatGuidFswMsg_sigma_BR_get
    if _newclass:
        sigma_BR = _swig_property(_QUAT_PID.QuatGuidFswMsg_sigma_BR_get, _QUAT_PID.QuatGuidFswMsg_sigma_BR_set)
    __swig_setmethods__["q_BN"] = _QUAT_PID.QuatGuidFswMsg_q_BN_set
    __swig_getmethods__["q_BN"] = _QUAT_PID.QuatGuidFswMsg_q_BN_get
    if _newclass:
        q_BN = _swig_property(_QUAT_PID.QuatGuidFswMsg_q_BN_get, _QUAT_PID.QuatGuidFswMsg_q_BN_set)
    __swig_setmethods__["q_BR"] = _QUAT_PID.QuatGuidFswMsg_q_BR_set
    __swig_getmethods__["q_BR"] = _QUAT_PID.QuatGuidFswMsg_q_BR_get
    if _newclass:
        q_BR = _swig_property(_QUAT_PID.QuatGuidFswMsg_q_BR_get, _QUAT_PID.QuatGuidFswMsg_q_BR_set)
    __swig_setmethods__["PRV_ang"] = _QUAT_PID.QuatGuidFswMsg_PRV_ang_set
    __swig_getmethods__["PRV_ang"] = _QUAT_PID.QuatGuidFswMsg_PRV_ang_get
    if _newclass:
        PRV_ang = _swig_property(_QUAT_PID.QuatGuidFswMsg_PRV_ang_get, _QUAT_PID.QuatGuidFswMsg_PRV_ang_set)

    def __init__(self):
        this = _QUAT_PID.new_QuatGuidFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _QUAT_PID.delete_QuatGuidFswMsg
    __del__ = lambda self: None
QuatGuidFswMsg_swigregister = _QUAT_PID.QuatGuidFswMsg_swigregister
QuatGuidFswMsg_swigregister(QuatGuidFswMsg)

sizeof_QuatGuidFswMsg = _QUAT_PID.sizeof_QuatGuidFswMsg

import sys
protectAllClasses(sys.modules[__name__])

# This file is compatible with both classic and new-style classes.

