import streamlit as st  
# from SessionState import get  # muss zuerst installiert werden  
import requests  
from PIL import Image  
from io import BytesIO  
  
st.title('what makes you happy')  
  
if st.button('Neues Bild'):  
    response = requests.get('https://api.thecatapi.com/v1/images/search')  
    data = response.json()  
  
    image_url = data[0]['url']  
    response = requests.get(image_url)  
    image = Image.open(BytesIO(response.content))  
  
    st.image(image, caption='katzen-Bilder ♥', use_column_width=True)  

import streamlit as st  
  
st.title('tell me how your day was!')  
  
user_input = st.text_input("Schreiben Sie hier Ihre Antwort", key="input1")  
  
if user_input:  
    st.write(f"Sie haben geschrieben: {user_input}")  

# import streamlit as st  
import random  
  
st.title('langweile?')  
  
# Texteingabefeld  
user_input = st.text_input("Schreiben Sie hier Ihre Antwort")  
  
if user_input:  
    st.write(user_input)
  
#st.write('\n')  # Line break  

st.write('**Zahlraten-Spiel**')  
  
# Erzeugen Sie eine zufällige Zahl zwischen 1 und 100  
correct_number = random.randint(1, 100)  
  
# Lassen Sie den Benutzer eine Zahl eingeben  
user_guess = st.number_input('Raten Sie eine Zahl zwischen 1 und 100', step=1)  
  
if user_guess:  
    if user_guess > correct_number:  
        st.write('Zu hoch!')  
    elif user_guess < correct_number:  
        st.write('Zu niedrig!')  
    else:  
        st.write('Gratulation! Sie haben die richtige Zahl erraten!')  


  
# st.title('Tic Tac Toe Spiel')  
  
# # Session State erstellen  
# state = SessionState.get(board=[[" "]*3 for _ in range(3)], player="X")  
  
# # Spielbrett zeichnen und Klicks handhaben  
# for i in range(3):  
#     cols = st.beta_columns(3)  
#     for j in range(3):  
#         if cols[j].button(state.board[i][j], key=f"{i}{j}"):  
#             if state.board[i][j] == " ":  
#                 state.board[i][j] = state.player  
#                 state.player = "O" if state.player == "X" else "X"  
  
# # Überprüfen, ob jemand gewonnen hat  
# for player in ["X", "O"]:  
#     if any(  
#         all(state.board[i][j] == player for j in range(3)) or  # Zeilen  
#         all(state.board[j][i] == player for j in range(3)) or  # Spalten  
#         all(state.board[j][j] == player for j in range(3)) or  # Diagonale  
#         all(state.board[j][2-j] == player for j in range(3))   # Gegen-Diagonale  
#         for i in range(3)  
#     ):  
#         st.write(f"Spieler {player} hat gewonnen!")  
#         state.board = [[" "]*3 for _ in range(3)]  # Spielbrett zurücksetzen  
#         break  

("Brauchen sie hilfe in mathe?") 


  
num1 = st.number_input('Geben Sie die erste Zahl ein', value=0)  
num2 = st.number_input('Geben Sie die zweite Zahl ein', value=0)  
  
summe = num1 + num2  
  
st.write("Die Summe ist ", summe)  

  


option = st.selectbox('was ist ihre Lieblingsfarbe?:', ['1. lila ', '2. rosa', '3. pink '])  
st.write('Sie haben ausgewählt:', option) 



if st.checkbox('Klicken Sie mich an!'):  
    st.write('Checkbox ist ausgewählt')  
else:  
    st.write('Checkbox ist nicht ausgewählt') 

 
  

  

