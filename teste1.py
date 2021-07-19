import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [  [sg.Text('consultor de estoque')],
            [sg.Text('digite o item'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancelar')] ]

window = sg.Window('Armazem Rodrigues', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar': 
        break
    print('Você entrou com ', values[0])

window.close()