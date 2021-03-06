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
        mname = '.'.join((pkg, '_sunlineEKF')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_sunlineEKF')
    _sunlineEKF = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_sunlineEKF', [dirname(__file__)])
        except ImportError:
            import _sunlineEKF
            return _sunlineEKF
        try:
            _mod = imp.load_module('_sunlineEKF', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _sunlineEKF = swig_import_helper()
    del swig_import_helper
else:
    import _sunlineEKF
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
    return _sunlineEKF.new_doubleArray(nelements)
new_doubleArray = _sunlineEKF.new_doubleArray

def delete_doubleArray(ary):
    return _sunlineEKF.delete_doubleArray(ary)
delete_doubleArray = _sunlineEKF.delete_doubleArray

def doubleArray_getitem(ary, index):
    return _sunlineEKF.doubleArray_getitem(ary, index)
doubleArray_getitem = _sunlineEKF.doubleArray_getitem

def doubleArray_setitem(ary, index, value):
    return _sunlineEKF.doubleArray_setitem(ary, index, value)
doubleArray_setitem = _sunlineEKF.doubleArray_setitem

def new_longArray(nelements):
    return _sunlineEKF.new_longArray(nelements)
new_longArray = _sunlineEKF.new_longArray

def delete_longArray(ary):
    return _sunlineEKF.delete_longArray(ary)
delete_longArray = _sunlineEKF.delete_longArray

def longArray_getitem(ary, index):
    return _sunlineEKF.longArray_getitem(ary, index)
longArray_getitem = _sunlineEKF.longArray_getitem

def longArray_setitem(ary, index, value):
    return _sunlineEKF.longArray_setitem(ary, index, value)
longArray_setitem = _sunlineEKF.longArray_setitem

def new_intArray(nelements):
    return _sunlineEKF.new_intArray(nelements)
new_intArray = _sunlineEKF.new_intArray

def delete_intArray(ary):
    return _sunlineEKF.delete_intArray(ary)
delete_intArray = _sunlineEKF.delete_intArray

def intArray_getitem(ary, index):
    return _sunlineEKF.intArray_getitem(ary, index)
intArray_getitem = _sunlineEKF.intArray_getitem

def intArray_setitem(ary, index, value):
    return _sunlineEKF.intArray_setitem(ary, index, value)
intArray_setitem = _sunlineEKF.intArray_setitem

def new_shortArray(nelements):
    return _sunlineEKF.new_shortArray(nelements)
new_shortArray = _sunlineEKF.new_shortArray

def delete_shortArray(ary):
    return _sunlineEKF.delete_shortArray(ary)
delete_shortArray = _sunlineEKF.delete_shortArray

def shortArray_getitem(ary, index):
    return _sunlineEKF.shortArray_getitem(ary, index)
shortArray_getitem = _sunlineEKF.shortArray_getitem

def shortArray_setitem(ary, index, value):
    return _sunlineEKF.shortArray_setitem(ary, index, value)
shortArray_setitem = _sunlineEKF.shortArray_setitem


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


Update_sunlineEKF = _sunlineEKF.Update_sunlineEKF
SelfInit_sunlineEKF = _sunlineEKF.SelfInit_sunlineEKF
CrossInit_sunlineEKF = _sunlineEKF.CrossInit_sunlineEKF
Reset_sunlineEKF = _sunlineEKF.Reset_sunlineEKF
sizeof_SunlineFilterFswMsg = _sunlineEKF.sizeof_SunlineFilterFswMsg
sizeof_CSSConfigFswMsg = _sunlineEKF.sizeof_CSSConfigFswMsg
sizeof_sunlineEKFConfig = _sunlineEKF.sizeof_sunlineEKFConfig
UKF_MAX_DIM = _sunlineEKF.UKF_MAX_DIM

def ukfQRDJustR(sourceMat, nRow, nCol, destMat):
    return _sunlineEKF.ukfQRDJustR(sourceMat, nRow, nCol, destMat)
ukfQRDJustR = _sunlineEKF.ukfQRDJustR

def ukfLInv(sourceMat, nRow, nCol, destMat):
    return _sunlineEKF.ukfLInv(sourceMat, nRow, nCol, destMat)
ukfLInv = _sunlineEKF.ukfLInv

def ukfUInv(sourceMat, nRow, nCol, destMat):
    return _sunlineEKF.ukfUInv(sourceMat, nRow, nCol, destMat)
ukfUInv = _sunlineEKF.ukfUInv

def ukfLUD(sourceMat, nRow, nCol, destMat, indx):
    return _sunlineEKF.ukfLUD(sourceMat, nRow, nCol, destMat, indx)
ukfLUD = _sunlineEKF.ukfLUD

def ukfLUBckSlv(sourceMat, nRow, nCol, indx, bmat, destMat):
    return _sunlineEKF.ukfLUBckSlv(sourceMat, nRow, nCol, indx, bmat, destMat)
ukfLUBckSlv = _sunlineEKF.ukfLUBckSlv

def ukfMatInv(sourceMat, nRow, nCol, destMat):
    return _sunlineEKF.ukfMatInv(sourceMat, nRow, nCol, destMat)
ukfMatInv = _sunlineEKF.ukfMatInv

def ukfCholDecomp(sourceMat, nRow, nCol, destMat):
    return _sunlineEKF.ukfCholDecomp(sourceMat, nRow, nCol, destMat)
ukfCholDecomp = _sunlineEKF.ukfCholDecomp

def ukfCholDownDate(rMat, xVec, beta, nStates, rOut):
    return _sunlineEKF.ukfCholDownDate(rMat, xVec, beta, nStates, rOut)
ukfCholDownDate = _sunlineEKF.ukfCholDownDate
SKF_N_STATES = _sunlineEKF.SKF_N_STATES
SKF_N_STATES_SWITCH = _sunlineEKF.SKF_N_STATES_SWITCH
SKF_N_STATES_HALF = _sunlineEKF.SKF_N_STATES_HALF
MAX_N_CSS_MEAS = _sunlineEKF.MAX_N_CSS_MEAS
class SunlineFilterFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SunlineFilterFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SunlineFilterFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["timeTag"] = _sunlineEKF.SunlineFilterFswMsg_timeTag_set
    __swig_getmethods__["timeTag"] = _sunlineEKF.SunlineFilterFswMsg_timeTag_get
    if _newclass:
        timeTag = _swig_property(_sunlineEKF.SunlineFilterFswMsg_timeTag_get, _sunlineEKF.SunlineFilterFswMsg_timeTag_set)
    __swig_setmethods__["covar"] = _sunlineEKF.SunlineFilterFswMsg_covar_set
    __swig_getmethods__["covar"] = _sunlineEKF.SunlineFilterFswMsg_covar_get
    if _newclass:
        covar = _swig_property(_sunlineEKF.SunlineFilterFswMsg_covar_get, _sunlineEKF.SunlineFilterFswMsg_covar_set)
    __swig_setmethods__["state"] = _sunlineEKF.SunlineFilterFswMsg_state_set
    __swig_getmethods__["state"] = _sunlineEKF.SunlineFilterFswMsg_state_get
    if _newclass:
        state = _swig_property(_sunlineEKF.SunlineFilterFswMsg_state_get, _sunlineEKF.SunlineFilterFswMsg_state_set)
    __swig_setmethods__["stateError"] = _sunlineEKF.SunlineFilterFswMsg_stateError_set
    __swig_getmethods__["stateError"] = _sunlineEKF.SunlineFilterFswMsg_stateError_get
    if _newclass:
        stateError = _swig_property(_sunlineEKF.SunlineFilterFswMsg_stateError_get, _sunlineEKF.SunlineFilterFswMsg_stateError_set)
    __swig_setmethods__["postFitRes"] = _sunlineEKF.SunlineFilterFswMsg_postFitRes_set
    __swig_getmethods__["postFitRes"] = _sunlineEKF.SunlineFilterFswMsg_postFitRes_get
    if _newclass:
        postFitRes = _swig_property(_sunlineEKF.SunlineFilterFswMsg_postFitRes_get, _sunlineEKF.SunlineFilterFswMsg_postFitRes_set)
    __swig_setmethods__["numObs"] = _sunlineEKF.SunlineFilterFswMsg_numObs_set
    __swig_getmethods__["numObs"] = _sunlineEKF.SunlineFilterFswMsg_numObs_get
    if _newclass:
        numObs = _swig_property(_sunlineEKF.SunlineFilterFswMsg_numObs_get, _sunlineEKF.SunlineFilterFswMsg_numObs_set)

    def __init__(self):
        this = _sunlineEKF.new_SunlineFilterFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _sunlineEKF.delete_SunlineFilterFswMsg
    __del__ = lambda self: None
SunlineFilterFswMsg_swigregister = _sunlineEKF.SunlineFilterFswMsg_swigregister
SunlineFilterFswMsg_swigregister(SunlineFilterFswMsg)

class CSSConfigFswMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CSSConfigFswMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CSSConfigFswMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nCSS"] = _sunlineEKF.CSSConfigFswMsg_nCSS_set
    __swig_getmethods__["nCSS"] = _sunlineEKF.CSSConfigFswMsg_nCSS_get
    if _newclass:
        nCSS = _swig_property(_sunlineEKF.CSSConfigFswMsg_nCSS_get, _sunlineEKF.CSSConfigFswMsg_nCSS_set)
    __swig_setmethods__["cssVals"] = _sunlineEKF.CSSConfigFswMsg_cssVals_set
    __swig_getmethods__["cssVals"] = _sunlineEKF.CSSConfigFswMsg_cssVals_get
    if _newclass:
        cssVals = _swig_property(_sunlineEKF.CSSConfigFswMsg_cssVals_get, _sunlineEKF.CSSConfigFswMsg_cssVals_set)

    def __init__(self):
        this = _sunlineEKF.new_CSSConfigFswMsg()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _sunlineEKF.delete_CSSConfigFswMsg
    __del__ = lambda self: None
CSSConfigFswMsg_swigregister = _sunlineEKF.CSSConfigFswMsg_swigregister
CSSConfigFswMsg_swigregister(CSSConfigFswMsg)

class sunlineEKFConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sunlineEKFConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sunlineEKFConfig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["navStateOutMsgName"] = _sunlineEKF.sunlineEKFConfig_navStateOutMsgName_set
    __swig_getmethods__["navStateOutMsgName"] = _sunlineEKF.sunlineEKFConfig_navStateOutMsgName_get
    if _newclass:
        navStateOutMsgName = _swig_property(_sunlineEKF.sunlineEKFConfig_navStateOutMsgName_get, _sunlineEKF.sunlineEKFConfig_navStateOutMsgName_set)
    __swig_setmethods__["filtDataOutMsgName"] = _sunlineEKF.sunlineEKFConfig_filtDataOutMsgName_set
    __swig_getmethods__["filtDataOutMsgName"] = _sunlineEKF.sunlineEKFConfig_filtDataOutMsgName_get
    if _newclass:
        filtDataOutMsgName = _swig_property(_sunlineEKF.sunlineEKFConfig_filtDataOutMsgName_get, _sunlineEKF.sunlineEKFConfig_filtDataOutMsgName_set)
    __swig_setmethods__["cssDataInMsgName"] = _sunlineEKF.sunlineEKFConfig_cssDataInMsgName_set
    __swig_getmethods__["cssDataInMsgName"] = _sunlineEKF.sunlineEKFConfig_cssDataInMsgName_get
    if _newclass:
        cssDataInMsgName = _swig_property(_sunlineEKF.sunlineEKFConfig_cssDataInMsgName_get, _sunlineEKF.sunlineEKFConfig_cssDataInMsgName_set)
    __swig_setmethods__["cssConfigInMsgName"] = _sunlineEKF.sunlineEKFConfig_cssConfigInMsgName_set
    __swig_getmethods__["cssConfigInMsgName"] = _sunlineEKF.sunlineEKFConfig_cssConfigInMsgName_get
    if _newclass:
        cssConfigInMsgName = _swig_property(_sunlineEKF.sunlineEKFConfig_cssConfigInMsgName_get, _sunlineEKF.sunlineEKFConfig_cssConfigInMsgName_set)
    __swig_setmethods__["qObsVal"] = _sunlineEKF.sunlineEKFConfig_qObsVal_set
    __swig_getmethods__["qObsVal"] = _sunlineEKF.sunlineEKFConfig_qObsVal_get
    if _newclass:
        qObsVal = _swig_property(_sunlineEKF.sunlineEKFConfig_qObsVal_get, _sunlineEKF.sunlineEKFConfig_qObsVal_set)
    __swig_setmethods__["qProcVal"] = _sunlineEKF.sunlineEKFConfig_qProcVal_set
    __swig_getmethods__["qProcVal"] = _sunlineEKF.sunlineEKFConfig_qProcVal_get
    if _newclass:
        qProcVal = _swig_property(_sunlineEKF.sunlineEKFConfig_qProcVal_get, _sunlineEKF.sunlineEKFConfig_qProcVal_set)
    __swig_setmethods__["dt"] = _sunlineEKF.sunlineEKFConfig_dt_set
    __swig_getmethods__["dt"] = _sunlineEKF.sunlineEKFConfig_dt_get
    if _newclass:
        dt = _swig_property(_sunlineEKF.sunlineEKFConfig_dt_get, _sunlineEKF.sunlineEKFConfig_dt_set)
    __swig_setmethods__["timeTag"] = _sunlineEKF.sunlineEKFConfig_timeTag_set
    __swig_getmethods__["timeTag"] = _sunlineEKF.sunlineEKFConfig_timeTag_get
    if _newclass:
        timeTag = _swig_property(_sunlineEKF.sunlineEKFConfig_timeTag_get, _sunlineEKF.sunlineEKFConfig_timeTag_set)
    __swig_setmethods__["state"] = _sunlineEKF.sunlineEKFConfig_state_set
    __swig_getmethods__["state"] = _sunlineEKF.sunlineEKFConfig_state_get
    if _newclass:
        state = _swig_property(_sunlineEKF.sunlineEKFConfig_state_get, _sunlineEKF.sunlineEKFConfig_state_set)
    __swig_setmethods__["x"] = _sunlineEKF.sunlineEKFConfig_x_set
    __swig_getmethods__["x"] = _sunlineEKF.sunlineEKFConfig_x_get
    if _newclass:
        x = _swig_property(_sunlineEKF.sunlineEKFConfig_x_get, _sunlineEKF.sunlineEKFConfig_x_set)
    __swig_setmethods__["xBar"] = _sunlineEKF.sunlineEKFConfig_xBar_set
    __swig_getmethods__["xBar"] = _sunlineEKF.sunlineEKFConfig_xBar_get
    if _newclass:
        xBar = _swig_property(_sunlineEKF.sunlineEKFConfig_xBar_get, _sunlineEKF.sunlineEKFConfig_xBar_set)
    __swig_setmethods__["covarBar"] = _sunlineEKF.sunlineEKFConfig_covarBar_set
    __swig_getmethods__["covarBar"] = _sunlineEKF.sunlineEKFConfig_covarBar_get
    if _newclass:
        covarBar = _swig_property(_sunlineEKF.sunlineEKFConfig_covarBar_get, _sunlineEKF.sunlineEKFConfig_covarBar_set)
    __swig_setmethods__["covar"] = _sunlineEKF.sunlineEKFConfig_covar_set
    __swig_getmethods__["covar"] = _sunlineEKF.sunlineEKFConfig_covar_get
    if _newclass:
        covar = _swig_property(_sunlineEKF.sunlineEKFConfig_covar_get, _sunlineEKF.sunlineEKFConfig_covar_set)
    __swig_setmethods__["stateTransition"] = _sunlineEKF.sunlineEKFConfig_stateTransition_set
    __swig_getmethods__["stateTransition"] = _sunlineEKF.sunlineEKFConfig_stateTransition_get
    if _newclass:
        stateTransition = _swig_property(_sunlineEKF.sunlineEKFConfig_stateTransition_get, _sunlineEKF.sunlineEKFConfig_stateTransition_set)
    __swig_setmethods__["kalmanGain"] = _sunlineEKF.sunlineEKFConfig_kalmanGain_set
    __swig_getmethods__["kalmanGain"] = _sunlineEKF.sunlineEKFConfig_kalmanGain_get
    if _newclass:
        kalmanGain = _swig_property(_sunlineEKF.sunlineEKFConfig_kalmanGain_get, _sunlineEKF.sunlineEKFConfig_kalmanGain_set)
    __swig_setmethods__["dynMat"] = _sunlineEKF.sunlineEKFConfig_dynMat_set
    __swig_getmethods__["dynMat"] = _sunlineEKF.sunlineEKFConfig_dynMat_get
    if _newclass:
        dynMat = _swig_property(_sunlineEKF.sunlineEKFConfig_dynMat_get, _sunlineEKF.sunlineEKFConfig_dynMat_set)
    __swig_setmethods__["measMat"] = _sunlineEKF.sunlineEKFConfig_measMat_set
    __swig_getmethods__["measMat"] = _sunlineEKF.sunlineEKFConfig_measMat_get
    if _newclass:
        measMat = _swig_property(_sunlineEKF.sunlineEKFConfig_measMat_get, _sunlineEKF.sunlineEKFConfig_measMat_set)
    __swig_setmethods__["obs"] = _sunlineEKF.sunlineEKFConfig_obs_set
    __swig_getmethods__["obs"] = _sunlineEKF.sunlineEKFConfig_obs_get
    if _newclass:
        obs = _swig_property(_sunlineEKF.sunlineEKFConfig_obs_get, _sunlineEKF.sunlineEKFConfig_obs_set)
    __swig_setmethods__["yMeas"] = _sunlineEKF.sunlineEKFConfig_yMeas_set
    __swig_getmethods__["yMeas"] = _sunlineEKF.sunlineEKFConfig_yMeas_get
    if _newclass:
        yMeas = _swig_property(_sunlineEKF.sunlineEKFConfig_yMeas_get, _sunlineEKF.sunlineEKFConfig_yMeas_set)
    __swig_setmethods__["procNoise"] = _sunlineEKF.sunlineEKFConfig_procNoise_set
    __swig_getmethods__["procNoise"] = _sunlineEKF.sunlineEKFConfig_procNoise_get
    if _newclass:
        procNoise = _swig_property(_sunlineEKF.sunlineEKFConfig_procNoise_get, _sunlineEKF.sunlineEKFConfig_procNoise_set)
    __swig_setmethods__["measNoise"] = _sunlineEKF.sunlineEKFConfig_measNoise_set
    __swig_getmethods__["measNoise"] = _sunlineEKF.sunlineEKFConfig_measNoise_get
    if _newclass:
        measNoise = _swig_property(_sunlineEKF.sunlineEKFConfig_measNoise_get, _sunlineEKF.sunlineEKFConfig_measNoise_set)
    __swig_setmethods__["postFits"] = _sunlineEKF.sunlineEKFConfig_postFits_set
    __swig_getmethods__["postFits"] = _sunlineEKF.sunlineEKFConfig_postFits_get
    if _newclass:
        postFits = _swig_property(_sunlineEKF.sunlineEKFConfig_postFits_get, _sunlineEKF.sunlineEKFConfig_postFits_set)
    __swig_setmethods__["cssNHat_B"] = _sunlineEKF.sunlineEKFConfig_cssNHat_B_set
    __swig_getmethods__["cssNHat_B"] = _sunlineEKF.sunlineEKFConfig_cssNHat_B_get
    if _newclass:
        cssNHat_B = _swig_property(_sunlineEKF.sunlineEKFConfig_cssNHat_B_get, _sunlineEKF.sunlineEKFConfig_cssNHat_B_set)
    __swig_setmethods__["CBias"] = _sunlineEKF.sunlineEKFConfig_CBias_set
    __swig_getmethods__["CBias"] = _sunlineEKF.sunlineEKFConfig_CBias_get
    if _newclass:
        CBias = _swig_property(_sunlineEKF.sunlineEKFConfig_CBias_get, _sunlineEKF.sunlineEKFConfig_CBias_set)
    __swig_setmethods__["numStates"] = _sunlineEKF.sunlineEKFConfig_numStates_set
    __swig_getmethods__["numStates"] = _sunlineEKF.sunlineEKFConfig_numStates_get
    if _newclass:
        numStates = _swig_property(_sunlineEKF.sunlineEKFConfig_numStates_get, _sunlineEKF.sunlineEKFConfig_numStates_set)
    __swig_setmethods__["numObs"] = _sunlineEKF.sunlineEKFConfig_numObs_set
    __swig_getmethods__["numObs"] = _sunlineEKF.sunlineEKFConfig_numObs_get
    if _newclass:
        numObs = _swig_property(_sunlineEKF.sunlineEKFConfig_numObs_get, _sunlineEKF.sunlineEKFConfig_numObs_set)
    __swig_setmethods__["numActiveCss"] = _sunlineEKF.sunlineEKFConfig_numActiveCss_set
    __swig_getmethods__["numActiveCss"] = _sunlineEKF.sunlineEKFConfig_numActiveCss_get
    if _newclass:
        numActiveCss = _swig_property(_sunlineEKF.sunlineEKFConfig_numActiveCss_get, _sunlineEKF.sunlineEKFConfig_numActiveCss_set)
    __swig_setmethods__["numCSSTotal"] = _sunlineEKF.sunlineEKFConfig_numCSSTotal_set
    __swig_getmethods__["numCSSTotal"] = _sunlineEKF.sunlineEKFConfig_numCSSTotal_get
    if _newclass:
        numCSSTotal = _swig_property(_sunlineEKF.sunlineEKFConfig_numCSSTotal_get, _sunlineEKF.sunlineEKFConfig_numCSSTotal_set)
    __swig_setmethods__["sensorUseThresh"] = _sunlineEKF.sunlineEKFConfig_sensorUseThresh_set
    __swig_getmethods__["sensorUseThresh"] = _sunlineEKF.sunlineEKFConfig_sensorUseThresh_get
    if _newclass:
        sensorUseThresh = _swig_property(_sunlineEKF.sunlineEKFConfig_sensorUseThresh_get, _sunlineEKF.sunlineEKFConfig_sensorUseThresh_set)
    __swig_setmethods__["eKFSwitch"] = _sunlineEKF.sunlineEKFConfig_eKFSwitch_set
    __swig_getmethods__["eKFSwitch"] = _sunlineEKF.sunlineEKFConfig_eKFSwitch_get
    if _newclass:
        eKFSwitch = _swig_property(_sunlineEKF.sunlineEKFConfig_eKFSwitch_get, _sunlineEKF.sunlineEKFConfig_eKFSwitch_set)
    __swig_setmethods__["outputSunline"] = _sunlineEKF.sunlineEKFConfig_outputSunline_set
    __swig_getmethods__["outputSunline"] = _sunlineEKF.sunlineEKFConfig_outputSunline_get
    if _newclass:
        outputSunline = _swig_property(_sunlineEKF.sunlineEKFConfig_outputSunline_get, _sunlineEKF.sunlineEKFConfig_outputSunline_set)
    __swig_setmethods__["cssSensorInBuffer"] = _sunlineEKF.sunlineEKFConfig_cssSensorInBuffer_set
    __swig_getmethods__["cssSensorInBuffer"] = _sunlineEKF.sunlineEKFConfig_cssSensorInBuffer_get
    if _newclass:
        cssSensorInBuffer = _swig_property(_sunlineEKF.sunlineEKFConfig_cssSensorInBuffer_get, _sunlineEKF.sunlineEKFConfig_cssSensorInBuffer_set)
    __swig_setmethods__["navStateOutMsgId"] = _sunlineEKF.sunlineEKFConfig_navStateOutMsgId_set
    __swig_getmethods__["navStateOutMsgId"] = _sunlineEKF.sunlineEKFConfig_navStateOutMsgId_get
    if _newclass:
        navStateOutMsgId = _swig_property(_sunlineEKF.sunlineEKFConfig_navStateOutMsgId_get, _sunlineEKF.sunlineEKFConfig_navStateOutMsgId_set)
    __swig_setmethods__["filtDataOutMsgId"] = _sunlineEKF.sunlineEKFConfig_filtDataOutMsgId_set
    __swig_getmethods__["filtDataOutMsgId"] = _sunlineEKF.sunlineEKFConfig_filtDataOutMsgId_get
    if _newclass:
        filtDataOutMsgId = _swig_property(_sunlineEKF.sunlineEKFConfig_filtDataOutMsgId_get, _sunlineEKF.sunlineEKFConfig_filtDataOutMsgId_set)
    __swig_setmethods__["cssDataInMsgId"] = _sunlineEKF.sunlineEKFConfig_cssDataInMsgId_set
    __swig_getmethods__["cssDataInMsgId"] = _sunlineEKF.sunlineEKFConfig_cssDataInMsgId_get
    if _newclass:
        cssDataInMsgId = _swig_property(_sunlineEKF.sunlineEKFConfig_cssDataInMsgId_get, _sunlineEKF.sunlineEKFConfig_cssDataInMsgId_set)
    __swig_setmethods__["cssConfigInMsgId"] = _sunlineEKF.sunlineEKFConfig_cssConfigInMsgId_set
    __swig_getmethods__["cssConfigInMsgId"] = _sunlineEKF.sunlineEKFConfig_cssConfigInMsgId_get
    if _newclass:
        cssConfigInMsgId = _swig_property(_sunlineEKF.sunlineEKFConfig_cssConfigInMsgId_get, _sunlineEKF.sunlineEKFConfig_cssConfigInMsgId_set)

    def __init__(self):
        this = _sunlineEKF.new_sunlineEKFConfig()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _sunlineEKF.delete_sunlineEKFConfig
    __del__ = lambda self: None
sunlineEKFConfig_swigregister = _sunlineEKF.sunlineEKFConfig_swigregister
sunlineEKFConfig_swigregister(sunlineEKFConfig)


def sunlineTimeUpdate(ConfigData, updateTime):
    return _sunlineEKF.sunlineTimeUpdate(ConfigData, updateTime)
sunlineTimeUpdate = _sunlineEKF.sunlineTimeUpdate

def sunlineMeasUpdate(ConfigData, updateTime):
    return _sunlineEKF.sunlineMeasUpdate(ConfigData, updateTime)
sunlineMeasUpdate = _sunlineEKF.sunlineMeasUpdate

def sunlineStateSTMProp(dynMat, dt, stateInOut, stateTransition):
    return _sunlineEKF.sunlineStateSTMProp(dynMat, dt, stateInOut, stateTransition)
sunlineStateSTMProp = _sunlineEKF.sunlineStateSTMProp

def sunlineHMatrixYMeas(states, numCSS, cssSensorCos, sensorUseThresh, cssNHat_B, CBias, obs, yMeas, numObs, measMat):
    return _sunlineEKF.sunlineHMatrixYMeas(states, numCSS, cssSensorCos, sensorUseThresh, cssNHat_B, CBias, obs, yMeas, numObs, measMat)
sunlineHMatrixYMeas = _sunlineEKF.sunlineHMatrixYMeas

def sunlineKalmanGain(covarBar, hObs, qObsVal, numObs, kalmanGain):
    return _sunlineEKF.sunlineKalmanGain(covarBar, hObs, qObsVal, numObs, kalmanGain)
sunlineKalmanGain = _sunlineEKF.sunlineKalmanGain

def sunlineDynMatrix(stateInOut, dt, dynMat):
    return _sunlineEKF.sunlineDynMatrix(stateInOut, dt, dynMat)
sunlineDynMatrix = _sunlineEKF.sunlineDynMatrix

def sunlineCKFUpdate(xBar, kalmanGain, covarBar, qObsVal, numObs, yObs, hObs, x, covar):
    return _sunlineEKF.sunlineCKFUpdate(xBar, kalmanGain, covarBar, qObsVal, numObs, yObs, hObs, x, covar)
sunlineCKFUpdate = _sunlineEKF.sunlineCKFUpdate

def sunlineEKFUpdate(kalmanGain, covarBar, qObsVal, numObs, yObs, hObs, states, x, covar):
    return _sunlineEKF.sunlineEKFUpdate(kalmanGain, covarBar, qObsVal, numObs, yObs, hObs, states, x, covar)
sunlineEKFUpdate = _sunlineEKF.sunlineEKFUpdate

import sys
protectAllClasses(sys.modules[__name__])

# This file is compatible with both classic and new-style classes.


