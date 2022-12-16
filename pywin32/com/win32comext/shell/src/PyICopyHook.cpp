// This file implements the ICopyHookA and ICopyHookW interfaces and
// Gateways for Python.
// Generated by makegw.py

#include "shell_pch.h"
#include "PyICopyHook.h"

// @doc - This file contains autoduck documentation
// ---------------------------------------------------
//
// Interface Implementation

PyICopyHookA::PyICopyHookA(IUnknown *pdisp) : PyIUnknown(pdisp) { ob_type = &type; }

PyICopyHookA::~PyICopyHookA() {}

/* static */ ICopyHookA *PyICopyHookA::GetI(PyObject *self) { return (ICopyHookA *)PyIUnknown::GetI(self); }

// @pymethod |PyICopyHookA|CopyCallback|Description of CopyCallback.
PyObject *PyICopyHookA::CopyCallback(PyObject *self, PyObject *args)
{
    ICopyHookA *pICH = GetI(self);
    if (pICH == NULL)
        return NULL;
    // @pyparm HWND|hwnd||Description for hwnd
    // @pyparm int|wFunc||Description for wFunc
    // @pyparm int|wFlags||Description for wFlags
    // @pyparm string/<o unicode>|srcFile||Description for srcFile
    // @pyparm int|srcAttribs||Description for srcAttribs
    // @pyparm string/<o unicode>|destFile||Description for destFile
    // @pyparm int|destAttribs||Description for destAttribs
    PyObject *obsrcFile;
    PyObject *obdestFile;
    HWND hwnd;
    PyObject *obhwnd;
    UINT wFunc;
    UINT wFlags;
    LPSTR srcFile;
    DWORD srcAttribs;
    LPSTR destFile;
    DWORD destAttribs;
    if (!PyArg_ParseTuple(args, "OiiOlOl:CopyCallback", &obhwnd, &wFunc, &wFlags, &obsrcFile, &srcAttribs, &obdestFile,
                          &destAttribs))
        return NULL;
    if (!PyWinObject_AsHANDLE(obhwnd, (HANDLE *)&hwnd))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (bPythonIsHappy && !PyWinObject_AsString(obsrcFile, &srcFile))
        bPythonIsHappy = FALSE;
    if (bPythonIsHappy && !PyWinObject_AsString(obdestFile, &destFile))
        bPythonIsHappy = FALSE;
    if (!bPythonIsHappy)
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pICH->CopyCallback(hwnd, wFunc, wFlags, srcFile, srcAttribs, destFile, destAttribs);
    PyWinObject_FreeString(srcFile);
    PyWinObject_FreeString(destFile);

    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pICH, IID_IShellCopyHook);
    Py_INCREF(Py_None);
    return Py_None;
}

// @object PyICopyHookA|Description of the interface
static struct PyMethodDef PyICopyHookA_methods[] = {
    {"CopyCallback", PyICopyHookA::CopyCallback, 1},  // @pymeth CopyCallback|Description of CopyCallback
    {NULL}};

PyComTypeObject PyICopyHookA::type("PyICopyHookA", &PyIUnknown::type, sizeof(PyICopyHookA), PyICopyHookA_methods,
                                   GET_PYCOM_CTOR(PyICopyHookA));
// ---------------------------------------------------
//
// Gateway Implementation
STDMETHODIMP_(UINT)
PyGCopyHookA::CopyCallback(
    /* [unique][in] */ HWND hwnd,
    /* [unique][in] */ UINT wFunc,
    /* [unique][in] */ UINT wFlags,
    /* [unique][in] */ LPCSTR srcFile,
    /* [unique][in] */ DWORD srcAttribs,
    /* [unique][in] */ LPCSTR destFile,
    /* [unique][in] */ DWORD destAttribs)
{
    PY_GATEWAY_METHOD;
    PyObject *result;
    HRESULT hr = InvokeViaPolicy("CopyCallback", &result, "Niizlzl", PyWinLong_FromHANDLE(hwnd), wFunc, wFlags, srcFile,
                                 srcAttribs, destFile, destAttribs);
    if (FAILED(hr))
        return hr;
    hr = PyLong_AsLong(result);
    if ((hr == -1) && PyErr_Occurred())
        hr = MAKE_PYCOM_GATEWAY_FAILURE_CODE("CopyCallBack");
    Py_DECREF(result);
    return hr;
}

// ICopyHookW
PyICopyHookW::PyICopyHookW(IUnknown *pdisp) : PyIUnknown(pdisp) { ob_type = &type; }

PyICopyHookW::~PyICopyHookW() {}

/* static */ ICopyHookW *PyICopyHookW::GetI(PyObject *self) { return (ICopyHookW *)PyIUnknown::GetI(self); }

// @pymethod |PyICopyHookW|CopyCallback|Description of CopyCallback.
PyObject *PyICopyHookW::CopyCallback(PyObject *self, PyObject *args)
{
    ICopyHookW *pICH = GetI(self);
    if (pICH == NULL)
        return NULL;
    // @pyparm HWND|hwnd||Description for hwnd
    // @pyparm int|wFunc||Description for wFunc
    // @pyparm int|wFlags||Description for wFlags
    // @pyparm string/<o unicode>|srcFile||Description for srcFile
    // @pyparm int|srcAttribs||Description for srcAttribs
    // @pyparm string/<o unicode>|destFile||Description for destFile
    // @pyparm int|destAttribs||Description for destAttribs
    PyObject *obsrcFile;
    PyObject *obdestFile;
    HWND hwnd;
    PyObject *obhwnd;
    UINT wFunc;
    UINT wFlags;
    LPWSTR srcFile;
    DWORD srcAttribs;
    LPWSTR destFile;
    DWORD destAttribs;
    if (!PyArg_ParseTuple(args, "OiiOlOl:CopyCallback", &obhwnd, &wFunc, &wFlags, &obsrcFile, &srcAttribs, &obdestFile,
                          &destAttribs))
        return NULL;
    if (!PyWinObject_AsHANDLE(obhwnd, (HANDLE *)&hwnd))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (bPythonIsHappy && !PyWinObject_AsWCHAR(obsrcFile, &srcFile))
        bPythonIsHappy = FALSE;
    if (bPythonIsHappy && !PyWinObject_AsWCHAR(obdestFile, &destFile))
        bPythonIsHappy = FALSE;
    if (!bPythonIsHappy)
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pICH->CopyCallback(hwnd, wFunc, wFlags, srcFile, srcAttribs, destFile, destAttribs);
    PyWinObject_FreeWCHAR(srcFile);
    PyWinObject_FreeWCHAR(destFile);

    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pICH, IID_IShellCopyHook);
    Py_INCREF(Py_None);
    return Py_None;
}

// @object PyICopyHookW|Description of the interface
static struct PyMethodDef PyICopyHookW_methods[] = {
    {"CopyCallback", PyICopyHookW::CopyCallback, 1},  // @pymeth CopyCallback|Description of CopyCallback
    {NULL}};

PyComTypeObject PyICopyHookW::type("PyICopyHookW", &PyIUnknown::type, sizeof(PyICopyHookW), PyICopyHookW_methods,
                                   GET_PYCOM_CTOR(PyICopyHookW));
// ---------------------------------------------------
//
// Gateway Implementation
STDMETHODIMP_(UINT)
PyGCopyHookW::CopyCallback(
    /* [unique][in] */ HWND hwnd,
    /* [unique][in] */ UINT wFunc,
    /* [unique][in] */ UINT wFlags,
    /* [unique][in] */ LPCWSTR srcFile,
    /* [unique][in] */ DWORD srcAttribs,
    /* [unique][in] */ LPCWSTR destFile,
    /* [unique][in] */ DWORD destAttribs)
{
    PY_GATEWAY_METHOD;
    PyObject *result;
    HRESULT hr =
        InvokeViaPolicy("CopyCallback", &result, "NiiNlNl", PyWinLong_FromHANDLE(hwnd), wFunc, wFlags,
                        PyWinObject_FromWCHAR(srcFile), srcAttribs, PyWinObject_FromWCHAR(destFile), destAttribs);
    if (FAILED(hr))
        return hr;
    hr = PyLong_AsLong(result);
    if ((hr == -1) && PyErr_Occurred())
        hr = MAKE_PYCOM_GATEWAY_FAILURE_CODE("CopyCallBack");
    Py_DECREF(result);
    return hr;
}
