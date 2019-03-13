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
        mname = '.'.join((pkg, '_dvExecuteGuidance')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_dvExecuteGuidance')
    _dvExecuteGuidance = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_dvExecuteGuidance', [dirname(__file__)])
        except ImportError:
            import _dvExecuteGuidance
            return _dvExecuteGuidance
        try:
            _mod = imp.load_module('_dvExecuteGuidance', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _dvExecuteGuidance = swig_import_helper()
    del swig_import_helper
else:
    import _dvExecuteGuidance
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
    return _dvExecuteGuidance.new_doubleArray(nelements)
new_doubleArray = _dvExecuteGuidance.new_doubleArray

def delete_doubleArray(ary):
    return _dvExecuteGuidance.delete_doubleArray(ary)
delete_doubleArray = _dvExecuteGuidance.delete_doubleArray

def doubleArray_getitem(ary, index):
    return _dvExecuteGuidance.doubleArray_getitem(ary, index)
doubleArray_getitem = _dvExecuteGuidance.doubleArray_getitem

def doubleArray_setitem(ary, index, value):
    return _dvExecuteGuidance.doubleArray_setitem(ary, index, value)
doubleArray_setitem = _dvExecuteGuidance.doubleArray_setitem

def new_longArray(nelements):
    return _dvExecuteGuidance.new_longArray(nelements)
new_longArray = _dvExecuteGuidance.new_longArray

def delete_longArray(ary):
    return _dvExecuteGuidance.delete_longArray(ary)
delete_longArray = _dvExecuteGuidance.delete_longArray

def longArray_getitem(ary, index):
    return _dvExecuteGuidance.longArray_getitem(ary, index)
longArray_getitem = _dvExecuteGuidance.longArray_getitem

def longArray_setitem(ary, index, value):
    return _dvExecuteGuidance.longArray_setitem(ary, index, value)
longArray_setitem = _dvExecuteGuidance.longArray_setitem

def new_intArray(nelements):
    return _dvExecuteGuidance.new_intArray(nelements)
new_intArray = _dvExecuteGuidance.new_intArray

def delete_intArray(ary):
    return _dvExecuteGuidance.delete_intArray(ary)
delete_intArray = _dvExecuteGuidance.delete_intArray

def intArray_getitem(ary, index):
    return _dvExecuteGuidance.intArray_getitem(ary, index)
intArray_getitem = _dvExecuteGuidance.intArray_getitem

def intArray_setitem(ary, index, value):
    return _dvExecuteGuidance.intArray_setitem(ary, index, value)
intArray_setitem = _dvExecuteGuidance.intArray_setitem

def new_shortArray(nelements):
    return _dvExecuteGuidance.new_shortArray(nelements)
new_shortArray = _dvExecuteGuidance.new_shortArray

def delete_shortArray(ary):
    return _dvExecuteGuidance.delete_shortArray(ary)
delete_shortArray = _dvExecuteGuidance.delete_shortArray

def shortArray_getitem(ary, index):
    return _dvExecuteGuidance.shortArray_getitem(ary, index)
shortArray_getitem = _dvExecuteGuidance.shortArray_getitem

def shortArray_setitem(ary, index, value):
    return _dvExecuteGuidance.shortArray_setitem(ary, index, value)
shortArray_setitem = _dvExecuteGuidance.shortArray_setitem


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


Update_dvExecuteGuidance = _dvExecuteGuidance.Update_dvExecuteGuidance
SelfInit_dvExecuteGuidance = _dvExecuteGuidance.SelfInit_dvExecuteGuidance
CrossInit_dvExecuteGuidance = _dvExecuteGuidance.CrossInit_dvExecuteGuidance
sizeof_dvExecutionData = _dvExecuteGuidance.sizeof_dvExecutionData
sizeof_dvExecuteGuidanceConfig = _dvExecuteGuidance.sizeof_dvExecuteGuidanceConfig
sizeof_NavTransIntMsg = _dvExecuteGuidance.sizeof_NavTransIntMsg
sizeof_DvBurnCmdFswMsg = _dvExecuteGuidance.sizeof_DvBurnCmdFswMsg
class dvExecutionData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dvExecutionData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dvExecutionData, name)
    __repr__ = _swig_repr
    __swig_setmethods__["burnExecuting"] = _dvExecuteGuidance.dvExecutionData_burnExecuting_set
    __swig_getmethods__["burnExecuting"] = _dvExecuteGuidance.dvExecutionData_burnExecuting_get
    if _newclass:
        burnExecuting = _swig_property(_dvExecuteGuidance.dvExecutionData_burnExecuting_get, _dvExecuteGuidance.dvExecutionData_burnExecuting_set)
    __swig_setmethods__["burnComplete"] = _dvExecuteGuidance.dvExecutionData_burnComplete_set
    __swig_getmethods__["burnComplete"] = _dvExecuteGuidance.dvExecutionData_burnComplete_get
    if _newclass:
        burnComplete = _swig_property(_dvExecuteGuidance.dvExecutionData_burnComplete_get, _dvExecuteGuidance.dvExecutionData_burnComplete_set)

    def __init__(self):
        this = _dvExecuteGuidance.new_dvExecutionData()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _dvExecuteGuidance.delete_dvExecutionData
    __del__ = lambda self: None
dvExecutionData_swigregister = _dvExecuteGuidance.dvExecutionData_swigregister
dvExecutionData_swigregister(dvExecutionData)

class dvExecuteGuidanceConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dvExecuteGuidanceConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dvExecuteGuidanceConfig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["outputDataName"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_outputDataName_set
    __swig_getmethods__["outputDataName"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_outputDataName_get
    if _newclass:
        outputDataName = _swig_property(_dvExecuteGuidance.dvExecuteGuidanceConfig_outputDataName_get, _dvExecuteGuidance.dvExecuteGuidanceConfig_outputDataName_set)
    __swig_setmethods__["inputNavDataName"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_inputNavDataName_set
    __swig_getmethods__["inputNavDataName"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_inputNavDataName_get
    if _newclass:
        inputNavDataName = _swig_property(_dvExecuteGuidance.dvExecuteGuidanceConfig_inputNavDataName_get, _dvExecuteGuidance.dvExecuteGuidanceConfig_inputNavDataName_set)
    __swig_setmethods__["inputBurnDataName"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_inputBurnDataName_set
    __swig_getmethods__["inputBurnDataName"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_inputBurnDataName_get
    if _newclass:
        inputBurnDataName = _swig_property(_dvExecuteGuidance.dvExecuteGuidanceConfig_inputBurnDataName_get, _dvExecuteGuidance.dvExecuteGuidanceConfig_inputBurnDataName_set)
    __swig_setmethods__["outputThrName"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_outputThrName_set
    __swig_getmethods__["outputThrName"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_outputThrName_get
    if _newclass:
        outputThrName = _swig_property(_dvExecuteGuidance.dvExecuteGuidanceConfig_outputThrName_get, _dvExecuteGuidance.dvExecuteGuidanceConfig_outputThrName_set)
    __swig_setmethods__["dvInit"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_dvInit_set
    __swig_getmethods__["dvInit"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_dvInit_get
    if _newclass:
        dvInit = _swig_property(_dvExecuteGuidance.dvExecuteGuidanceConfig_dvInit_get, _dvExecuteGuidance.dvExecuteGuidanceConfig_dvInit_set)
    __swig_setmethods__["burnExecuting"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_burnExecuting_set
    __swig_getmethods__["burnExecuting"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_burnExecuting_get
    if _newclass:
        burnExecuting = _swig_property(_dvExecuteGuidance.dvExecuteGuidanceConfig_burnExecuting_get, _dvExecuteGuidance.dvExecuteGuidanceConfig_burnExecuting_set)
    __swig_setmethods__["burnComplete"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_burnComplete_set
    __swig_getmethods__["burnComplete"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_burnComplete_get
    if _newclass:
        burnComplete = _swig_property(_dvExecuteGuidance.dvExecuteGuidanceConfig_burnComplete_get, _dvExecuteGuidance.dvExecuteGuidanceConfig_burnComplete_set)
    __swig_setmethods__["outputMsgID"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_outputMsgID_set
    __swig_getmethods__["outputMsgID"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_outputMsgID_get
    if _newclass:
        outputMsgID = _swig_property(_dvExecuteGuidance.dvExecuteGuidanceConfig_outputMsgID_get, _dvExecuteGuidance.dvExecuteGuidanceConfig_outputMsgID_set)
    __swig_setmethods__["outputThrID"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_outputThrID_set
    __swig_getmethods__["outputThrID"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_outputThrID_get
    if _newclass:
        outputThrID = _swig_property(_dvExecuteGuidance.dvExecuteGuidanceConfig_outputThrID_get, _dvExecuteGuidance.dvExecuteGuidanceConfig_outputThrID_set)
    __swig_setmethods__["inputNavID"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_inputNavID_set
    __swig_getmethods__["inputNavID"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_inputNavID_get
    if _newclass:
        inputNavID = _swig_property(_dvExecuteGuidance.dvExecuteGuidanceConfig_inputNavID_get, _dvExecuteGuidance.dvExecuteGuidanceConfig_inputNavID_set)
    __swig_setmethods__["inputBurnCmdID"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_inputBurnCmdID_set
    __swig_getmethods__["inputBurnCmdID"] = _dvExecuteGuidance.dvExecuteGuidanceConfig_inputBurnCmdID_get
    if _newclass:
        inputBurnCmdID = _swig_property(_dvExecuteGuidance.dvExecuteGuidanceConfig_inputBurnCmdID_get, _dvExecuteGuidance.dvExecuteGuidanceConfig_inputBurnCmdID_set)

    def __init__(self):
        this = _dvExecuteGuidance.new_dvExecuteGuidanceConfig()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _dvExecuteGuidance.delete_dvExecuteGuidanceConfig
    __del__ = lambda self: None
dvExecuteGuidanceConfig_swigregister = _dvExecuteGuidance.dvExecuteGuidanceConfig_swigregister
dvExecuteGuidanceConfig_swigregister(dvExecuteGuidanceConfig)

class NavTransIntMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NavTransIntMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NavTransIntMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["timeTag"] = _dvExecuteGuidance.NavTransIntMsg_timeTag_set
    __swig_getmethods__["timeTag"] = _dvExecuteGuidance.NavTransIntMsg_timeTag_get
    if _newclass:
        timeTag = _swig_property(_dvExecuteGuidance.NavTransIntMsg_timeTag_get, _dvExecuteGuidance.NavTransIntMsg_timeTag_set)
    __swig_setmethods__["r_BN_N"] = _dvExecuteGuidance.NavTransIntMsg_r_BN_N_set
    __swig_getmethods__["r_BN_N"] = _dvExecuteGuidance.NavTransIntMsg_r_BN_N_get
    if _newclass:
        r_BN_N = _swig_property(_dvExecuteGuidance.NavTransIntMsg_r_BN_N_get, _dvExecuteGuidance.NavTransIntMsg_r_BN_N_set)
    __swig_setmethods__["v_BN_N"] = _dvExecuteGuidance.NavTransIntMsg_v_BN_N_set
    __swig_getmethods__["v_BN_N"] = _dvExecuteGuidance.NavTransIntMsg_v_BN_N_get
    if _newclass:
        v_BN_N = _swig_property(_dvExecuteGuidance.NavTransIntMsg_v_BN_N_get, _dvExecuteGuidance.NavTransIntMsg_v_BN_N_set)
    __swig_setmethods__["vehAccumDV"] = _dvExecuteGuidance.NavTransIntMsg_vehAccumDV_set
    __swig_getmethods__["vehAccumDV"] = _dvExecuteGuidance.NavTransIntMsg_vehAccumDV_get
    if _newclass:
        vehAccumDV = _swig_property(_dvExecuteGuidance.NavTransIntMsg_vehAccumDV_get, _dvExecuteGuidance.NavTransIntMsg_vehAccumDV_set)

    def __init__(self):
        this = _dvExecuteGuidance.new_NavTransIntMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _dvExecuteGuidance.delete_NavTransIntMsg
    __del__ = lambda self: None
NavTransIntMsg_swigregister = _dvExecuteGuidance.NavTransIntMsg_swigregister
NavTransIntMsg_swigregister(NavTransIntMsg)

class DvBurnCmdFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DvBurnCmdFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DvBurnCmdFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["dvInrtlCmd"] = _dvExecuteGuidance.DvBurnCmdFswMsg_dvInrtlCmd_set
    __swig_getmethods__["dvInrtlCmd"] = _dvExecuteGuidance.DvBurnCmdFswMsg_dvInrtlCmd_get
    if _newclass:
        dvInrtlCmd = _swig_property(_dvExecuteGuidance.DvBurnCmdFswMsg_dvInrtlCmd_get, _dvExecuteGuidance.DvBurnCmdFswMsg_dvInrtlCmd_set)
    __swig_setmethods__["dvRotVecUnit"] = _dvExecuteGuidance.DvBurnCmdFswMsg_dvRotVecUnit_set
    __swig_getmethods__["dvRotVecUnit"] = _dvExecuteGuidance.DvBurnCmdFswMsg_dvRotVecUnit_get
    if _newclass:
        dvRotVecUnit = _swig_property(_dvExecuteGuidance.DvBurnCmdFswMsg_dvRotVecUnit_get, _dvExecuteGuidance.DvBurnCmdFswMsg_dvRotVecUnit_set)
    __swig_setmethods__["dvRotVecMag"] = _dvExecuteGuidance.DvBurnCmdFswMsg_dvRotVecMag_set
    __swig_getmethods__["dvRotVecMag"] = _dvExecuteGuidance.DvBurnCmdFswMsg_dvRotVecMag_get
    if _newclass:
        dvRotVecMag = _swig_property(_dvExecuteGuidance.DvBurnCmdFswMsg_dvRotVecMag_get, _dvExecuteGuidance.DvBurnCmdFswMsg_dvRotVecMag_set)
    __swig_setmethods__["burnStartTime"] = _dvExecuteGuidance.DvBurnCmdFswMsg_burnStartTime_set
    __swig_getmethods__["burnStartTime"] = _dvExecuteGuidance.DvBurnCmdFswMsg_burnStartTime_get
    if _newclass:
        burnStartTime = _swig_property(_dvExecuteGuidance.DvBurnCmdFswMsg_burnStartTime_get, _dvExecuteGuidance.DvBurnCmdFswMsg_burnStartTime_set)

    def __init__(self):
        this = _dvExecuteGuidance.new_DvBurnCmdFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _dvExecuteGuidance.delete_DvBurnCmdFswMsg
    __del__ = lambda self: None
DvBurnCmdFswMsg_swigregister = _dvExecuteGuidance.DvBurnCmdFswMsg_swigregister
DvBurnCmdFswMsg_swigregister(DvBurnCmdFswMsg)


import sys
protectAllClasses(sys.modules[__name__])

# This file is compatible with both classic and new-style classes.

