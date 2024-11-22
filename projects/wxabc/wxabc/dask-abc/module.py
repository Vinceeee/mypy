def print_fib(n: int):
    result = fib(n)
    print(f"fib: {n} is {result}")
    return result


def fib(n: int) -> int:
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def long_running_process_with_jvm():
    from multiprocessing import Process

    def _inner():
        import jpype
        import jpype.imports
        from jpype import JClass

        # 启动JVM，确保提供正确的类路径
        jpype.startJVM(classpath=["./java"])
        counter = JClass("Counter")()
        counter.printNumbers()
        jpype.shutdownJVM()

    p = Process(target=_inner)
    p.start()
    p.join()
