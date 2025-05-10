use pyo3::create_exception;
use pyo3::exceptions::PyException;
use pyo3::prelude::*;
use pyo3::types::IntoPyDict;

create_exception!(mymodule, CustomError, PyException);

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_play_in_python() {
        Python::with_gil(|py| {
            let ctx = [("CustomError", py.get_type::<CustomError>())].into_py_dict(py);
            pyo3::py_run!(
                py,
                *ctx,
                "assert str(CustomError) == \"<class 'mymodule.CustomError'>\""
            );
            pyo3::py_run!(py, *ctx, "assert CustomError('oops').args == ('oops',)");
        });
    }
}
