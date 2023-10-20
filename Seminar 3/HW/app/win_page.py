import flet as ft


class WinPage(ft.UserControl):
    def __init__(self, winner):
        super().__init__()
        self.win_text = ft.Text('Пользователь победил!' if winner == 'user' else 'Компьютер победил!',
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
