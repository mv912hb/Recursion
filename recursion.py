#############################################################################################
# FILE : ex7.py
# WRITER : Boris Vedernikov, vedernikov.b, 342733474
# EXERCISE : intro2cs ex7 2021
# DESCRIPTION: 14 functions(some of them made to help) for solving problems using recursion
#############################################################################################

from typing import *

def print_to_n(n: int) -> None:
    if n < 1:
        return None
    else:
        print_to_n(n-1)
        print(n)

def digit_sum(n: int) -> int:
    if n == 0:
        return 0
    else:
        return (n % 10 + digit_sum((n // 10)))

def has_divisor_smaller_than(n: int, i: int) -> bool:
    if i > 1:
        if n % i == 0:
            return True
        return has_divisor_smaller_than(n, i - 1)
    else:
        return False


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    else:
        return not has_divisor_smaller_than(n, n // 2)

def play_hanoi(hanoi: Any, n: int, src: Any, dest: Any, temp: Any) -> None:
    if n <= 0:
        return
    if n == 1:
        hanoi.move(src, dest)
    if n == 2:
        hanoi.move(src, temp)                               # move one to temporary
        hanoi.move(src, dest)                               # move second to destination
        hanoi.move(temp, dest)                              # move first from temporary to destination
    else:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        hanoi.move(src, dest)                               # last to destination
        play_hanoi(hanoi, n - 1, temp, dest, src)

def print_sequences_helper(char_list: List[str], n: int, lst: List[str] = []) -> None:
    if len(lst) == n:
        print("".join(lst))
    else:
        for i in range(len(char_list)):
            print_sequences_helper(char_list, n, lst + [char_list[i]])

def print_sequences(char_list: List[str], n: int) -> None:
    print_sequences_helper(char_list, n)

def print_no_repetition_sequences_helper(char_list: List[str], n: int, lst: List[str] = []) -> None:
    if len(lst) == n:
        print("".join(lst))
    else:
        for i in range(len(char_list)):
            temp_list = [char_list[j] for j in range(len(char_list)) if i != j]
            print_no_repetition_sequences_helper(temp_list, n, lst + [char_list[i]])

def print_no_repetition_sequences(char_list: List[str], n: int) -> None:
    print_no_repetition_sequences_helper(char_list, n)

def checker(result: List[str]) -> bool:
  count = 0
  for i in result:
    if count < 0:
      return False
    if i == "(":
      count += 1
    else:
      count -= 1
  if count != 0:
    return False
  return True

def parenthese_helper(char_list: str, n: int, lst: List[str] = [], result: List[str] = []) -> None:
  if len(lst) == n:
    if checker(lst):
      result.append("".join(lst))
  else:
    for i in range(len(char_list)):
      parenthese_helper(char_list, n, lst + [char_list[i]], result)

def parentheses(n: int) -> List[str]:
  a: List[str] = []
  parenthese_helper("()", n*2, [], a)
  return a

def flood_fill(image: List[List[str]], start: Tuple[int, int]) -> None:
    if image[start[0]][start[1]] == "*":
        return
    image[start[0]][start[1]] = "*"
    if start[0] > 0:
        flood_fill(image, (start[0] - 1, start[1]))
    if start[0] < len(image) - 1:
        flood_fill(image, (start[0] + 1, start[1]))
    if start[1] > 0:
        flood_fill(image, (start[0], start[1] - 1))
    if start[1] < len(image) - 1:
        flood_fill(image, (start[0], start[1] + 1))








