from tkinter import *

russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
russian_alphabet_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
shifted = []
english_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
english_alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = ',!#$%&*+-=?@^_. '


def shift_is_valid(shift, language):
    if shift.isdigit():
        if language == 'russian' and 1 <= int(shift) <= 32:
            lbl_incorrect_format.configure(pady='-50', fg='LightSteelBlue3')
            return True
        elif language == 'english' and 1 <= int(shift) <= 26:
            lbl_incorrect_format.configure(pady='-50', fg='LightSteelBlue3')
            return True
        else:
            lbl_incorrect_format.configure(text='Unacceptable value', fg='red')
            lbl_incorrect_format.grid(column=1, row=7, sticky='nw')
            return False
    else:
        return False


def language_is_valid(language, text):
    if language == 'russian' and len(text) != 0:
        for l in range(len(text)):
            if text[l] in russian_alphabet or text[l] in russian_alphabet_upper:
                return True
    elif language == 'english' and len(text) != 0:
        for l in range(len(text)):
            if text[l] in english_alphabet or text[l] in english_alphabet_upper:
                return True
    else:
        return False


def validation(proc, lang, shift, text):
    counter = 0
    if proc == 0:
        counter += 1
        lbl_processNotChosen= Label(window, text='Should not be empty', fg='red', width='17', bg='LightSteelBlue3')
        lbl_processNotChosen.place(x=105, y=40)
    else:
        lbl_processNotChosen = Label(window, text='Should not be empty', fg='LightSteelBlue3', width='17', bg='LightSteelBlue3')
        lbl_processNotChosen.place(x=105, y=40)

    if lang == 0:
        counter += 1
        lbl_langNotChosen= Label(window, text='Should not be empty', fg='red', width='17', bg='LightSteelBlue3')
        lbl_langNotChosen.place(x=115, y=93)
    else:
        lbl_langNotChosen = Label(window, text='Should not be empty', fg='LightSteelBlue3', width='17', bg='LightSteelBlue3')
        lbl_langNotChosen.place(x=115, y=93)

    if len(shift) == 0:
        counter += 1
        lbl_incorrect_format.configure(text='Should not be empty', fg='red', width='17')
        lbl_incorrect_format.grid(column=1, row=7, sticky='nw')
    else:
        lbl_incorrect_format.configure(text='Should not be empty', fg='LightSteelBlue3', width='17')
        lbl_incorrect_format.grid(column=1, row=7, sticky='nw')

    if len(text) == 0:
        counter += 1
        lbl_incorrect_language.configure(text='Should not be empty', fg='red')
        lbl_incorrect_language.place(x=337, y=222)
    else:
        lbl_incorrect_language.configure(text='Should not be empty', fg='LightSteelBlue3', width='17')
        lbl_incorrect_language.place(x=337, y=222)
    return counter == 0



# после нажатия на кнопку Generate
def generate():
    proc = process_elected.get()
    lang = language_elected.get()
    shift = shift_number.get()
    text = phrase.get()
    
    if validation(proc, lang, shift, text):
        if proc == 1:
            process = 'encryption'
        elif proc == 2:
            process = 'decryption'

        if lang == 1:
            language = 'russian'
        if lang == 2:
            language = 'english'

        size = result.size()
        if size != 0:
            result.delete(0, size)

    # проверка на то, что число сдвига ограничено и для каждого языка свое ограничение
        if shift_is_valid(shift, language):
            lbl_incorrect_format.configure(text='Incorrect value', width='14', fg='LightSteelBlue3',
                                           bg='LightSteelBlue3')
        else:
            lbl_incorrect_format.configure(text='Incorrect value', width='20', fg='red')
            lbl_incorrect_format.grid(column=1, row=7, sticky='nw')

    # проверка на то, что выбранный язык и запись для шифрования/дешифрования одного языка
        if language_is_valid(language, text):
            lbl_incorrect_language.configure(text='Some letters are not in a language you chosen', fg='LightSteelBlue3')
        else:
            lbl_incorrect_language.configure(text='Some letters are not in a language you chosen', fg='red')
            lbl_incorrect_language.place(x=337, y=222)

        for i in range(len(text)):
            if text[i] in digits or text[i] in punctuation:
                shifted.append(text[i])
            else:
                if language == "russian":
                    if process == 'encryption':
                        if text[i] in russian_alphabet:
                            shifted.append(russian_alphabet[(russian_alphabet.find(text[i])) + int(shift)])
                        else:
                            shifted.append(russian_alphabet_upper[(russian_alphabet_upper.find(text[i])) + int(shift)])
                    if process == 'decryption':
                        if text[i] in russian_alphabet:
                            shifted.append(russian_alphabet[(russian_alphabet.find(text[i])) - int(shift)])
                        else:
                            shifted.append(russian_alphabet_upper[(russian_alphabet_upper.find(text[i])) - int(shift)])
                if language == "english":
                    if process == 'encryption':
                        if text[i] in english_alphabet:
                            shifted.append(english_alphabet[(english_alphabet.find(text[i])) + int(shift)])
                        else:
                            shifted.append(english_alphabet_upper[(english_alphabet_upper.find(text[i])) + int(shift)])
                    if process == 'decryption':
                        if text[i] in english_alphabet:
                            shifted.append(english_alphabet[(english_alphabet.find(text[i])) - int(shift)])
                        else:
                            shifted.append(english_alphabet_upper[(english_alphabet_upper.find(text[i])) - int(shift)])
        result.insert(END, ''.join(shifted))
        shifted.clear()



window = Tk()
window.title("Приложение Шифр Цезаря")
window.config(bg='LightSteelBlue3')
window.geometry('620x320')
lbl = Label(window, text=" Caesar text encryption and decryption", font=("Arial", 10, "bold"), bg='LightSteelBlue3',
            padx="10", pady="10")
lbl.grid(column=0, row=0)

# выбираем процесс
header = Label(text="Select process:", padx=10)
header.grid(row=1, column=0, sticky=W)
processes = [("encryption", 1), ("decryption", 2)]
process_elected = IntVar()
column = 0
for txt, val in processes:
    Radiobutton(text=txt, value=val, variable=process_elected, padx=5, pady=5, bg='LightSteelBlue3').\
        grid(column=column, row=2, sticky=W)
    column += 1

# выбираем язык
header2 = Label(text="Select language:", padx=10)
header2.grid(row=3, column=0, sticky=W)
languages = [("russian", 1), ("english", 2)]
language_elected = IntVar()
column = 0
for txt, val in languages:
    Radiobutton(text=txt, value=val, variable=language_elected, padx=5, pady=5, bg='LightSteelBlue3').\
        grid(column=column, row=4, sticky=W)
    column += 1

# выбираем shift
lbl_shift = Label(window, text='Put down a number (1,2,3...) - shift:', width='28', height='1')
lbl_shift.grid(column=0, row=6, sticky=W)
lbl_shift_recommend = Label(window, text='*for russian language - from 1 to 32, for english language - from 1 to 26',
                            font=("Arial", 8), bg='LightSteelBlue3', padx=5)
lbl_shift_recommend.grid(column=0, row=7, sticky=N)
shift_number = Entry(window)
shift_number.grid(column=1, row=6, sticky=W)

# вводим запись для шифрования/дешифрования
lbl_text = Label(window, text='Put down your text for encoding:', width='27', height='1')
lbl_text.grid(column=0, row=8, sticky=W, pady=15)
phrase = Entry(window, width='40')
phrase.grid(column=1, row=8, sticky=W, pady=5)

# кнопка Выполнить
btn_perform = Button(window, text="Generate", bg="gray", fg="black", command=generate)
btn_perform.place(x=442, y=240)

lbl_incorrect_format = Label(window, text='Incorrect value', width='14', bg='LightSteelBlue3')
lbl_result = Label(window, text='Result', font=("Arial", 10, "bold"), width='14', fg='black')
lbl_result.grid(column=0, row=10, sticky=W, pady=5, padx=2)
result = Listbox(window,  width='45', height='1')
result.place(x=3, y=270)
lbl_incorrect_language = Label(window, width='40', bg='LightSteelBlue3')



window.mainloop()
