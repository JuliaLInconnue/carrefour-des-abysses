#################################################################################
# by sDextra 
#################################################################################
# 1110011 1000100 1100101 1111000 1110100 1110010 1100001
#################################################################################

# row - field width
# column - field height
# speed - falling speed
# tops - number of top places
# level - level of difficulty
# mode - presence of a bonus
# impossible - without I tetromino
# for_level - the number of lines for level-up

# Highscore
init -100:
    if persistent.highscore is None:
        $ persistent.highscore = []

init python:
    # Tetromino Symbols
    symb_field = '·'
    symb_red = 'R'
    symb_cyan = 'C'
    symb_blue = 'B'
    symb_green = 'G'
    symb_orange = 'O'
    symb_purple = 'P'
    symb_yellow = 'Y'
    coloring = [symb_red, symb_cyan, symb_blue, symb_green, symb_orange, symb_purple, symb_yellow]

    row = 10
    column = 20

    tops = 10
    level = 1
    for_level = 20
    mode = False
    impossible = False
    speed = 0.4
    speed_limit = 0.05
    speed_acceleration = 0.03

    # Main Class
    class Tetris():
        def __init__(self, speed=.5, level=1, mode=False, bonus=0):
            self.field = ['·']*(row*column)
            self.active = 0
            self.rotate = 0
            self.tetrominos = {1:[1,1, 1,1], 2:[1,1,1,1, 0,0,0,0], 3:[1,0,0, 1,1,1], 4:[0,0,1, 1,1,1], 5:[0,1,1, 1,1,0], 6:[1,1,0, 0,1,1], 7:[0,1,0, 1,1,1] }
            self.next = self.get_tetromino()
            self.tetromino = []
            self.block = True
            self.can_rotation = True
            self.mode = mode
            self.bonus = bonus
            self.lines = 0
            self.lines_counter = 0
            self.point = 0
            self.level = level
            self.start_speed = speed
            self.can_skip = True
            self.speed = self.start_speed
            self.end = False

        def delete_I(self):
            self.tetrominos.pop(2)

        def get_tetromino(self):
            m = []
            for tetromino in self.tetrominos.values():
                m.append(tetromino)
            r = renpy.random.choice(m)
            return r

        def get_tetromino_i(self, i):
            return self.tetrominos.get(i)

        def clear(self, end=False):
            i = 0
            for cell in self.field:
                for color in coloring:
                    if cell == color:
                        self.field[i] = symb_field
                i += 1
            if end:
                self.end_turn()

        def delete(self):
            self.clear(end=True)
            self.bonus -= 1

        def draw_tetromino(self):
            self.clear()
            j = self.tetromino_index_start()
            i = 0
            for cell in self.tetromino:
                if cell:
                    # Tetromino O
                    if self.tetromino == [1,1, 1,1]:
                        self.field[self.active+j] = symb_yellow
                    # Tetromino I
                    elif self.tetromino == [1,1,1,1, 0,0,0,0] or self.tetromino == [0,0,0,0, 1,1,1,1]:
                        self.field[self.active+j] = symb_purple
                    # Tetromino J
                    elif self.tetromino == [1,0,0, 1,1,1] and not self.rotate or self.tetromino == [1,1,1, 0,0,1] and self.rotate == 180:
                        self.field[self.active+j] = symb_blue
                    elif self.tetromino == [1,1, 1,0, 1,0] and self.rotate == 90 or self.tetromino == [0,1, 0,1, 1,1] and self.rotate == 270:
                        self.field[self.active+j] = symb_blue
                    # Tetromino L
                    elif self.tetromino == [0,0,1, 1,1,1] and not self.rotate or self.tetromino == [1,1,1, 1,0,0] and self.rotate == 180:
                        self.field[self.active+j] = symb_orange
                    elif self.tetromino == [1,0, 1,0, 1,1] and self.rotate == 90 or self.tetromino == [1,1, 0,1, 0,1] and self.rotate == 270:
                        self.field[self.active+j] = symb_orange
                    # Tetromino S
                    elif self.tetromino == [0,1,1, 1,1,0] and not self.rotate or self.tetromino == [0,1,1, 1,1,0] and self.rotate == 180:
                        self.field[self.active+j] = symb_green
                    elif self.tetromino == [1,0, 1,1, 0,1] and self.rotate == 90 or self.tetromino == [1,0, 1,1, 0,1] and self.rotate == 270:
                        self.field[self.active+j] = symb_green
                    # Tetromino Z
                    elif self.tetromino == [1,1,0, 0,1,1] and not self.rotate or self.tetromino == [1,1,0, 0,1,1] and self.rotate == 180:
                        self.field[self.active+j] = symb_red
                    elif self.tetromino == [0,1, 1,1, 1,0] and self.rotate == 90 or self.tetromino == [0,1, 1,1, 1,0] and self.rotate == 270:
                        self.field[self.active+j] = symb_red
                    # Tetromino T
                    elif self.tetromino == [0,1,0, 1,1,1] and not self.rotate or self.tetromino == [1,1,1, 0,1,0] and self.rotate == 180:
                        self.field[self.active+j] = symb_cyan
                    elif self.tetromino == [1,0, 1,1, 1,0] and self.rotate == 90 or self.tetromino == [0,1, 1,1, 0,1] and self.rotate == 270:
                        self.field[self.active+j] = symb_cyan

                j = self.tetromino_index_count(j, i)
                i += 1

        def new(self):
            self.line_checker()

            self.rotate = 0
            self.active = self.center()
            self.tetromino = self.next
            self.next = self.get_tetromino()

            self.draw_tetromino()
            self.block = False
            self.can_rotation = True

        def move(self):
            if self.check_let(offset=row*2):
                self.slow()

            if self.check_let():
                self.end_turn()
                return

            self.active += row
            self.draw_tetromino()

        def shift(self, line):
            for l in reversed(range(1, line+1)):
                a = l*row
                b = a+row
                c = (l-1)*row
                d = c+row 
                self.field[a:b] = self.field[c:d]
                self.field[c:d] = [symb_field]*row

        def fast(self):
            self.speed = speed_acceleration
        def slow(self):
            self.speed_update()
        def boost(self):
            if self.speed == speed_acceleration:
                self.slow()
            else:
                self.fast()

        def left(self):
            x = self.find_x_cell(left=True)
            if x > 0:
                if not self.check_let(offset=-1-row):
                    self.active -= 1
                    self.draw_tetromino()

        def right(self):
            x = self.find_x_cell(right=True)
            if x < row-1:
                if not self.check_let(offset=1-row):
                    self.active += 1
                    self.draw_tetromino()

        def find_x_cell(self, left=False, right=False):
            m = []
            i = 0
            x = 0
            for cell in self.field:
                for color in coloring:
                    if cell == color:
                        x,y = self.coordinate_index(i)
                        m.append(x) 
                i += 1

            if m != []:
                if left:
                    x = min(m)
                elif right:
                    x = max(m)

            return x

        def outward(self):
            j = self.tetromino_index_start()
            k = 0 
            for cell in self.tetromino:
                if cell:
                    i = self.active+j
                    x,y = self.coordinate_index(i)
                    xx, yy = self.coordinate()
                    if xx >= row-3:
                        if x == 0:
                            return True
                j = self.tetromino_index_count(j, k)
                k += 1
            return False

        def check_let(self, offset=0):
            j = self.tetromino_index_start()
            k = 0 
            for cell in self.tetromino:
                if cell:
                    i = (self.active+j)+row+offset
                    x,y = self.coordinate_index(i)
                    if y <= column-1:
                        for color in coloring:
                            if self.field[i] == color.lower():
                                return True
                    else:
                        return True
                j = self.tetromino_index_count(j, k)
                k += 1
            return False

        def check_let_for_skip(self, offset=0):
            j = self.tetromino_index_start()
            k = 0
            for cell in self.tetromino:
                if cell:
                    i = (self.active+j)+row+offset
                    x,y = self.coordinate_index(i)
                    if y <= column-1:
                        for color in coloring:
                            if self.field[i] == color.lower():
                                return self.active+offset
                    else:
                        return self.active+offset
                j = self.tetromino_index_count(j, k)
                k += 1

        def skip(self):
            self.can_skip = False
            for c in range(column):
                s = self.check_let_for_skip(offset=row*c)
                if s:
                    break

            self.active = s
            self.draw_tetromino()
            self.end_turn()

        def can_skip_reload(self):
            self.can_skip = True

        def tetromino_index_start(self):
            l = len(self.tetromino)
            j = 0 if l == 8 else -1
            return j

        def tetromino_index_count(self, j, i):
            l = len(self.tetromino)

            if self.rotate == 90:
                if i == 1 or i == 3:
                    j += row-2

            elif self.rotate == 180:
                if l == 6:
                    if j == 1:
                        j += row-3
                elif l == 8:
                    j += row-1

            elif self.rotate == 270:
                if i == 1 or i == 3:
                    j += row-2

            else:
                if l == 4:
                    if j == 0:
                        j += row-2
                elif l == 8:
                    pass

                else:
                    if j == 1:
                        j += row-3
            j += 1
            return j

        def coordinate(self):
            i = self.active
            y = i // row 
            x = i - y*row
            return x,y

        def coordinate_index(self, i):
            y = i // row 
            x = i - y*row
            return x,y

        def hardening(self):
            i = 0
            for cell in self.field:
                for color in coloring:
                    if cell == color:
                        self.field[i] = color.lower()
                i+=1

        def rotation(self):
            l = len(self.tetromino)
            temp = self.tetromino[:]
            temp_rotate = self.rotate

            if l == 8:
                self.rotate = 180 if not self.rotate else False
            elif l == 6:
                if not self.rotate:
                    self.rotate = 90
                    if self.tetromino == [1,0,0, 1,1,1]:
                        self.tetromino = [1,1, 1,0, 1,0]
                    elif self.tetromino == [0,0,1, 1,1,1]:
                        self.tetromino = [1,0, 1,0, 1,1]
                    elif self.tetromino == [0,1,1, 1,1,0]:
                        self.tetromino = [1,0, 1,1, 0,1]
                    elif self.tetromino == [1,1,0, 0,1,1]:
                        self.tetromino = [0,1, 1,1, 1,0]
                    elif self.tetromino == [0,1,0, 1,1,1]:
                        self.tetromino = [1,0, 1,1, 1,0]

                elif self.rotate == 90:
                    self.rotate = 180
                    if self.tetromino == [1,1, 1,0, 1,0]:
                        self.tetromino = [1,0,0, 1,1,1]
                    elif self.tetromino == [1,0, 1,0, 1,1]:
                        self.tetromino = [0,0,1, 1,1,1]
                    elif self.tetromino == [1,0, 1,1, 0,1]:
                        self.tetromino = [0,1,1, 1,1,0] 
                    elif self.tetromino == [0,1, 1,1, 1,0]:
                        self.tetromino = [1,1,0, 0,1,1]
                    elif self.tetromino == [1,0, 1,1, 1,0]:
                        self.tetromino = [0,1,0, 1,1,1]

                    self.tetromino = self.tetromino[::-1]
                
                elif self.rotate == 180:
                    self.rotate = 270
                    if self.tetromino == [1,1,1, 0,0,1]:
                        self.tetromino = [0,1, 0,1, 1,1]
                    elif self.tetromino == [1,1,1, 1,0,0]:
                        self.tetromino = [1,1, 0,1, 0,1]
                    elif self.tetromino == [0,1,1, 1,1,0]: 
                        self.tetromino = [1,0, 1,1, 0,1]
                    elif self.tetromino == [1,1,0, 0,1,1]:
                        self.tetromino = [0,1, 1,1, 1,0]
                    elif self.tetromino == [1,1,1, 0,1,0]:
                        self.tetromino = [0,1, 1,1, 0,1]

                else:
                    self.rotate = 0
                    self.tetromino = self.tetromino[::-1]

                    if self.tetromino == [1,1, 1,0, 1,0]:
                        self.tetromino = [1,0,0, 1,1,1]
                    elif self.tetromino == [1,0, 1,0, 1,1]:
                        self.tetromino = [0,0,1, 1,1,1]
                    elif self.tetromino == [1,0, 1,1, 0,1]:
                        self.tetromino = [0,1,1, 1,1,0]
                    elif self.tetromino == [0,1,1, 1,1,0]:
                        self.tetromino = [1,1, 0,0, 1,1]
                    elif self.tetromino == [1,0, 1,1, 1,0]:
                        self.tetromino = [0,1,0, 1,1,1]

            if self.check_let(offset=-row) or self.check_let() or self.outward():
                self.rotate = temp_rotate
                self.tetromino = temp[:]

            self.draw_tetromino()

        def center(self):
            return int(row/2)

        def stats_update(self, line):
            self.lines += line
            self.lines_counter += line
            if self.lines_counter >= for_level:
                self.level += 1
                self.point += 100 * self.level
                self.lines_counter -= for_level
                self.speed_update()
            point = 100 if line == 1 else 300 if line == 2 else 700 if line == 3 else 1500
            self.point += point
            if line == 4 and self.mode:
                self.bonus += 1
        
        def speed_update(self):
            self.speed = self.start_speed - (self.level*0.01) if self.start_speed - (self.level*0.01) > speed_limit else speed_limit

        def line_checker(self):
            checker = 0
            clear_line = 0
            for line in range(column):
                for cell in range(row):
                    
                    for color in coloring:
                        if self.field[(line*row)+cell] == color.lower():
                            checker += 1

                    if checker == row:
                        self.shift(line)
                        clear_line += 1
                checker = 0

            if clear_line > 0:
                renpy.vibrate(0.5)
                self.stats_update(clear_line)

        def highscore_update(self):
            if persistent.highscore == [] or self.point > persistent.highscore[-1]:
                persistent.highscore.append(self.point)
                persistent.highscore.sort(reverse=True)
                if len(persistent.highscore) > tops:
                    persistent.highscore = persistent.highscore[:tops]

        def end_checker(self):
            for c in range(row):
                for color in coloring:
                    if self.field[row+c] == color.lower():
                        self.end = True
                        break

        def end_turn(self):
            self.slow()
            self.can_rotation = False
            self.hardening()
            self.end_checker()
            self.point += self.level
            self.block = True
            if self.end:
                self.highscore_update()
                renpy.hide_screen('draw_tetris')
                renpy.show_screen('game_over')

        def restart(self):
            self.level = store.level
            self.mode = store.mode
            self.field = ['·']*(row*column)
            self.speed = self.start_speed
            self.active = 0
            self.block = True
            self.can_rotation = True
            self.lines_counter = 0
            self.lines = 0
            self.point = 0
            self.bonus = 0
            self.end = False
            self.speed_update()

    def draw_next(n):
        t = ''
        l = len(n)
        i = 0
        for cell in n:
            if cell:
                # O
                if n == [1,1, 1,1]:
                    t += '{image=UI/arcade/Tetris/yellow.webp}'
                # I
                elif n == [1,1,1,1, 0,0,0,0]:
                    t += '{image=UI/arcade/Tetris/purple.webp}'
                # J
                elif n == [1,0,0, 1,1,1]:
                    t += '{image=UI/arcade/Tetris/blue.webp}'
                # L
                elif n == [0,0,1, 1,1,1]:
                    t += '{image=UI/arcade/Tetris/orange.webp}'
                # S
                elif n == [0,1,1, 1,1,0]:
                    t += '{image=UI/arcade/Tetris/green.webp}'
                # Z
                elif n == [1,1,0, 0,1,1]:
                    t += '{image=UI/arcade/Tetris/red.webp}'
                # T
                elif n == [0,1,0, 1,1,1]:
                    t += '{image=UI/arcade/Tetris/cyan.webp}'
            else:
                t += '{image=UI/arcade/Tetris/empty.webp}'

            if l == 4:
                if i == 1:
                    t += '\n'
            elif l == 6:
                if i == 2:
                    t += '\n'            
            elif l == 8:
                if i == 3:
                    t += '\n'            
            i+=1

        return t

    key_left = False
    key_right = False
    import pygame
    class KeyCatcher(renpy.Displayable):
        def render(self,w,h,st,at):
            return Null().render(w,h,st,at)
        def event(self, event, x, y, st):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    store.key_left = True
                elif event.key == pygame.K_RIGHT:
                    store.key_right = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    store.key_left = False
                elif event.key == pygame.K_RIGHT:
                    store.key_right = False

    def brightness(image, b=0.2):
        return im.MatrixColor(image, im.matrix.brightness(b))

image im_key = KeyCatcher()

### TETRIS DRAW SCREEN ###
screen draw_tetris():

    textbutton "Abandonner":
        xpos 0.05
        ypos 0.4
        background '#011400' 
        hover_background '#004303'
        text_style "terminal_button"
        action Confirm("Souhaites-tu vraiment abandonner ?",[Hide("draw_tetris"), ToggleScreen ('game_over')], Return(), frame_conf="gui/terminal_frame.webp")
    textbutton "Pause":
        xpos 0.05
        ypos 0.3
        background '#011400' 
        hover_background '#004303'
        text_style "terminal_button"
        action ShowMenu('preferences')

    frame xysize 750,940 align .5,.5:
        background Frame("gui/terminal_frame.webp")
        add 'im_key'
        add '#000000' size 550, 930 xpos 0
        frame xysize 35*row,35*column yalign .5 xalign .37:
            background Frame("gui/terminal_frame.webp")
            add "UI/arcade/Tetris/fond_tetris_[fond_tetris].jpg" align .5,.5 size 35*row,35*column

        vbox yalign .5 xalign .37:
            for clm in range(column):
                hbox:
                    for cell in tetris.field[row*clm : row*(clm+1)]:

                        if cell == symb_red or cell == symb_red.lower():
                            add 'UI/arcade/Tetris/red.webp'
                        elif cell == symb_green or cell == symb_green.lower():
                            add 'UI/arcade/Tetris/green.webp'
                        elif cell == symb_blue or cell == symb_blue.lower():
                            add 'UI/arcade/Tetris/blue.webp'

                        elif cell == symb_yellow or cell == symb_yellow.lower():
                            add 'UI/arcade/Tetris/yellow.webp'
                        elif cell == symb_cyan or cell == symb_cyan.lower():
                            add 'UI/arcade/Tetris/cyan.webp'
                        elif cell == symb_purple or cell == symb_purple.lower():
                            add 'UI/arcade/Tetris/purple.webp'
                        elif cell == symb_orange or cell == symb_orange.lower():
                            add 'UI/arcade/Tetris/orange.webp'

                        else:
                            add 'UI/arcade/Tetris/empty.webp'

        if renpy.variant("small"):
            $ vboxalign = (1.70, .2)
        else:
            $ vboxalign = (1.62, .2)

        vbox align vboxalign xsize 300:
            text 'NEXT' xanchor 1.0 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
            text '%s'%(draw_next(tetris.next)) xanchor 1.0 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
            
            null height 60
            
            text 'LEVEL' xanchor 1.0 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
            text '%s'%(tetris.level) xanchor 1.0 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
            text 'LINES' xanchor 1.0 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
            text '%s'%(tetris.lines) xanchor 1.0 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
            text 'SCORE' xanchor 1.0 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
            text '%s'%(tetris.point) xanchor 1.0 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
            
            text 'HIGHS' xanchor 1.0 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
            $ highscore = persistent.highscore[0] if persistent.highscore != [] else 0
            text '%s'%(highscore) xanchor 1.0 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
            
            if tetris.mode:
                null height 50
                text 'BONUS' xanchor 1.0 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
                text '%s'%(tetris.bonus) xanchor 1.0 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
            
            text "Original \n sDextra" xanchor 1.0 font "gui/DigitTech16-Regular.ttf" color "#00ff26"

    # ANDROID
    if renpy.variant("small"):
        button background 'gui/left.webp' hover_background brightness('gui/left.webp') xysize 250, 250 focus_mask True action Function(tetris.left) align .03,.9
        button background 'gui/right.webp' hover_background brightness('gui/right.webp') xysize 250, 250 focus_mask True action Function(tetris.right) align .195,.9
        button background 'gui/down.webp' hover_background brightness('gui/down.webp') xysize 250, 250 focus_mask True action Function(tetris.boost) align .81,.9
        button background 'gui/rotate.webp' hover_background brightness('gui/rotate.webp') xysize 250, 250 focus_mask True action If(tetris.can_rotation, Function(tetris.rotation)) align .97,.9
        if tetris.bonus:
            button background 'gui/bonus.webp' hover_background brightness('gui/bonus.webp') xysize 250, 250 focus_mask True action Function(tetris.delete) align .89,.5

    # PC
    else:
        if tetris.can_skip:
            key 'K_RETURN' action Function(tetris.skip)
        else:
            timer .2 action Function(tetris.can_skip_reload)
        if tetris.can_rotation:
            key 'mousedown_1' action Function(tetris.rotation)
            key 'K_UP' action Function(tetris.rotation)
        if tetris.bonus:
            key 'mousedown_2' action Function(tetris.delete)
            key 'K_SPACE' action Function(tetris.delete)
        
        key 'mousedown_3' action Function(tetris.boost)
        key 'mouseup_3' action Function(tetris.slow)
        key 'K_DOWN' action Function(tetris.boost)

        key 'K_RIGHT' action Function(tetris.right)
        if key_right:
            use keydown_right_move

        key 'K_LEFT' action Function(tetris.left)
        if key_left:
            use keydown_left_move

    use tetromino_animation

screen keydown_right_move():
    timer 0.05 repeat True action Function(tetris.right)
screen keydown_left_move():
    timer 0.05 repeat True action Function(tetris.left)
screen tetromino_animation():
    timer tetris.speed repeat True action If(tetris.block, Function(tetris.new), Function(tetris.move))

### GAME OVER SCREEN ###
screen game_over():
    vbox align (.5,.45) xsize 500:
        text 'GAME OVER' size 60 xalign .5 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
        text 'LEVEL - [tetris.level]' size 40 xalign .5 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
        text 'LINES - [tetris.lines]' size 40 xalign .5 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
        text 'SCORE - [tetris.point]' size 40 xalign .5 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
        null height 20
        $ i = 1
        for highscore in persistent.highscore:
            if highscore == tetris.point:
                text 'top [i] - [highscore]' size 45 xalign .5 color '#f00' font "gui/DigitTech16-Regular.ttf"
            else:
                text 'top [i] - [highscore]' size 40 xalign .5 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
            $ i += 1
    textbutton 'Reessayer' action [Hide('game_over'), Jump('tetris_reload')] align .5,.85 text_style "terminal_button"
    textbutton 'Retour' action [Hide('game_over'), ToggleScreen ('arcade')] align .5,.90 text_style "terminal_button"

label tetris_start:
    python:
        store.impossible = False
    show arcade_terminal
    call screen difficulty_choice
    jump tetris_start_2

label tetris_start_2:
    $ tetris = Tetris(speed=speed, mode=mode, level=level, bonus=0)
    $ tetris.speed_update()
    if impossible:
        $ tetris.delete_I()

    call screen draw_tetris

label tetris_reload:
    $ tetris.restart()
    call screen draw_tetris


init python:

    def set_mode_classic():
        store.fond_tetris = 1
        store.row = 10
        store.column = 20
        store.speed = 0.4
    def set_mode_new():
        store.fond_tetris = 2
        store.row = 12
        store.column = 25
        store.speed = 0.3
        store.mode = True
    def set_mode_hard():
        store.fond_tetris = 3
        store.row = 13
        store.column = 25
        store.speed = 0.2
        store.mode = True
    def set_mode_impos():
        store.fond_tetris = 4
        store.row = 15
        store.column = 26
        store.speed = 0.2
        store.impossible = True

label custom_tetris:
    python:
        store.fond_tetris = 5
        store.row = int(renpy.input("Combien de lignes ?", default = "20"))
        store.column = int(renpy.input("Combien de colonnes ?", default = "10"))
        store.speed = float(renpy.input("Quel temps de chute initial ?", default = "0.4"))
        store.impossible = True
    jump tetris_start_2

screen difficulty_choice():
    add "arcade_terminal"
    vbox align .5,.5 spacing 30:
        button background '#011400' hover_background '#004303' xysize 400,100 action Function(set_mode_classic), Return():
            text 'Classic' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
        button background '#011400' hover_background '#004303' xysize 400,100 action Function(set_mode_new), Return():
            text 'Normal' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
        button background '#011400' hover_background '#004303' xysize 400,100 action Function(set_mode_hard), Return():
            text 'Hardcore' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
        button background '#011400' hover_background '#004303' xysize 400,100 action Function(set_mode_impos), Return():
            text 'Impossible' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
        button background '#011400' hover_background '#004303' xysize 400,100 action Jump("custom_tetris"), Return():
            text 'Custom' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
    textbutton "> Retour":
        xpos 0.05
        ypos 0.5
        text_style "terminal_button"
        background '#011400' 
        hover_background '#004303'
        action [Hide('difficulty_choice'), ToggleScreen ('arcade')]

#################################################################################
# by sDextra 
#################################################################################
# 1110011 1000100 1100101 1111000 1110100 1110010 1100001
#################################################################################




init python:
    
    import os
    #config.log = os.path.join(config.gamedir, "test.log")

    # Set the default value.
    if persistent.autofinish is None:
        persistent.autofinish = True
    
    class ExplodeFactory: # the factory that makes the particles
        
        def __init__(self, theDisplayable, explodeTime=0, numParticles=10):
            self.displayable = theDisplayable
            self.time = explodeTime
            self.particleMax = numParticles
       
        def create(self, partList, timePassed):
                newParticles = None
                if partList == None or len(partList) < self.particleMax:
                    if timePassed < self.time or self.time == 0:
                        newParticles = self.createParticles()
                return newParticles
                
            
        def createParticles(self):
            timeDelay = renpy.random.random() * 0.6
            return [ExplodeParticle(self.displayable, timeDelay)]

        def predict(self):
            return [self.displayable]
    
    class ExplodeParticle:
 
           

        def __init__(self, theDisplayable, timeDelay):
            self.displayable = theDisplayable
            self.delay = timeDelay
            self.xSpeed = (renpy.random.random() - 0.5) * 25
            self.ySpeed = (renpy.random.random() - 0.5) * 25
            self.x = 640
            self.y = 360
        
        def update(self, theTime):
            
            if (theTime > self.delay):
                self.ySpeed += 0.2
                self.x += self.xSpeed
                self.y += self.ySpeed
                
                if self.x > 1280 or self.x < 0 or self.y > 720 or self.y < 0:
                    return None
        
            return (self.x, self.y, theTime, self.displayable)           

init:

    image bg table = "UI/arcade/solitaire_tapis.webp"
    image dim = "#00000088"
    image boom = Particles(ExplodeFactory("images/card/card_back.webp", numParticles=10, explodeTime = 5.0))  

    # Some styles for show text.
    $ style.centered_text.drop_shadow = (2, 2)
    $ style.centered_text.drop_shadow_color = "#000b"
  
label newgame_solitaire:
    scene bg table
    hide screen abandon_solitaire
    show dim
    with dissolve

    call screen game_choice

    $ k = _return
    
    
label start_game:

    python:
        k.set_sensitive(False)
        k.show()
    

label continue:
    hide dim
    with dissolve

screen abandon_solitaire:
    textbutton "Abandonner":
        xpos 0.1
        ypos 0.9
        background '#011400' 
        hover_background '#004303'
        text_style "terminal_button"
        action Confirm("Souhaites-tu vraiment abandonner ?", Jump("newgame_solitaire"), Jump("continue"), frame_conf="gui/terminal_frame.webp")

label quick_continue:
    
    while True:
        show screen abandon_solitaire
        python:
            k.set_sensitive(True)
            event = k.interact()

            if event:
                renpy.checkpoint()
            
        if event == "win":
            call screen game_over_solitaire

screen game_over_solitaire():
    add "dim"
    add "boom"
    vbox align (.5,.45) xsize 500:
        text 'Felicitations !' size 100 align .5, .5 font "gui/DigitTech16-Regular.ttf" color "#00ff26"
    textbutton 'Reessayer' action [Hide('game_over_solitaire'), Jump('newgame_solitaire')] align .5,.85 text_style "terminal_button"
    textbutton 'Retour' action [Hide('game_over_solitaire'), ToggleScreen ('arcade')] align .5,.90 text_style "terminal_button"
    
screen game_choice:
    add "arcade_terminal"
    #label "{size = 60} {color = '#00ff2f'} {font=gui/DigitTech16-Regular.ttf}- Klondide"
    text "Klondike" align .5,.25 size 50 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
    textbutton "> Par 1 ":
        xpos 0.3
        ypos 0.3
        background '#011400' 
        hover_background '#004303'
        text_style "terminal_button"
        action Return(Klondike(1))
    textbutton "> Par 3 ":
        xpos 0.3
        ypos 0.4
        background '#011400' 
        hover_background '#004303'
        text_style "terminal_button"
        action Return(Klondike(3))
    textbutton "> Double Par 1 ":
        xpos 0.5
        ypos 0.3
        background '#011400' 
        hover_background '#004303'
        text_style "terminal_button"
        action Return(DblKlondike(1))
    textbutton "> Double Par 3 ":
        xpos 0.5
        ypos 0.4
        background '#011400' 
        hover_background '#004303'
        text_style "terminal_button"
        action Return(DblKlondike(3))
    text "Spider" align .5,.53 size 50 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
    textbutton "> 1 suite":
        xpos 0.3
        ypos 0.57
        background '#011400' 
        hover_background '#004303'
        text_style "terminal_button"
        action Return((Spider(1)))
    textbutton "> 2 suite":
        xpos 0.5
        ypos 0.57
        background '#011400' 
        hover_background '#004303'
        text_style "terminal_button"
        action Return((Spider(2)))
    textbutton "> 4 suite":
        xpos 0.7
        ypos 0.57
        background '#011400' 
        hover_background '#004303'
        text_style "terminal_button"
        action Return((Spider(4)))
    text "Autre" align .5,.67 size 50 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
    textbutton "Perpetual Motion":
        xpos 0.3
        ypos 0.7
        background '#011400' 
        hover_background '#004303'
        text_style "terminal_button"
        action Return((Perpetual()))
    textbutton "Canfield":
        xpos 0.7
        ypos 0.7
        background '#011400' 
        hover_background '#004303'
        text_style "terminal_button"
        action Return((Canfield()))
    textbutton "> Retour":
        xpos 0.3
        ypos 0.85
        text_style "terminal_button"
        background '#011400' 
        hover_background '#004303'
        action [Hide('game_choice'), ToggleScreen ('arcade')]



init python:

    def set_mode_Easy():
        if renpy.variant('pc') or renpy.variant('web'):
            store.bombs = 109
        elif renpy.variant('mobile') or renpy.variant('touch'):
            store.bombs = 24
    def set_mode_Medium():
        if renpy.variant('pc') or renpy.variant('web'):
            store.bombs = 131
        elif renpy.variant('mobile') or renpy.variant('touch'):
            store.bombs = 29
    def set_mode_Hard():
        if renpy.variant('pc') or renpy.variant('web'):
            store.bombs = 164
        elif renpy.variant('mobile') or renpy.variant('touch'):
            store.bombs = 36
    def set_mode_Impos():
        if renpy.variant('pc') or renpy.variant('web'):
            store.bombs = 218
        elif renpy.variant('mobile') or renpy.variant('touch'):
            store.bombs = 48

screen difficulty_choice_mine():
    vbox align .5,.5 spacing 30:
        button background '#011400' hover_background '#004303' xysize 800,200 action Function(set_mode_Easy), Return():
            text 'Easy' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
        button background '#011400' hover_background '#004303' xysize 800,200 action Function(set_mode_Medium), Return():
            text 'Normal' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
        button background '#011400' hover_background '#004303' xysize 800,200 action Function(set_mode_Hard), Return():
            text 'Hardcore' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
        button background '#011400' hover_background '#004303' xysize 800,200 action Function(set_mode_Impos), Return():
            text 'Impossible' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"

#minesweeper
init python:
    
    import random

    class MinesweeperGame:

        def __init__(self, dimx, dimy, bombs):

            if dimx > dimy:

                self.dimx = dimx

                self.dimy = dimy

            else:

                self.dimx = dimy

                self.dimy = dimx

            self.bombs = bombs

            self.table = MinesweeperTileset(self.dimx, self.dimy, bombs)
            
            if renpy.variant('pc') or renpy.variant('web'):
                self.dim = 700//self.dimy
            elif renpy.variant('mobile') or renpy.variant('touch'):
                self.dim = 700//self.dimy

            self.colors = [u'#fff',u'#060afe',u'#388e3c',u'#d32f2f',u'#ba2fd3',u'#d38f2f',u'#2fbed3',u'#2fd38f',u'#f5e42b']


    class MinesweeperTileset:

        def __init__(self, dimx, dimy, bombs):

            self.explosion = False

            self.bombs = bombs

            self.opened = 0

            self.marked = 0

            self.tiles = []

            self.dimx = dimx

            self.dimy = dimy

            for i in range(dimy):

                self.tiles.append([])

                for j in range(dimx):

                    self.tiles[i].append(MinesweeperTile(posi = i, posj = j))

            self.pomlist = range(dimx*dimy)

            random.shuffle(self.pomlist)

            for i in range(bombs):

                ii = self.pomlist[i] // dimx
                jj = self.pomlist[i] % dimx

                self.tiles[ii][jj].bomb = True

                pomarr = self.getNeighbours(ii,jj)

                for x in pomarr:

                    x.num += 1

        def getNeighbours(self, posi, posj):

            nbrs = []

            if (posi == 0 and posj == 0):

                nbrs.append(self.tiles[posi+1][posj+1])
                nbrs.append(self.tiles[posi+1][posj])
                nbrs.append(self.tiles[posi][posj+1])

            elif (posi == 0 and posj == self.dimx - 1):

                nbrs.append(self.tiles[posi][posj-1])
                nbrs.append(self.tiles[posi+1][posj])
                nbrs.append(self.tiles[posi+1][posj-1])

            elif (posi == self.dimy - 1 and posj == 0):

                nbrs.append(self.tiles[posi-1][posj+1])
                nbrs.append(self.tiles[posi-1][posj])
                nbrs.append(self.tiles[posi][posj+1])

            elif (posi == self.dimy - 1 and posj == self.dimx - 1):

                nbrs.append(self.tiles[posi-1][posj-1])
                nbrs.append(self.tiles[posi-1][posj])
                nbrs.append(self.tiles[posi][posj-1])

            else:

                if posi == 0:

                    nbrs.append(self.tiles[posi+1][posj-1])
                    nbrs.append(self.tiles[posi+1][posj])
                    nbrs.append(self.tiles[posi+1][posj+1])
                    nbrs.append(self.tiles[posi][posj-1])
                    nbrs.append(self.tiles[posi][posj+1])

                elif posj == 0:

                    nbrs.append(self.tiles[posi-1][posj])
                    nbrs.append(self.tiles[posi+1][posj])
                    nbrs.append(self.tiles[posi-1][posj+1])
                    nbrs.append(self.tiles[posi][posj+1])
                    nbrs.append(self.tiles[posi+1][posj+1])

                elif posi == self.dimy - 1:

                    nbrs.append(self.tiles[posi-1][posj-1])
                    nbrs.append(self.tiles[posi-1][posj])
                    nbrs.append(self.tiles[posi-1][posj+1])
                    nbrs.append(self.tiles[posi][posj-1])
                    nbrs.append(self.tiles[posi][posj+1])

                elif posj == self.dimx - 1:

                    nbrs.append(self.tiles[posi-1][posj-1])
                    nbrs.append(self.tiles[posi][posj-1])
                    nbrs.append(self.tiles[posi+1][posj-1])
                    nbrs.append(self.tiles[posi-1][posj])
                    nbrs.append(self.tiles[posi+1][posj])

                else:

                    nbrs.append(self.tiles[posi-1][posj-1])
                    nbrs.append(self.tiles[posi-1][posj])
                    nbrs.append(self.tiles[posi-1][posj+1])
                    nbrs.append(self.tiles[posi][posj-1])
                    nbrs.append(self.tiles[posi][posj+1])
                    nbrs.append(self.tiles[posi+1][posj-1])
                    nbrs.append(self.tiles[posi+1][posj])
                    nbrs.append(self.tiles[posi+1][posj+1])

            return nbrs


        def open(self, posi, posj):

            self.tiles[posi][posj].opened = True

            self.opened += 1

            if self.tiles[posi][posj].bomb == True:

                self.explosion = True

            else:

                if not self.tiles[posi][posj].num:

                    pomarr = self.getNeighbours(posi,posj)

                    for x in pomarr:

                        if not x.opened:

                            self.open(posi = x.posi, posj = x.posj)


        def toggle(self, posi, posj):

            self.tiles[posi][posj].marked ^= True

            if self.tiles[posi][posj].marked:
                
                self.marked += 1

            else:

                self.marked -= 1 

        def force_open(self, posi, posj):

            nbrs = self.getNeighbours(posi,posj)

            pomnum = 0
            for x in nbrs:

                if x.marked:

                    pomnum+=1

            if pomnum == self.tiles[posi][posj].num:

                for x in nbrs:

                    if not x.opened and not x.marked:

                        self.open(posi = x.posi, posj = x.posj)

            # else:

            #     for x in nbrs:

            #         if not x.opened:

            #             x.hlight = True


            

    class MinesweeperTile:

        def __init__(self, posi, posj):

            self.posi = posi
            self.posj = posj

            self.bomb = False
            self.marked = False
            self.num = 0
            self.opened = False
            self.hlight = False


transform hlighttf():

    easeout 0.3 alpha 0.5
    easein 0.3 alpha 1.0

screen msw_screen(ms):

    modal True
    zorder 100

    textbutton "Abandonner":
        xpos 0.1
        ypos 0.2
        background '#011400' 
        hover_background '#004303'
        text_style "terminal_button"
        action Confirm("Souhaites-tu vraiment abandonner ?", [Hide("msw_screen"),Jump("exit_minesweeper")], NullAction(), frame_conf="gui/terminal_frame.webp")

    frame:
        background Frame("gui/terminal_frame.webp", gui.frame_borders, tile=gui.frame_tile)
        xalign 0.85
        yalign 0.2
        
        fixed:

            xsize 200
            ysize 100


            vbox:
                label "Bombs":
                    text_style "terminal_button"
                    xpos 0.1
                hbox:
                    xpos 0.3
                    text str(ms.table.marked) color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
                    text "/"
                    text str(ms.table.bombs) color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
    frame:
        background Frame("gui/terminal_frame.webp", gui.frame_borders, tile=gui.frame_tile)
        xalign 0.5
        yalign 0.82
    
        fixed:

            xsize 1700
            ysize 700
    
            for i in range(len(ms.table.tiles)):

                for j in range(len(ms.table.tiles[i])):

                    button:

                        xsize ms.dim
                        ysize ms.dim

                        xpos j * ms.dim
                        ypos i * ms.dim

                        if not ms.table.tiles[i][j].opened:
                            
                            background Transform('UI/arcade/Tetris/green.webp' , size=(ms.dim, ms.dim))
                            hover_background Transform('UI/arcade/Tetris/red.webp' , size=(ms.dim, ms.dim))
                            alternate [Function(ms.table.toggle, posi = i, posj = j)]
                            action [Function(ms.table.open, posi = i, posj = j)]
                            if ms.table.tiles[i][j].marked:

                                add Transform("UI/arcade/flag.webp", size=(ms.dim, ms.dim))

                            if ms.table.tiles[i][j].hlight:

                                at hlighttf

                                $ ms.table.tiles[i][j].hlight = False

                        else:

                            background u'#000000'
                            alternate [Function(ms.table.force_open, posi = i, posj = j)]
                            action [Function(ms.table.force_open, posi = i, posj = j)]
                            if ms.table.tiles[i][j].bomb:

                                add Transform("UI/arcade/mine.webp", size=(ms.dim, ms.dim))

                            elif ms.table.tiles[i][j].num:

                                text (str(ms.table.tiles[i][j].num)) xalign 0.5 yalign 0.5 color ms.colors[ms.table.tiles[i][j].num] font "gui/DigitTech16-Regular.ttf"


                        
                        #hovered []

    if ms.table.explosion:

        button:

            background u'#191316aa'
            xsize 1920
            ysize 1080

            action [Hide("msw_screen"),Confirm ("Souhaitez-vous continuer ?", Jump("minesweeper_start_2"), Jump("minesweeper_start"), frame_conf="gui/terminal_frame.webp")]

        vbox:
            xalign 0.5 
            yalign 0.5
            text "Game Over" align .5,.5 size 50 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"

    if ms.dimx*ms.dimy - ms.table.opened == ms.table.bombs:

        button:

            background u'#191316aa'
            xsize 1920
            ysize 1080

            action [Hide("msw_screen"),Confirm ("Souhaitez-vous continuer ?", Jump("minesweeper_start_2"), Jump("minesweeper_start"), frame_conf="gui/terminal_frame.webp")]

        vbox:
            xalign 0.5 
            yalign 0.5
            text "Victory" align .5,.5 size 50 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"

default bombs = 0
default dimx = 0
default dimy = 0

init python:
    def set_mode_Easy():
        if renpy.variant('pc') or renpy.variant('web'):
            store.bombs = 109
        elif renpy.variant('mobile') or renpy.variant('touch'):
            store.bombs = 24
    def set_mode_Medium():
        if renpy.variant('pc') or renpy.variant('web'):
            store.bombs = 131
        elif renpy.variant('mobile') or renpy.variant('touch'):
            store.bombs = 29
    def set_mode_Hard():
        if renpy.variant('pc') or renpy.variant('web'):
            store.bombs = 164
        elif renpy.variant('mobile') or renpy.variant('touch'):
            store.bombs = 36
    def set_mode_Impos():
        if renpy.variant('pc') or renpy.variant('web'):
            store.bombs = 218
        elif renpy.variant('mobile') or renpy.variant('touch'):
            store.bombs = 48

label custom_minesweeper:
    show arcade_terminal
    python:
        store.dimx = int(renpy.input("Combien de lignes ?", default = "10"))
        store.dimy = int(renpy.input("Combien de colonnes ?", default = "24"))
        store.bombs = int(renpy.input("Combien de bombes ?", default = "24"))
    jump minesweeper_start_2

screen difficulty_choice_mine():
    add "arcade_terminal"
    vbox align .5,.5 spacing 20:
        button background '#011400' hover_background '#004303' xysize 400,100 action Function(set_mode_Easy), Return():
            text 'Easy' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
        button background '#011400' hover_background '#004303' xysize 400,100 action Function(set_mode_Medium), Return():
            text 'Normal' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
        button background '#011400' hover_background '#004303' xysize 400,100 action Function(set_mode_Hard), Return():
            text 'Hardcore' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
        button background '#011400' hover_background '#004303' xysize 400,100 action Function(set_mode_Impos), Return():
            text 'Impossible' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
        button background '#011400' hover_background '#004303' xysize 400,100 action Jump("custom_minesweeper"), Return():
            text 'Custom' align .5,.5 size 60 color '#00ff2f' font "gui/DigitTech16-Regular.ttf"
    textbutton "> Retour":
        xpos 0.05
        ypos 0.5
        text_style "terminal_button"
        background '#011400' 
        hover_background '#004303'
        action [Hide('difficulty_choice_mine'), ToggleScreen ('arcade')]

label minesweeper_start:
    if renpy.variant('pc') or renpy.variant('web'):
        python:
            store.dimx = 21
            store.dimy = 52
    elif renpy.variant('mobile') or renpy.variant('touch'):
        python:
            store.dimx = 10
            store.dimy = 24
    call screen difficulty_choice_mine
    jump minesweeper_start_2

label minesweeper_start_2:
    $ msgame = MinesweeperGame(dimx = store.dimx ,dimy = store.dimy, bombs = store.bombs)   
    show screen msw_screen(ms = msgame)

label exit_minesweeper:
    scene
    call screen arcade