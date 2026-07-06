meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Una respuesta común a algo gracioso",
            "WTF": "una respuesta a algo que te sorprende",
            "WTh": "una respuesta a algo que te sorprende",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[world])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("palabra no encorntrada")
