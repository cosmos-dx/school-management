// This file implements the IBackgroundCopyJob Interface for Python.
// Generated by makegw.py

#include "bits_pch.h"
#include "PyIBackgroundCopyJob.h"

// @doc - This file contains autoduck documentation
// ---------------------------------------------------
//
// Interface Implementation

PyIBackgroundCopyJob::PyIBackgroundCopyJob(IUnknown *pdisp) : PyIUnknown(pdisp) { ob_type = &type; }

PyIBackgroundCopyJob::~PyIBackgroundCopyJob() {}

/* static */ IBackgroundCopyJob *PyIBackgroundCopyJob::GetI(PyObject *self)
{
    return (IBackgroundCopyJob *)PyIUnknown::GetI(self);
}

// @pymethod |PyIBackgroundCopyJob|AddFileSet|Description of AddFileSet.
PyObject *PyIBackgroundCopyJob::AddFileSet(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    // @pyparm [<o PyBG_FILE_INFO, ...]|pFileSet||Description for pFileSet
    PyObject *obFileSet;
    if (!PyArg_ParseTuple(args, "O:AddFileSet", &obFileSet))
        return NULL;
    ULONG cFileCount;
    BG_FILE_INFO *pFileSet;
    if (!PyObject_AsBG_FILE_INFO_LIST(obFileSet, &cFileCount, &pFileSet))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->AddFileSet(cFileCount, pFileSet);
    PyObject_FreeBG_FILE_INFO_LIST(cFileCount, pFileSet);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIBackgroundCopyJob|AddFile|Description of AddFile.
PyObject *PyIBackgroundCopyJob::AddFile(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    // @pyparm <o unicode>|RemoteUrl||Description for RemoteUrl
    // @pyparm <o unicode>|LocalName||Description for LocalName
    PyObject *obRemoteUrl;
    PyObject *obLocalName;
    LPWSTR RemoteUrl;
    LPWSTR LocalName;
    if (!PyArg_ParseTuple(args, "OO:AddFile", &obRemoteUrl, &obLocalName))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (bPythonIsHappy && !PyWinObject_AsBstr(obRemoteUrl, &RemoteUrl))
        bPythonIsHappy = FALSE;
    if (bPythonIsHappy && !PyWinObject_AsBstr(obLocalName, &LocalName))
        bPythonIsHappy = FALSE;
    if (!bPythonIsHappy)
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->AddFile(RemoteUrl, LocalName);
    SysFreeString(RemoteUrl);
    SysFreeString(LocalName);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIBackgroundCopyJob|EnumFiles|Description of EnumFiles.
PyObject *PyIBackgroundCopyJob::EnumFiles(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    IEnumBackgroundCopyFiles *pEnum;
    if (!PyArg_ParseTuple(args, ":EnumFiles"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->EnumFiles(&pEnum);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyCom_PyObjectFromIUnknown(pEnum, IID_IEnumBackgroundCopyFiles, FALSE);
}

// @pymethod |PyIBackgroundCopyJob|Suspend|Description of Suspend.
PyObject *PyIBackgroundCopyJob::Suspend(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":Suspend"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->Suspend();
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyLong_FromLong(hr);
}

// @pymethod |PyIBackgroundCopyJob|Resume|Description of Resume.
PyObject *PyIBackgroundCopyJob::Resume(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":Resume"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->Resume();
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyLong_FromLong(hr);
}

// @pymethod |PyIBackgroundCopyJob|Cancel|Description of Cancel.
PyObject *PyIBackgroundCopyJob::Cancel(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":Cancel"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->Cancel();
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyLong_FromLong(hr);
}

// @pymethod |PyIBackgroundCopyJob|Complete|Description of Complete.
PyObject *PyIBackgroundCopyJob::Complete(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":Complete"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->Complete();

    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyLong_FromLong(hr);
}

// @pymethod |PyIBackgroundCopyJob|GetId|Description of GetId.
PyObject *PyIBackgroundCopyJob::GetId(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    GUID val;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetId(&val);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyWinObject_FromIID(val);
}

// @pymethod |PyIBackgroundCopyJob|GetType|Description of GetType.
PyObject *PyIBackgroundCopyJob::GetType(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":GetType"))
        return NULL;
    HRESULT hr;
    BG_JOB_TYPE val;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetType(&val);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyLong_FromLong(val);
}

// @pymethod |PyIBackgroundCopyJob|GetProgress|Description of GetProgress.
PyObject *PyIBackgroundCopyJob::GetProgress(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":GetProgress"))
        return NULL;
    BG_JOB_PROGRESS val;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetProgress(&val);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyObject_FromBG_JOB_PROGRESS(&val);
}

// @pymethod |PyIBackgroundCopyJob|GetTimes|Description of GetTimes.
PyObject *PyIBackgroundCopyJob::GetTimes(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":GetTimes"))
        return NULL;
    BG_JOB_TIMES val;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetTimes(&val);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyObject_FromBG_JOB_TIMES(&val);
}

// @pymethod |PyIBackgroundCopyJob|GetState|Description of GetState.
PyObject *PyIBackgroundCopyJob::GetState(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":GetState"))
        return NULL;
    BG_JOB_STATE val;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetState(&val);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyLong_FromLong((long)val);
}

// @pymethod |PyIBackgroundCopyJob|GetError|Description of GetError.
PyObject *PyIBackgroundCopyJob::GetError(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    IBackgroundCopyError *ppError;
    if (!PyArg_ParseTuple(args, ":GetError"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetError(&ppError);
    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyCom_PyObjectFromIUnknown(ppError, IID_IBackgroundCopyError, FALSE);
}

// @pymethod |PyIBackgroundCopyJob|GetOwner|Description of GetOwner.
PyObject *PyIBackgroundCopyJob::GetOwner(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    LPWSTR val;
    if (!PyArg_ParseTuple(args, ":GetOwner"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetOwner(&val);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    PyObject *ret = PyWinObject_FromWCHAR(val);
    CoTaskMemFree(val);
    return ret;
}

// @pymethod |PyIBackgroundCopyJob|SetDisplayName|Description of SetDisplayName.
PyObject *PyIBackgroundCopyJob::SetDisplayName(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    // @pyparm <o unicode>|Val||Description for Val
    PyObject *obVal;
    LPWSTR Val;
    if (!PyArg_ParseTuple(args, "O:SetDisplayName", &obVal))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (!PyWinObject_AsBstr(obVal, &Val))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->SetDisplayName(Val);
    SysFreeString(Val);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIBackgroundCopyJob|GetDisplayName|Description of GetDisplayName.
PyObject *PyIBackgroundCopyJob::GetDisplayName(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    LPWSTR pVal;
    if (!PyArg_ParseTuple(args, ":GetDisplayName"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetDisplayName(&pVal);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    PyObject *ret = PyWinObject_FromWCHAR(pVal);
    CoTaskMemFree(pVal);
    return ret;
}

// @pymethod |PyIBackgroundCopyJob|SetDescription|Description of SetDescription.
PyObject *PyIBackgroundCopyJob::SetDescription(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    // @pyparm <o unicode>|Val||Description for Val
    PyObject *obVal;
    LPWSTR Val;
    if (!PyArg_ParseTuple(args, "O:SetDescription", &obVal))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (!PyWinObject_AsWCHAR(obVal, &Val))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->SetDescription(Val);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIBackgroundCopyJob|GetDescription|Description of GetDescription.
PyObject *PyIBackgroundCopyJob::GetDescription(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    LPWSTR pVal;
    if (!PyArg_ParseTuple(args, ":GetDescription"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetDescription(&pVal);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    PyObject *ret = PyWinObject_FromWCHAR(pVal);
    CoTaskMemFree(pVal);
    return ret;
}

// @pymethod |PyIBackgroundCopyJob|SetPriority|Description of SetPriority.
PyObject *PyIBackgroundCopyJob::SetPriority(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    BG_JOB_PRIORITY val;
    // @pyparm int|Val||Description for Val
    if (!PyArg_ParseTuple(args, "l:SetPriority", &val))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->SetPriority(val);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIBackgroundCopyJob|GetPriority|Description of GetPriority.
PyObject *PyIBackgroundCopyJob::GetPriority(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":GetPriority"))
        return NULL;
    BG_JOB_PRIORITY val;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetPriority(&val);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyLong_FromLong(val);
}

// @pymethod |PyIBackgroundCopyJob|SetNotifyFlags|Description of SetNotifyFlags.
PyObject *PyIBackgroundCopyJob::SetNotifyFlags(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    // @pyparm int|Val||Description for Val
    ULONG Val;
    if (!PyArg_ParseTuple(args, "l:SetNotifyFlags", &Val))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->SetNotifyFlags(Val);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIBackgroundCopyJob|GetNotifyFlags|Description of GetNotifyFlags.
PyObject *PyIBackgroundCopyJob::GetNotifyFlags(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":GetNotifyFlags"))
        return NULL;
    ULONG val;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetNotifyFlags(&val);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyLong_FromUnsignedLong(val);
}

// @pymethod |PyIBackgroundCopyJob|SetNotifyInterface|Description of SetNotifyInterface.
PyObject *PyIBackgroundCopyJob::SetNotifyInterface(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    // @pyparm <o PyIUnknown *>|Val||Description for Val
    PyObject *obVal;
    IUnknown *Val;
    if (!PyArg_ParseTuple(args, "O:SetNotifyInterface", &obVal))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (!PyCom_InterfaceFromPyInstanceOrObject(obVal, IID_IUnknown, (void **)&Val, TRUE /* bNoneOK */))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->SetNotifyInterface(Val);
    if (Val)
        Val->Release();
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIBackgroundCopyJob|GetNotifyInterface|Description of GetNotifyInterface.
PyObject *PyIBackgroundCopyJob::GetNotifyInterface(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    IUnknown *pVal;
    if (!PyArg_ParseTuple(args, ":GetNotifyInterface"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetNotifyInterface(&pVal);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyCom_PyObjectFromIUnknown(pVal, IID_IUnknown, FALSE);
}

// @pymethod |PyIBackgroundCopyJob|SetMinimumRetryDelay|Description of SetMinimumRetryDelay.
PyObject *PyIBackgroundCopyJob::SetMinimumRetryDelay(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    // @pyparm int|Seconds||Description for Seconds
    ULONG Seconds;
    if (!PyArg_ParseTuple(args, "l:SetMinimumRetryDelay", &Seconds))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->SetMinimumRetryDelay(Seconds);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIBackgroundCopyJob|GetMinimumRetryDelay|Description of GetMinimumRetryDelay.
PyObject *PyIBackgroundCopyJob::GetMinimumRetryDelay(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":GetMinimumRetryDelay"))
        return NULL;
    HRESULT hr;
    ULONG seconds;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetMinimumRetryDelay(&seconds);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyLong_FromUnsignedLong(seconds);
}

// @pymethod |PyIBackgroundCopyJob|SetNoProgressTimeout|Description of SetNoProgressTimeout.
PyObject *PyIBackgroundCopyJob::SetNoProgressTimeout(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    // @pyparm int|Seconds||Description for Seconds
    ULONG Seconds;
    if (!PyArg_ParseTuple(args, "l:SetNoProgressTimeout", &Seconds))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->SetNoProgressTimeout(Seconds);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIBackgroundCopyJob|GetNoProgressTimeout|Description of GetNoProgressTimeout.
PyObject *PyIBackgroundCopyJob::GetNoProgressTimeout(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":GetNoProgressTimeout"))
        return NULL;
    ULONG seconds;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetNoProgressTimeout(&seconds);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyLong_FromUnsignedLong(seconds);
}

// @pymethod |PyIBackgroundCopyJob|GetErrorCount|Description of GetErrorCount.
PyObject *PyIBackgroundCopyJob::GetErrorCount(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":GetErrorCount"))
        return NULL;
    ULONG errors;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetErrorCount(&errors);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyLong_FromUnsignedLong(errors);
}

// @pymethod |PyIBackgroundCopyJob|SetProxySettings|Description of SetProxySettings.
PyObject *PyIBackgroundCopyJob::SetProxySettings(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    BG_JOB_PROXY_USAGE ProxyUsage;
    // @pyparm int|ProxyUsage||Description for ProxyUsage
    WCHAR *ProxyList;
    PyObject *obProxyList;
    // @pyparm unicode|ProxyList||Description for ProxyList
    WCHAR *ProxyBypassList;
    PyObject *obProxyBypassList;
    // @pyparm unicode|ProxyBypassList||Description for ProxyBypassList
    if (!PyArg_ParseTuple(args, "lOO:SetProxySettings", &ProxyUsage, &obProxyList, &obProxyBypassList))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (bPythonIsHappy && !PyWinObject_AsWCHAR(obProxyList, &ProxyList, TRUE))
        bPythonIsHappy = FALSE;
    if (bPythonIsHappy && !PyWinObject_AsWCHAR(obProxyBypassList, &ProxyBypassList, TRUE))
        bPythonIsHappy = FALSE;
    if (!bPythonIsHappy)
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->SetProxySettings(ProxyUsage, ProxyList, ProxyBypassList);
    PyWinObject_FreeWCHAR(ProxyList);
    PyWinObject_FreeWCHAR(ProxyBypassList);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIBackgroundCopyJob|GetProxySettings|Description of GetProxySettings.
PyObject *PyIBackgroundCopyJob::GetProxySettings(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":GetProxySettings"))
        return NULL;
    BG_JOB_PROXY_USAGE ProxyUsage;
    WCHAR *proxyList, *bypassList;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->GetProxySettings(&ProxyUsage, &proxyList, &bypassList);
    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    PyObject *ret =
        Py_BuildValue("lNN", ProxyUsage, PyWinObject_FromWCHAR(proxyList), PyWinObject_FromWCHAR(bypassList));
    CoTaskMemFree(proxyList);
    CoTaskMemFree(bypassList);
    return ret;
}

// @pymethod |PyIBackgroundCopyJob|TakeOwnership|Description of TakeOwnership.
PyObject *PyIBackgroundCopyJob::TakeOwnership(PyObject *self, PyObject *args)
{
    IBackgroundCopyJob *pIBCJ = GetI(self);
    if (pIBCJ == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":TakeOwnership"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIBCJ->TakeOwnership();
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIBCJ, IID_IBackgroundCopyJob);
    return PyLong_FromLong(hr);
}

// @object PyIBackgroundCopyJob|Description of the interface
static struct PyMethodDef PyIBackgroundCopyJob_methods[] = {
    {"AddFileSet", PyIBackgroundCopyJob::AddFileSet, 1},    // @pymeth AddFileSet|Description of AddFileSet
    {"AddFile", PyIBackgroundCopyJob::AddFile, 1},          // @pymeth AddFile|Description of AddFile
    {"EnumFiles", PyIBackgroundCopyJob::EnumFiles, 1},      // @pymeth EnumFiles|Description of EnumFiles
    {"Suspend", PyIBackgroundCopyJob::Suspend, 1},          // @pymeth Suspend|Description of Suspend
    {"Resume", PyIBackgroundCopyJob::Resume, 1},            // @pymeth Resume|Description of Resume
    {"Cancel", PyIBackgroundCopyJob::Cancel, 1},            // @pymeth Cancel|Description of Cancel
    {"Complete", PyIBackgroundCopyJob::Complete, 1},        // @pymeth Complete|Description of Complete
    {"GetId", PyIBackgroundCopyJob::GetId, 1},              // @pymeth GetId|Description of GetId
    {"GetType", PyIBackgroundCopyJob::GetType, 1},          // @pymeth GetType|Description of GetType
    {"GetProgress", PyIBackgroundCopyJob::GetProgress, 1},  // @pymeth GetProgress|Description of GetProgress
    {"GetTimes", PyIBackgroundCopyJob::GetTimes, 1},        // @pymeth GetTimes|Description of GetTimes
    {"GetState", PyIBackgroundCopyJob::GetState, 1},        // @pymeth GetState|Description of GetState
    {"GetError", PyIBackgroundCopyJob::GetError, 1},        // @pymeth GetError|Description of GetError
    {"GetOwner", PyIBackgroundCopyJob::GetOwner, 1},        // @pymeth GetOwner|Description of GetOwner
    {"SetDisplayName", PyIBackgroundCopyJob::SetDisplayName,
     1},  // @pymeth SetDisplayName|Description of SetDisplayName
    {"GetDisplayName", PyIBackgroundCopyJob::GetDisplayName,
     1},  // @pymeth GetDisplayName|Description of GetDisplayName
    {"SetDescription", PyIBackgroundCopyJob::SetDescription,
     1},  // @pymeth SetDescription|Description of SetDescription
    {"GetDescription", PyIBackgroundCopyJob::GetDescription,
     1},                                                    // @pymeth GetDescription|Description of GetDescription
    {"SetPriority", PyIBackgroundCopyJob::SetPriority, 1},  // @pymeth SetPriority|Description of SetPriority
    {"GetPriority", PyIBackgroundCopyJob::GetPriority, 1},  // @pymeth GetPriority|Description of GetPriority
    {"SetNotifyFlags", PyIBackgroundCopyJob::SetNotifyFlags,
     1},  // @pymeth SetNotifyFlags|Description of SetNotifyFlags
    {"GetNotifyFlags", PyIBackgroundCopyJob::GetNotifyFlags,
     1},  // @pymeth GetNotifyFlags|Description of GetNotifyFlags
    {"SetNotifyInterface", PyIBackgroundCopyJob::SetNotifyInterface,
     1},  // @pymeth SetNotifyInterface|Description of SetNotifyInterface
    {"GetNotifyInterface", PyIBackgroundCopyJob::GetNotifyInterface,
     1},  // @pymeth GetNotifyInterface|Description of GetNotifyInterface
    {"SetMinimumRetryDelay", PyIBackgroundCopyJob::SetMinimumRetryDelay,
     1},  // @pymeth SetMinimumRetryDelay|Description of SetMinimumRetryDelay
    {"GetMinimumRetryDelay", PyIBackgroundCopyJob::GetMinimumRetryDelay,
     1},  // @pymeth GetMinimumRetryDelay|Description of GetMinimumRetryDelay
    {"SetNoProgressTimeout", PyIBackgroundCopyJob::SetNoProgressTimeout,
     1},  // @pymeth SetNoProgressTimeout|Description of SetNoProgressTimeout
    {"GetNoProgressTimeout", PyIBackgroundCopyJob::GetNoProgressTimeout,
     1},  // @pymeth GetNoProgressTimeout|Description of GetNoProgressTimeout
    {"GetErrorCount", PyIBackgroundCopyJob::GetErrorCount, 1},  // @pymeth GetErrorCount|Description of GetErrorCount
    {"SetProxySettings", PyIBackgroundCopyJob::SetProxySettings,
     1},  // @pymeth SetProxySettings|Description of SetProxySettings
    {"GetProxySettings", PyIBackgroundCopyJob::GetProxySettings,
     1},  // @pymeth GetProxySettings|Description of GetProxySettings
    {"TakeOwnership", PyIBackgroundCopyJob::TakeOwnership, 1},  // @pymeth TakeOwnership|Description of TakeOwnership
    {NULL}};

PyComTypeObject PyIBackgroundCopyJob::type("PyIBackgroundCopyJob", &PyIUnknown::type, sizeof(PyIBackgroundCopyJob),
                                           PyIBackgroundCopyJob_methods, GET_PYCOM_CTOR(PyIBackgroundCopyJob));