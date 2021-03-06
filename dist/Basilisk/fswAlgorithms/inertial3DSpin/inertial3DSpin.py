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
        mname = '.'.join((pkg, '_inertial3DSpin')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_inertial3DSpin')
    _inertial3DSpin = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_inertial3DSpin', [dirname(__file__)])
        except ImportError:
            import _inertial3DSpin
            return _inertial3DSpin
        try:
            _mod = imp.load_module('_inertial3DSpin', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _inertial3DSpin = swig_import_helper()
    del swig_import_helper
else:
    import _inertial3DSpin
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
    return _inertial3DSpin.new_doubleArray(nelements)
new_doubleArray = _inertial3DSpin.new_doubleArray

def delete_doubleArray(ary):
    return _inertial3DSpin.delete_doubleArray(ary)
delete_doubleArray = _inertial3DSpin.delete_doubleArray

def doubleArray_getitem(ary, index):
    return _inertial3DSpin.doubleArray_getitem(ary, index)
doubleArray_getitem = _inertial3DSpin.doubleArray_getitem

def doubleArray_setitem(ary, index, value):
    return _inertial3DSpin.doubleArray_setitem(ary, index, value)
doubleArray_setitem = _inertial3DSpin.doubleArray_setitem

def new_longArray(nelements):
    return _inertial3DSpin.new_longArray(nelements)
new_longArray = _inertial3DSpin.new_longArray

def delete_longArray(ary):
    return _inertial3DSpin.delete_longArray(ary)
delete_longArray = _inertial3DSpin.delete_longArray

def longArray_getitem(ary, index):
    return _inertial3DSpin.longArray_getitem(ary, index)
longArray_getitem = _inertial3DSpin.longArray_getitem

def longArray_setitem(ary, index, value):
    return _inertial3DSpin.longArray_setitem(ary, index, value)
longArray_setitem = _inertial3DSpin.longArray_setitem

def new_intArray(nelements):
    return _inertial3DSpin.new_intArray(nelements)
new_intArray = _inertial3DSpin.new_intArray

def delete_intArray(ary):
    return _inertial3DSpin.delete_intArray(ary)
delete_intArray = _inertial3DSpin.delete_intArray

def intArray_getitem(ary, index):
    return _inertial3DSpin.intArray_getitem(ary, index)
intArray_getitem = _inertial3DSpin.intArray_getitem

def intArray_setitem(ary, index, value):
    return _inertial3DSpin.intArray_setitem(ary, index, value)
intArray_setitem = _inertial3DSpin.intArray_setitem

def new_shortArray(nelements):
    return _inertial3DSpin.new_shortArray(nelements)
new_shortArray = _inertial3DSpin.new_shortArray

def delete_shortArray(ary):
    return _inertial3DSpin.delete_shortArray(ary)
delete_shortArray = _inertial3DSpin.delete_shortArray

def shortArray_getitem(ary, index):
    return _inertial3DSpin.shortArray_getitem(ary, index)
shortArray_getitem = _inertial3DSpin.shortArray_getitem

def shortArray_setitem(ary, index, value):
    return _inertial3DSpin.shortArray_setitem(ary, index, value)
shortArray_setitem = _inertial3DSpin.shortArray_setitem


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


Update_inertial3DSpin = _inertial3DSpin.Update_inertial3DSpin
SelfInit_inertial3DSpin = _inertial3DSpin.SelfInit_inertial3DSpin
CrossInit_inertial3DSpin = _inertial3DSpin.CrossInit_inertial3DSpin
Reset_inertial3DSpin = _inertial3DSpin.Reset_inertial3DSpin
sizeof_inertial3DSpinConfig = _inertial3DSpin.sizeof_inertial3DSpinConfig
sizeof_AttRefFswMsg = _inertial3DSpin.sizeof_AttRefFswMsg
class inertial3DSpinConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, inertial3DSpinConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, inertial3DSpinConfig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sigma_RN"] = _inertial3DSpin.inertial3DSpinConfig_sigma_RN_set
    __swig_getmethods__["sigma_RN"] = _inertial3DSpin.inertial3DSpinConfig_sigma_RN_get
    if _newclass:
        sigma_RN = _swig_property(_inertial3DSpin.inertial3DSpinConfig_sigma_RN_get, _inertial3DSpin.inertial3DSpinConfig_sigma_RN_set)
    __swig_setmethods__["omega_spin"] = _inertial3DSpin.inertial3DSpinConfig_omega_spin_set
    __swig_getmethods__["omega_spin"] = _inertial3DSpin.inertial3DSpinConfig_omega_spin_get
    if _newclass:
        omega_spin = _swig_property(_inertial3DSpin.inertial3DSpinConfig_omega_spin_get, _inertial3DSpin.inertial3DSpinConfig_omega_spin_set)
    __swig_setmethods__["priorTime"] = _inertial3DSpin.inertial3DSpinConfig_priorTime_set
    __swig_getmethods__["priorTime"] = _inertial3DSpin.inertial3DSpinConfig_priorTime_get
    if _newclass:
        priorTime = _swig_property(_inertial3DSpin.inertial3DSpinConfig_priorTime_get, _inertial3DSpin.inertial3DSpinConfig_priorTime_set)
    __swig_setmethods__["outputDataName"] = _inertial3DSpin.inertial3DSpinConfig_outputDataName_set
    __swig_getmethods__["outputDataName"] = _inertial3DSpin.inertial3DSpinConfig_outputDataName_get
    if _newclass:
        outputDataName = _swig_property(_inertial3DSpin.inertial3DSpinConfig_outputDataName_get, _inertial3DSpin.inertial3DSpinConfig_outputDataName_set)
    __swig_setmethods__["outputMsgID"] = _inertial3DSpin.inertial3DSpinConfig_outputMsgID_set
    __swig_getmethods__["outputMsgID"] = _inertial3DSpin.inertial3DSpinConfig_outputMsgID_get
    if _newclass:
        outputMsgID = _swig_property(_inertial3DSpin.inertial3DSpinConfig_outputMsgID_get, _inertial3DSpin.inertial3DSpinConfig_outputMsgID_set)
    __swig_setmethods__["inputRefName"] = _inertial3DSpin.inertial3DSpinConfig_inputRefName_set
    __swig_getmethods__["inputRefName"] = _inertial3DSpin.inertial3DSpinConfig_inputRefName_get
    if _newclass:
        inputRefName = _swig_property(_inertial3DSpin.inertial3DSpinConfig_inputRefName_get, _inertial3DSpin.inertial3DSpinConfig_inputRefName_set)
    __swig_setmethods__["inputRefID"] = _inertial3DSpin.inertial3DSpinConfig_inputRefID_set
    __swig_getmethods__["inputRefID"] = _inertial3DSpin.inertial3DSpinConfig_inputRefID_get
    if _newclass:
        inputRefID = _swig_property(_inertial3DSpin.inertial3DSpinConfig_inputRefID_get, _inertial3DSpin.inertial3DSpinConfig_inputRefID_set)
    __swig_setmethods__["attRefOut"] = _inertial3DSpin.inertial3DSpinConfig_attRefOut_set
    __swig_getmethods__["attRefOut"] = _inertial3DSpin.inertial3DSpinConfig_attRefOut_get
    if _newclass:
        attRefOut = _swig_property(_inertial3DSpin.inertial3DSpinConfig_attRefOut_get, _inertial3DSpin.inertial3DSpinConfig_attRefOut_set)

    def __init__(self):
        this = _inertial3DSpin.new_inertial3DSpinConfig()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _inertial3DSpin.delete_inertial3DSpinConfig
    __del__ = lambda self: None
inertial3DSpinConfig_swigregister = _inertial3DSpin.inertial3DSpinConfig_swigregister
inertial3DSpinConfig_swigregister(inertial3DSpinConfig)


def computeReference_inertial3DSpin(ConfigData, omega_R0N_N, domega_R0N_N, omega_RR0_R, dt):
    return _inertial3DSpin.computeReference_inertial3DSpin(ConfigData, omega_R0N_N, domega_R0N_N, omega_RR0_R, dt)
computeReference_inertial3DSpin = _inertial3DSpin.computeReference_inertial3DSpin
class AttRefFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AttRefFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AttRefFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sigma_RN"] = _inertial3DSpin.AttRefFswMsg_sigma_RN_set
    __swig_getmethods__["sigma_RN"] = _inertial3DSpin.AttRefFswMsg_sigma_RN_get
    if _newclass:
        sigma_RN = _swig_property(_inertial3DSpin.AttRefFswMsg_sigma_RN_get, _inertial3DSpin.AttRefFswMsg_sigma_RN_set)
    __swig_setmethods__["omega_RN_N"] = _inertial3DSpin.AttRefFswMsg_omega_RN_N_set
    __swig_getmethods__["omega_RN_N"] = _inertial3DSpin.AttRefFswMsg_omega_RN_N_get
    if _newclass:
        omega_RN_N = _swig_property(_inertial3DSpin.AttRefFswMsg_omega_RN_N_get, _inertial3DSpin.AttRefFswMsg_omega_RN_N_set)
    __swig_setmethods__["domega_RN_N"] = _inertial3DSpin.AttRefFswMsg_domega_RN_N_set
    __swig_getmethods__["domega_RN_N"] = _inertial3DSpin.AttRefFswMsg_domega_RN_N_get
    if _newclass:
        domega_RN_N = _swig_property(_inertial3DSpin.AttRefFswMsg_domega_RN_N_get, _inertial3DSpin.AttRefFswMsg_domega_RN_N_set)

    def __init__(self):
        this = _inertial3DSpin.new_AttRefFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _inertial3DSpin.delete_AttRefFswMsg
    __del__ = lambda self: None
AttRefFswMsg_swigregister = _inertial3DSpin.AttRefFswMsg_swigregister
AttRefFswMsg_swigregister(AttRefFswMsg)


import sys
protectAllClasses(sys.modules[__name__])

# This file is compatible with both classic and new-style classes.


