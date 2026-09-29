# Write code below 💖
import time
import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def lineloop(length, line):
  return length * line

def loading(textLoading, howlong):
  for i in range(howlong):
    print(f'{textLoading} {lineloop(50, "")} {i}s', end='\r', flush=True)
    time.sleep(1)
    i += 1

def calculator(firstNumber, operating_symbol, secondNumber):
  if operating_symbol == '+':
    result = firstNumber + secondNumber
  elif operating_symbol == '-':
    result = firstNumber - secondNumber
  elif operating_symbol == '*':
    result = firstNumber * secondNumber
  elif operating_symbol == '/':
    result = firstNumber / secondNumber
  return result

def finalResult(num1, op, num2):
  result = calculator(num1, op, num2)
  print(f'{num1} {op} {num2} = {result}')

def main():
  print(str(lineloop(15, '=')) + ' The Calculator ' + str(lineloop(15, '=')))


def redo(message):
  redo = input(f'{message} (Y/n) ')
  redo.upper

  if redo == 'Y':
    print(message)
    loading('Rebooting...', 5)
    clear()
    main()
  elif redo == 'N':
    loading('Exiting...', 2)
    clear()
    sys.exit()

def function():
  while True:

    try:
      q_num1 = float(input('Input first digit: '))

      q_op = input('Input operation ( + | - | * | / |): ')
      timesToRepeat = 5
      while (q_op != '+') and (q_op != '-') and (q_op != '*') and (q_op != '/') and (timesToRepeat <= 0):
        print('You inputed the wrong operating symbol')
        q_op = input('Please re-input it: ')
        timesToRepeat -= 1

      q_num2 = float(input('Input second digit: '))

      makingSure = input(f'Are you sure that your question is\n{q_num1} {q_op} {q_num2} = ?\n(Y/n) ')
      makingSure.upper

      if makingSure == 'Y':
        loading('Loading...', 2)
        loading('calculating...', 3)
        clear()

        finalResult(q_num1, q_op, q_num2)

        redo('Do you want to continue?')
        continue
      elif makingSure == 'N':
        redo('Do you want to retry?')
        continue

    except ZeroDivisionError:
      print('Answer Out of Bound')
      print("Please don't divide 0 by 0")
      redo('Do you want to restart?')
      continue
    except ValueError:
      print("Error")
      loading('calculating error...', 4)
      print('You inputed the wrong type, please input as number and not other characters')
      redo('Do you want to restart')
      continue

  print(lineloop('\n', loading('', 10)))
  clear()

main()
function()


