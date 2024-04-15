import pygame
import random
import sys

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
max_level = 100
initial_chance = 100  # 초기 강화 확률
chance_decrease_rate = 1  # 강화 확률이 1%씩 감소하도록 설정

# 검 강화 함수
def enhance_sword(level, chance):
    # 레벨이 만렙에 도달하면 게임 종료
    if level >= max_level:
        return "Max level reached"
    
    # 강화 시도
    rand_num = random.randint(1, 100)
    if rand_num <= chance:
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
                    result = enhance_sword(level, chance)
                    show_result(result)
                    
                    # 강화 결과에 따라 레벨과 확률 조정
                    if result == "Success":
                        level += 1
                        chance = max(0, chance - chance_decrease_rate)
                    elif result == "Failure":

                        level = 1
                        chance = 100 
        
        # 화면 지우기
        screen.fill(WHITE)
        
        # 현재 레벨과 강화 확률 표시
        level_text = font.render(f"level: {level}", True, BLACK)
        chance_text = font.render(f"possibility: {chance}%", True, BLACK)
        screen.blit(level_text, (20, 20))
        screen.blit(chance_text, (20, 60))
        
        # 화면 업데이트
        pygame.display.flip()

# 메인 함수 호출
if __name__ == "__main__":
    main()
