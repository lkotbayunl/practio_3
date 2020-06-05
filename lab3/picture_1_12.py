from graph import *


# _______________blue_sky
def blue_sky():
    penColor(0, 0, 0)
    penSize(1)
    brushColor(117, 187, 253)
    rectangle(0, 0, 800, 800)


def grey_mountain():
    penColor(50, 50, 50)
    penSize(1)
    brushColor('grey')
    polygon([(0, 800),
             (0, 250), (75, 50),
             (150, 200), (175, 150),
             (225, 250), (350, 50),
             (450, 150), (500, 10),
             (800, 800)])


def green_field():
    counter = 0
    penColor(50, 50, 50)
    penSize(1)
    brushColor(100, 230, 100)
    List_of_corteges = [[0, 800]]
    for h in range(800):
        List_of_corteges.append([0, 350])
        for j in range(1):
            List_of_corteges[h][j] += h + 3
    for lift in range(100):
        if lift < 100:
            List_of_corteges[lift][1] -= counter
        if lift > 20:
            if lift < 80:
                List_of_corteges[lift][1] -= 2
        counter += 0.5
    for plato in range(100, 250):
        List_of_corteges[plato][1] = List_of_corteges[lift][1]
    for down in range(250, 300):
        List_of_corteges[down][1] = List_of_corteges[plato][1]
    for plato2 in range(300, 800):
        List_of_corteges[plato2][1] = 350
    List_of_corteges[0][0] = 0
    List_of_corteges[1][0] = 0
    List_of_corteges[800][1] = 800
    List_of_corteges[800][0] = 800
    polygon(List_of_corteges)


def lama():
    x1 = 185
    y1 = 302
    x2 = 198
    y2 = 300
    neck_y = 345
    neck_R = 14
    leg_R = 10
    leg_y = 475
    leg_y2 = 450
    R = 5
    penColor(220, 220, 220)
    penSize(1)
    brushColor(220, 220, 220)

    # ------HEAD----------
    circle(200, 320, 20)
    circle(217, 323, 14)
    # --------------------

    for counter in range(5):
        circle(x1, y1, R)
        circle(x2, y2, R)
        x1 -= 2
        y1 -= 3
        x2 -= 2
        y2 -= 3
        R -= 1
    for counter_neck in range(6):
        if counter_neck < 3:
            circle(198, neck_y, neck_R)
            neck_R += 2
        else:
            circle(198, neck_y, neck_R)
            neck_R -= 2
        neck_y += 15
    # ----------------BODY------------------
    circle(140, 450, 35)
    circle(115, 450, 25)
    circle(165, 450, 35)
    circle(190, 450, 25)
    # ---------------------------------------

    for counter_leg in range(6):
        if counter_leg < 2:
            circle(195, leg_y, leg_R)
            circle(133, leg_y, leg_R)
            circle(170, leg_y2, leg_R)
            circle(110, leg_y2, leg_R)
            leg_R += 1
        else:
            circle(195, leg_y, leg_R)
            circle(133, leg_y, leg_R)
            circle(170, leg_y2, leg_R)
            circle(110, leg_y2, leg_R)
            leg_R -= 2
        leg_y2 += 11
        leg_y += 11
        if counter_leg == 5:
            circle(202, leg_y - 5, 10)
            circle(140, leg_y - 5, 10)
            circle(177, leg_y2 - 5, 10)
            circle(117, leg_y2 - 5, 10)

    # --------EYES-------
    penColor(153, 153, 255)
    penSize(1)
    brushColor(180, 155, 255)
    circle(202, 317, 10)

    penColor(0, 0, 0)
    penSize(1)
    brushColor(0, 0, 0)
    circle(205, 316, 5)

    penColor(255, 255, 255)
    penSize(1)
    brushColor(255, 255, 255)
    circle(203, 314, 2)


def flowers(x: "coords between 400 and 450", y: "coords between 450 and 550"):
    # -----------WHITE-----------
    penColor(150, 150, 150)
    penSize(1)
    brushColor(255, 225, 255)
    circle(x, y - 12, 8)
    circle(x - 10, y - 10, 6)
    circle(x + 10, y - 10, 6)
    circle(x + 12, y, 8)
    circle(x + 10, y + 10, 6)
    circle(x, y + 12, 8)
    circle(x - 10, y + 10, 6)
    circle(x - 12, y, 8)

    # ------------YELLOW---------
    penColor(200, 200, 200)
    penSize(1)
    brushColor(240, 240, 0)
    circle(x, y, 9)
    # ---------------------------


def grass():
    penColor(70, 220, 50)
    penSize(1)
    brushColor(70, 200, 50)
    circle(430, 500, 80)
    flowers(450, 450)
    flowers(380, 480)
    flowers(400, 520)
    flowers(455, 550)


blue_sky()
grey_mountain()
green_field()
lama()
grass()
run()
