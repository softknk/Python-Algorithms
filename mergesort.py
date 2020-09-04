def mergesort(n):
  if len(n) == 0 or len(n) == 1:
    return n

  left = list()
  right = list()

  divide(n, left, right)

  left = mergesort(left)
  right = mergesort(right)

  return pack(left, right)


def divide(target, left, right):
  """
  divides the target list into left and right list
  """
  mid = len(target) // 2
  for i in range(mid):
    left.append(target[i])
  for i in range(mid, len(target)):
    right.append(target[i])
  print("left: {}".format(left))  # debug purpose
  print("right: {}".format(right))  # debug purpose


def pack(left, right):
  """
  connects to sorted lists to one sorted list
  """
  pack = list()
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      pack.append(left[i])
      i = i + 1
    else:
      pack.append(right[j])
      j = j + 1
  if i >= len(left) and j < len(right):
    for k in range(j, len(right)):
      pack.append(right[k])
  elif j >= len(right) and i < len(left):
    for k in range(i, len(left)):
      pack.append(left[k])
  print("packed: {}".format(pack)) # debug purpose
  return pack
