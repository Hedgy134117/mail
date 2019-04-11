import smtplib
import PySimpleGUI as sg

# layout of GUI
layout = [
    # sender email
    [sg.Text("Your Email", size=(15, 1)), sg.InputText(key='semail')],
    # sender password
    [sg.Text("Your Passowrd", size=(15, 1)), sg.InputText(key='pass')],
    # receiver email
    [sg.Text("Receiver Email", size=(15, 1)), sg.InputText(key='remail')],
    # times to send
    [sg.Text("Times to Send", size=(15, 1)), sg.InputText(key='tts')],
    # subject of email
    [sg.Text("Subject of Email", size=(15, 1)), sg.InputText(key='subject')],
    # body of email
    [sg.Text("Body", size=(15, 1)), sg.InputText(key='body')],
    # send button
    [sg.Button("Send")]
]

# make the window
window = sg.Window("Email Sender").Layout(layout)

# connect to gmail server
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.connect("smtp.gmail.com", 465)

# infinite loop
while True:
    # every event is stored in the values dictionary
    event, values = window.Read()

    # if the send button is pressed
    if event == "Send":
        # print the sender email, password, and receiver email in console
        print(values['semail'], values['pass'], values['remail'])

        # login to the email, send the email to the receiver with the subject and body
        # for the amount of times that the user inputs
        for i in range(int(values['tts'])):
            server.login(values['semail'], values['pass'])
            server.sendmail(values['semail'], values['remail'],
                            ("Subject: %s\n%s" % (values['subject'], values['body'])))

    # if the user exits out of the window
    if event == None:
        # leave the server
        server.quit()

        # end the loop
        break

