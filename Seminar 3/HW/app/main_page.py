import flet as ft


class MainPage(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.welcome_text = ft.Text('Крестики-Нолики',
                                    size=24,
                                    weight="bold"
                                    )
        self.start_game = ft.ElevatedButton(
            text='Начать игру',
            on_click=lambda _: self.page.go("/game")
        )

    def build(self):
        return ft.Column(
            [
                self.welcome_text,
                self.start_game
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
