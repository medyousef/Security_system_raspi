# Security_system_raspi
Security system to detect burglers and send their picture with Email.
#requirement 
Raspberry PI 3 or higher, Raspberry  PI camera 1.3 or newer, a PIR Infrared Motion Sensor Detector Module HC-SR501
Consider changing/checking the directories adresses in the project.py file(PI username and folder names)
Change the sending Email here: yag= yagmail.SMTP("youssefraspitest@gmail.com", password)
change the receiver Email adress here yag.send(to='medyousef95@gmail.com')
Override the password file .email_password with a password GENERATED from the sending Account like in the video lin below:
https://www.youtube.com/watch?v=7UkAcIFrlGo
