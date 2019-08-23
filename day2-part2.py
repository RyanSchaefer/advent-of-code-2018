boxes = open("day2.txt", 'r').readlines()
flag = False
for i, box in enumerate(boxes):
    for obox in boxes[i+1:]:
        for i in range(len(box)):
            if box[i] != obox[i]:
                if flag:
                    flag = False
                    break
                flag = True
        if flag:
            print(box, obox)
            break