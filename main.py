import flet as ft
from parser import init

#create list
anime = init()

#main pg
def main(page: ft.Page):
    page.title = "Top animes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    MainText = ft.Text(value='Top 5 Animes',color='blue',size=25,italic=True, weight=ft.FontWeight.BOLD)
    page.add(
        ft.Row(
            [
                MainText,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    # lisview
    lv = ft.ListView(expand=True, spacing=5)

    # func onClick for add  in listview el from list anime
    def onClick(e):
        for i in anime:
            lv.controls.append(ft.Text(f" {i}", text_align='CENTER', color='white', weight=ft.FontWeight.BOLD))
        page.update(lv)

    # show empty lv
    page.add(
        ft.Row(
            [
                lv
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    # show button with method onlick
    page.add(
        ft.Row(
            [
                ft.ElevatedButton("Click me!", on_click=onClick)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


    #func for route
    def route_change(e: ft.RouteChangeEvent):
        if e.route == '/store':
            page.clean()
            page.update()
            page.add(ft.Row(
                [
                    ft.Text(value='TopAnimeApp'),
                ],

                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row([
                ft.Text(value='A web application written in python using the Flet framework'),

            ],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.IconButton(
                        icon=ft.icons.HOME,
                        icon_color="blue400",
                        icon_size=20,
                        on_click=go_main,

                    ),

                ], alignment=ft.MainAxisAlignment.CENTER)
            )
        if e.route == '/main':
            page.clean()
            page.update()
            page.add(
                ft.Row(
                    [
                        MainText,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )
            page.add(
                ft.Row(
                    [
                        lv
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )

            # show button with method onlick
            page.add(
                ft.Row(
                    [
                        ft.ElevatedButton("Click me!", on_click=onClick)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )
            page.add(
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.EXPLORE,
                            icon_color="blue400",
                            icon_size=20,
                            on_click=go_store,

                        ),

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            )


    #func change route /main
    def go_main(e):
        page.route = "/main"
        page.update()

    # func change route /store
    def go_store(e):
        page.route = "/store"
        page.update()


    #add btn
    page.on_route_change = route_change
    page.add(
        ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.EXPLORE,
                    icon_color="blue400",
                    icon_size=20,
                    on_click=go_store,

                ),

            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    )

ft.app(target=main, route_url_strategy="hash")