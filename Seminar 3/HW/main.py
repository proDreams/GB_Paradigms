import flet as ft
from app.main_page import MainPage
from app.game_page import GamePage
from app.win_page import WinPage


def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    MainPage()
                ],
                padding=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER
                # scroll=ft.ScrollMode.AUTO
            )
        )
        if page.route == "/game":
            page.views.append(
                ft.View(
                    "/game",
                    [
                        GamePage()
                    ],
                    padding=20,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER
                    # scroll=ft.ScrollMode.AUTO
                )
            )
        if '/win_page' in page.route:
            page.views.append(
                ft.View(
                    "/win_page",
                    [
                        WinPage(str(page.route).split('=')[-1])
                    ],
                    padding=20,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER
                    # scroll=ft.ScrollMode.AUTO
                )
            )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.title = "Крестики-Нолики"
    page.window_width = 350
    page.window_height = 380
    # page.window_resizable = False
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == "__main__":
    ft.app(
        target=main,
    )
