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
        mname = '.'.join((pkg, '_thrustRWDesat')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_thrustRWDesat')
    _thrustRWDesat = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_thrustRWDesat', [dirname(__file__)])
        except ImportError:
            import _thrustRWDesat
            return _thrustRWDesat
        try:
            _mod = imp.load_module('_thrustRWDesat', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _thrustRWDesat = swig_import_helper()
    del swig_import_helper
else:
    import _thrustRWDesat
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
    return _thrustRWDesat.new_doubleArray(nelements)
new_doubleArray = _thrustRWDesat.new_doubleArray

def delete_doubleArray(ary):
    return _thrustRWDesat.delete_doubleArray(ary)
delete_doubleArray = _thrustRWDesat.delete_doubleArray

def doubleArray_getitem(ary, index):
    return _thrustRWDesat.doubleArray_getitem(ary, index)
doubleArray_getitem = _thrustRWDesat.doubleArray_getitem

def doubleArray_setitem(ary, index, value):
    return _thrustRWDesat.doubleArray_setitem(ary, index, value)
doubleArray_setitem = _thrustRWDesat.doubleArray_setitem

def new_longArray(nelements):
    return _thrustRWDesat.new_longArray(nelements)
new_longArray = _thrustRWDesat.new_longArray

def delete_longArray(ary):
    return _thrustRWDesat.delete_longArray(ary)
delete_longArray = _thrustRWDesat.delete_longArray

def longArray_getitem(ary, index):
    return _thrustRWDesat.longArray_getitem(ary, index)
longArray_getitem = _thrustRWDesat.longArray_getitem

def longArray_setitem(ary, index, value):
    return _thrustRWDesat.longArray_setitem(ary, index, value)
longArray_setitem = _thrustRWDesat.longArray_setitem

def new_intArray(nelements):
    return _thrustRWDesat.new_intArray(nelements)
new_intArray = _thrustRWDesat.new_intArray

def delete_intArray(ary):
    return _thrustRWDesat.delete_intArray(ary)
delete_intArray = _thrustRWDesat.delete_intArray

def intArray_getitem(ary, index):
    return _thrustRWDesat.intArray_getitem(ary, index)
intArray_getitem = _thrustRWDesat.intArray_getitem

def intArray_setitem(ary, index, value):
    return _thrustRWDesat.intArray_setitem(ary, index, value)
intArray_setitem = _thrustRWDesat.intArray_setitem

def new_shortArray(nelements):
    return _thrustRWDesat.new_shortArray(nelements)
new_shortArray = _thrustRWDesat.new_shortArray

def delete_shortArray(ary):
    return _thrustRWDesat.delete_shortArray(ary)
delete_shortArray = _thrustRWDesat.delete_shortArray

def shortArray_getitem(ary, index):
    return _thrustRWDesat.shortArray_getitem(ary, index)
shortArray_getitem = _thrustRWDesat.shortArray_getitem

def shortArray_setitem(ary, index, value):
    return _thrustRWDesat.shortArray_setitem(ary, index, value)
shortArray_setitem = _thrustRWDesat.shortArray_setitem


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


Update_thrustRWDesat = _thrustRWDesat.Update_thrustRWDesat
SelfInit_thrustRWDesat = _thrustRWDesat.SelfInit_thrustRWDesat
CrossInit_thrustRWDesat = _thrustRWDesat.CrossInit_thrustRWDesat
Reset_thrustRWDesat = _thrustRWDesat.Reset_thrustRWDesat
class VehicleConfigFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VehicleConfigFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VehicleConfigFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ISCPntB_B"] = _thrustRWDesat.VehicleConfigFswMsg_ISCPntB_B_set
    __swig_getmethods__["ISCPntB_B"] = _thrustRWDesat.VehicleConfigFswMsg_ISCPntB_B_get
    if _newclass:
        ISCPntB_B = _swig_property(_thrustRWDesat.VehicleConfigFswMsg_ISCPntB_B_get, _thrustRWDesat.VehicleConfigFswMsg_ISCPntB_B_set)
    __swig_setmethods__["CoM_B"] = _thrustRWDesat.VehicleConfigFswMsg_CoM_B_set
    __swig_getmethods__["CoM_B"] = _thrustRWDesat.VehicleConfigFswMsg_CoM_B_get
    if _newclass:
        CoM_B = _swig_property(_thrustRWDesat.VehicleConfigFswMsg_CoM_B_get, _thrustRWDesat.VehicleConfigFswMsg_CoM_B_set)
    __swig_setmethods__["CurrentADCSState"] = _thrustRWDesat.VehicleConfigFswMsg_CurrentADCSState_set
    __swig_getmethods__["CurrentADCSState"] = _thrustRWDesat.VehicleConfigFswMsg_CurrentADCSState_get
    if _newclass:
        CurrentADCSState = _swig_property(_thrustRWDesat.VehicleConfigFswMsg_CurrentADCSState_get, _thrustRWDesat.VehicleConfigFswMsg_CurrentADCSState_set)

    def __init__(self):
        this = _thrustRWDesat.new_VehicleConfigFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrustRWDesat.delete_VehicleConfigFswMsg
    __del__ = lambda self: None
VehicleConfigFswMsg_swigregister = _thrustRWDesat.VehicleConfigFswMsg_swigregister
VehicleConfigFswMsg_swigregister(VehicleConfigFswMsg)

sizeof_thrustRWDesatConfig = _thrustRWDesat.sizeof_thrustRWDesatConfig
sizeof_VehicleConfigFswMsg = _thrustRWDesat.sizeof_VehicleConfigFswMsg
class thrustRWDesatConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, thrustRWDesatConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, thrustRWDesatConfig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["inputSpeedName"] = _thrustRWDesat.thrustRWDesatConfig_inputSpeedName_set
    __swig_getmethods__["inputSpeedName"] = _thrustRWDesat.thrustRWDesatConfig_inputSpeedName_get
    if _newclass:
        inputSpeedName = _swig_property(_thrustRWDesat.thrustRWDesatConfig_inputSpeedName_get, _thrustRWDesat.thrustRWDesatConfig_inputSpeedName_set)
    __swig_setmethods__["inputRWConfigData"] = _thrustRWDesat.thrustRWDesatConfig_inputRWConfigData_set
    __swig_getmethods__["inputRWConfigData"] = _thrustRWDesat.thrustRWDesatConfig_inputRWConfigData_get
    if _newclass:
        inputRWConfigData = _swig_property(_thrustRWDesat.thrustRWDesatConfig_inputRWConfigData_get, _thrustRWDesat.thrustRWDesatConfig_inputRWConfigData_set)
    __swig_setmethods__["inputThrConfigName"] = _thrustRWDesat.thrustRWDesatConfig_inputThrConfigName_set
    __swig_getmethods__["inputThrConfigName"] = _thrustRWDesat.thrustRWDesatConfig_inputThrConfigName_get
    if _newclass:
        inputThrConfigName = _swig_property(_thrustRWDesat.thrustRWDesatConfig_inputThrConfigName_get, _thrustRWDesat.thrustRWDesatConfig_inputThrConfigName_set)
    __swig_setmethods__["inputMassPropsName"] = _thrustRWDesat.thrustRWDesatConfig_inputMassPropsName_set
    __swig_getmethods__["inputMassPropsName"] = _thrustRWDesat.thrustRWDesatConfig_inputMassPropsName_get
    if _newclass:
        inputMassPropsName = _swig_property(_thrustRWDesat.thrustRWDesatConfig_inputMassPropsName_get, _thrustRWDesat.thrustRWDesatConfig_inputMassPropsName_set)
    __swig_setmethods__["outputThrName"] = _thrustRWDesat.thrustRWDesatConfig_outputThrName_set
    __swig_getmethods__["outputThrName"] = _thrustRWDesat.thrustRWDesatConfig_outputThrName_get
    if _newclass:
        outputThrName = _swig_property(_thrustRWDesat.thrustRWDesatConfig_outputThrName_get, _thrustRWDesat.thrustRWDesatConfig_outputThrName_set)
    __swig_setmethods__["rwAlignMap"] = _thrustRWDesat.thrustRWDesatConfig_rwAlignMap_set
    __swig_getmethods__["rwAlignMap"] = _thrustRWDesat.thrustRWDesatConfig_rwAlignMap_get
    if _newclass:
        rwAlignMap = _swig_property(_thrustRWDesat.thrustRWDesatConfig_rwAlignMap_get, _thrustRWDesat.thrustRWDesatConfig_rwAlignMap_set)
    __swig_setmethods__["thrAlignMap"] = _thrustRWDesat.thrustRWDesatConfig_thrAlignMap_set
    __swig_getmethods__["thrAlignMap"] = _thrustRWDesat.thrustRWDesatConfig_thrAlignMap_get
    if _newclass:
        thrAlignMap = _swig_property(_thrustRWDesat.thrustRWDesatConfig_thrAlignMap_get, _thrustRWDesat.thrustRWDesatConfig_thrAlignMap_set)
    __swig_setmethods__["thrTorqueMap"] = _thrustRWDesat.thrustRWDesatConfig_thrTorqueMap_set
    __swig_getmethods__["thrTorqueMap"] = _thrustRWDesat.thrustRWDesatConfig_thrTorqueMap_get
    if _newclass:
        thrTorqueMap = _swig_property(_thrustRWDesat.thrustRWDesatConfig_thrTorqueMap_get, _thrustRWDesat.thrustRWDesatConfig_thrTorqueMap_set)
    __swig_setmethods__["maxFiring"] = _thrustRWDesat.thrustRWDesatConfig_maxFiring_set
    __swig_getmethods__["maxFiring"] = _thrustRWDesat.thrustRWDesatConfig_maxFiring_get
    if _newclass:
        maxFiring = _swig_property(_thrustRWDesat.thrustRWDesatConfig_maxFiring_get, _thrustRWDesat.thrustRWDesatConfig_maxFiring_set)
    __swig_setmethods__["thrFiringPeriod"] = _thrustRWDesat.thrustRWDesatConfig_thrFiringPeriod_set
    __swig_getmethods__["thrFiringPeriod"] = _thrustRWDesat.thrustRWDesatConfig_thrFiringPeriod_get
    if _newclass:
        thrFiringPeriod = _swig_property(_thrustRWDesat.thrustRWDesatConfig_thrFiringPeriod_get, _thrustRWDesat.thrustRWDesatConfig_thrFiringPeriod_set)
    __swig_setmethods__["numRWAs"] = _thrustRWDesat.thrustRWDesatConfig_numRWAs_set
    __swig_getmethods__["numRWAs"] = _thrustRWDesat.thrustRWDesatConfig_numRWAs_get
    if _newclass:
        numRWAs = _swig_property(_thrustRWDesat.thrustRWDesatConfig_numRWAs_get, _thrustRWDesat.thrustRWDesatConfig_numRWAs_set)
    __swig_setmethods__["numThrusters"] = _thrustRWDesat.thrustRWDesatConfig_numThrusters_set
    __swig_getmethods__["numThrusters"] = _thrustRWDesat.thrustRWDesatConfig_numThrusters_get
    if _newclass:
        numThrusters = _swig_property(_thrustRWDesat.thrustRWDesatConfig_numThrusters_get, _thrustRWDesat.thrustRWDesatConfig_numThrusters_set)
    __swig_setmethods__["accumulatedImp"] = _thrustRWDesat.thrustRWDesatConfig_accumulatedImp_set
    __swig_getmethods__["accumulatedImp"] = _thrustRWDesat.thrustRWDesatConfig_accumulatedImp_get
    if _newclass:
        accumulatedImp = _swig_property(_thrustRWDesat.thrustRWDesatConfig_accumulatedImp_get, _thrustRWDesat.thrustRWDesatConfig_accumulatedImp_set)
    __swig_setmethods__["currDMDir"] = _thrustRWDesat.thrustRWDesatConfig_currDMDir_set
    __swig_getmethods__["currDMDir"] = _thrustRWDesat.thrustRWDesatConfig_currDMDir_get
    if _newclass:
        currDMDir = _swig_property(_thrustRWDesat.thrustRWDesatConfig_currDMDir_get, _thrustRWDesat.thrustRWDesatConfig_currDMDir_set)
    __swig_setmethods__["totalAccumFiring"] = _thrustRWDesat.thrustRWDesatConfig_totalAccumFiring_set
    __swig_getmethods__["totalAccumFiring"] = _thrustRWDesat.thrustRWDesatConfig_totalAccumFiring_get
    if _newclass:
        totalAccumFiring = _swig_property(_thrustRWDesat.thrustRWDesatConfig_totalAccumFiring_get, _thrustRWDesat.thrustRWDesatConfig_totalAccumFiring_set)
    __swig_setmethods__["DMThresh"] = _thrustRWDesat.thrustRWDesatConfig_DMThresh_set
    __swig_getmethods__["DMThresh"] = _thrustRWDesat.thrustRWDesatConfig_DMThresh_get
    if _newclass:
        DMThresh = _swig_property(_thrustRWDesat.thrustRWDesatConfig_DMThresh_get, _thrustRWDesat.thrustRWDesatConfig_DMThresh_set)
    __swig_setmethods__["previousFiring"] = _thrustRWDesat.thrustRWDesatConfig_previousFiring_set
    __swig_getmethods__["previousFiring"] = _thrustRWDesat.thrustRWDesatConfig_previousFiring_get
    if _newclass:
        previousFiring = _swig_property(_thrustRWDesat.thrustRWDesatConfig_previousFiring_get, _thrustRWDesat.thrustRWDesatConfig_previousFiring_set)
    __swig_setmethods__["inputRWConfID"] = _thrustRWDesat.thrustRWDesatConfig_inputRWConfID_set
    __swig_getmethods__["inputRWConfID"] = _thrustRWDesat.thrustRWDesatConfig_inputRWConfID_get
    if _newclass:
        inputRWConfID = _swig_property(_thrustRWDesat.thrustRWDesatConfig_inputRWConfID_get, _thrustRWDesat.thrustRWDesatConfig_inputRWConfID_set)
    __swig_setmethods__["inputSpeedID"] = _thrustRWDesat.thrustRWDesatConfig_inputSpeedID_set
    __swig_getmethods__["inputSpeedID"] = _thrustRWDesat.thrustRWDesatConfig_inputSpeedID_get
    if _newclass:
        inputSpeedID = _swig_property(_thrustRWDesat.thrustRWDesatConfig_inputSpeedID_get, _thrustRWDesat.thrustRWDesatConfig_inputSpeedID_set)
    __swig_setmethods__["inputThrConID"] = _thrustRWDesat.thrustRWDesatConfig_inputThrConID_set
    __swig_getmethods__["inputThrConID"] = _thrustRWDesat.thrustRWDesatConfig_inputThrConID_get
    if _newclass:
        inputThrConID = _swig_property(_thrustRWDesat.thrustRWDesatConfig_inputThrConID_get, _thrustRWDesat.thrustRWDesatConfig_inputThrConID_set)
    __swig_setmethods__["inputMassPropID"] = _thrustRWDesat.thrustRWDesatConfig_inputMassPropID_set
    __swig_getmethods__["inputMassPropID"] = _thrustRWDesat.thrustRWDesatConfig_inputMassPropID_get
    if _newclass:
        inputMassPropID = _swig_property(_thrustRWDesat.thrustRWDesatConfig_inputMassPropID_get, _thrustRWDesat.thrustRWDesatConfig_inputMassPropID_set)
    __swig_setmethods__["outputThrID"] = _thrustRWDesat.thrustRWDesatConfig_outputThrID_set
    __swig_getmethods__["outputThrID"] = _thrustRWDesat.thrustRWDesatConfig_outputThrID_get
    if _newclass:
        outputThrID = _swig_property(_thrustRWDesat.thrustRWDesatConfig_outputThrID_get, _thrustRWDesat.thrustRWDesatConfig_outputThrID_set)

    def __init__(self):
        this = _thrustRWDesat.new_thrustRWDesatConfig()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrustRWDesat.delete_thrustRWDesatConfig
    __del__ = lambda self: None
thrustRWDesatConfig_swigregister = _thrustRWDesat.thrustRWDesatConfig_swigregister
thrustRWDesatConfig_swigregister(thrustRWDesatConfig)

class THRArrayConfigFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, THRArrayConfigFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, THRArrayConfigFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numThrusters"] = _thrustRWDesat.THRArrayConfigFswMsg_numThrusters_set
    __swig_getmethods__["numThrusters"] = _thrustRWDesat.THRArrayConfigFswMsg_numThrusters_get
    if _newclass:
        numThrusters = _swig_property(_thrustRWDesat.THRArrayConfigFswMsg_numThrusters_get, _thrustRWDesat.THRArrayConfigFswMsg_numThrusters_set)
    __swig_setmethods__["thrusters"] = _thrustRWDesat.THRArrayConfigFswMsg_thrusters_set
    __swig_getmethods__["thrusters"] = _thrustRWDesat.THRArrayConfigFswMsg_thrusters_get
    if _newclass:
        thrusters = _swig_property(_thrustRWDesat.THRArrayConfigFswMsg_thrusters_get, _thrustRWDesat.THRArrayConfigFswMsg_thrusters_set)

    def __init__(self):
        this = _thrustRWDesat.new_THRArrayConfigFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrustRWDesat.delete_THRArrayConfigFswMsg
    __del__ = lambda self: None
THRArrayConfigFswMsg_swigregister = _thrustRWDesat.THRArrayConfigFswMsg_swigregister
THRArrayConfigFswMsg_swigregister(THRArrayConfigFswMsg)

sizeof_THRArrayConfigFswMsg = _thrustRWDesat.sizeof_THRArrayConfigFswMsg
class THRArrayOnTimeCmdIntMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, THRArrayOnTimeCmdIntMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, THRArrayOnTimeCmdIntMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["OnTimeRequest"] = _thrustRWDesat.THRArrayOnTimeCmdIntMsg_OnTimeRequest_set
    __swig_getmethods__["OnTimeRequest"] = _thrustRWDesat.THRArrayOnTimeCmdIntMsg_OnTimeRequest_get
    if _newclass:
        OnTimeRequest = _swig_property(_thrustRWDesat.THRArrayOnTimeCmdIntMsg_OnTimeRequest_get, _thrustRWDesat.THRArrayOnTimeCmdIntMsg_OnTimeRequest_set)

    def __init__(self):
        this = _thrustRWDesat.new_THRArrayOnTimeCmdIntMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _thrustRWDesat.delete_THRArrayOnTimeCmdIntMsg
    __del__ = lambda self: None
THRArrayOnTimeCmdIntMsg_swigregister = _thrustRWDesat.THRArrayOnTimeCmdIntMsg_swigregister
THRArrayOnTimeCmdIntMsg_swigregister(THRArrayOnTimeCmdIntMsg)


import sys
protectAllClasses(sys.modules[__name__])

# This file is compatible with both classic and new-style classes.


