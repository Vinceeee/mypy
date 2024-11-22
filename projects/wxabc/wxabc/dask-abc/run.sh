# 启动一个scheduler和两个worker
dask-scheduler &
dask-worker tcp://127.0.0.1:8786 --nprocs 1 --nthreads 4
