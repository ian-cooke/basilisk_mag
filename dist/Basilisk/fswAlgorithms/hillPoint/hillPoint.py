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
        mname = '.'.join((pkg, '_hillPoint')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_hillPoint')
    _hillPoint = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_hillPoint', [dirname(__file__)])
        except ImportError:
            import _hillPoint
            return _hillPoint
        try:
            _mod = imp.load_module('_hillPoint', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _hillPoint = swig_import_helper()
    del swig_import_helper
else:
    import _hillPoint
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
    return _hillPoint.new_doubleArray(nelements)
new_doubleArray = _hillPoint.new_doubleArray

def delete_doubleArray(ary):
    return _hillPoint.delete_doubleArray(ary)
delete_doubleArray = _hillPoint.delete_doubleArray

def doubleArray_getitem(ary, index):
    return _hillPoint.doubleArray_getitem(ary, index)
doubleArray_getitem = _hillPoint.doubleArray_getitem

def doubleArray_setitem(ary, index, value):
    return _hillPoint.doubleArray_setitem(ary, index, value)
doubleArray_setitem = _hillPoint.doubleArray_setitem

def new_longArray(nelements):
    return _hillPoint.new_longArray(nelements)
new_longArray = _hillPoint.new_longArray

def delete_longArray(ary):
    return _hillPoint.delete_longArray(ary)
delete_longArray = _hillPoint.delete_longArray

def longArray_getitem(ary, index):
    return _hillPoint.longArray_getitem(ary, index)
longArray_getitem = _hillPoint.longArray_getitem

def longArray_setitem(ary, index, value):
    return _hillPoint.longArray_setitem(ary, index, value)
longArray_setitem = _hillPoint.longArray_setitem

def new_intArray(nelements):
    return _hillPoint.new_intArray(nelements)
new_intArray = _hillPoint.new_intArray

def delete_intArray(ary):
    return _hillPoint.delete_intArray(ary)
delete_intArray = _hillPoint.delete_intArray

def intArray_getitem(ary, index):
    return _hillPoint.intArray_getitem(ary, index)
intArray_getitem = _hillPoint.intArray_getitem

def intArray_setitem(ary, index, value):
    return _hillPoint.intArray_setitem(ary, index, value)
intArray_setitem = _hillPoint.intArray_setitem

def new_shortArray(nelements):
    return _hillPoint.new_shortArray(nelements)
new_shortArray = _hillPoint.new_shortArray

def delete_shortArray(ary):
    return _hillPoint.delete_shortArray(ary)
delete_shortArray = _hillPoint.delete_shortArray

def shortArray_getitem(ary, index):
    return _hillPoint.shortArray_getitem(ary, index)
shortArray_getitem = _hillPoint.shortArray_getitem

def shortArray_setitem(ary, index, value):
    return _hillPoint.shortArray_setitem(ary, index, value)
shortArray_setitem = _hillPoint.shortArray_setitem


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


Update_hillPoint = _hillPoint.Update_hillPoint
SelfInit_hillPoint = _hillPoint.SelfInit_hillPoint
CrossInit_hillPoint = _hillPoint.CrossInit_hillPoint
Reset_hillPoint = _hillPoint.Reset_hillPoint
class hillPointConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hillPointConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hillPointConfig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["outputDataName"] = _hillPoint.hillPointConfig_outputDataName_set
    __swig_getmethods__["outputDataName"] = _hillPoint.hillPointConfig_outputDataName_get
    if _newclass:
        outputDataName = _swig_property(_hillPoint.hillPointConfig_outputDataName_get, _hillPoint.hillPointConfig_outputDataName_set)
    __swig_setmethods__["outputMsgID"] = _hillPoint.hillPointConfig_outputMsgID_set
    __swig_getmethods__["outputMsgID"] = _hillPoint.hillPointConfig_outputMsgID_get
    if _newclass:
        outputMsgID = _swig_property(_hillPoint.hillPointConfig_outputMsgID_get, _hillPoint.hillPointConfig_outputMsgID_set)
    __swig_setmethods__["inputNavDataName"] = _hillPoint.hillPointConfig_inputNavDataName_set
    __swig_getmethods__["inputNavDataName"] = _hillPoint.hillPointConfig_inputNavDataName_get
    if _newclass:
        inputNavDataName = _swig_property(_hillPoint.hillPointConfig_inputNavDataName_get, _hillPoint.hillPointConfig_inputNavDataName_set)
    __swig_setmethods__["inputNavID"] = _hillPoint.hillPointConfig_inputNavID_set
    __swig_getmethods__["inputNavID"] = _hillPoint.hillPointConfig_inputNavID_get
    if _newclass:
        inputNavID = _swig_property(_hillPoint.hillPointConfig_inputNavID_get, _hillPoint.hillPointConfig_inputNavID_set)
    __swig_setmethods__["inputCelMessName"] = _hillPoint.hillPointConfig_inputCelMessName_set
    __swig_getmethods__["inputCelMessName"] = _hillPoint.hillPointConfig_inputCelMessName_get
    if _newclass:
        inputCelMessName = _swig_property(_hillPoint.hillPointConfig_inputCelMessName_get, _hillPoint.hillPointConfig_inputCelMessName_set)
    __swig_setmethods__["inputCelID"] = _hillPoint.hillPointConfig_inputCelID_set
    __swig_getmethods__["inputCelID"] = _hillPoint.hillPointConfig_inputCelID_get
    if _newclass:
        inputCelID = _swig_property(_hillPoint.hillPointConfig_inputCelID_get, _hillPoint.hillPointConfig_inputCelID_set)
    __swig_setmethods__["attRefOut"] = _hillPoint.hillPointConfig_attRefOut_set
    __swig_getmethods__["attRefOut"] = _hillPoint.hillPointConfig_attRefOut_get
    if _newclass:
        attRefOut = _swig_property(_hillPoint.hillPointConfig_attRefOut_get, _hillPoint.hillPointConfig_attRefOut_set)

    def __init__(self):
        this = _hillPoint.new_hillPointConfig()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _hillPoint.delete_hillPointConfig
    __del__ = lambda self: None
hillPointConfig_swigregister = _hillPoint.hillPointConfig_swigregister
hillPointConfig_swigregister(hillPointConfig)


def computeHillPointingReference(ConfigData, r_BN_N, v_BN_N, celBdyPositonVector, celBdyVelocityVector):
    return _hillPoint.computeHillPointingReference(ConfigData, r_BN_N, v_BN_N, celBdyPositonVector, celBdyVelocityVector)
computeHillPointingReference = _hillPoint.computeHillPointingReference
class EphemerisIntMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, EphemerisIntMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, EphemerisIntMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["r_BdyZero_N"] = _hillPoint.EphemerisIntMsg_r_BdyZero_N_set
    __swig_getmethods__["r_BdyZero_N"] = _hillPoint.EphemerisIntMsg_r_BdyZero_N_get
    if _newclass:
        r_BdyZero_N = _swig_property(_hillPoint.EphemerisIntMsg_r_BdyZero_N_get, _hillPoint.EphemerisIntMsg_r_BdyZero_N_set)
    __swig_setmethods__["v_BdyZero_N"] = _hillPoint.EphemerisIntMsg_v_BdyZero_N_set
    __swig_getmethods__["v_BdyZero_N"] = _hillPoint.EphemerisIntMsg_v_BdyZero_N_get
    if _newclass:
        v_BdyZero_N = _swig_property(_hillPoint.EphemerisIntMsg_v_BdyZero_N_get, _hillPoint.EphemerisIntMsg_v_BdyZero_N_set)
    __swig_setmethods__["timeTag"] = _hillPoint.EphemerisIntMsg_timeTag_set
    __swig_getmethods__["timeTag"] = _hillPoint.EphemerisIntMsg_timeTag_get
    if _newclass:
        timeTag = _swig_property(_hillPoint.EphemerisIntMsg_timeTag_get, _hillPoint.EphemerisIntMsg_timeTag_set)

    def __init__(self):
        this = _hillPoint.new_EphemerisIntMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _hillPoint.delete_EphemerisIntMsg
    __del__ = lambda self: None
EphemerisIntMsg_swigregister = _hillPoint.EphemerisIntMsg_swigregister
EphemerisIntMsg_swigregister(EphemerisIntMsg)

class NavTransIntMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NavTransIntMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NavTransIntMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["timeTag"] = _hillPoint.NavTransIntMsg_timeTag_set
    __swig_getmethods__["timeTag"] = _hillPoint.NavTransIntMsg_timeTag_get
    if _newclass:
        timeTag = _swig_property(_hillPoint.NavTransIntMsg_timeTag_get, _hillPoint.NavTransIntMsg_timeTag_set)
    __swig_setmethods__["r_BN_N"] = _hillPoint.NavTransIntMsg_r_BN_N_set
    __swig_getmethods__["r_BN_N"] = _hillPoint.NavTransIntMsg_r_BN_N_get
    if _newclass:
        r_BN_N = _swig_property(_hillPoint.NavTransIntMsg_r_BN_N_get, _hillPoint.NavTransIntMsg_r_BN_N_set)
    __swig_setmethods__["v_BN_N"] = _hillPoint.NavTransIntMsg_v_BN_N_set
    __swig_getmethods__["v_BN_N"] = _hillPoint.NavTransIntMsg_v_BN_N_get
    if _newclass:
        v_BN_N = _swig_property(_hillPoint.NavTransIntMsg_v_BN_N_get, _hillPoint.NavTransIntMsg_v_BN_N_set)
    __swig_setmethods__["vehAccumDV"] = _hillPoint.NavTransIntMsg_vehAccumDV_set
    __swig_getmethods__["vehAccumDV"] = _hillPoint.NavTransIntMsg_vehAccumDV_get
    if _newclass:
        vehAccumDV = _swig_property(_hillPoint.NavTransIntMsg_vehAccumDV_get, _hillPoint.NavTransIntMsg_vehAccumDV_set)

    def __init__(self):
        this = _hillPoint.new_NavTransIntMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _hillPoint.delete_NavTransIntMsg
    __del__ = lambda self: None
NavTransIntMsg_swigregister = _hillPoint.NavTransIntMsg_swigregister
NavTransIntMsg_swigregister(NavTransIntMsg)

class AttRefFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AttRefFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AttRefFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sigma_RN"] = _hillPoint.AttRefFswMsg_sigma_RN_set
    __swig_getmethods__["sigma_RN"] = _hillPoint.AttRefFswMsg_sigma_RN_get
    if _newclass:
        sigma_RN = _swig_property(_hillPoint.AttRefFswMsg_sigma_RN_get, _hillPoint.AttRefFswMsg_sigma_RN_set)
    __swig_setmethods__["omega_RN_N"] = _hillPoint.AttRefFswMsg_omega_RN_N_set
    __swig_getmethods__["omega_RN_N"] = _hillPoint.AttRefFswMsg_omega_RN_N_get
    if _newclass:
        omega_RN_N = _swig_property(_hillPoint.AttRefFswMsg_omega_RN_N_get, _hillPoint.AttRefFswMsg_omega_RN_N_set)
    __swig_setmethods__["domega_RN_N"] = _hillPoint.AttRefFswMsg_domega_RN_N_set
    __swig_getmethods__["domega_RN_N"] = _hillPoint.AttRefFswMsg_domega_RN_N_get
    if _newclass:
        domega_RN_N = _swig_property(_hillPoint.AttRefFswMsg_domega_RN_N_get, _hillPoint.AttRefFswMsg_domega_RN_N_set)

    def __init__(self):
        this = _hillPoint.new_AttRefFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _hillPoint.delete_AttRefFswMsg
    __del__ = lambda self: None
AttRefFswMsg_swigregister = _hillPoint.AttRefFswMsg_swigregister
AttRefFswMsg_swigregister(AttRefFswMsg)

sizeof_EphemerisIntMsg = _hillPoint.sizeof_EphemerisIntMsg
sizeof_hillPointConfig = _hillPoint.sizeof_hillPointConfig
sizeof_NavTransIntMsg = _hillPoint.sizeof_NavTransIntMsg
sizeof_AttRefFswMsg = _hillPoint.sizeof_AttRefFswMsg

import sys
protectAllClasses(sys.modules[__name__])

# This file is compatible with both classic and new-style classes.

