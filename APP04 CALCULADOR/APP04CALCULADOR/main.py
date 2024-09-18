import flet as ft


def main(page: ft.Page):
    page.title="Calculadora"
    page.bgcolor="red"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    lbl1=ft.texT("Calculadora",
                style=ft.TextStyle(size=50,weight="bold"))
    


ft.app(main)
