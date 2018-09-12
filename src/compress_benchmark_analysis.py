import os
import subprocess
import time
import matplotlib.pyplot as plt
import pandas as pd

def log(text):
    print(time.strftime("%Y/%m/%d %H:%M:%S") + ' - ' + text)


def write_log_2_file(lines):
    pass


def execute(command, print_command=True, print_output=False, print_error=True, param_shell=True):
    if print_command:
        log("> " + command)
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=param_shell,
                             cwd=execute.cwd)
    stdout_lines, stderr_lines = popen.communicate()
    stderr_lines = stderr_lines.decode("utf-8")
    stdout_lines = stdout_lines.decode("utf-8")
    write_log_2_file(stderr_lines)
    write_log_2_file(stdout_lines)
    if print_output:
        if stdout_lines:
            print(stdout_lines)
        if stderr_lines:
            print(stderr_lines)
    if popen.returncode is not None and popen.returncode != 0:
        if stderr_lines and not print_output and print_error:
            print(stderr_lines)
        raise RuntimeError(stdout_lines + stderr_lines)
    return (stdout_lines + stderr_lines).splitlines()

lz4_bench = 'lz4 -b1 {file} -e19'
zstd_bench = 'zstd -b1 {file} -e19'
benchs = [lz4_bench,zstd_bench]

def benchmark(benchmark_folder):
    files = [x for x in os.listdir(benchmark_folder) if not os.path.isdir(x)]
    for bench in benchs:
        for file_name in files:
            result = execute(bench.format(file=file_name), print_command=True, print_output=True, print_error=True,
                             param_shell=True)


def pandas_task():
    # todo
    df = pd.read_csv()
    fig = plt.figure('test')
    for compress_method in df.compress_method.unique():
        # for file_size in df.file_size.unique():
        for file_size in ['2k','64k','1M','16M','128M']:
            subDf = df[(df['compress_method']==compress_method)&(df['file_size']==file_size)]
            labelstr = compress_method+'_'+file_size
            # print(subDf)
            ax = fig.add_subplot(111)
            ax.scatter(subDf['ratio'],subDf['compress'], label = labelstr)
            plt.xlabel('compress ratio')
            plt.ylabel('compress speed(MB/s)')
            plt.title('HI1616 Compress Performance')
            plt.legend()
    plt.savefig('./compress.png')
    plt.show()
    fig.clear()


