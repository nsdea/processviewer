import os
import subprocess

def tasks(sort='memory'):
    output_list = subprocess.check_output('TASKLIST', shell=True).decode('utf-8').strip().split('\n')[3:]
    processes = []

    for e in output_list:
        process = {}
        process['name'] = e.split()[0]

        if process['name'].endswith('.'): process['name'] += 'exe'
        elif process['name'].endswith('.e'): process['name'] += 'xe'
        elif process['name'].endswith('.ex'): process['name'] += 'e'
        if not process['name'].endswith('.exe'): process['name'] += '.exe'

        try:
            process['pids'] = [int(e.split()[1])]
        except ValueError:
            process['pids'] = [e.split()[1]]

        process['sessiontype'] = e.split()[2]
        process['sessioncount'] = e.split()[3]
        process['memory'] = int(e.split()[4].replace('.', ''))
        process['instances'] = 1

        already_in_list = False
        for p in processes:
            if p['name'] == process['name']:
                already_in_list = True

                p['pids'].append(process['pids'])
                p['memory'] += process['memory']
                p['instances'] += 1
        
        if not already_in_list and process['name'] != 'Memory.exe':
            processes.append(process)

    return sorted(processes, key=lambda x: x[sort], reverse=True)

def kill(task: dict):
    print(task)
    _ = os.system(f'TASKKILL /IM {task["name"]} /F')

if __name__ == '__main__':
    for p in tasks():
        print(p)