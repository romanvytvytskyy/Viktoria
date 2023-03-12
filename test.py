wals = sprite.Group()

w1 = Wall(...)
...
w_n = Wall(...)

wals.add(w1)
...
wals.add(w_n)


# In loop
wals.draw(mw)
groupcollide(hero, wals, False, False)


map1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

walls = []

if level1:
    level = map1


for i in level:
    for j in i:
        if i[j] == 1:
            w = Wall(50, 50, i*50, j*50)
            walls.append(w)

    for wall in walls:
        wall.draw_wall()

    if collide(treashure):
        level1 = False
        level2 = True
