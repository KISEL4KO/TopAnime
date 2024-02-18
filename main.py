import flet as ft
from parser import init

#create list
anime = init()

#main pg
def main(page: ft.Page):
    page.title = "Top animes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    MainText = ft.Text(value='Top 5 Animes',color='green',size=25,italic=True, weight=ft.FontWeight.BOLD)

    #show text
    page.add(
        ft.Row(
            [
                MainText,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    #lisview
    lv = ft.ListView(expand=True, spacing=5)


    #func onClick for add  in listview el from list anime
    def onClick(e):
        for i in anime:
            lv.controls.append(ft.Text(f" {i}",text_align='CENTER',color='green',weight=ft.FontWeight.BOLD))
        page.update(lv)



    #show empty lv
    page.add(
        ft.Row(
            [
                lv
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    #show button with method onlick
    page.add(
        ft.Row(
            [
                ft.ElevatedButton("Click me!",on_click=onClick)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)