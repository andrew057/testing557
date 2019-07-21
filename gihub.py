from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import datetime
import random
import time
import calendar
import mysql.connector
import pytz
import os
token = os.environ.get( 'BOT_TOKEN' )
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)
mas = [0]*13
mas[1] = "работа, слесарь-электрик"
mas[2] = "работа, машинист"
mas[3] = "работа, ремонт путей на зиле"
mas[4] = "работа, собеседование"
mas[5] = "работа, сотрудник сс"
mas[6] = "работа, пост на зиле"
mas[7] = "работа, диспетчер"
mas[8] = "работа, влажная уборка"
mas[9] = "афк, не у пк"
mas[10] = 'афк, перерыв'
mas[11] = "афк, рп сон"
mas[12] = 'афк, вне смены'
def findint( string ):
    for i in range(1,12 + 1):
        if mas[i] == string:
            return i
            break
def keyboardd(response):
    keyboard = VkKeyboard(one_time=False)
    if response == 'привет' or response=="старт":

        keyboard.add_button('Закрыть', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Репорт', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Спек', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('По уровню', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()
        keyboard.add_button('Информация по игре', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Жалобы', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()
        keyboard.add_button('Задать вопрос администрации', color=VkKeyboardColor.PRIMARY)
    elif response=="начать" or response == 'подтвердить' or response == 'вышел' or response =='убратьстатистику':
         
        keyboard.add_button('Закрыть', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button("Работа", color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Афк', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вышел', color=VkKeyboardColor.PRIMARY)        
    elif response=="работа":
        
        keyboard.add_button('Закрыть', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button("Работа, слесарь-электрик", color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button("Работа, машинист", color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button("Работа, ремонт путей на ЗИЛе", color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button("Работа, собеседование", color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button("Работа, сотрудник СС", color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button("Работа, пост на ЗИЛе", color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button("Работа, диспетчер", color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button("Работа, влажная уборка", color=VkKeyboardColor.NEGATIVE)
        
        keyboard.add_line()
        keyboard.add_button('Подтвердить', color=VkKeyboardColor.PRIMARY)
        
        keyboard.add_line()
        keyboard.add_button('УбратьСтатистику', color=VkKeyboardColor.PRIMARY)
    elif response=="афк":
        
        keyboard.add_button('Закрыть', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button("Афк, не у ПК", color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('Афк, перерыв', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button("Афк, РП сон", color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('Афк, вне смены', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Подтвердить', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('УбратьСтатистику', color=VkKeyboardColor.PRIMARY)
    elif response == 'закрыть':
        keyboard.add_button('Начать', color=VkKeyboardColor.DEFAULT)
        
        
    
        
   

    keyboard = keyboard.get_keyboard()
    return keyboard
'''def sqlQuery( query, number ):
   mySQLServer = "localhost\SQLExpress"
   myDatabase = "TestDb"
   connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + mySQLServer + ';'
                              'Database=' + myDatabase + ';')
   cursor = connection.cursor()
   cursor.execute(query)
   if number == 1:
       result = cursor.fetchall()
       return result
   if number == 2:
       connection.commit()
       cursor.close()
       connection.close()'''
def sqlQuery( query, number ):
   ps = os.environ.get( 'PASSWORD' )
   conn = mysql.connector.connect( host = '46.174.50.9', user = 'u8894_testonlik', password = str( ps ), database = 'u8894_testonlik' )
   cursor = conn.cursor()
   cursor.execute(query)
   if number == 1:
       result = cursor.fetchall()
       return result
   if number == 2:
       conn.commit()
       cursor.close()
       conn.close()
def tostring( string ):
    tmp = ''
    for i in range(0, len(string) - 1 ):
        if string[i]!=' ' or string[i+1] != ' ':
            tmp = tmp + string[i]
    if string[len(string) - 1] != ' ':
        tmp = tmp + string[len(string) - 1]
    return tmp
            
def proverka( string, number ):
    if number == 1 and string.find('работа') != -1:
        return -1
    
    elif number == 2 and string.find('афк') != -1:
        return -1
        
def beseda( id, number ):
    name = sqlQuery("Select nick from everyData WHERE id='"+str(id)+"'", 1 )
    if number == 1:
        string = '✅У игрока '+str(name[0][0])+' изменена статистика на '+str(tmpStatus)+'\nНа сервере работают: '
    elif number == 2:
        string = '⚠Игрок '+str(name[0][0])+' вышел с сервера.\nНа сервере работают: '
    workers = sqlQuery("Select nick from everyData where Works = '1'", 1 )
    i = 0
    while True:
        try:
            string = string + '\n'+ tostring( workers[i][0] )
            stata = sqlQuery("Select status from everyData where Nick = '"+str(tostring( workers[i][0] ))+"'", 1 )[0][0]
            print( stata )
            string = string + ' (' + mas[ int( stata ) ] +')'
            i = i + 1
        except Exception:
                break
    if i == 0:
        string = string + '\nНикто'
    i = 0
    string = string + '\n\nНа сервере в афк: '
    afk = sqlQuery("Select nick from everyData where Works = '0'", 1 )
    while True:
        try:
            string = string + '\n'+ tostring( afk[i][0] )
            stata = sqlQuery("Select status from everyData where Nick = '"+str(tostring( afk[i][0] ))+"'", 1 )[0][0]
            string = string + ' (' + tostring( mas[ int( stata ) ] ) +') '
            i = i + 1
        except Exception:
                break
    if i == 0:
        string = string +'\n'+'Никто'
    return string
def hoursMinutes():
    now = str( datetime.datetime.now(pytz.timezone("Europe/Moscow")) )
    res = now[11:16]
    return int( res[0:2] ) * 60 + int( res[3:5] )
def mounthDay():
    now = str( datetime.datetime.now(pytz.timezone("Europe/Moscow")) )[0:10]
    res = now[8:10] + '.' + now[5:7]
    return res
def counting(id, number):
    lastGoing = sqlQuery( "Select lastGoing from everyData where id = +'"+str( id ) + " ' ", 1 )
    if tostring ( str( lastGoing[0][0] ) ) != 'None' and int( number ) == 1:
        onlik = hoursMinutes() - int( lastGoing[0][0] )
        sqlQuery("UPDATE everyData SET lastGoing='None' WHERE id='"+str(id)+"'", 2 )
        tmpOnlik = sqlQuery( 'Select `'+str(mounthDay())+'`' +" from everyData where id = +'"+str( id ) + " ' ", 1)
        if tostring( str( tmpOnlik[0][0] ) ) == 'None':
            onlik = onlik + 1 - 1
        else:
            onlik = onlik + int( tmpOnlik[0][0] )
        sqlQuery('UPDATE everyData SET `'+str(mounthDay())+'`'+" = '"+str(onlik) + " 'WHERE id='"+str(id)+"'", 2 )
    if tostring( str( lastGoing[0][0] ) ) == 'None' and int( number ) == 2:
        sqlQuery("UPDATE everyData SET lastGoing='"+str(hoursMinutes())+"' WHERE id='"+str(id)+"'", 2 )
def statistic( id ):
    chislo = int( mounthDay().split('.')[0] )
    #chislo = 4
    mounth = int( mounthDay().split('.')[1] ) # now
    #mounth = 7
    regData = str ( tostring( sqlQuery( "select reg from everyData where id = '" + str( id ) + "'", 1 )[0][0] ) )
    print( regData )
    message = ''
    data = ''
    tmpMounth = int( regData.split('.')[1] ) # reg mounth
    if chislo >= 5:
        if mounth > tmpMounth:
            k = 1
        else:
            k = int( regData.split('.')[0] )
        for i in range( k, chislo + 1):
            if i < 10:
                data = '0'
            data = data + str(i)
            data = data + '.'
            if mounth < 10:
                data = data + '0'
            data = data + str( mounth )
            onlik = sqlQuery( 'select `'+str(data) +'`' +"from everyData where id = '"+str(id)+"'", 1 )
            if tostring( str (onlik[0][0]) ) == 'None':
                onlik = '0 hours, 0 minutes - ' + str( data )
            else:
                onlik = str( int( onlik[0][0] ) // 60 ) + ' hours, ' + str( int( onlik[0][0] ) % 60 ) + ' minutes - ' + str( data )
            data = ''
            message = message + onlik + '\n'
    else:
        print( tmpMounth )
        print( mounth )
        if tmpMounth == mounth - 1:
            k1 = int( regData.split('.')[0] )
            k2 = 1
        elif tmpMounth == mounth:
            k1 = calendar.monthrange(2019,mounth - 1)[1] + 1
            k2 = int( regData.split('.')[0] )
        else:
            k1 = 1
            k2 = 1
        print( k1 )
        print( k2 )
        for i in range( k1, calendar.monthrange(2019,mounth - 1)[1] + 1 ):
            if i < 10:
                data = '0'
            data = data + str(i)
            data = data + '.'
            if mounth < 10:
                data = data + '0'
            data = data + str( mounth - 1 )
            onlik = sqlQuery( 'select `'+str(data) +'`' +"from everyData where id = '"+str(id)+"'", 1 )
            if tostring( str (onlik[0][0]) ) == 'None':
                onlik = '0 hours, 0 minutes - ' + str( data )
            else:
                onlik = str( int( onlik[0][0] ) // 60 ) + ' hours, ' + str( int( onlik[0][0] ) % 60 ) + ' minutes - ' + str( data )
            data = ''
            message = message + onlik + '\n'
        for i in range( k2, chislo + 1 ):
            if i < 10:
                data = '0'
            data = data + str(i)
            data = data + '.'
            if mounth < 10:
                data = data + '0'
            data = data + str( mounth )
            onlik = sqlQuery( 'select `'+str(data) +'`' +"from everyData where id = '"+str(id)+"'", 1 )
            if tostring( str (onlik[0][0]) ) == 'None':
                onlik = '0 hours, 0 minutes - ' + str( data )
            else:
                onlik = str( int( onlik[0][0] ) // 60 ) + ' hours, ' + str( int( onlik[0][0] ) % 60 ) + ' minutes - ' + str( data )
            data = ''
            message = message + onlik + '\n'
            
    return message
def adminPlayer( id, nick ):
    try:
        adminZapros = sqlQuery( "Select Adminka from everyData where id = '"+str(id)+"'", 1 )
        adminZapros = tostring( str( adminZapros[0][0] ) )
    except Exception:
        adminZapros = 'No'
    try:
        zaprosExist = sqlQuery( "Select Nick from everyData where id = '"+str(nick)+"'", 1 )
        zaprosExist = tostring( str( zaprosExist[0][0] ) )
    except Exception:
        zaprosExist = ''
    return adminZapros, zaprosExist  
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            response=event.text.lower()
            keyboard = keyboardd(response)
            if  event.from_user and not event.from_me:
                zaprosChecking = sqlQuery( "Select Nick from everyData where id = +'"+str( event.user_id ) + " ' ", 1)
                if response == "начать":
                    if len(zaprosChecking) == 0:
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы еще не зарегистрированы!', 'random_id': 0})
                    else:
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Выберите пункт меню!', 'random_id': 0,'keyboard':keyboard})
                elif response.split(' ')[0]=='!зарегистрировать' and len( response.split(' ') ) == 3:
                    try:
                        zapros = sqlQuery( "Select Nick from everyData where id = +'"+str( event.text.split(' ')[1] ) + " ' ", 1)
                    except Exception:
                        zapros = ''
                    try:
                        zaprosadm = sqlQuery( "Select Adminka from everyData where id = +'"+str( event.user_id ) + " ' ", 1)
                        zaprosadm = tostring( zaprosadm[0][0] )
                    except Exception:
                        zaprosadm = 'Koz'
                    try:
                        tmpZapros = sqlQuery( "Select id from everyData where Nick = '"+str( event.text.split(' ')[2] ) + " ' ", 1)
                    except Exception:
                        tmpZapros = ''
                    if zaprosadm != 'Yes':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы не админ!', 'random_id': 0})
                    else:
                        if len( zapros ) != 0:
                            vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Игрок уже  зарегистрирован!', 'random_id': 0})
                        elif len( tmpZapros ) != 0:
                            vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Такой ник уже  зарегистрирован!', 'random_id': 0})
                        else:
                            sqlQuery("INSERT INTO everyData(Nick,id) VALUES ('"+str(event.text.split(' ')[2])+"','"+str(response.split(' ')[1])+"')", 2 )
                            vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Аккаунт зарегистрирован!', 'random_id': 0})
                            sqlQuery( "update everyData set reg = '" + str( mounthDay() ) + "' where id = '"+str(response.split(' ')[1])+"'", 2 )
                elif response.split(' ')[0]=='!убрать' and len( response.split(' ') ) == 2:
                    try:
                        zapros = sqlQuery( "Select Nick from everyData where id = +'"+str( response.split(' ')[1] ) + " ' ", 1)
                    except Exception:
                        zapros = ''
                    try:
                        zaprosadm = sqlQuery( "Select Adminka from everyData where id = +'"+str( event.user_id ) + " ' ", 1)
                        zaprosadm = tostring( zaprosadm[0][0] )
                    except Exception:
                        zaprosadm = 'Koz'
                    if zaprosadm != 'Yes':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы не админ!', 'random_id': 0}) 
                    else:
                        if len(zapros) == 0:
                            vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Такого игрока и так нет в базе!', 'random_id': 0})
                        else:
                            sqlQuery("DELETE FROM everyData where id ='"+str(response.split(' ')[1])+"'", 2 )
                            vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Удален!', 'random_id': 0})
                elif (response == 'вышел'):
                    lastGoing = sqlQuery( "Select lastGoing from everyData where id = +'"+str( event.user_id ) + "' ", 1 )
                    works = sqlQuery( "Select Works from everyData where id = +'"+str( event.user_id ) + "' ", 1)
                    print(str(works[0][0]))
                    if tostring( str(works[0][0]) )!='0' and tostring( str(works[0][0]) )!='1':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы не на сервере!', 'random_id': 0})
                    else:
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы успешно вышли!', 'random_id': 0,'keyboard':keyboard})
                        sqlQuery("UPDATE everyData SET Works=-1 WHERE id='"+str(event.user_id)+"'", 2 )
                        sqlQuery("UPDATE everyData SET Status='None' WHERE id='"+str(event.user_id)+"'", 2 )
                        vk_session.method('messages.send', {'chat_id': '1', 'message': str(beseda(event.user_id,2)), 'random_id': 0})
                    counting( event.user_id, 1 )
                elif (response.split(',')[0] == 'работа' or response.split(',')[0] == 'афк' or response == 'подтвердить' or response == 'вышел') and len(zaprosChecking) == 0:
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Зарегистрируйтесь!', 'random_id': 0})
                elif response == 'работа':
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Выберите несколько пунктов меню, в конце подтвердите!', 'random_id': 0,'keyboard':keyboard})
                elif response == 'афк':
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Выберите несколько пунктов меню, в конце подтвердите!', 'random_id': 0,'keyboard':keyboard})
                elif (response.split(',')[0] == 'работа' or response.split(',')[0] == 'афк') and response != 'работа' and response != 'афк':
                    try:
                        tmpStatus = str( sqlQuery( "select tmpStatus from everyData where id = '" +str(event.user_id) + "'", 1 )[0][0] )
                        tmpStatusNumber = int( tostring( tmpStatus ) )
                        tmpStatus = mas[tmpStatusNumber]
                    except Exception:
                        tmpStatus = 'None'
    
                    print( tmpStatus )
                    if tmpStatus != 'None':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Выбрать следует только что-то одно.\nСейчас у Вас выбрано:\n'+str(tmpStatus), 'random_id': 0})
                    else:
                        print( findint( str( response ) ) )
                        sqlQuery( "update everyData set tmpStatus = '" + str( findint( str( response ) ) ) + "' where id = '" + str(event.user_id) + "' ", 2 )
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы выбрали статус:\n'+str(response)+'\nДля отмены статуса введите "убратьстатистику"', 'random_id': 0})                    

                elif response == 'афк':
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Выберите соответствующие пункты меню!', 'random_id': 0,'keyboard':keyboard})
                elif response == 'подтвердить':
                    try:
                        tmpStatus = sqlQuery( "Select tmpStatus from everyData where id = +'"+str( event.user_id ) + " ' ", 1 )
                        tmpStatusNumber = int( tostring( str( tmpStatus[0][0] ) ) ) # номер статуса в массиве
                        tmpStatus = mas[tmpStatusNumber] # сам статус
                    except Exception:
                        tmpStatus = 'None'
                    if tostring( str(tmpStatus) ).split(',')[0] == 'афк':
                        sqlQuery("UPDATE everyData SET Works=0 WHERE id='"+str(event.user_id)+"'", 2 )
                        sqlQuery("UPDATE everyData SET tmpStatus='None' WHERE id='"+str(event.user_id)+"'", 2 )
                        sqlQuery("UPDATE everyData SET Status='"+str( tmpStatusNumber )+ "' WHERE id='"+str(event.user_id)+"'", 2 )
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы зашли со статусом "'+str(tmpStatus)+'"!', 'random_id': 0,'keyboard':keyboard})
                        vk_session.method('messages.send', {'chat_id': '1', 'message': str(beseda(event.user_id,1)), 'random_id': 0})
                        counting( event.user_id, 1 )
                    elif tmpStatus == None or str(tmpStatus)[0:4] == 'None':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Выберите статус!', 'random_id': 0})
                    else:
                        sqlQuery("UPDATE everyData SET Works=1 WHERE id='"+str(event.user_id)+"'", 2 )
                        sqlQuery("UPDATE everyData SET tmpStatus='None' WHERE id='"+str(event.user_id)+"'", 2 )
                        sqlQuery("UPDATE everyData SET Status='"+str(tmpStatusNumber)+ "' WHERE id='"+str(event.user_id)+"'", 2 )
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы зашли со статусом "'+str(tmpStatus)+'"!', 'random_id': 0, 'keyboard':keyboard})
                        vk_session.method('messages.send', {'chat_id': '1', 'message': str(beseda(event.user_id,1)), 'random_id': 0})
                        counting( event.user_id, 2 )
                elif response == 'закрыть':
                     vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы закрыли меню! Для начала счета онлайна наберите начать', 'random_id': 0, 'keyboard':keyboard})
                elif response.split(' ')[0] == '!назначитьадмина' and len( response.split(' ') ) == 2 and ( str( event.user_id ) == '414517334' or str( event.user_id ) == '405960444' ):
                    try:
                        query = sqlQuery( "Select Adminka from everyData where id = '"+str(response.split(' ')[1])+"'", 1 )
                        print( query[0][0] )
                    except Exception:
                        query = 'No'
                    try:
                        nick = sqlQuery( "Select Nick from everyData where id = '"+str(response.split(' ')[1])+"'", 1 )
                    except Exception:
                        nick = ''
                    if len(query) != 0:
                        query = tostring( str( query[0][0] ) )
                    if tostring( str( query ) ) == 'Yes':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'У этого игрока уже есть админка!', 'random_id': 0})
                    elif len( nick ) == 0:
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Этот игрок не зарегистрирован!', 'random_id': 0})
                    else:
                        sqlQuery( "update everyData set Adminka = 'Yes' where id = '"+str(response.split(' ')[1]) + "'", 2 )
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Админка выдана!', 'random_id': 0})
                elif response.split(' ')[0] == '!убратьадмина' and len( response.split(' ') ) == 2 and ( str( event.user_id ) == '414517334' or str( event.user_id ) == '405960444' ):
                    try:
                        query = sqlQuery( "Select Adminka from everyData where id = '"+str(response.split(' ')[1])+"'", 1 )
                        print( query[0][0] )
                    except Exception:
                        query = 'No'
                    try:
                        nick = sqlQuery( "Select Nick from everyData where id = '"+str(response.split(' ')[1])+"'", 1 )
                    except Exception:
                        nick = ''
                    if len(query) != 0:
                        query = tostring( str( query[0][0] ) )
                    if tostring( str( query ) ) != 'Yes':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'У этого игрока и так админки не было!', 'random_id': 0})
                    else:
                        sqlQuery( "update everyData set Adminka = 'No' where id = '"+str(response.split(' ')[1]) + "'", 2 )
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Админка забрана!', 'random_id': 0})
                elif response == '!моя статистика':
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': str(statistic(event.user_id)), 'random_id': 0})
                elif response.split(' ')[0] == '!статистика' and len( response.split(' ') ) == 2:
                    try:
                        id = tostring( str( sqlQuery( "select id from everyData where nick = '" + str( event.text.split(' ')[1] ) +"'", 1 )[0][0] ) )
                    except Exception:
                        id = ''
                    adminZapros, zaprosExist = adminPlayer( event.user_id, id )
                    if adminZapros != 'Yes':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы не админ!', 'random_id': 0})
                    else:
                        if len( zaprosExist ) == 0:
                            vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Такой игрок не зарегистрирован!', 'random_id': 0})
                        else:
                            vk_session.method('messages.send', {'user_id': event.user_id, 'message': str( statistic(id ) ), 'random_id': 0})
                elif response.split(' ')[0] == '!специальновышел' and len( response.split(' ') ) == 2:
                    adminZapros, zaprosExist = adminPlayer( event.user_id, response.split(' ')[1] )
                    if adminZapros != 'Yes':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы не админ!', 'random_id': 0})
                    else:
                        if len( zaprosExist ) == 0:
                            vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Такой игрок не зарегистрирован!', 'random_id': 0})
                        else:
                            try:
                                onlik = sqlQuery( "Select Works from everyData where id = '"+str(response.split(' ')[1])+"'", 1 )
                                onlik = tostring( str( onlik[0][0] ) )
                            except Exception:
                                onlik = ''
                            if onlik != '1' and onlik != '0':
                                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Такой игрок не на сервере!', 'random_id': 0})
                            else:
                                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Такой игрок принудительно вышел!', 'random_id': 0})
                                sqlQuery( "Update everyData set Works = '-1' where id = '"+str(response.split(' ')[1])+"'", 2 )
                                sqlQuery( "Update everyData set Status = 'None' where id = '"+str(response.split(' ')[1])+"'", 2 )
                                vk_session.method('messages.send', {'chat_id': '1', 'message': str( beseda( response.split(' ')[1], 2 ) ), 'random_id': 0})
                                counting( response.split(' ')[1], 1 )
                elif response == 'убратьстатистику':
                    try:
                        tmpStatus = sqlQuery( "Select tmpStatus from everyData where id = '"+str(event.user_id)+"'", 1 )
                        tmpStatusNumber = int( tostring( str( tmpStatus[0][0] ) ) )
                        tmpStatus = mas[tmpStatusNumber]
                    except Exception:
                        tmpStatus = 'None'
                    print( tmpStatus )
                    if str( tmpStatus ) != 'None':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы обнулили то, что выбрано!', 'random_id': 0,'keyboard':keyboard})
                        sqlQuery( "Update everyData set tmpStatus = 'None' where id = '"+str(event.user_id)+"'", 2 )
                elif response.split(' ')[0] == '!изменитьник' and len( response.split(' ') ) == 3:
                    try:
                        nick = sqlQuery( "select nick from everyData where id = '" + str( response.split(' ')[1] ) +"'", 1 )
                        nick = tostring( str( nick[0][0] ) )
                    except Exception:
                        nick = ''
                    try:
                        adminka = sqlQuery( "select adminka from everyData where id = '" + str( event.user_id ) +"'", 1 )
                        adminka = tostring( str( adminka[0][0] ) )
                    except Exception:
                        adminka = ''
                    print( adminka )
                    if len( adminka ) == 0 or adminka == 'None':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы не админ!', 'random_id': 0})
                    elif len( nick ) == 0 or nick == 'None':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Такой id не зарегистрирован!', 'random_id': 0})
                    else:
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Good', 'random_id': 0})
                        sqlQuery( "update everyData set nick = '" + str( event.text.split(' ')[2] ) + "' where id = '" + str( response.split(' ')[1] ) + "'", 2 )
                elif response.split(' ')[0] == '!members' and len( response.split(' ') ) == 2:
                    try:
                        admin = sqlQuery( "select adminka from everyData where id = '" + str( event.user_id ) + "'", 1 )
                        admin = tostring( str( admin[0][0] ) )
                    except Exception:
                        admin = 'None'
                    if admin == 'Yes':
                        if response.split(' ')[1] == '2':
                            result = sqlQuery( "select nick from everyData where adminka ='Yes'", 1 )
                            string = 'Админы:\n'
                        else:
                            result = sqlQuery( "select * from everyData", 1 )
                            string = 'Все зарегистрированные:\n'
                        i = 0
                        while True:
                            try:
                                string = string + tostring( str( result[i][0] ) ) + '\n'
                                i = i + 1
                            except Exception:
                                break
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': str( string ), 'random_id': 0})
                    else:
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы не админ!', 'random_id': 0})
                elif response.split(' ')[0] == 'getdata' and len( response.split(' ') ) == 2:
                    try:
                        id = tostring( sqlQuery( "select id from everyData where nick = '" + str( event.text.split(' ')[1] ) + "'", 1 ) [0][0] )
                        x = vk_session.method('users.get', {'user_ids': str(id)})
                        string = 'Пользователь: ' + str(x[0]['first_name']) + ' ' + str( x[0]['last_name'] ) + '\nid: ' + str(id)
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': str(string), 'random_id': 0})
                    except Exception:
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Bad sintaxis', 'random_id': 0})
                else:
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Неверный синтаксис!', 'random_id': 0})
