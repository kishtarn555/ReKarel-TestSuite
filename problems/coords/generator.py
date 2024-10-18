from KarelGenerator.KarelInput import KarelInputCase, EvalFlags,Point
from KarelGenerator.KarelOutput import KarelOutputCase

import os
sizes = [
    (5, 5),
    (15, 21),
    (35, 32),
    (10, 1),
    (1, 1),
    (2, 1),
    (1, 2),
    (35, 35),
]
directory = os.path.dirname(os.path.realpath(__file__))
for [idx,[w,h]] in enumerate(sizes):
    input = KarelInputCase(
        width=w,
        height=h,
        beeperBag=-1,
        evaluationFlags = EvalFlags.ALLBEEPERS
    )
    output = KarelOutputCase()
    for x in range(1, w+1):
        for y in range(1, h+1):
            output.setBeepers(Point(x, y), x*100+y)

    input.write(f"{directory}/cases/c{idx}.in")
    output.write(f"{directory}/cases/c{idx}.out",input = input)