import multiprocessing


def f():
    import logging
    from time import sleep

    logging.basicConfig(datefmt="%Y-%m-%d %H:%M:%S", filename="/tmp/test.log")
    for i in range(10):
        logging.info(f"log - {i}")
        sleep(1)


def main():
    p = multiprocessing.Process(target=f)
    p.daemon = True
    p.start()
    print("done.")


if __name__ == "__main__":
    main()
