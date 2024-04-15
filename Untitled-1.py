import pygame
import random
import sys
percentage_list = [100,100,100,95,95,90,90,90,85,85,80,70,60,50,50,100,100]
price_list = [0,100,200,300,1000,3000,5000,10000,20000,50000,100000,1000000,2000000]
# Pygame 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 1500, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("검 강화 게임")

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 폰트 설정
font = pygame.font.Font(None, 36)

# 검 초기 레벨과 강화 확률 설정
initial_level = 1
max_level = 15
money = 10000
initial_chance = percentage_list[0]  # 초기 강화 확률
# 검 강화 함수
def enhance_sword(level, chance):
    global money
    # 레벨이 만렙에 도달하면 게임 종료
    if level >= max_level:
        return "Max level reached"
    
    # 강화 시도

    rand_num = random.randint(1, 100)
    money = money - price_list[level-1]
    if rand_num <= percentage_list[level-1]:
        print(percentage_list[level-1])
        print('eeee')
        return "Success"
    else:
        return "Failure"

# 결과 표시 함수
def show_result(result):
    result_text = font.render(f"강화 결과: {result}", True, BLACK)
    screen.blit(result_text, (WIDTH // 2 - 100, HEIGHT // 2))

# 메인 함수
def main():
    level = initial_level
    chance = initial_chance
    
    while True:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 스페이스 바를 눌렀을 때 검 강화 시도
                if event.key == pygame.K_SPACE:
                    if money >= price_list[level-1]:
                        result = enhance_sword(level, chance)
                        show_result(result)
                    else:
                        dedededed = font.render(f"돈이 부족해", True, BLACK)
                        screen.blit(dedededed, (WIDTH // 2 - 100, HEIGHT // 2))
                    # 강화 결과에 따라 레벨과 확률 조정
                    if result == "Success":
                        level += 1

                    elif result == "Failure":

                        level = 1
                        chance = 100 
                    else:
                        win_text = font.render("미친 운 개좋네", True, BLACK)
                        screen.blit(win_text,(WIDTH // 2 - 10, HEIGHT // 2))
                    
        
        # 화면 지우기
        screen.fill(WHITE)
        
        # 현재 레벨과 강화 확률 표시
        level_text = font.render(f"level: {level}", True, BLACK)
        money_text = font.render(f"money:{money}", True, BLACK)
        chance = percentage_list[level-1]
        chance_text = font.render(f"possibility: {chance}%", True, BLACK)
        screen.blit(level_text, (20, 20))
        screen.blit(chance_text, (20, 60))
        screen.blit(money_text,(10,100))
        
        # 화면 업데이트
        pygame.display.flip()

# 메인 함수 호출
if __name__ == "__main__":
    main()
