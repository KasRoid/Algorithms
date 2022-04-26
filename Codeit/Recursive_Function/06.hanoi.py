# 이 게임의 목표는 왼쪽 기둥에 있는 원판들을 모두 오른쪽 기둥으로 옮기는 것 입니다.
# 지켜야 할 규칙은 두가지 입니다:
# 한 번에 하나의 원판만 옮길 수 있다.
# 큰 원판이 작은 원판 위에 있어서는 안 된다.

def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    other_peg = 6 - start_peg - end_peg
    if num_disks == 0:
        return
    hanoi(num_disks - 1, start_peg, other_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks - 1, other_peg, end_peg)


# 테스트 코드 (포함하여 제출해 주세요)
# hanoi(1, 1, 3)
# hanoi(2, 1, 3)
hanoi(3, 1, 3)
