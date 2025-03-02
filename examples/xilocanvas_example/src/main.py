import flet as ft
import math

from xilocanvas import Xilocanvas
import flet.canvas as cv


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    stroke_paint = ft.Paint(stroke_width=2, style=ft.PaintingStyle.STROKE)
    fill_paint = ft.Paint(style=ft.PaintingStyle.FILL)

    image = ft.Image(
        src=f"https://picsum.photos/200/200?1",
        width=300,
        height=300
    )

    def on_cap(event):
        image.src_base64 = event.data
        image.update()

    xilocanvas = Xilocanvas(
        [
            cv.Circle(100, 100, 50, stroke_paint),
            cv.Circle(80, 90, 10, stroke_paint),
            cv.Circle(84, 87, 5, fill_paint),
            cv.Circle(120, 90, 10, stroke_paint),
            cv.Circle(124, 87, 5, fill_paint),
            cv.Arc(70, 95, 60, 40, 0, math.pi, paint=stroke_paint),
        ],
        width=float("inf"),
        expand=True,
        on_capture=on_cap
    )

    page.add(
        ft.Container(
            height=350,
            width=200,
            alignment = ft.alignment.center,
            bgcolor=ft.Colors.PURPLE_200,
            content=xilocanvas
        ),
        ft.ElevatedButton("PRINT", on_click= lambda x: xilocanvas.capture()),
        image
    )


ft.app(main)
