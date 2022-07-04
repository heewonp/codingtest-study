import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = []
start = None # 시작 위치
monster_count = 0 # 몬스터 개체 수
box_count = 0 # 아이템 상자 개수
move = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]} # 이동
move_count = 0 # 총 턴 수
death_by = '' # 사망 원인
is_win = False # 보스 처치 여부
spike_damage = 5 # 가시 데미지 (기본 5, DX 장신구 있으면 1)
last_step = '.'

def user_hp_to_0(death, mon = None, mon_hp = None): # user의 hp가 0이 되었을 때
    if 'RE' in user['ACC']: # RE 장신구가 있으면
        user['ACC'].remove('RE') # 제거하고
        user['HP'] = user['MAX_HP'] # 체력 풀로
        global last_step
        last_step = '.'
        global index
        index = start # 시작 지점으로 이동
        if mon: # 몬스터에게 죽었으면 몬스터 체력도 초기화
            mon['HP'] = mon_hp
        return False
    else:
        global death_by
        user['HP'] = 0 # hp가 음수가 되지 않도록
        death_by = death # 원인 저장
        return True

for i in range(N): # grid 채우기
    line = list(input())
    for k in line:
        if k == '@': # 시작 위치가 있을 때
            j = line.index('@') # 위치를 찾고
            start = [i, j] # start에 저장
        if k == '&' or k == 'M': # 몬스터 개수 세기
            monster_count += 1
        if k == 'B':
            box_count += 1
    grid.append(line)
    
S = list(input()) # 이동 방법

monster = {}
for _ in range(monster_count): # 몬스터 정보 저장
    monster_info = input().split() # x, y, name, att, def, hp, exp
    monster[(int(monster_info[0]) - 1, int(monster_info[1]) - 1)] = {
        'name' : monster_info[2],
        'ATT' : int(monster_info[3]),
        'DEF' : int(monster_info[4]),
        'HP' : int(monster_info[5]),
        'EXP' : int(monster_info[6])
    }

item_box = {}
for _ in range(box_count): # 아이템 상자 저장
    box_info = input().split() # x, y, type, s
    item_box[(int(box_info[0]) - 1, int(box_info[1]) - 1)] = {
        'TYPE' : box_info[2],
        'S' : box_info[3]
    }
    
index = start

user = { # user 정보
    'LV' : 1,
    'HP' : 20,
    'MAX_HP' : 20,
    'ATT' : 2,
    'EQUIPPED_ATT' : 0,
    'DEF' : 2,
    'EQUIPPED_DEF' : 0,
    'EXP' : 0,
    'REQUIRED_EXP' : 5,
    'ACC' : []
}

for i in S: # 순서대로 수행
    if i == '\n':
        break
    move_count += 1
    next_x = index[0] + move[i][0] # 다음 단계의 x 위치
    next_y = index[1] + move[i][1] # 다음 단계의 y 위치
    next_index = [next_x, next_y]
    
    grid[index[0]][index[1]] = '.'
    # 다음 단계의 위치가 grid 안이거나 다음 단계가 벽이 아닐 때
    if 0 <= next_x < N and 0 <= next_y < M and grid[next_x][next_y] != '#':
        if last_step == '^':
            grid[index[0]][index[1]] = '^'
        index = next_index
    else: # 이전 단계를 한번 더 수행
        grid[index[0]][index[1]] = last_step
        
    if grid[index[0]][index[1]] == '.': # 빈 칸
        last_step = grid[index[0]][index[1]]
        grid[index[0]][index[1]] = '@'
        continue
    elif grid[index[0]][index[1]] == 'B': # 상자 칸
        if item_box[(index[0], index[1])]['TYPE'] == 'O': # 장신구 상자
            if item_box[(index[0], index[1])]['S'] in user['ACC'] or len(user['ACC']) == 4: # 이미 존재하는 장신구일 때 / 장신구 4개가 다 찼을 때
                last_step = '.'
                grid[index[0]][index[1]] = '@'
                continue
            user['ACC'].append(item_box[(index[0], index[1])]['S'])
            if item_box[(index[0], index[1])]['S'] == 'DX': # DX : 가시 데미지 1로 고정
                spike_damage = 1
        else: # 무기/방어구 상자
            if item_box[(index[0], index[1])]['TYPE'] == 'W': # 무기 상자
                user['EQUIPPED_ATT'] = int(item_box[(index[0], index[1])]['S'])
            else: # 방어구 상자
                user['EQUIPPED_DEF'] = int(item_box[(index[0], index[1])]['S'])
        last_step = '.'
        grid[index[0]][index[1]] = '@'
        continue
    elif grid[index[0]][index[1]] == '^': # 가시 칸
        last_step = grid[index[0]][index[1]]
        user['HP'] -= spike_damage # 가시 데미지 계산
        if user['HP'] <= 0: # hp가 0 이하로 떨어졌을 때
            if user_hp_to_0('^'):
                break
        grid[index[0]][index[1]] = '@'
    elif grid[index[0]][index[1]] == '&' or grid[index[0]][index[1]] == 'M': # 몬스터 / 보스 칸
        last_step = '.'
        p_mon = monster[(index[0], index[1])]
        mon_hp = p_mon['HP'] # RE 장신구 발동 시 몬스터 체력 초기화를 위해 체력 저장
        turn = 1
        if 'HU' in user['ACC'] and grid[index[0]][index[1]] == 'M': # HU 장신구 착용 중에 보스 조우 시 체력 완전 회복
            user['HP'] = user['MAX_HP']
        while user['HP'] > 0 and p_mon['HP'] > 0: # 둘 중 한쪽의 hp가 0 이하가 되기 전까지
            if turn % 2 == 1: # user가 선공
                if turn == 1 and 'CO' in user['ACC']: # CO 장신구 보유 시 첫 공격은 공격럭이 2배
                    if 'DX' in user['ACC']: # CO와 DX 장신구 동시 보유 시 첫 공격은 공격력이 3배
                        p_mon['HP'] -= max(1, 3 * (user['ATT'] + user['EQUIPPED_ATT']) - p_mon['DEF'])
                    else:
                        p_mon['HP'] -= max(1, 2 * (user['ATT'] + user['EQUIPPED_ATT']) - p_mon['DEF'])
                else:
                    p_mon['HP'] -= max(1, (user['ATT'] + user['EQUIPPED_ATT']) - p_mon['DEF'])
            else: # 몬스터 공격 턴
                if turn == 2 and 'HU' in user['ACC'] and grid[index[0]][index[1]] == 'M': # HU 장신구는 보스의 첫 공격을 무효화해준다
                    pass
                else:
                    user['HP'] -= max(1, p_mon['ATT'] - (user['DEF'] + user['EQUIPPED_DEF']))
            turn += 1
        if user['HP'] <= 0: # user의 hp가 먼저 0 이하로 떨어진 경우
            if user_hp_to_0(p_mon['name'], p_mon, mon_hp):
                break
        else: # 몬스터를 잡은 경우
            if 'EX' in user['ACC']: # EX 장신구가 있는 경우 경험치를 1.2배 얻음
                user['EXP'] += int(p_mon['EXP'] * 1.2)
            else:
                user['EXP'] += p_mon['EXP']
            if 'HR' in user['ACC']: # HR 장신구가 있으면 몬스터를 처치할 때마다 체력 3 회복 / 단, 최대 체력 이상으로는 회복 불가능
                user['HP'] = min(user['HP'] + 3, user['MAX_HP'])
            if user['EXP'] >= user['REQUIRED_EXP']: # 현재 경험치가 레벨업을 위한 경험치를 넘겼을 때
                user['LV'] += 1 # 레벨 1 증가
                user['EXP'] = 0 # 초과한 경험치는 그대로 소멸
                user['REQUIRED_EXP'] += 5 # 요구 경험치 5 증가
                user['MAX_HP'] += 5 # 최대 HP 5 증가
                user['HP'] = user['MAX_HP'] # HP 회복
                user['ATT'] += 2 # 공격력 / 방어력 2씩 증가
                user['DEF'] += 2
            if grid[index[0]][index[1]] == 'M': # 보스를 잡았을 때
                is_win = True # 게임 클리어
                grid[index[0]][index[1]] = '@'
                break
        grid[index[0]][index[1]] = '@'
            
for i in range(N): # 진행 완료 / 게임 클리어 / user 사망 시
    for j in range(M):
        print(grid[i][j], end='')
    print()
print(f'Passed Turns : {move_count}')
print(f'LV : {user["LV"]}')
print(f'HP : {user["HP"]}/{user["MAX_HP"]}')
print(f'ATT : {user["ATT"]}+{user["EQUIPPED_ATT"]}')
print(f'DEF : {user["DEF"]}+{user["EQUIPPED_DEF"]}')
print(f'EXP : {user["EXP"]}/{user["REQUIRED_EXP"]}')
if death_by == '^': # 가시
    print('YOU HAVE BEEN KILLED BY SPIKE TRAP..')
elif death_by != '': # 몬스터 
    print(f'YOU HAVE BEEN KILLED BY {death_by}..')
elif is_win: # 보스 처치
    print('YOU WIN!')
else: # 진행 완료
    print('Press any key to continue.')
