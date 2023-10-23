from random import choice
from time import sleep

import flet as ft


class GamePage(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.available_turns = 8
        self.player_text = ft.Text(
            'Сейчас ходит:',
            size=18,
            weight="bold"
        )
        self.exit_game = ft.ElevatedButton(
            text='Выйти',
            on_click=lambda _: self.page.go("/")
        )
        self.current_turn = self.drop_coin()
        self.game_board = self.get_board()
        self.bot_turn = ft.Text(
            'Компьютер - O',
            size=18,
            weight="bold",
            visible=True if self.current_turn == 'bot' else False
        )
        self.user_turn = ft.Text(
            'Пользователь - X',
            size=18,
            weight="bold",
            visible=True if self.current_turn == 'user' else False
        )
        self.start_game = ft.ElevatedButton(text='Начать сначала?', on_click=lambda _: self.page.go("/game"))

    def build(self):
        return ft.Column(
            [
                ft.Row(
                    [
                        self.player_text,
                        self.user_turn,
                        self.bot_turn
                    ]
                ),
                ft.Row(
                    self.game_board,
                    wrap=True,
                    width=240
                ),
                ft.Row(
                    [
                        self.exit_game,
                        self.start_game
                    ],
                    alignment='center',
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def get_board(self):
        buttons = []
        for _ in range(1, 10):
            temp = ft.Container(
                content=ft.Text(
                    value='',
                    color='black',
                    size=48,
                    weight='bold'
                ),
                # margin=10,
                # padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.GREEN_200,
                width=70,
                height=70,
                border_radius=10,
                ink=True,
                on_click=lambda e: self.user_action(e),
            )
            buttons.append(temp)
        if self.current_turn == 'bot':
            choice(buttons).content.value = 'O'
            choice(buttons).on_click = False
            self.available_turns -= 1
        return buttons

    def user_action(self, e):
        e.control.content.value = 'X'
        e.control.on_click = None
        self.available_turns -= 1
        if self.check_win():
            self.page.go(route="/win_page", winner=self.current_turn)
        else:
            self.current_turn = 'bot'
            self.bot_turn.visible = True
            self.user_turn.visible = False
            self.update()
            self.bot_action()

    def bot_action(self):
        sleep(0.3)
        if not self.available_turns:
            self.page.go("/win_page", winner='nobody')
        else:
            self.available_turns -= 1
            while True:
                e = choice(self.game_board)
                if e.content.value == 'X' or e.content.value == 'O':
                    continue
                break
            e.content.value = 'O'
            e.on_click = None
            if self.check_win():
                self.page.go("/win_page", winner=self.current_turn)
            else:
                self.current_turn = 'user'
                self.bot_turn.visible = False
                self.user_turn.visible = True
                self.update()

    def check_win(self):
        win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for combination in win_combinations:
            if (self.game_board[combination[0]].content.value == self.game_board[combination[1]].content.value
                    == self.game_board[combination[2]].content.value != ""):
                return True
        return False

    @staticmethod
    def drop_coin():
        return choice(['user', 'bot'])
