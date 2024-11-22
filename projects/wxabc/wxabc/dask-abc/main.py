from distributed import Client
from module import long_running_process_with_jvm, print_fib


def main():
    client = Client("127.0.0.1:8786")

    def done_callback(future):
        print(f"{future} done.")

    client.upload_file("./module.py")
    client.submit(print_fib, 10)
    result = client.submit(long_running_process_with_jvm)
    result.result()


main()
