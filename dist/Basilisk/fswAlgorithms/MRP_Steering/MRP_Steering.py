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
        mname = '.'.join((pkg, '_MRP_Steering')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_MRP_Steering')
    _MRP_Steering = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_MRP_Steering', [dirname(__file__)])
        except ImportError:
            import _MRP_Steering
            return _MRP_Steering
        try:
            _mod = imp.load_module('_MRP_Steering', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _MRP_Steering = swig_import_helper()
    del swig_import_helper
else:
    import _MRP_Steering
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
    return _MRP_Steering.new_doubleArray(nelements)
new_doubleArray = _MRP_Steering.new_doubleArray

def delete_doubleArray(ary):
    return _MRP_Steering.delete_doubleArray(ary)
delete_doubleArray = _MRP_Steering.delete_doubleArray

def doubleArray_getitem(ary, index):
    return _MRP_Steering.doubleArray_getitem(ary, index)
doubleArray_getitem = _MRP_Steering.doubleArray_getitem

def doubleArray_setitem(ary, index, value):
    return _MRP_Steering.doubleArray_setitem(ary, index, value)
doubleArray_setitem = _MRP_Steering.doubleArray_setitem

def new_longArray(nelements):
    return _MRP_Steering.new_longArray(nelements)
new_longArray = _MRP_Steering.new_longArray

def delete_longArray(ary):
    return _MRP_Steering.delete_longArray(ary)
delete_longArray = _MRP_Steering.delete_longArray

def longArray_getitem(ary, index):
    return _MRP_Steering.longArray_getitem(ary, index)
longArray_getitem = _MRP_Steering.longArray_getitem

def longArray_setitem(ary, index, value):
    return _MRP_Steering.longArray_setitem(ary, index, value)
longArray_setitem = _MRP_Steering.longArray_setitem

def new_intArray(nelements):
    return _MRP_Steering.new_intArray(nelements)
new_intArray = _MRP_Steering.new_intArray

def delete_intArray(ary):
    return _MRP_Steering.delete_intArray(ary)
delete_intArray = _MRP_Steering.delete_intArray

def intArray_getitem(ary, index):
    return _MRP_Steering.intArray_getitem(ary, index)
intArray_getitem = _MRP_Steering.intArray_getitem

def intArray_setitem(ary, index, value):
    return _MRP_Steering.intArray_setitem(ary, index, value)
intArray_setitem = _MRP_Steering.intArray_setitem

def new_shortArray(nelements):
    return _MRP_Steering.new_shortArray(nelements)
new_shortArray = _MRP_Steering.new_shortArray

def delete_shortArray(ary):
    return _MRP_Steering.delete_shortArray(ary)
delete_shortArray = _MRP_Steering.delete_shortArray

def shortArray_getitem(ary, index):
    return _MRP_Steering.shortArray_getitem(ary, index)
shortArray_getitem = _MRP_Steering.shortArray_getitem

def shortArray_setitem(ary, index, value):
    return _MRP_Steering.shortArray_setitem(ary, index, value)
shortArray_setitem = _MRP_Steering.shortArray_setitem


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


Update_MRP_Steering = _MRP_Steering.Update_MRP_Steering
SelfInit_MRP_Steering = _MRP_Steering.SelfInit_MRP_Steering
CrossInit_MRP_Steering = _MRP_Steering.CrossInit_MRP_Steering
Reset_MRP_Steering = _MRP_Steering.Reset_MRP_Steering
sizeof_MRP_SteeringConfig = _MRP_Steering.sizeof_MRP_SteeringConfig
sizeof_AttGuidFswMsg = _MRP_Steering.sizeof_AttGuidFswMsg
sizeof_RateCmdFswMsg = _MRP_Steering.sizeof_RateCmdFswMsg
class MRP_SteeringConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MRP_SteeringConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MRP_SteeringConfig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["K1"] = _MRP_Steering.MRP_SteeringConfig_K1_set
    __swig_getmethods__["K1"] = _MRP_Steering.MRP_SteeringConfig_K1_get
    if _newclass:
        K1 = _swig_property(_MRP_Steering.MRP_SteeringConfig_K1_get, _MRP_Steering.MRP_SteeringConfig_K1_set)
    __swig_setmethods__["K3"] = _MRP_Steering.MRP_SteeringConfig_K3_set
    __swig_getmethods__["K3"] = _MRP_Steering.MRP_SteeringConfig_K3_get
    if _newclass:
        K3 = _swig_property(_MRP_Steering.MRP_SteeringConfig_K3_get, _MRP_Steering.MRP_SteeringConfig_K3_set)
    __swig_setmethods__["omega_max"] = _MRP_Steering.MRP_SteeringConfig_omega_max_set
    __swig_getmethods__["omega_max"] = _MRP_Steering.MRP_SteeringConfig_omega_max_get
    if _newclass:
        omega_max = _swig_property(_MRP_Steering.MRP_SteeringConfig_omega_max_get, _MRP_Steering.MRP_SteeringConfig_omega_max_set)
    __swig_setmethods__["ignoreOuterLoopFeedforward"] = _MRP_Steering.MRP_SteeringConfig_ignoreOuterLoopFeedforward_set
    __swig_getmethods__["ignoreOuterLoopFeedforward"] = _MRP_Steering.MRP_SteeringConfig_ignoreOuterLoopFeedforward_get
    if _newclass:
        ignoreOuterLoopFeedforward = _swig_property(_MRP_Steering.MRP_SteeringConfig_ignoreOuterLoopFeedforward_get, _MRP_Steering.MRP_SteeringConfig_ignoreOuterLoopFeedforward_set)
    __swig_setmethods__["outputDataName"] = _MRP_Steering.MRP_SteeringConfig_outputDataName_set
    __swig_getmethods__["outputDataName"] = _MRP_Steering.MRP_SteeringConfig_outputDataName_get
    if _newclass:
        outputDataName = _swig_property(_MRP_Steering.MRP_SteeringConfig_outputDataName_get, _MRP_Steering.MRP_SteeringConfig_outputDataName_set)
    __swig_setmethods__["outputMsgID"] = _MRP_Steering.MRP_SteeringConfig_outputMsgID_set
    __swig_getmethods__["outputMsgID"] = _MRP_Steering.MRP_SteeringConfig_outputMsgID_get
    if _newclass:
        outputMsgID = _swig_property(_MRP_Steering.MRP_SteeringConfig_outputMsgID_get, _MRP_Steering.MRP_SteeringConfig_outputMsgID_set)
    __swig_setmethods__["inputGuidName"] = _MRP_Steering.MRP_SteeringConfig_inputGuidName_set
    __swig_getmethods__["inputGuidName"] = _MRP_Steering.MRP_SteeringConfig_inputGuidName_get
    if _newclass:
        inputGuidName = _swig_property(_MRP_Steering.MRP_SteeringConfig_inputGuidName_get, _MRP_Steering.MRP_SteeringConfig_inputGuidName_set)
    __swig_setmethods__["inputGuidID"] = _MRP_Steering.MRP_SteeringConfig_inputGuidID_set
    __swig_getmethods__["inputGuidID"] = _MRP_Steering.MRP_SteeringConfig_inputGuidID_get
    if _newclass:
        inputGuidID = _swig_property(_MRP_Steering.MRP_SteeringConfig_inputGuidID_get, _MRP_Steering.MRP_SteeringConfig_inputGuidID_set)
    __swig_setmethods__["outMsg"] = _MRP_Steering.MRP_SteeringConfig_outMsg_set
    __swig_getmethods__["outMsg"] = _MRP_Steering.MRP_SteeringConfig_outMsg_get
    if _newclass:
        outMsg = _swig_property(_MRP_Steering.MRP_SteeringConfig_outMsg_get, _MRP_Steering.MRP_SteeringConfig_outMsg_set)

    def __init__(self):
        this = _MRP_Steering.new_MRP_SteeringConfig()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _MRP_Steering.delete_MRP_SteeringConfig
    __del__ = lambda self: None
MRP_SteeringConfig_swigregister = _MRP_Steering.MRP_SteeringConfig_swigregister
MRP_SteeringConfig_swigregister(MRP_SteeringConfig)


def MRPSteeringLaw(configData, sigma_BR, omega_ast, omega_ast_p):
    return _MRP_Steering.MRPSteeringLaw(configData, sigma_BR, omega_ast, omega_ast_p)
MRPSteeringLaw = _MRP_Steering.MRPSteeringLaw
class AttGuidFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AttGuidFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AttGuidFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sigma_BR"] = _MRP_Steering.AttGuidFswMsg_sigma_BR_set
    __swig_getmethods__["sigma_BR"] = _MRP_Steering.AttGuidFswMsg_sigma_BR_get
    if _newclass:
        sigma_BR = _swig_property(_MRP_Steering.AttGuidFswMsg_sigma_BR_get, _MRP_Steering.AttGuidFswMsg_sigma_BR_set)
    __swig_setmethods__["omega_BR_B"] = _MRP_Steering.AttGuidFswMsg_omega_BR_B_set
    __swig_getmethods__["omega_BR_B"] = _MRP_Steering.AttGuidFswMsg_omega_BR_B_get
    if _newclass:
        omega_BR_B = _swig_property(_MRP_Steering.AttGuidFswMsg_omega_BR_B_get, _MRP_Steering.AttGuidFswMsg_omega_BR_B_set)
    __swig_setmethods__["omega_RN_B"] = _MRP_Steering.AttGuidFswMsg_omega_RN_B_set
    __swig_getmethods__["omega_RN_B"] = _MRP_Steering.AttGuidFswMsg_omega_RN_B_get
    if _newclass:
        omega_RN_B = _swig_property(_MRP_Steering.AttGuidFswMsg_omega_RN_B_get, _MRP_Steering.AttGuidFswMsg_omega_RN_B_set)
    __swig_setmethods__["domega_RN_B"] = _MRP_Steering.AttGuidFswMsg_domega_RN_B_set
    __swig_getmethods__["domega_RN_B"] = _MRP_Steering.AttGuidFswMsg_domega_RN_B_get
    if _newclass:
        domega_RN_B = _swig_property(_MRP_Steering.AttGuidFswMsg_domega_RN_B_get, _MRP_Steering.AttGuidFswMsg_domega_RN_B_set)
    __swig_setmethods__["PRV"] = _MRP_Steering.AttGuidFswMsg_PRV_set
    __swig_getmethods__["PRV"] = _MRP_Steering.AttGuidFswMsg_PRV_get
    if _newclass:
        PRV = _swig_property(_MRP_Steering.AttGuidFswMsg_PRV_get, _MRP_Steering.AttGuidFswMsg_PRV_set)

    def __init__(self):
        this = _MRP_Steering.new_AttGuidFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _MRP_Steering.delete_AttGuidFswMsg
    __del__ = lambda self: None
AttGuidFswMsg_swigregister = _MRP_Steering.AttGuidFswMsg_swigregister
AttGuidFswMsg_swigregister(AttGuidFswMsg)

class RateCmdFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RateCmdFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RateCmdFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["omega_BastR_B"] = _MRP_Steering.RateCmdFswMsg_omega_BastR_B_set
    __swig_getmethods__["omega_BastR_B"] = _MRP_Steering.RateCmdFswMsg_omega_BastR_B_get
    if _newclass:
        omega_BastR_B = _swig_property(_MRP_Steering.RateCmdFswMsg_omega_BastR_B_get, _MRP_Steering.RateCmdFswMsg_omega_BastR_B_set)
    __swig_setmethods__["omegap_BastR_B"] = _MRP_Steering.RateCmdFswMsg_omegap_BastR_B_set
    __swig_getmethods__["omegap_BastR_B"] = _MRP_Steering.RateCmdFswMsg_omegap_BastR_B_get
    if _newclass:
        omegap_BastR_B = _swig_property(_MRP_Steering.RateCmdFswMsg_omegap_BastR_B_get, _MRP_Steering.RateCmdFswMsg_omegap_BastR_B_set)

    def __init__(self):
        this = _MRP_Steering.new_RateCmdFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _MRP_Steering.delete_RateCmdFswMsg
    __del__ = lambda self: None
RateCmdFswMsg_swigregister = _MRP_Steering.RateCmdFswMsg_swigregister
RateCmdFswMsg_swigregister(RateCmdFswMsg)


import sys
protectAllClasses(sys.modules[__name__])

# This file is compatible with both classic and new-style classes.

