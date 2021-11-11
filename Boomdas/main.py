from solver import main
import itertools

# This will likely not truly work for a LONG time due to the abundance of edge cases
def solve_all():
  for order in itertools.permutations(('1', '2', '3', '4', '5', '6', '7', '8', '9')):
    #print_order = True  # For thorough debugging
    print_order = (order[6:9] == ('7', '8', '9'))
    if print_order:  # Print progress
      print(''.join(order))
    main(int(''.join(order)))  # Sequentially attempt all possible orders
  print("Finished solving all possible orders")

#solve_all()
main(0)