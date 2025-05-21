import pygame
import random

pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тест по программированию")
clock = pygame.time.Clock()

# Цвета и шрифты
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
FONT_SIZE = 36
BUTTON_WIDTH, BUTTON_HEIGHT = 300, 50
MARGIN = 20

# Класс для хранения вопросов
class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

# Вопросы по теме "Программирование"
questions_data = [
    ("Что такое переменная в программировании?",
     ["Место для хранения данных", "Функция для вычислений", "Тип данных"], 0),
    ("Какой язык программирования используется для разработки веб-сайтов?",
     ["Python", "JavaScript", "C++"], 1),
    ("Что означает термин 'отладка' (debugging)?",
     ["Создание программы", "Поиск и исправление ошибок", "Обучение модели"], 1),
    ("Что такое функция в программировании?",
     ["Объект данных", "Блок кода, выполняющий определённую задачу", "Тип переменной"], 1),
    ("Какой язык считается языком высокого уровня?",
     ["Assembler", "Python", "Machine Code"], 1)
]

# Преобразуем данные в объекты Question и перемешиваем их порядок
questions = [Question(qd[0], qd[1], qd[2]) for qd in questions_data]
random.shuffle(questions)

# Вспомогательные функции
def draw_text(surface, size, color, text, x, y):
    font = pygame.font.SysFont(None, size)
    label = font.render(text, True, color)
    rect = label.get_rect(center=(x, y))
    surface.blit(label, rect)

def draw_button(surface, x, y, width, height, text):
    # Заполняем кнопку светло-серым цветом для лучшей видимости
    pygame.draw.rect(surface, GRAY, (x,y,width,height))
    # Обводка кнопки черной линией
    pygame.draw.rect(surface, BLACK, (x,y,width,height), 2)
    draw_text(surface, FONT_SIZE -4 , BLACK, text, x + width //2 , y + height //2)

def show_question(question):
    selected_option_index = None
    hovered_option_index = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for i in range(len(question.options)):
                    x = WIDTH //2 - BUTTON_WIDTH //2
                    y = HEIGHT //4 + (i+1) * (BUTTON_HEIGHT + MARGIN)
                    button_rect = pygame.Rect(x,y,BUTTON_WIDTH,BUTTON_HEIGHT)
                    if button_rect.collidepoint(pos):
                        selected_option_index = i
                        if selected_option_index == question.correct_answer:
                            return True
                        else:
                            return False

        # Обновляем выделение при наведении курсора
        mouse_pos = pygame.mouse.get_pos()
        hovered_option_index = None
        for i in range(len(question.options)):
            x = WIDTH //2 - BUTTON_WIDTH //2
            y = HEIGHT //4 + (i+1) * (BUTTON_HEIGHT + MARGIN)
            button_rect = pygame.Rect(x,y,BUTTON_WIDTH,BUTTON_HEIGHT)
            if button_rect.collidepoint(mouse_pos):
                hovered_option_index = i

        screen.fill(WHITE)

        # Отрисовка вопроса
        draw_text(screen, FONT_SIZE -4 , BLACK,
                  question.question , WIDTH//2 , HEIGHT//4 - FONT_SIZE)

        # Отрисовка вариантов с подсветкой при наведении или выборе
        for i, option in enumerate(question.options):
            x = WIDTH //2 - BUTTON_WIDTH //2
            y = HEIGHT //4 + (i+1) * (BUTTON_HEIGHT + MARGIN)

            # Цвет фона кнопки: светло-серый или чуть темнее при наведении/выборе
            if i == hovered_option_index:
                bg_color = (180, 180, 180)
            elif i == selected_option_index:
                bg_color = (150, 150, 150)
            else:
                bg_color= GRAY

            # Рисуем кнопку с выбранным цветом фона
            pygame.draw.rect(screen,(bg_color), (x,y,BUTTON_WIDTH,BUTTON_HEIGHT))
            pygame.draw.rect(screen,(0), (x,y,BUTTON_WIDTH,BUTTON_HEIGHT),2)
            draw_text(screen,FONT_SIZE -4 , BLACK,
                      str(i+1)+". "+option , x + BUTTON_WIDTH//2 , y + BUTTON_HEIGHT//2)

        pygame.display.update()
        clock.tick(60)

# Основные переменные
current_question_idx=0
score=0

# Основной цикл игры
running=True

while running:
    if current_question_idx >= len(questions):
        if score > len(questions) / 2:
            verdict = "Отлично!"
        elif score == len(questions) / 2:
            verdict = "Неплохо!"
        else:
            verdict = "Попробуйте еще раз"

        screen.fill(WHITE)
        final_score_text = f"Ваш результат: {score} из {len(questions)} - {verdict}"
        draw_text(screen, FONT_SIZE * 2, BLACK, final_score_text, WIDTH // 2, HEIGHT // 2)
        pygame.display.update()
        # Ожидание закрытия окна или нажатия клавиши для выхода
        waiting_for_exit = True
        while waiting_for_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    waiting_for_exit = False
                    running = False
            clock.tick(60)
        break

    result= show_question(questions[current_question_idx])
    if result=='quit':
        running=False
        break
    elif result is True:
        score+=1

    current_question_idx+=1

pygame.quit()