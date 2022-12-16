// This file implements the IExplorerBrowser Interface and Gateway for Python.
// Generated by makegw.py

#include "shell_pch.h"
#include "PyIExplorerBrowser.h"

// @doc - This file contains autoduck documentation
// ---------------------------------------------------
//
// Interface Implementation

PyIExplorerBrowser::PyIExplorerBrowser(IUnknown *pdisp) : PyIUnknown(pdisp) { ob_type = &type; }

PyIExplorerBrowser::~PyIExplorerBrowser() {}

/* static */ IExplorerBrowser *PyIExplorerBrowser::GetI(PyObject *self)
{
    return (IExplorerBrowser *)PyIUnknown::GetI(self);
}

// @pymethod |PyIExplorerBrowser|Initialize|Description of Initialize.
PyObject *PyIExplorerBrowser::Initialize(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    // @pyparm HWND|hwndParent||Description for hwndParent
    RECT rc;
    PyObject *obprc;
    // @pyparm <o PyRECT>|prc||Description for prc
    FOLDERSETTINGS fs;
    PyObject *obpfs;
    // @pyparm <o PyFOLDERSETTINGS>|pfs||Description for pfs
    HWND hwndParent;
    PyObject *obhwnd;
    if (!PyArg_ParseTuple(args, "OOO:Initialize", &obhwnd, &obprc, &obpfs))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (bPythonIsHappy && !PyWinObject_AsHANDLE(obhwnd, (HANDLE *)&hwndParent))
        bPythonIsHappy = FALSE;
    if (bPythonIsHappy && !PyWinObject_AsRECT(obprc, &rc))
        bPythonIsHappy = FALSE;
    if (bPythonIsHappy && !PyObject_AsFOLDERSETTINGS(obpfs, &fs))
        bPythonIsHappy = FALSE;
    if (!bPythonIsHappy)
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->Initialize(hwndParent, &rc, &fs);
    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIExplorerBrowser|Destroy|Description of Destroy.
PyObject *PyIExplorerBrowser::Destroy(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":Destroy"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->Destroy();

    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod <o PyHANDLE>|PyIExplorerBrowser|SetRect|Description of SetRect.
PyObject *PyIExplorerBrowser::SetRect(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    HDWP hdwp;
    PyObject *obphdwp;
    // @pyparm <o PyHDWP>|hdwp||Description for phdwp
    RECT rcBrowser;
    PyObject *obrcBrowser;
    // @pyparm <o PyRECT>|rcBrowser||Description for rcBrowser
    if (!PyArg_ParseTuple(args, "OO:SetRect", &obphdwp, &obrcBrowser))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (bPythonIsHappy && !PyWinObject_AsHANDLE(obphdwp, &hdwp))
        bPythonIsHappy = FALSE;
    if (bPythonIsHappy && !PyWinObject_AsRECT(obrcBrowser, &rcBrowser))
        bPythonIsHappy = FALSE;
    if (!bPythonIsHappy)
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->SetRect(&hdwp, rcBrowser);
    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    return PyWinLong_FromHANDLE(hdwp);
}

// @pymethod |PyIExplorerBrowser|SetPropertyBag|Description of SetPropertyBag.
PyObject *PyIExplorerBrowser::SetPropertyBag(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    // @pyparm str|PropertyBag||Description for pszPropertyBag
    PyObject *obPropertyBag;
    TmpWCHAR PropertyBag;
    if (!PyArg_ParseTuple(args, "O:SetPropertyBag", &obPropertyBag))
        return NULL;
    if (!PyWinObject_AsWCHAR(obPropertyBag, &PropertyBag))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->SetPropertyBag(PropertyBag);
    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIExplorerBrowser|SetEmptyText|Description of SetEmptyText.
PyObject *PyIExplorerBrowser::SetEmptyText(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    // @pyparm str|EmptyText||Description for pszEmptyText
    PyObject *obEmptyText;
    TmpWCHAR EmptyText;
    if (!PyArg_ParseTuple(args, "O:SetEmptyText", &obEmptyText))
        return NULL;

    if (!PyWinObject_AsWCHAR(obEmptyText, &EmptyText))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->SetEmptyText(EmptyText);
    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIExplorerBrowser|SetFolderSettings|Description of SetFolderSettings.
PyObject *PyIExplorerBrowser::SetFolderSettings(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    FOLDERSETTINGS fs;
    PyObject *obpfs;
    // @pyparm <o PyFOLDERSETTINGS>|pfs||Description for pfs
    if (!PyArg_ParseTuple(args, "O:SetFolderSettings", &obpfs))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (bPythonIsHappy && !PyObject_AsFOLDERSETTINGS(obpfs, &fs))
        bPythonIsHappy = FALSE;
    if (!bPythonIsHappy)
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->SetFolderSettings(&fs);
    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod int|PyIExplorerBrowser|Advise|Description of Advise.
PyObject *PyIExplorerBrowser::Advise(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    // @pyparm <o PyIExplorerBrowserEvents>|psbe||Description for psbe
    PyObject *obpsbe;
    IExplorerBrowserEvents *psbe;
    if (!PyArg_ParseTuple(args, "O:Advise", &obpsbe))
        return NULL;
    if (!PyCom_InterfaceFromPyInstanceOrObject(obpsbe, IID_IExplorerBrowserEvents, (void **)&psbe, TRUE /* bNoneOK */))
        return NULL;
    HRESULT hr;
    DWORD dwCookie;
    PY_INTERFACE_PRECALL;
    hr = pIEB->Advise(psbe, &dwCookie);
    if (psbe)
        psbe->Release();
    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    return PyLong_FromLong(dwCookie);
}

// @pymethod |PyIExplorerBrowser|Unadvise|Description of Unadvise.
PyObject *PyIExplorerBrowser::Unadvise(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    // @pyparm int|dwCookie||Description for dwCookie
    DWORD dwCookie;
    if (!PyArg_ParseTuple(args, "l:Unadvise", &dwCookie))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->Unadvise(dwCookie);

    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIExplorerBrowser|SetOptions|Description of SetOptions.
PyObject *PyIExplorerBrowser::SetOptions(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    EXPLORER_BROWSER_OPTIONS dwFlag;
    PyObject *obdwFlag;
    // @pyparm <o PyEXPLORER_BROWSER_OPTIONS>|dwFlag||Description for dwFlag
    if (!PyArg_ParseTuple(args, "O:SetOptions", &obdwFlag))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (bPythonIsHappy && !PyObject_AsEXPLORER_BROWSER_OPTIONS(obdwFlag, &dwFlag))
        bPythonIsHappy = FALSE;
    if (!bPythonIsHappy)
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->SetOptions(dwFlag);
    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod int|PyIExplorerBrowser|GetOptions|Description of GetOptions.
PyObject *PyIExplorerBrowser::GetOptions(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    EXPLORER_BROWSER_OPTIONS dwFlag;
    if (!PyArg_ParseTuple(args, ":GetOptions"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->GetOptions(&dwFlag);
    PY_INTERFACE_POSTCALL;
    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    return PyLong_FromUnsignedLong(dwFlag);
}

// @pymethod |PyIExplorerBrowser|BrowseToIDList|Description of BrowseToIDList.
PyObject *PyIExplorerBrowser::BrowseToIDList(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    PCUIDLIST_RELATIVE pidl;
    PyObject *obpidl;
    // @pyparm <o PyPCUIDLIST_RELATIVE>|pidl||Description for pidl
    // @pyparm int|uFlags||Description for uFlags
    UINT uFlags;
    if (!PyArg_ParseTuple(args, "Oi:BrowseToIDList", &obpidl, &uFlags))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (bPythonIsHappy && !PyObject_AsPCUIDLIST_RELATIVE(obpidl, &pidl, TRUE))
        bPythonIsHappy = FALSE;
    if (!bPythonIsHappy)
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->BrowseToIDList(pidl, uFlags);
    PY_INTERFACE_POSTCALL;
    PyObject_FreePCUIDLIST_RELATIVE(pidl);

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIExplorerBrowser|BrowseToObject|Description of BrowseToObject.
PyObject *PyIExplorerBrowser::BrowseToObject(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    // @pyparm <o PyIUnknown>|punk||Description for punk
    // @pyparm int|uFlags||Description for uFlags
    PyObject *obpunk;
    IUnknown *punk;
    UINT uFlags;
    if (!PyArg_ParseTuple(args, "Oi:BrowseToObject", &obpunk, &uFlags))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (bPythonIsHappy &&
        !PyCom_InterfaceFromPyInstanceOrObject(obpunk, IID_IUnknown, (void **)&punk, TRUE /* bNoneOK */))
        bPythonIsHappy = FALSE;
    if (!bPythonIsHappy)
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->BrowseToObject(punk, uFlags);
    if (punk)
        punk->Release();

    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIExplorerBrowser|FillFromObject|Description of FillFromObject.
PyObject *PyIExplorerBrowser::FillFromObject(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    // @pyparm <o PyIUnknown>|punk||Description for punk
    EXPLORER_BROWSER_FILL_FLAGS dwFlags;
    PyObject *obdwFlags;
    // @pyparm <o PyEXPLORER_BROWSER_FILL_FLAGS>|dwFlags||Description for dwFlags
    PyObject *obpunk;
    IUnknown *punk;
    if (!PyArg_ParseTuple(args, "OO:FillFromObject", &obpunk, &obdwFlags))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (bPythonIsHappy &&
        !PyCom_InterfaceFromPyInstanceOrObject(obpunk, IID_IUnknown, (void **)&punk, TRUE /* bNoneOK */))
        bPythonIsHappy = FALSE;
    if (bPythonIsHappy && !PyObject_AsEXPLORER_BROWSER_FILL_FLAGS(obdwFlags, &dwFlags))
        bPythonIsHappy = FALSE;
    if (!bPythonIsHappy)
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->FillFromObject(punk, dwFlags);
    if (punk)
        punk->Release();
    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod |PyIExplorerBrowser|RemoveAll|Description of RemoveAll.
PyObject *PyIExplorerBrowser::RemoveAll(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    if (!PyArg_ParseTuple(args, ":RemoveAll"))
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->RemoveAll();

    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    Py_INCREF(Py_None);
    return Py_None;
}

// @pymethod <o PyIUnknown>|PyIExplorerBrowser|GetCurrentView|Description of GetCurrentView.
PyObject *PyIExplorerBrowser::GetCurrentView(PyObject *self, PyObject *args)
{
    IExplorerBrowser *pIEB = GetI(self);
    if (pIEB == NULL)
        return NULL;
    // @pyparm <o PyIID>|riid||Description for riid
    PyObject *obriid;
    IID riid;
    void *ppv;
    if (!PyArg_ParseTuple(args, "O:GetCurrentView", &obriid))
        return NULL;
    BOOL bPythonIsHappy = TRUE;
    if (!PyWinObject_AsIID(obriid, &riid))
        bPythonIsHappy = FALSE;
    if (!bPythonIsHappy)
        return NULL;
    HRESULT hr;
    PY_INTERFACE_PRECALL;
    hr = pIEB->GetCurrentView(riid, &ppv);
    PY_INTERFACE_POSTCALL;

    if (FAILED(hr))
        return PyCom_BuildPyException(hr, pIEB, IID_IExplorerBrowser);
    return PyCom_PyObjectFromIUnknown((IUnknown *)ppv, riid, FALSE);
}

// @object PyIExplorerBrowser|Description of the interface
static struct PyMethodDef PyIExplorerBrowser_methods[] = {
    {"Initialize", PyIExplorerBrowser::Initialize, 1},          // @pymeth Initialize|Description of Initialize
    {"Destroy", PyIExplorerBrowser::Destroy, 1},                // @pymeth Destroy|Description of Destroy
    {"SetRect", PyIExplorerBrowser::SetRect, 1},                // @pymeth SetRect|Description of SetRect
    {"SetPropertyBag", PyIExplorerBrowser::SetPropertyBag, 1},  // @pymeth SetPropertyBag|Description of SetPropertyBag
    {"SetEmptyText", PyIExplorerBrowser::SetEmptyText, 1},      // @pymeth SetEmptyText|Description of SetEmptyText
    {"SetFolderSettings", PyIExplorerBrowser::SetFolderSettings,
     1},                                                // @pymeth SetFolderSettings|Description of SetFolderSettings
    {"Advise", PyIExplorerBrowser::Advise, 1},          // @pymeth Advise|Description of Advise
    {"Unadvise", PyIExplorerBrowser::Unadvise, 1},      // @pymeth Unadvise|Description of Unadvise
    {"SetOptions", PyIExplorerBrowser::SetOptions, 1},  // @pymeth SetOptions|Description of SetOptions
    {"GetOptions", PyIExplorerBrowser::GetOptions, 1},  // @pymeth GetOptions|Description of GetOptions
    {"BrowseToIDList", PyIExplorerBrowser::BrowseToIDList, 1},  // @pymeth BrowseToIDList|Description of BrowseToIDList
    {"BrowseToObject", PyIExplorerBrowser::BrowseToObject, 1},  // @pymeth BrowseToObject|Description of BrowseToObject
    {"FillFromObject", PyIExplorerBrowser::FillFromObject, 1},  // @pymeth FillFromObject|Description of FillFromObject
    {"RemoveAll", PyIExplorerBrowser::RemoveAll, 1},            // @pymeth RemoveAll|Description of RemoveAll
    {"GetCurrentView", PyIExplorerBrowser::GetCurrentView, 1},  // @pymeth GetCurrentView|Description of GetCurrentView
    {NULL}};

PyComTypeObject PyIExplorerBrowser::type("PyIExplorerBrowser", &PyIUnknown::type, sizeof(PyIExplorerBrowser),
                                         PyIExplorerBrowser_methods, GET_PYCOM_CTOR(PyIExplorerBrowser));
