import flet as ft


class WinPage(ft.UserControl):
    def __init__(self, winner):
        super().__init__()
        if winner == 'user':
            self.winner = 'Пользователь победил!'
        elif winner == 'bot':
            self.winner = 'Компьютер победил!'
        else:
            self.winner = 'Ничья!'
        self.win_text = ft.Text(self.winner,
                                size=18,
                                weight="bold"
                                )
        self.start_game = ft.ElevatedButton(text='Начать сначала?', on_click=lambda _: self.page.go("/game"))

    def build(self):
        return ft.Column(
            [
                self.win_text,
                self.start_game
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
