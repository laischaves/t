import argparse
import csv
import os
import datetime
from py_markdown_table.markdown_table import markdown_table

def create_parser():
  parser = argparse.ArgumentParser(description='T')
  parser.add_argument('-a', '--add', metavar='', help='Add')
  parser.add_argument('-l', '--list', action='store_true', help='List')
  parser.add_argument('-r', '--remove', metavar='', help='Remove')
  parser.add_argument('-md', '--table', action='store_true', help='Table Markdown')
  return parser

def add_t(tk):
  with open('tasks.txt', 'a') as file:
    for index in enumerate(tk, start=0):
        x = '#'+str(index)
    task = ('task: {ta}'.format(ta=tk))
    task2 = ('task: {ta}\ncreated @: {time}'.format(ta=tk, time=str(datetime.date.today())))
    file.write(task)
    with open('tasks2.txt', 'a') as file:
      file.write(task2)
def list_t():
  if os.path.exists('tasks.txt'):
    with open('tasks.txt', 'r') as file:
      tasks = file.readlines()
      for index, task in enumerate(tasks, start=0):
        print(f'#{index}: {task.strip()}')
  else:
    print('None')
def remove_t(index):
  if os.path.exists('tasks.txt'):
    with open('tasks.txt', 'r') as file:
      tasks = file.readlines()
    with open('tasks.txt', 'w') as file:
      for i, task in enumerate(tasks, start=0):
        if i != index:
          file.write(task)
    print('Removed')
  else:
    print('None')

def table_t():
  res = []
  with open('tasks2.txt', 'r') as file:
    reader = csv.reader(file, delimiter=':')
    res = [{row[0].strip(): row[1].strip() for row in reader}]
  print(markdown_table(res).get_markdown())



def main():
  parser = create_parser()
  args = parser.parse_args()

  if args.add:
    add_t(args.add)
  elif args.list:
    list_t()
  elif args.remove:
    remove_t(int(args.remove))
  elif args.table:
    table_t()
  else:
    parser.print_help

  if os.path.exists('tasks.txt'):
    with open('tasks.txt', 'r') as file:
      tasks = file.readlines()


#    lines = file.readlines()
#  for line in lines:
#    key, value = line.strip().split(':')
#    res[key.strip()] = value.strip()

if __name__ == '__main__':
  main()
