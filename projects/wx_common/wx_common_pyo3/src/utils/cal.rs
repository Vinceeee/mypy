pub fn inner_cal(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_inner_cal() {
        assert_eq!(inner_cal(1, 2), 3);
    }
}
