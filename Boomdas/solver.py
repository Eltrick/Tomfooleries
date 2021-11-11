import copy  # For deep-copying data to sort
# For waiting after each move
import time
SLEEP_TIME = 0.5
PRINT_NON_FAIL = (SLEEP_TIME > 0)

# Constant movement table (URDL = 0123)
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
names = ("up", "right", "down", "left")

def print_ary(ary):
  top = 0
  while(''.join(ary[top]).strip() == ''):
    top += 1
  bottom = 16
  while(''.join(ary[bottom]).strip() == ''):
    bottom -= 1
  left = 16
  for row in range(top, bottom + 1):
    left = min(left, len(ary[row]) - len(''.join(ary[row]).lstrip()))
  right_list = []
  if PRINT_NON_FAIL:
    print()  # Top newline for spacing
  for row in range(top, bottom + 1):
    right = 16 - (len(ary[row]) - len(''.join(ary[row]).rstrip()))
    if PRINT_NON_FAIL:
      print(''.join(ary[row][left : right + 1]))
    right_list.append(right)
  if PRINT_NON_FAIL:
    print()  # Bottom newline for spacing
  return top, bottom, left, right_list

def solved(current, coords, top, left):
  coords_top = min(coords[0:18:2])
  coords_left = min(coords[1:18:2])
  y_off = top - coords_top
  x_off = left - coords_left
  for i in range(0, 18, 2):
    if((not (0 <= coords[i] + y_off <= 16)) or
    (not (0 <= coords[i + 1] + x_off <= 16)) or
    (current[coords[i] + y_off][coords[i + 1] + x_off] == ' ')):
      return False
  return True

def _move(ary, y, x, d):
  y_m = y + dy[d]
  x_m = x + dx[d]
  if ary[y_m][x_m] != ' ':
    _move(ary, y_m, x_m, d)
  ary[y][x], ary[y_m][x_m] = ary[y_m][x_m], ary[y][x]

def move(ary, y, x, d):
  if PRINT_NON_FAIL:
    print("Move " + ary[y][x] + " " + names[d] + ":")
  _move(ary, y, x, d)
  time.sleep(SLEEP_TIME)
  return print_ary(ary)

def build_row(current, g_width):
  top = 7
  bottom = 9
  left = 7  # 3*3 values
  right_list = [9, 9, 9]
  if g_width == 2:
    move(current, 7, 8, 2)
    move(current, 8, 8, 2)
    _move(current, 7, 9, 3)
    move(current, 8, 9, 3)
    move(current, 9, 9, 2)
    top, bottom, left, right_list = move(current, 10, 9, 3)
  elif g_width == 4:
    move(current, 8, 7, 1)
    top, bottom, left, right_list = move(current, 8, 10, 0)
  elif g_width == 5:
    move(current, 8, 7, 1)
    move(current, 8, 8, 1)
    _move(current, 8, 11, 0)
    top, bottom, left, right_list = move(current, 8, 10, 0)
  elif g_width != 3:
    for i in range(3, 9):  # Widen to 7 wide
      move(current, 8 + (i // 5), 4 + i - 2 * (i // 5), 1)
    for i in range(11, 14):  # Invisibly move rightmost 4 up
      _move(current, 9, i, 0)
    move(current, 8, 10, 0)  # Move joining link up
    # Either push 7th wide back in, or up
    if g_width == 6: move(current, 8, 13, 3)
    else: _move(current, 8, 13, 0)
        # Push 6th up, finishing if not 8 wide
    top, bottom, left, right_list = move(current, 8, 12, 0)
        # If 8 wide, push bottom 2 right then up
    if g_width == 8:
      for i in range(9, 13):
        move(current, 8, i, 1)
      top, bottom, left, right_list = move(current, 8, 14, 0)
  return top, bottom, left, right_list

def build_col(current, g_height):
  top = 7
  bottom = 9
  left = 7  # 3*3 values
  right_list = [9, 9, 9]
  # 2 or 6+ tall should be impossible with wide gap
  if g_height == 4:
    move(current, 7, 8, 2)
    top, bottom, left, right_list = move(current, 10, 8, 3)
  elif g_height == 5:
    move(current, 7, 8, 2)
    move(current, 8, 8, 2)
    _move(current, 11, 8, 3)
    top, bottom, left, right_list = move(current, 10, 8, 3)
  elif g_height != 3:
    print("Impossible height encountered in build_col")
    return 0, 0, 0, 0  # This will trigger an emergency stop
  return top, bottom, left, right_list

def calc_blocks(string):
  i = 0
  block = 0
  blocks = []
  on_gap = False
  for i in range(0, len(string)):
    # If a gap started or ended...
    if (string[i] == ' ') != on_gap:
      # Update status, record, reset
      on_gap = not on_gap
      blocks.append(block)
      block = 0
    # Grow current block length
    block += 1
  blocks.append(block)  # Record final block
  return blocks  # Return filled list

# Note: for the following 3 methods, the top row is always y=7

def _take_right(current, col, count, g_count):
  # 1: Scan column right of this one, its height - 1 = available
  r_avail = len(''.join(current[i][col + 1] for i in range(0, 17)).strip()) - 1
  r_taken = 0  # Bugfix: track amount taken to avoid over-raising a column
  # 2: If available is less than (g_count - count), _take_right on right
  if r_avail < g_count - count:  # Availability accumulates in count
    r_taken = _take_right(current, col + 1, count + r_avail, g_count)[1]
  # 3: Move right column up as much as needed now that it'll suffice
  for i in range(7, 7 + count + r_taken - g_count, -1):
    move(current, i + r_avail, col + 1, 0)
    r_taken += 1  # Each of these means 1 was taken
  # 4: For all pushed up except bottom-most, _move left
  for i in range(5, 5 + count - r_taken - g_count, -1):
    _move(current, i, col + 1, 3)
  # 5: For bottom-most, move left and return
  return move(current, 6, col + 1, 3), r_taken

def take_right(current, col, count, g_count, g_coords):
  # 1: _take_right with same parameters as this call
  top, bottom, left, right_list = _take_right(current, col, count, g_count)[0]
  while top < 7:  # 2: Push this column down to fit, return at end
    if solved(current, g_coords, top, left): break  # Possible early solve
    top, bottom, left, right_list = move(current, top, col, 2)
  return top, bottom, left, right_list

def give_right(current, col, count, g_count, g_coords):
  # 1: Push column up (count - g_count)
  for i in range(6 + count, 6 + g_count, -1):
    move(current, i, col, 0)
  # 2: For all pushed up except bottom-most, _move right
  for i in range(5, 5 + g_count - count, -1):
    _move(current, i, col, 1)
  # 3: For bottom-most, move right, redrawing grid
  top, bottom, left, right_list = move(current, 6, col, 1)
  while top < 7:  # 4: Push right column down to fit, return at end
    if solved(current, g_coords, top, left): break  # Possible early solve
    top, bottom, left, right_list = move(current, top, col + 1, 2)
  return top, bottom, left, right_list

def _take_down(current, row, count, g_count):
  # 1: Scan row below this one, its width - 1 = available
  d_avail = len(''.join(current[row + 1]).strip()) - 1
  d_taken = 0  # Like _take_right, keep track of this
  # 2: If available is less than (g_count - count), _take_down on below
  if d_avail < g_count - count:  # Availability accumulates in count
    d_taken = _take_down(current, row + 1, count + d_avail, g_count)[1]
  # 3: Move below row as much as needed now that it'll suffice
  for i in range(7, 7 + count + d_taken - g_count, -1):
    move(current, row + 1, i + d_avail, 3)
    d_taken += 1  # Each of these means 1 was taken
  # 4: For all pushed left except right-most, _move up
  for i in range(5, 5 + count - d_taken - g_count, -1):
    _move(current, row + 1, i, 0)
  # 5: For right-most, move up and return
  return move(current, row + 1, 6, 0), d_taken

def take_down(current, row, count, g_count, g_coords):
  # 1: _take_down with same parameters as this call
  top, bottom, left, right_list = _take_down(current, row, count, g_count)[0]
  while left < 7:  # 2: Push this row right to fit, return at end
    if solved(current, g_coords, top, left): break  # Possible early solve
    top, bottom, left, right_list = move(current, row, left, 1)
  return top, bottom, left, right_list

def give_down(current, row, count, g_count, g_coords):
  # 1: Push row left (count - g_count)
  for i in range(6 + count, 6 + g_count, -1):
    move(current, row, i, 3)
  # 2: For all pushed left except right-most, _move down
  for i in range(5, 5 + g_count - count, -1):
    _move(current, row, i, 2)
  # 3: For right-most, move down, redrawing grid
  top, bottom, left, right_list = move(current, row, 6, 2)
  while left < 7:  # 4: Push below row right to fit, return at end
    if solved(current, g_coords, top, left): break  # Possible early solve
    top, bottom, left, right_list = move(current, row + 1, left, 1)
  return top, bottom, left, right_list

# TODO All of these
def br_special():
  pass

def bl_special():
  pass

def tr_special():
  pass

def tl_special():
  pass

def check_special(current, goal, g_coords, g_top, g_bottom, g_left, g_right):
  for row in range(1, 16):
    for col in range(1, 16):
      if (goal[row][col] == ' ' and
      goal[row + 1][col] != ' ' and
      goal[row - 1][col] != ' ' and
      goal[row][col + 1] != ' ' and
      goal[row][col - 1] != ' '):
        step = -9  # Special case, probably
        if goal[row + 1][col + 1] == ' ':
          br_special()
        elif goal[row + 1][col - 1] == ' ':
          bl_special()
        elif goal[row - 1][col + 1] == ' ':
          tr_special()
        elif goal[row - 1][col - 1] == ' ':
          tl_special()
        else:  # False alarm, proceed as normal
          step = 1
        return step
  return 1  # Normal case

# Method to solve in the other direction (lots of semi-repeated code)
def solve_by_rows(current, goal, g_coords, g_top, g_bottom,
g_left, g_right, top, bottom, left, right_list):
  g_height = g_bottom - g_top + 1
  g_rows = []  # List of (left, blocks) tuples
  for g_row_index in range(g_top, g_bottom + 1):
    g_row = ''.join(goal[g_row_index])
    g_row_left = len(g_row) - len(g_row.lstrip())
    g_row_blocks = calc_blocks(g_row.strip())
    g_rows.append((g_row_left, g_row_blocks))
    # Tall gap impossible if this method called
  
  step = 1  # Main solving-by-rows loop
  g_rows_copy = copy.deepcopy(g_rows)
  g_rows_copy.sort()  # Check for 4*3 ring patterns
  if g_rows_copy == [[1], [1, 1, 1], [3], [3]]:
    step = -9  # TODO
  elif g_rows_copy == [[1, 1, 1], [1, 1, 1], [2], [3]]:
    step = -9  # TODO
  
  while not solved(current, g_coords, top, left):
    if step == 1:  # First column
      top, bottom, left, right_list = build_col(current, g_height)
      if top == bottom: break  # Emergency error check
      step = 2  # Assuming no error, END STEP 1
    elif step == 2:  # Closing row gaps
      if g_height == 4:
        top, bottom, left, right_list = move(current, 7, 9, 3)
      elif g_height == 5:
        _move(current, 7, 9, 3)
        top, bottom, left, right_list = move(current, 8, 9, 3)
      step = top  # Step now counts rows
    elif 2 < step < bottom:  # Main row manipulation
      g_index = g_top + step - top
      g_count = g_coords[0:18:2].count(g_index)
      count = len(''.join(current[step]).strip())
      if count < g_count:  # If too short, take
        top, bottom, left, right_list = take_down(
          current, step, count, g_count, g_coords)
      elif count > g_count:  # If too tall, give
        top, bottom, left, right_list = give_down(
          current, step, count, g_count, g_coords)
      step = (step + 1) % bottom  # Move to next row (0=done)
    elif -3 < step < 1:  # Final step: all rows done, just align
      # Go from top to bottom, possibly skipping rows
      unmoved = True  # Track movement in each part
      for row in range(top, bottom + 1):
        g_row_left = g_rows[row - top][0]
        g_row_blocks = g_rows[row - top][1]
        u_row = ''.join(current[row - 1])
        # u_left is not needed, but can be found similar to m_left and b_left
        u_right = 16 - (len(u_row) - len(u_row.rstrip())) % 16
        m_row = ''.join(current[row])
        m_left = (len(m_row) - len(m_row.lstrip())) % 16
        m_right = 16 - (len(m_row) - len(m_row.rstrip())) % 16
        b_row = ''.join(current[row + 1])
        b_left = (len(b_row) - len(b_row.lstrip())) % 16
        b_right = 16 - (len(b_row) - len(b_row.rstrip())) % 16

        if step < 0:  # Gap movement, -1 * step = gap occurrence
          if len(g_row_blocks) > -2 * step:  # If there's an unset gap...
            last_block = m_left + sum(g_row_blocks[0:-2*step-1]) - 1
            if current[row][last_block + 1] == ' ':
              continue  # and it's not done already...
            unmoved = False  # There will be movement, so mark it
            d_scan = 0  # -1 = up, 1 = down, 0 = none: scan direction
            # Check the side rows for failure to cover the gap and its edges
            for i in range(last_block, last_block + g_row_blocks[-2*step-1] + 2):
              if current[row - 1][i] == ' ':
                d_scan = -1  # Above row fails
                break
              elif current[row + 1][i] == ' ':
                d_scan = 1  # Below row fails
                break
            
            # Now that the scan direction is determined, scan/fix blockage
            movement = 0  # Tracks length+dir of movement in this step
            # If there's blockage, move it away to avoid strange issues
            while(d_scan != 0 and current[row][last_block] != ' '):
              # Always move the column away from the blockage
              movement += d_scan
              col = ''.join(current[i][last_block] for i in range(0, 17))
              # Upper edge if going down, else lower edge
              col_edge = (len(col) - len(col.lstrip()) if (
                d_scan < 0) else 16 - (len(col) - len(col.rstrip())))
              top, bottom, left, right_list = move(
                current, col_edge, last_block, 1 - d_scan)
            
            # With the blockage out of the way, set up the gap
            for col in range(last_block + 1, last_block + g_row_blocks[-2*step-1] + 1):
              scan_row = row + d_scan  # Check unanchored rows
              while(d_scan != 0 and current[scan_row][col] != ' '
              and current[scan_row][col + 1] == ' '):  # Bugfix: Wide row up
                _move(current, scan_row, col, 1)  # Hidden movement
                scan_row += d_scan  # Check for any more ^ before redraw
              top, bottom, left, right_list = move(current, row, col, 1)
            
            # Finally, re-position the blockage so it fits the goal
            while(movement != 0):
              movement -= d_scan
              col = ''.join(current[i][last_block] for i in range(0, 17))
              # Upper edge if going down, else lower edge
              col_edge = (len(col) - len(col.lstrip()) if (
                d_scan > 0) else 16 - (len(col) - len(col.rstrip())))
              top, bottom, left, right_list = move(
                current, col_edge, last_block, 1 + d_scan)
          # END POSSIBLE GAP MOVEMENT
        # Always check left movement after possible gap movement
        left_gap = g_row_left - g_left
        for i in range(m_left - left, left_gap):
          # Multiple 1-wide rows moving together
          if m_left == m_right and b_left == b_right:
            if m_left >= u_right:
              break  # Unlikely but safe check
            # Find the first non-1-wide row below this
            scan_index = row + 2  # row + 1 is known 1-wide
            scan_row = ''.join(current[scan_index])
            while len(scan_row.strip()) == 1:  # Until non-1-wide found...
              scan_index += 1  # Increment index and update stored row
              scan_row = ''.join(current[scan_index])
            
            # Check right of scanned row (use rightmost possible right if empty)
            scan_right = 16 - (len(scan_row) - len(scan_row.rstrip())) % 16
            if m_left >= scan_right:  # If that column is too high...
              break  # Don't move this group until later
            # Actual movement (combined with below, visible move)
            for j in range(row + 1, scan_index):
              _move(current, j, m_left, 1)
            # END MULTI-1-WIDE MOVEMENT
          elif m_left >= u_right or m_left >= b_right:
            break  # Don't move too far! (Possible exception above)
          top, bottom, left, right_list = move(current, row, m_left, 1)
          m_left += 1  # Move as close to goal as possible
          m_right += 1  # Mark movement
          unmoved = False
      if unmoved:  # If there's no movement...
        step -= 1  # Begin processing the next set of gaps
    else:  # Failure to solve printed in main method, not here
      break  # Therefore, just end the loop, which ends the method

def main(order):
  if order == 0:  # Prompt for order and prepare variables
    order = int(input("Enter the 9 digits with no spaces: "))
  current = [[' '] * 17 for i in range(0, 17)]
  goal = [[' '] * 17 for i in range(0, 17)]
  g_coords = [8, 8]  # y then x, extended in pairs

  # Fill current/goal arrays from given order
  goal[8][8] = '0'
  for i in range(0, 9):
    # Current array always starts 3*3
    row = i // 3 + 7
    col = i % 3 + 7
    current[row][col] = (str(order))[i]
    # Goal calculations start at 1
    if i != 0:  # First i digits of order
      calc = order // (10 ** (9 - i))
      base = (calc // 4) % i
      y = g_coords[2 * base]
      x = g_coords[2 * base + 1]
      while goal[y][x] != ' ':
        y += dy[calc % 4]
        x += dx[calc % 4]
      goal[y][x] = str(i)
      g_coords.extend((y, x))
  
  # Print arrays and check dimensions/possibility
  if PRINT_NON_FAIL:
    print("\nCurrent state (taken from input):")
  top, bottom, left, right_list = print_ary(current)
  if PRINT_NON_FAIL:
    print("Goal state (only shape matters):")
  g_top, g_bottom, g_left, g_right_list = print_ary(goal)
  g_right = max(g_right_list)
  g_width = g_right - g_left + 1
  if g_width == 1 or g_width == 9:
    print("Submit with any shape. (9*1 or 1*9 goal = impossible)")
    print("Order that yielded an impossible goal: " + str(order))
    return  # Immediately end if impossible goal detected
  
  # Record goal column data in case wide gaps appear
  g_cols = []  # List of (top, blocks) tuples
  gap_width = 1  # Max possible gap width
  for g_col_index in range(g_left, g_right + 1):
    g_col = ''.join(goal[i][g_col_index] for i in range(0, 17))
    g_col_top = len(g_col) - len(g_col.lstrip())
    g_col_blocks = calc_blocks(g_col.strip())
    g_cols.append((g_col_top, g_col_blocks))
    # If this and a column left of this have gaps...
    if g_col_index > g_left and len(g_col_blocks
    ) > 1 and len(g_cols[g_col_index - g_left - 1][1]) > 1:
      gap_width += 1  # The widest gap must grow
  
  # Finally, start making the shape (might be special)
  step = check_special(current, goal, g_coords,
  g_top, g_bottom, g_left, g_right)  # Weird step tracker

  g_cols_copy = copy.deepcopy(g_cols)
  g_cols_copy.sort()  # Check for 4*3 ring patterns
  if g_cols_copy == [[1], [1, 1, 1], [3], [3]]:
    step = -9  # TODO
  elif g_cols_copy == [[1, 1, 1], [1, 1, 1], [2], [3]]:
    step = -9  # TODO
  elif gap_width > 1:  # Else if there's a gap over 1 wide, solve by rows
    solve_by_rows(current, goal, g_coords, g_top, g_bottom,
      g_left, g_right, top, bottom, left, right_list)
    step = -9
  
  while not solved(current, g_coords, top, left):
    # BEGIN MAIN ALGORITHM

    if step == 1:  # First row
      top, bottom, left, right_list = build_row(current, g_width)
      step = 2  # END STEP 1
    elif step == 2:  # Closing column gaps
      if g_width == 4:
        top, bottom, left, right_list = move(current, 9, 7, 0)
      elif g_width == 5:
        _move(current, 9, 7, 0)
        top, bottom, left, right_list = move(current, 9, 8, 0)
      step = left  # Step now counts columns
    elif 2 < step < max(right_list):  # Main column manipulation
      g_index = g_left + step - left
      g_count = g_coords[1:18:2].count(g_index)
      count = len(''.join(current[i][step] for i in range(0, 17)).strip())
      if count < g_count:  # If too short, take
        top, bottom, left, right_list = take_right(
          current, step, count, g_count, g_coords)
      elif count > g_count:  # If too tall, give
        top, bottom, left, right_list = give_right(
          current, step, count, g_count, g_coords)
      step = (step + 1) % max(right_list)  # Move to next column (0=done)
    elif -3 < step < 1:  # Final step: all columns done, just align
      # Go from left to right, possibly skipping columns
      unmoved = True  # Track movement in each part
      for col in range(left, max(right_list) + 1):
        g_col_top = g_cols[col - left][0]
        g_col_blocks = g_cols[col - left][1]
        l_col = ''.join(current[i][col - 1] for i in range(0, 17))
        # l_top is not needed, but can be found similar to m_top and r_top
        l_bottom = 16 - (len(l_col) - len(l_col.rstrip())) % 16
        m_col = ''.join(current[i][col] for i in range(0, 17))
        m_top = (len(m_col) - len(m_col.lstrip())) % 16
        m_bottom = 16 - (len(m_col) - len(m_col.rstrip())) % 16
        r_col = ''.join(current[i][col + 1] for i in range(0, 17))
        r_top = (len(r_col) - len(r_col.lstrip())) % 16
        r_bottom = 16 - (len(r_col) - len(r_col.rstrip())) % 16

        if step < 0:  # Gap movement, -1 * step = gap occurrence
          if len(g_col_blocks) > -2 * step:  # If there's an unset gap...
            last_block = m_top + sum(g_col_blocks[0:-2*step-1]) - 1
            if current[last_block + 1][col] == ' ':
              continue  # and it's not done already...
            unmoved = False  # There will be movement, so mark it
            d_scan = 0  # -1 = left, 1 = right, 0 = none: scan direction
            # Check the side columns for failure to cover the gap and its edges
            for i in range(last_block, last_block + g_col_blocks[-2*step-1] + 2):
              if current[i][col - 1] == ' ':
                d_scan = -1  # Left column fails
                break
              elif current[i][col + 1] == ' ':
                d_scan = 1  # Right column fails
                break
            
            # Now that the scan direction is determined, scan/fix blockage
            movement = 0  # Tracks length+dir of movement in this step
            # If there's blockage, move it away to avoid strange issues
            while(d_scan != 0 and current[last_block][col] != ' '):
              # Always move the row away from the blockage
              movement += d_scan
              row = ''.join(current[last_block])
              # Left edge if going right, else right edge
              row_edge = (len(row) - len(row.lstrip()) if (
                d_scan < 0) else 16 - (len(row) - len(row.rstrip())))
              top, bottom, left, right_list = move(
                current, last_block, row_edge, 2 + d_scan)
            
            # With the blockage out of the way, set up the gap
            for row in range(last_block + 1, last_block + g_col_blocks[-2*step-1] + 1):
              scan_col = col + d_scan  # Check unanchored columns
              while(d_scan != 0 and current[row][scan_col] != ' '
              and current[row + 1][scan_col] == ' '):  # Bugfix: Tall column left
                _move(current, row, scan_col, 2)  # Hidden movement
                scan_col += d_scan  # Check for any more ^ before redraw
              top, bottom, left, right_list = move(current, row, col, 2)
            
            # Finally, re-position the blockage so it fits the goal
            while(movement != 0):
              movement -= d_scan
              row = ''.join(current[last_block])
              # Left edge if going right, else right edge
              row_edge = (len(row) - len(row.lstrip()) if (
                d_scan > 0) else 16 - (len(row) - len(row.rstrip())))
              top, bottom, left, right_list = move(
                current, last_block, row_edge, 2 - d_scan)
          # END POSSIBLE GAP MOVEMENT
        # Always check top movement after possible gap movement
        top_gap = g_col_top - g_top
        for i in range(m_top - top, top_gap):
          # Multiple 1-high columns moving together
          if m_top == m_bottom and r_top == r_bottom:
            if m_top >= l_bottom:
              break  # Unlikely but safe check
            # Find the first non-1-high column right of this
            scan_index = col + 2  # col + 1 is known 1-high
            scan_col = ''.join(current[i][scan_index] for i in range(0, 17))
            while len(scan_col.strip()) == 1:  # Until non-1-high found...
              scan_index += 1  # Increment index and update stored column
              scan_col = ''.join(current[i][scan_index] for i in range(0, 17))
            
            # Check bottom of scanned column (use lowest possible bottom if empty)
            scan_bottom = 16 - (len(scan_col) - len(scan_col.rstrip())) % 16
            if m_top >= scan_bottom:  # If that column is too high...
              break  # Don't move this group until later
            # Actual movement (combined with below, visible move)
            for j in range(col + 1, scan_index):
              _move(current, m_top, j, 2)
            # END MULTI-1-HIGH MOVEMENT
          elif m_top >= l_bottom or m_top >= r_bottom:
            break  # Don't move too far! (Possible exception above)
          top, bottom, left, right_list = move(current, m_top, col, 2)
          m_top += 1  # Move as close to goal as possible
          m_bottom += 1  # Mark movement
          unmoved = False
      if unmoved:  # If there's no movement...
        step -= 1  # Begin processing the next set of gaps
    else:  # Failsafe: If the step gets too high or too low, end
      print("Failure to solve with order " + str(order))
      break
    
    # END MAIN ALGORITHM
  if PRINT_NON_FAIL:
    print("Ensure your current shape lines up with the goal (below).")
    print_ary(goal)  # Final instructions after match detected
    print("Assuming it matches (again, only shape matters), submit.")