// This file declares the IScheduledWorkItem Interface for Python.
// Generated by makegw.py
// ---------------------------------------------------
//
// Interface Declaration

#include "PythonCOM.h"
#include "mstask.h"

class PyIScheduledWorkItem : public PyIUnknown {
   public:
    MAKE_PYCOM_CTOR(PyIScheduledWorkItem);
    static IScheduledWorkItem *GetI(PyObject *self);
    static PyComTypeObject type;

    // The Python methods
    static PyObject *CreateTrigger(PyObject *self, PyObject *args);
    static PyObject *DeleteTrigger(PyObject *self, PyObject *args);
    static PyObject *GetTriggerCount(PyObject *self, PyObject *args);
    static PyObject *GetTrigger(PyObject *self, PyObject *args);
    static PyObject *GetTriggerString(PyObject *self, PyObject *args);
    static PyObject *GetRunTimes(PyObject *self, PyObject *args);
    static PyObject *GetNextRunTime(PyObject *self, PyObject *args);
    static PyObject *SetIdleWait(PyObject *self, PyObject *args);
    static PyObject *GetIdleWait(PyObject *self, PyObject *args);
    static PyObject *Run(PyObject *self, PyObject *args);
    static PyObject *Terminate(PyObject *self, PyObject *args);
    static PyObject *EditWorkItem(PyObject *self, PyObject *args);
    static PyObject *GetMostRecentRunTime(PyObject *self, PyObject *args);
    static PyObject *GetStatus(PyObject *self, PyObject *args);
    static PyObject *GetExitCode(PyObject *self, PyObject *args);
    static PyObject *SetComment(PyObject *self, PyObject *args);
    static PyObject *GetComment(PyObject *self, PyObject *args);
    static PyObject *SetCreator(PyObject *self, PyObject *args);
    static PyObject *GetCreator(PyObject *self, PyObject *args);
    static PyObject *SetWorkItemData(PyObject *self, PyObject *args);
    static PyObject *GetWorkItemData(PyObject *self, PyObject *args);
    static PyObject *SetErrorRetryCount(PyObject *self, PyObject *args);
    static PyObject *GetErrorRetryCount(PyObject *self, PyObject *args);
    static PyObject *SetErrorRetryInterval(PyObject *self, PyObject *args);
    static PyObject *GetErrorRetryInterval(PyObject *self, PyObject *args);
    static PyObject *SetFlags(PyObject *self, PyObject *args);
    static PyObject *GetFlags(PyObject *self, PyObject *args);
    static PyObject *SetAccountInformation(PyObject *self, PyObject *args);
    static PyObject *GetAccountInformation(PyObject *self, PyObject *args);

   protected:
    PyIScheduledWorkItem(IUnknown *pdisp);
    ~PyIScheduledWorkItem();
};
