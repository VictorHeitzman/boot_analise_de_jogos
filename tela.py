from tkinter import *
import requests


def buscar_giros():
    giros = []
    data = requests.get('https://blaze.com/api/roulette_games/recent').json()[:5][::-1]
    for p, item in enumerate(data):
        giros.append([data[p]['color'],data[p]['roll']])

    print('passou 1')

    return giros

def return_cor_num(giros):
    info = []

    for item in giros:
        if item[0] == 1:
            info.append(['red','white',item[1]])
        elif item[0] == 2:
            info.append(['black','white',item[1]])
        else: info.append(['white','black',item[1]])
    
    print('passou 2')

    return info

def atualizar():
    dados_blaze = buscar_giros()
    info = return_cor_num(dados_blaze)

    n1.config(text=info[0][2])
    n2.config(text=info[1][2])
    n3.config(text=info[2][2])
    n4.config(text=info[3][2])
    n5.config(text=info[4][2])

    n1.config(background=info[0][0])
    n2.config(background=info[1][0])
    n3.config(background=info[2][0])
    n4.config(background=info[3][0])
    n5.config(background=info[4][0])

    cor_prev = ''

    if sum([num[1] for num in dados_blaze]) %2 == 0:
        cor_prev = 'black'
    else:
        cor_prev = 'red'
    
    print('passou 3')

    previsao = Label(height=2,width=96, bg=cor_prev)
    previsao.grid(row=3,column=0,columnspan=5)



root = Tk()

root.resizable(False,False)
root.title('bot_')

txt = Label(text='Giros Double Blaze', bg='black', fg='white', height=2,font='arial 11',width=96)
txt.grid(row=0,column=0,columnspan=5)

n1 = Label(text='', bg='gray', fg='white', height=5,font='arial 11',width=15)
n2 = Label(text='', bg='gray', fg='white', height=5,font='arial 11',width=15)
n3 = Label(text='', bg='gray', fg='white', height=5,font='arial 11',width=15)
n4 = Label(text='', bg='gray', fg='white', height=5,font='arial 11',width=15)
n5 = Label(text='', bg='gray', fg='white', height=5,font='arial 11',width=15)

n1.grid(row=1,column=0)
n2.grid(row=1,column=1)
n3.grid(row=1,column=2)
n4.grid(row=1,column=3)
n5.grid(row=1,column=4)


btn = Button(text='clique for reflash',
             height=2,
             width=96,
             font='arial 12',
             command=atualizar)
btn.grid(row=2,column=0,columnspan=5)



root.mainloop()