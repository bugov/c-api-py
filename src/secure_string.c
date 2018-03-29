#define PY_SSIZE_T_CLEAN

#include <Python.h>
#include <string.h>

static PyObject* secure_string_flush(PyObject *self, PyObject *args) {
    char *buffer;
    Py_ssize_t length;

    if (! PyArg_ParseTuple(args, "s#", &buffer, &length)) {
        return NULL;
    }
    
    memset(buffer, 0, length);
    return Py_BuildValue("");
}

static PyMethodDef secure_string_methods[] = {
    { "flush", secure_string_flush, METH_VARARGS, "flush string memory" },
    { NULL, NULL, 0, NULL },
};

static struct PyModuleDef secure_string_def = {
	PyModuleDef_HEAD_INIT,
	"secure_string",
	NULL,
	-1,
	secure_string_methods,
};

PyMODINIT_FUNC PyInit_secure_string(void) {
    return PyModule_Create(&secure_string_def);
}
