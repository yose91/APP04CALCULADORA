import flet as ft
def calc_suma(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(textNum2.value.strip())
        resultado=num1+num2
        lblResultado.value="Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
        
def calc_resta(textNum1,txtNum2,lblResultado):
    try
        num1


def main(page: ft.Page):
    page.title="Calculadora"
    page.bgcolor="green"
    
    txtNum1=ft.TextField(label="Ingresa el primer numero,color"="yellow")
    txtNum2=ft.TextField(label="ingresael segundo numero",color="yellow")
    lblResultado=ft.Text("Resultado: ",color="yellow")
    
    btnSuma=ft.ElevatedButton(text="+",on_click=on_calc_suma)
    btnResta=ft.ElevatedButton(text="-",on_click=on_calc_resta)
    btnMultiplicacion=ft.ElevatedButton(text="*",on_click=on_calc_multiplicacion)
    btnDivision=ft.ElevatedButton(text="/",on_click=on_calc_division)
    
    page.add(
        ft.Column(controls=[
            ft.Row(controls=[
                txtNum1,
                txtNum2,
            ],aligment="center"),
        ]),
        ft.Row(controls=[lblResultado],alignment="center"),
        ft.Row(controls=[
            btnSuma,
            btnResta,
            btnMultiplicacion,
            btnDivision,
        ],alignment="center")
    )
    


ft.app(main)


ft.app(main)
