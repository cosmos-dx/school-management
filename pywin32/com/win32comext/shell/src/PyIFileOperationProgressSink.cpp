// This file implements the IFileOperationProgressSink Gateway for Python.
// Generated by makegw.py

#include "shell_pch.h"
#include "PyIFileOperationProgressSink.h"

// @doc - This file contains autoduck documentation
// ---------------------------------------------------
//
// Gateway Implementation
// @pymethod |PyGFileOperationProgressSink|StartOperations|Called as operation begins, before any modifications are done
STDMETHODIMP PyGFileOperationProgressSink::StartOperations(void)
{
    PY_GATEWAY_METHOD;
    HRESULT hr = InvokeViaPolicy("StartOperations", NULL);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|FinishOperations|Called after all actions have been performed
// @pyparm int|Result||HRESULT of last operation performed
STDMETHODIMP PyGFileOperationProgressSink::FinishOperations(
    /* [in] */ HRESULT hrResult)
{
    PY_GATEWAY_METHOD;
    HRESULT hr = InvokeViaPolicy("FinishOperations", NULL, "l", hrResult);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|PreRenameItem|Called before each file rename
// @pyparm int|Flags||Flags specifying copy behaviour, combination of shellcon.TSF_* flags
// @pyparm <o PyIShellItem>|Item||Shell interface of the copied item
// @pyparm str|NewName||New display name of the item
STDMETHODIMP PyGFileOperationProgressSink::PreRenameItem(
    /* [in] */ DWORD dwFlags,
    /* [in] */ IShellItem *psiItem,
    /* [string][unique][in] */ LPCWSTR pszNewName)
{
    PY_GATEWAY_METHOD;
    PyObject *obpsiItem;
    PyObject *obpszNewName;
    obpsiItem = PyCom_PyObjectFromIUnknown(psiItem, IID_IShellItem, TRUE);
    obpszNewName = PyWinObject_FromWCHAR(pszNewName);
    HRESULT hr = InvokeViaPolicy("PreRenameItem", NULL, "kOO", dwFlags, obpsiItem, obpszNewName);
    Py_XDECREF(obpsiItem);
    Py_XDECREF(obpszNewName);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|PostRenameItem|Called after each file rename
// @pyparm int|Flags||Flags specifying rename behaviour, combination of shellcon.TSF_* flags
// @pyparm <o PyIShellItem>|Item||Shell interface of item before rename
// @pyparm str|NewName||The new name of the item, may be mangled to resolve filename conflicts
// @pyparm int|hrRename||HRESULT of the rename operation
// @pyparm <o PyIShellItem>|NewlyCreated||Shell interface of the item after rename
STDMETHODIMP PyGFileOperationProgressSink::PostRenameItem(
    /* [in] */ DWORD dwFlags,
    /* [in] */ IShellItem *psiItem,
    /* [string][in] */ LPCWSTR pszNewName,
    /* [in] */ HRESULT hrRename,
    /* [in] */ IShellItem *psiNewlyCreated)
{
    PY_GATEWAY_METHOD;
    PyObject *obpsiItem;
    PyObject *obpszNewName;
    PyObject *obpsiNewlyCreated;
    obpsiItem = PyCom_PyObjectFromIUnknown(psiItem, IID_IShellItem, TRUE);
    obpszNewName = PyWinObject_FromWCHAR(pszNewName);
    obpsiNewlyCreated = PyCom_PyObjectFromIUnknown(psiNewlyCreated, IID_IShellItem, TRUE);
    HRESULT hr =
        InvokeViaPolicy("PostRenameItem", NULL, "kOOlO", dwFlags, obpsiItem, obpszNewName, hrRename, obpsiNewlyCreated);
    Py_XDECREF(obpsiItem);
    Py_XDECREF(obpszNewName);
    Py_XDECREF(obpsiNewlyCreated);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|PreMoveItem|Called before each move operation
// @pyparm int|Flags||Flags specifying move behaviour, combination of shellcon.TSF_* flags
// @pyparm <o PyIShellItem>|Item||The item to be moved
// @pyparm <o PyIShellItem>|DestinationFolder||The folder into which it will be moved
// @pyparm str|NewName||Name of moved item, may be None if not to be changed
STDMETHODIMP PyGFileOperationProgressSink::PreMoveItem(
    /* [in] */ DWORD dwFlags,
    /* [in] */ IShellItem *psiItem,
    /* [in] */ IShellItem *psiDestinationFolder,
    /* [string][unique][in] */ LPCWSTR pszNewName)
{
    PY_GATEWAY_METHOD;
    PyObject *obpsiItem;
    PyObject *obpsiDestinationFolder;
    PyObject *obpszNewName;
    obpsiItem = PyCom_PyObjectFromIUnknown(psiItem, IID_IShellItem, TRUE);
    obpsiDestinationFolder = PyCom_PyObjectFromIUnknown(psiDestinationFolder, IID_IShellItem, TRUE);
    obpszNewName = PyWinObject_FromWCHAR(pszNewName);
    HRESULT hr = InvokeViaPolicy("PreMoveItem", NULL, "kOOO", dwFlags, obpsiItem, obpsiDestinationFolder, obpszNewName);
    Py_XDECREF(obpsiItem);
    Py_XDECREF(obpsiDestinationFolder);
    Py_XDECREF(obpszNewName);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|PostMoveItem|Called after each move operation
// @pyparm int|Flags||Flags specifying move behaviour, combination of shellcon.TSF_* flags
// @pyparm <o PyIShellItem>|Item||Interface of the item before it was moved
// @pyparm <o PyIShellItem>|DestinationFolder||The folder into which it was moved
// @pyparm str|NewName||Name of item in its new location, may be mangled in case of conflict
// @pyparm int|hrMove||HRESULT of the move operation
// @pyparm <o PyIShellItem>|NewlyCreated||Shell interface of the item in its new location
STDMETHODIMP PyGFileOperationProgressSink::PostMoveItem(
    /* [in] */ DWORD dwFlags,
    /* [in] */ IShellItem *psiItem,
    /* [in] */ IShellItem *psiDestinationFolder,
    /* [string][unique][in] */ LPCWSTR pszNewName,
    /* [in] */ HRESULT hrMove,
    /* [in] */ IShellItem *psiNewlyCreated)
{
    PY_GATEWAY_METHOD;
    PyObject *obpsiItem;
    PyObject *obpsiDestinationFolder;
    PyObject *obpszNewName;
    PyObject *obpsiNewlyCreated;
    obpsiItem = PyCom_PyObjectFromIUnknown(psiItem, IID_IShellItem, TRUE);
    obpsiDestinationFolder = PyCom_PyObjectFromIUnknown(psiDestinationFolder, IID_IShellItem, TRUE);
    obpszNewName = PyWinObject_FromWCHAR(pszNewName);
    obpsiNewlyCreated = PyCom_PyObjectFromIUnknown(psiNewlyCreated, IID_IShellItem, TRUE);
    HRESULT hr = InvokeViaPolicy("PostMoveItem", NULL, "kOOOlO", dwFlags, obpsiItem, obpsiDestinationFolder,
                                 obpszNewName, hrMove, obpsiNewlyCreated);
    Py_XDECREF(obpsiItem);
    Py_XDECREF(obpsiDestinationFolder);
    Py_XDECREF(obpszNewName);
    Py_XDECREF(obpsiNewlyCreated);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|PreCopyItem|Called before each copy operation
// @pyparm int|Flags||Flags specifying copy behaviour, combination of shellcon.TSF_* flags
// @pyparm <o PyIShellItem>|Item||The item to be copied
// @pyparm <o PyIShellItem>|DestinationFolder||Folder into which it will be copied
// @pyparm str|NewName||Name to be given to the copy, will be None if keeping original name
STDMETHODIMP PyGFileOperationProgressSink::PreCopyItem(
    /* [in] */ DWORD dwFlags,
    /* [in] */ IShellItem *psiItem,
    /* [in] */ IShellItem *psiDestinationFolder,
    /* [string][unique][in] */ LPCWSTR pszNewName)
{
    PY_GATEWAY_METHOD;
    PyObject *obpsiItem;
    PyObject *obpsiDestinationFolder;
    PyObject *obpszNewName;
    obpsiItem = PyCom_PyObjectFromIUnknown(psiItem, IID_IShellItem, TRUE);
    obpsiDestinationFolder = PyCom_PyObjectFromIUnknown(psiDestinationFolder, IID_IShellItem, TRUE);
    obpszNewName = PyWinObject_FromWCHAR(pszNewName);
    HRESULT hr = InvokeViaPolicy("PreCopyItem", NULL, "kOOO", dwFlags, obpsiItem, obpsiDestinationFolder, obpszNewName);
    Py_XDECREF(obpsiItem);
    Py_XDECREF(obpsiDestinationFolder);
    Py_XDECREF(obpszNewName);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|PostCopyItem|Called after each copy operation
// @pyparm int|Flags||Flags specifying copy behaviour, combination of shellcon.TSF_* flags
// @pyparm <o PyIShellItem>|Item||The original item
// @pyparm <o PyIShellItem>|DestinationFolder||Folder into which it was copied
// @pyparm str|NewName||Name of item after copy, may be mangled in case of name conflict
// @pyparm int|hrCopy||HRESULT of the copy operation
// @pyparm <o PyIShellItem>|NewlyCreated||Shell interface of the copy
STDMETHODIMP PyGFileOperationProgressSink::PostCopyItem(
    /* [in] */ DWORD dwFlags,
    /* [in] */ IShellItem *psiItem,
    /* [in] */ IShellItem *psiDestinationFolder,
    /* [string][unique][in] */ LPCWSTR pszNewName,
    /* [in] */ HRESULT hrCopy,
    /* [in] */ IShellItem *psiNewlyCreated)
{
    PY_GATEWAY_METHOD;
    PyObject *obpsiItem;
    PyObject *obpsiDestinationFolder;
    PyObject *obpszNewName;
    PyObject *obpsiNewlyCreated;
    obpsiItem = PyCom_PyObjectFromIUnknown(psiItem, IID_IShellItem, TRUE);
    obpsiDestinationFolder = PyCom_PyObjectFromIUnknown(psiDestinationFolder, IID_IShellItem, TRUE);
    obpszNewName = PyWinObject_FromWCHAR(pszNewName);
    obpsiNewlyCreated = PyCom_PyObjectFromIUnknown(psiNewlyCreated, IID_IShellItem, TRUE);
    HRESULT hr = InvokeViaPolicy("PostCopyItem", NULL, "kOOOlO", dwFlags, obpsiItem, obpsiDestinationFolder,
                                 obpszNewName, hrCopy, obpsiNewlyCreated);
    Py_XDECREF(obpsiItem);
    Py_XDECREF(obpsiDestinationFolder);
    Py_XDECREF(obpszNewName);
    Py_XDECREF(obpsiNewlyCreated);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|PreDeleteItem|Called before each delete operation
// @pyparm int|Flags||Flags specifying delete behaviour, combination of shellcon.TSF_* flags
// @pyparm <o PyIShellItem>|Item||Item to be deleted
STDMETHODIMP PyGFileOperationProgressSink::PreDeleteItem(
    /* [in] */ DWORD dwFlags,
    /* [in] */ IShellItem *psiItem)
{
    PY_GATEWAY_METHOD;
    PyObject *obpsiItem;
    obpsiItem = PyCom_PyObjectFromIUnknown(psiItem, IID_IShellItem, TRUE);
    HRESULT hr = InvokeViaPolicy("PreDeleteItem", NULL, "kO", dwFlags, obpsiItem);
    Py_XDECREF(obpsiItem);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|PostDeleteItem|Called after each delete operation
// @pyparm int|Flags||Flags specifying delete behaviour, combination of shellcon.TSF_* flags
// @pyparm <o PyIShellItem>|Item||Item that was deleted
// @pyparm int|hrDelete||HRESULT of the delete operation
// @pyparm <o PyIShellItem>|NewlyCreated||Item in the recycle bin, or None if deleted without recycling
STDMETHODIMP PyGFileOperationProgressSink::PostDeleteItem(
    /* [in] */ DWORD dwFlags,
    /* [in] */ IShellItem *psiItem,
    /* [in] */ HRESULT hrDelete,
    /* [in] */ IShellItem *psiNewlyCreated)
{
    PY_GATEWAY_METHOD;
    PyObject *obpsiItem;
    PyObject *obpsiNewlyCreated;
    obpsiItem = PyCom_PyObjectFromIUnknown(psiItem, IID_IShellItem, TRUE);
    obpsiNewlyCreated = PyCom_PyObjectFromIUnknown(psiNewlyCreated, IID_IShellItem, TRUE);
    HRESULT hr = InvokeViaPolicy("PostDeleteItem", NULL, "kOlO", dwFlags, obpsiItem, hrDelete, obpsiNewlyCreated);
    Py_XDECREF(obpsiItem);
    Py_XDECREF(obpsiNewlyCreated);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|PreNewItem|Called before each new file is created
// @pyparm int|Flags||Flags specifying creation behaviour, combination of shellcon.TSF_* flags
// @pyparm <o PyIShellItem>|DestinationFolder||Folder where item will be created
// @pyparm str|NewName||Name of item to be created
STDMETHODIMP PyGFileOperationProgressSink::PreNewItem(
    /* [in] */ DWORD dwFlags,
    /* [in] */ IShellItem *psiDestinationFolder,
    /* [string][unique][in] */ LPCWSTR pszNewName)
{
    PY_GATEWAY_METHOD;
    PyObject *obpsiDestinationFolder;
    PyObject *obpszNewName;
    obpsiDestinationFolder = PyCom_PyObjectFromIUnknown(psiDestinationFolder, IID_IShellItem, TRUE);
    obpszNewName = PyWinObject_FromWCHAR(pszNewName);
    HRESULT hr = InvokeViaPolicy("PreNewItem", NULL, "kOO", dwFlags, obpsiDestinationFolder, obpszNewName);
    Py_XDECREF(obpsiDestinationFolder);
    Py_XDECREF(obpszNewName);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|PostNewItem|Called after each new file is created
// @pyparm int|Flags||Flags specifying creation behaviour, combination of shellcon.TSF_* flags
// @pyparm <o PyIShellItem>|DestinationFolder||Folder in which item was created
// @pyparm str|NewName||Name of created item, may be mangled if file name conflicts occurred
// @pyparm str|TemplateName||Template file used to initialize new item
// @pyparm int|FileAttributes||File attributes of new item
// @pyparm int|hrNew||HRESULT of the create operation
// @pyparm <o PyIShellItem>|NewItem||Shell interface of created item
STDMETHODIMP PyGFileOperationProgressSink::PostNewItem(
    /* [in] */ DWORD dwFlags,
    /* [in] */ IShellItem *psiDestinationFolder,
    /* [string][unique][in] */ LPCWSTR pszNewName,
    /* [string][unique][in] */ LPCWSTR pszTemplateName,
    /* [in] */ DWORD dwFileAttributes,
    /* [in] */ HRESULT hrNew,
    /* [in] */ IShellItem *psiNewItem)
{
    PY_GATEWAY_METHOD;
    PyObject *obpsiDestinationFolder;
    PyObject *obpszNewName;
    PyObject *obpszTemplateName;
    PyObject *obpsiNewItem;
    obpsiDestinationFolder = PyCom_PyObjectFromIUnknown(psiDestinationFolder, IID_IShellItem, TRUE);
    obpszNewName = PyWinObject_FromWCHAR(pszNewName);
    obpszTemplateName = PyWinObject_FromWCHAR(pszTemplateName);
    obpsiNewItem = PyCom_PyObjectFromIUnknown(psiNewItem, IID_IShellItem, TRUE);
    HRESULT hr = InvokeViaPolicy("PostNewItem", NULL, "kOOOklO", dwFlags, obpsiDestinationFolder, obpszNewName,
                                 obpszTemplateName, dwFileAttributes, hrNew, obpsiNewItem);
    Py_XDECREF(obpsiDestinationFolder);
    Py_XDECREF(obpszNewName);
    Py_XDECREF(obpszTemplateName);
    Py_XDECREF(obpsiNewItem);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|UpdateProgress|Gives an estimate of total work completed
// @pyparm int|WorkTotal||Undimensioned number representing total amount of work
// @pyparm int|WorkSoFar||Undimensioned number representing amount already completed
STDMETHODIMP PyGFileOperationProgressSink::UpdateProgress(
    /* [in] */ UINT iWorkTotal,
    /* [in] */ UINT iWorkSoFar)
{
    PY_GATEWAY_METHOD;
    HRESULT hr = InvokeViaPolicy("UpdateProgress", NULL, "II", iWorkTotal, iWorkSoFar);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|ResetTimer|Not implemented, according to MSDN
STDMETHODIMP PyGFileOperationProgressSink::ResetTimer(void)
{
    PY_GATEWAY_METHOD;
    HRESULT hr = InvokeViaPolicy("ResetTimer", NULL);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|PauseTimer|Not implemented, according to MSDN
STDMETHODIMP PyGFileOperationProgressSink::PauseTimer(void)
{
    PY_GATEWAY_METHOD;
    HRESULT hr = InvokeViaPolicy("PauseTimer", NULL);
    return hr;
}

// @pymethod |PyGFileOperationProgressSink|ResumeTimer|Not implemented, according to MSDN
STDMETHODIMP PyGFileOperationProgressSink::ResumeTimer(void)
{
    PY_GATEWAY_METHOD;
    HRESULT hr = InvokeViaPolicy("ResumeTimer", NULL);
    return hr;
}
