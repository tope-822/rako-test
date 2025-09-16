import flet as ft

def main(page: ft.Page):
    page.title = "متابعة المناديب"
    page.vertical_alignment = ft.MainAxisAlignment.START

    mandoubs = []
    mandoub_list = ft.Column()

    name_input = ft.TextField(label="اسم المندوب", width=200)

    def add_mandoub(e):
        name = name_input.value.strip()
        if name:
            mandoub = {
                "name": name,
                "active": True
            }
            mandoubs.append(mandoub)
            mandoub_list.controls.append(
                ft.Row([
                    ft.Text(name),
                    ft.Switch(value=True, on_change=lambda ev, idx=len(mandoubs)-1: toggle_active(ev, idx)),
                    ft.Text("نشط", width=60)
                ])
            )
            name_input.value = ""
            page.update()

    def toggle_active(e, idx):
        mandoubs[idx]["active"] = e.control.value
        status = "نشط" if e.control.value else "غير نشط"
        mandoub_list.controls[idx].controls[2].value = status
        page.update()

    page.add(
        ft.Row([name_input, ft.ElevatedButton("إضافة", on_click=add_mandoub)]),
        ft.Text("قائمة المناديب:", style="headlineSmall"),
        mandoub_list
    )

ft.app(target=main)
