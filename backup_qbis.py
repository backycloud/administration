#!/usr/local/bin/python
# -*- coding: utf-8 -*- # Поддержка в файле кириллицы
#Определеям модули
import os,time
import smtplib
import email.utils
import base64
from email.mime.text import MIMEText

#Потовый ящики
from_addr = 'test@test.ru'
to_addrs = 'test@test.ru'

#Определяем дату
DATESMTP = time.strftime(" %d %b %Y в %H:%M:%S")
DATE = time.strftime('%d.%m.%Y')

#Параметры авторизации
#username = 'admin'
#Дешифруем пароль
p = "R2NnaHk2NjY="
pwd = p.decode('base64')

#Поехали!
#Сохраняем нашу БД или все бд.
def mysql ():

  DES = '/home/admin/' #Директория куда покладутся сохранения

  BD = ">" + " " + DES + DATE + ".sql"

  os.system("mysqldump --all-databases -uroot -p"+" %pwd "+" "+BD+" ") #Сохраняем базы

mysql ()
#Сохраняем пользовательские диреткории
def user_files ():

  DES = "/home/admin/" # директория куда покладутся сохранения

  SORS = "/var/www/" # Что копировать

  FIL = DES + DATE + ".tar.bz2"

  os.system("tar -cjf"+" "+FIL+" "+SORS+" ") #Создаем архив

user_files()

def delete_old ():
  os.system ("find /home/admin/ -name *.tar.bz2 -mtime +14 -delete")
  os.system ("find /home/admin/ -name *.sql -mtime +14 -delete")

delete_old()#Тело письма
text = 'Резервация окончена:'+DATESMTP

#Указываем кодировку
msg = MIMEText(text, "", "utf-8")

#Создаем заголовок сообщения
msg['To'] = email.utils.formataddr(('Кому', to_addrs))
msg['From'] = email.utils.formataddr(('admin@admin.ru', from_addr))
msg['Subject'] = 'Резервация окончена!'

#Отправка письма по завершению.
server = smtplib.SMTP('mail.mail.ru:25')
server.starttls()
#server.login(username,pwd)
server.sendmail(from_addr, to_addrs, msg.as_string())
server.quit()
