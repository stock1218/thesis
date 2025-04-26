#! python
import argparse
import re
import os
from subprocess import Popen, PIPE
import threading
from tqdm import tqdm
from pprint import pprint


CLANG_TIDY_PATH = ""
TARGET_PATH = ""
OUTPUT_PATH = ""

STDERR = ""

def write_output(output, name):
    with open(OUTPUT_PATH, "a", encoding="utf-8") as the_file:
        the_file.write(f"[{name}] {output}\n")

def process_stderr(pipe):
    global STDERR
    progress_bar = tqdm(total=100)
    while True:
        line = pipe.readline()
        STDERR += line.decode('utf-8')
        #print(f"TEST: {line.decode('utf-8').rstrip()}") #save to file instead
        write_output(f"{line.decode('utf-8')}", "stderr")
        progress = re.search(r'\[(\d+)/(\d+)\]', line.decode('utf-8'))
        if progress:
            done, remaining = map(int, progress.groups())
            #print(f"At {done}/{remaining}, {(done/remaining)*100:.2f}%")
            percent = round(((done/remaining) * 100), 2)
            progress_bar.n = percent
            progress_bar.refresh()
            if(percent == 100):
                break

    progress_bar.close()

def generate_stats(stderr, stdout):
    global STDERR
    results = {}

    # warnings
    matches = re.findall(r'.*this fix will not be applied.*', stdout)
    results['not_applied'] = len(matches)

    # unary ops
    matches = re.findall(r'.*unary operation.*', stdout)
    results['unary_ops'] = len(matches)
    results['unary_ops_strs'] = matches

    # non-assignment ops
    matches = re.findall(r'.*non-assignment operation.*', stdout)
    results['nonassignment_ops'] = len(matches)
    results['nonassignment_ops_strs'] = matches

    # assignment ops
    matches = re.findall(r'.*assignment operation.*', stdout)
    results['assignment_ops'] = len(matches)
    results['assignment_ops_strs'] = matches

    return results

def run_plugin():
    global STDERR
    STDERR = ""
    write_output("DEBUG MATCHER\n", "===")

    print("[*] Running debug plugin")

    # Run debug plugin
    result = Popen(f'{CLANG_TIDY_PATH} --checks="-*, modernize-use-checked-arithmetic-debug" {TARGET_PATH}', stdout=PIPE, stderr=PIPE)

    progress_thread = threading.Thread(target=process_stderr, args=(result.stderr,))

    progress_thread.start()
    progress_thread.join()

    stdout, stderr = result.communicate()
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')

    write_output(stdout, "stdout")
    write_output(stderr, "stderr")

    potential_results = generate_stats(stderr, stdout)

    STDERR = ""

    # Run typed debug plugin
    write_output("TYPED DEBUG MATCHER\n", "===")
    print("[*] Running typed debug plugin")

    # Run debug plugin
    result = Popen(f'{CLANG_TIDY_PATH} --checks="-*, modernize-use-checked-arithmetic-typed-debug" {TARGET_PATH}', stdout=PIPE, stderr=PIPE)

    progress_thread = threading.Thread(target=process_stderr, args=(result.stderr,))

    progress_thread.start()
    progress_thread.join()

    stdout, stderr = result.communicate()
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')

    write_output(stdout, "stdout")
    write_output(stderr, "stderr")

    typed_results = generate_stats(stderr, stdout)

    STDERR = ""

    # Run real plugin
    write_output("REAL MATCHER\n", "===")

    print("[*] Running plugin")

    result = Popen(f'{CLANG_TIDY_PATH} --checks="-*, modernize-use-checked-arithmetic" {TARGET_PATH}', stdout=PIPE, stderr=PIPE)

    progress_thread = threading.Thread(target=process_stderr, args=(result.stderr,))

    progress_thread.start()
    progress_thread.join()

    stdout, stderr = result.communicate()
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')

    write_output(stdout, "stdout")
    write_output(stderr, "stderr")

    real_results = generate_stats(stderr, stdout)

    return [potential_results, typed_results, real_results]


def print_stats(potential_results, typed_results, real_results):
    potential_unaryops = potential_results['unary_ops']
    potential_nonassignments = potential_results['nonassignment_ops']
    potential_assignments = potential_results['assignment_ops']
    potential_warnings = potential_unaryops + potential_nonassignments + potential_assignments

    typed_unaryops = typed_results['unary_ops']
    typed_nonassignments = typed_results['nonassignment_ops']
    typed_assignments = typed_results['assignment_ops']
    typed_warnings = typed_unaryops + typed_nonassignments + typed_assignments

    real_unaryops = real_results['unary_ops']
    real_nonassignments = real_results['nonassignment_ops']
    real_assignments = real_results['assignment_ops']
    real_warnings = real_unaryops + real_nonassignments + real_assignments
    not_applied = real_results['not_applied']

    stats = f'''
    Debug plugin stats:
        > Potential replacements: {potential_warnings}
        > Total unary operations: {potential_unaryops} ({(potential_unaryops/potential_warnings) * 100:.2f}%)
        > Total assignment operations: {potential_assignments} ({(potential_assignments/potential_warnings) * 100:.2f}%)
        > Total non-assignment operations: {potential_nonassignments} ({(potential_nonassignments/potential_warnings) * 100:.2f}%)

    Typed Debug plugin stats:
        > Potential replacements: {typed_warnings}
        > Total unary operations: {typed_unaryops} ({(typed_unaryops/typed_warnings) * 100:.2f}%)
        > Total assignment operations: {typed_assignments} ({(typed_assignments/typed_warnings) * 100:.2f}%)
        > Total non-assignment operations: {typed_nonassignments} ({(typed_nonassignments/typed_warnings) * 100:.2f}%)

    Real plugin stats:
        > Replacements: {real_warnings}
        > Total unary operations: {real_unaryops} ({(real_unaryops/real_warnings) * 100:.2f}%)
        > Total assignment operations: {real_assignments} ({(real_assignments/real_warnings) * 100:.2f}%)
        > Total non-assignment operations: {real_nonassignments} ({(real_nonassignments/real_warnings) * 100:.2f}%)
        > Overlapping fixes: {not_applied} ({(not_applied/real_warnings) * 100:.2f}%)

    Total performance stats:
        > Percentage of fixes: {real_warnings}/{potential_warnings} ({(real_warnings/potential_warnings) * 100:.2f}%)
        > Percentage of unary operations fixed: {real_unaryops}/{potential_unaryops} ({(real_unaryops/potential_unaryops) * 100:.2f}%)
        > Percentage of assignment operations fixed: {real_assignments}/{potential_assignments} ({(real_assignments/potential_assignments) * 100:.2f}%)
        > Percentage of nonassignmnet operations fixed: {real_nonassignments}/{potential_nonassignments} ({(real_nonassignments/potential_nonassignments) * 100:.2f}%)

    '''

    write_output(stats, "===")
    print(stats)


def run_tests():
    # run debug plugin on files
    res = run_plugin()
    potential_results = res[0]
    typed_results = res[1]
    real_results = res[2]

    print_stats(potential_results, typed_results, real_results)

    # run actual plugin and apply fixes
    # check the difference
    # check that programs still run

def main():
    global CLANG_TIDY_PATH
    global CLANG_FORMAT_PATH
    global TARGET_PATH
    global OUTPUT_PATH

    parser = argparse.ArgumentParser(description="Script for testing and collecting metrics on the use-checked-arithmetic clang-tidy plugin")

    parser.add_argument('--clang-tidy', required=True, help='Path to clang-tidy')
    parser.add_argument('--target', required=True, help='Target codebase to apply clang-tidy plugin to')
    parser.add_argument('--output', required=True, help='Output of the processed files')

    args = parser.parse_args()

    CLANG_TIDY_PATH = args.clang_tidy
    TARGET_PATH = args.target
    OUTPUT_PATH = args.output

    run_tests()

if(__name__ == '__main__'):
    main()
