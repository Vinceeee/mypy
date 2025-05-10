use pyo3::prelude::*;
use utils::cal::inner_cal;

pub mod utils;
/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// My python extension written in pyo3
#[pymodule]
fn wx_common_pyo3(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;

    #[pyfn(m)]
    fn add(a: i32, b: i32) -> i32 {
        inner_cal(a, b)
    }

    Ok(())
}
