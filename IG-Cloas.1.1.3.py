import os
try:
    import requests 
    import telebot 
except ImportError as error:
    os.system('pip install requests')
    os.system('pip install pyTekegramBotAPI')
import requests
from telebot import types 
import time
import telebot 
import random
import base64
from concurrent.futures import ThreadPoolExecutor
import json
import datetime
a=0
b=0
l=0
k=0
list=[]
lisisdd= []
listid=[]
sessoin = []
couin = []
ids1 = []
log=[]
th1 =[25]
listm =[25]
idporg = '48932473310'
token = input('>> Token : ')
tim3 = None 
acctive = None
api3 = None
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def mess(message):
    global sessoin 
    if acctive == None :
        iddss(message,acctive)
    elif acctive == True :  
        if sessoin == None or sessoin == []:
            l1 = types.InlineKeyboardButton(text="تسجيل دخول",callback_data="l1")
            l2 = types.InlineKeyboardButton(text="اضف سيشن",callback_data="l2")
            l3 = types.InlineKeyboardMarkup(row_width=1)
            l3.add(l1,l2)
            message = bot.send_message(message.chat.id,"انت لم تقوم باضافة سيشن ايدي او عملية تسجيل دخول\nعليك اضافة السيشن او تسجيل الدخول حتى تتمكن من متابعة استخدام البوت",reply_markup=l3)
        elif sessoin !=None or sessoin !=[]:
            print(sessoin,ids1)
            m1 = types.InlineKeyboardButton(text="قسم الكلوز",callback_data="m1")
            i3 = types.InlineKeyboardButton(text="تغير الحساب ",callback_data="i3")
            m3 = types.InlineKeyboardButton(text="زيد كريم",url='https://t.me/BBMZZ')
            m4 = types.InlineKeyboardMarkup(keyboard=[[m1],[i3],[m3]])
            message = bot.send_message(message.chat.id,'*>> مرحبا بك في البوت المجاني الخاص بخدمات انستكرام\n>> البوت يعمل بواسطة زيد كريم\n>> رقم النسخة 1.1.3\n>> يمكنك الان اخيتار القسم الذي يناسبك*\n',parse_mode='markdown',reply_markup=m4)
    elif acctive == False:
        bot.send_message(message.chat.id,'انت محظور للاسف - تواصل @BBMZZ')
@bot.callback_query_handler(func=lambda call:True)
def ca(call):
    if call.data =="m1":
        o1 = types.InlineKeyboardButton(text="سحب لستة ايديات",callback_data="o1")
        o2 = types.InlineKeyboardButton(text="اكمال سحب لستة ايديات",callback_data="o2")
        ig = types.InlineKeyboardButton(text="طلب ملف الايديات",callback_data='ig')
        o4 = types.InlineKeyboardButton(text="اضف كلوز من ملف ايديات",callback_data='o4')
        o5 = types.InlineKeyboardButton(text="تلكرام",url="https://t.me/BBMZZ")
        o3 = types.InlineKeyboardMarkup(row_width=1)
        o3.add(o1,o2,o4,ig,o5)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="اختار من القائمة الرئسية التي تظهر امامك عزيزي المستخدم",reply_markup=o3)
    elif call.data == 'o1':
        ie = types.InlineKeyboardButton(text="القائمة الرئسية",callback_data="m1")
        i1 =types.InlineKeyboardMarkup(row_width=1)
        i1.add(ie)
        message = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ارسل اليوزر الذي تود سحب ايديات منة",reply_markup=i1)
        bot.register_next_step_handler(message,info,message.id)
    elif call.data == "o2":
        b1 = types.InlineKeyboardButton(text="القائمة الرئسية",callback_data='m1')
        b2 = types.InlineKeyboardMarkup(row_width=1)
        b2.add(b1)
        message = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ارسل كلمة ايدي الحساب  ",reply_markup=b2)
        bot.register_next_step_handler(message,comp)
    elif call.data =='ig':
        try:
            
            i8 = types.InlineKeyboardButton(text="حذف الملف",callback_data="i8")
            i9 = types.InlineKeyboardButton(text="القائمة الرئسية",callback_data='m1')
            i10 = types.InlineKeyboardMarkup(row_width=2)
            i10.add(i8,i9)
            bot.send_document(call.message.chat.id,open('ids.txt','rb'),caption="هذا الملف الخاص بك",reply_markup=i10)
        except FileNotFoundError as error:
            i5 = types.InlineKeyboardButton(text="القائمة الرئسية",callback_data='m1')
            i6 = types.InlineKeyboardMarkup(row_width=1)
            i6.add(i5)
            bot.edit_message_text(chat_id=call.messagechat.id,message_id=call.message.message_id,text="انت لا تملك ملف ايديات عزيزي",reply_markup=i6)
    elif call.data == 'i8':
        try:
            os.remove('ids.txt')
            bot.send_message(call.message.chat.id,"تم حذف الملف بشكل صحيح")
        except Exception as df:
            bot.send_message(call.message.chat.id,text="لم يتم العثور عللى ملف ids.txt")
    elif call.data =="l1":
            tele = types.InlineKeyboardButton(text='Telegram',url='https://t.me/BBMZZ')
            tee = types.InlineKeyboardMarkup(keyboard=[[tele]])
            message = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ارسل اسم المستخدم مع كلمة المرور بهذا النمط : \n\n\r               username:password",reply_markup=tee)
            w1 = True
            bot.register_next_step_handler(message,logiaddsessoin,message.id,w1)
    elif call.data == 'l2':
        tele = types.InlineKeyboardButton(text='Telegram',url='https://t.me/BBMZZ')
        tee = types.InlineKeyboardMarkup(keyboard=[[tele]])
        message = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ارسل السيشن ايدي الان من فضلك - ",reply_markup=tee)
        w1 = False
        bot.register_next_step_handler(message,logiaddsessoin,message.id,w1)
    elif call.data == 'i3':
        loginaout(call.message)
    elif call.data =="o4":
        kf = types.InlineKeyboardButton(text="القائمة الرئسية",callback_data="m1")
        kg = types.InlineKeyboardMarkup(row_width=1)
        kg.add(kf)
        message = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ارسل ملف ايديات من فضلك - يجب عليك تغير حسابك قبل بدء عملية الاضافة",reply_markup=kg)
        bot.register_next_step_handler(message,fike)
def fike(message):
    try:
        filename = message.document.file_name
        if ('.txt') in filename:
            namefile =filename
            fil = bot.get_file(message.document.file_id)
            dow = bot.download_file(fil.file_path)
            with open(filename,'wb') as f0:
                f0.write(dow)
            fil = bot.get_file(message.document.file_id)
            bot.send_message(message.chat.id,"يتم الاضافة الان ارسل كلمة : استعلام كلوز للحصول على النتائج")
            rad(message,filename)
    except AttributeError as eeror:
        bot.send_message(message.chat.id,"الملف المرسل لا يمكن قراء")
def rad(message,filename):
    try:
        opw = open(filename,'r').read().splitlines()
        thre(message,opw)
    except FileNotFoundError as error:
        bot.send_message(message.chat.id,'الملف المرسل خطا')
def thre(message,opw):
    global th1
    th3 = random.choice(th1)
    th = ThreadPoolExecutor(max_workers=th3)
    for idsx in opw:
        th.submit(kk,message,idsx)
def kk(message,idsx):
    global sessoin,ids1,a,b,l,k,listid
    sessoin1 = random.choice(sessoin)
    id3 = random.choice(ids1)
    headers = {
        'Host': 'i.instagram.com',
        'X-Ig-App-Locale': 'ar_AR',
        'X-Ig-Device-Locale': 'en_US',
        'X-Ig-Mapped-Locale': 'ar_AR',
        'X-Pigeon-Session-Id': 'UFS-180e3591-58c3-4962-9dee-efb266fe6097-0',
        'X-Pigeon-Rawclienttime': '1737115666.630',
        'X-Ig-Bandwidth-Speed-Kbps': '2503.000',
        'X-Ig-Bandwidth-Totalbytes-B': '462827',
        'X-Ig-Bandwidth-Totaltime-Ms': '202',
        'X-Ig-App-Startup-Country': 'IQ',
        'X-Bloks-Version-Id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07',
        'X-Ig-Www-Claim': 'hmac.AR0Yzt_9JliyviDGGI-m_t_NQOWmV2spUIunOl20E_3fXrsP',
        'X-Bloks-Is-Layout-Rtl': 'true',
        'X-Ig-Device-Id': '19390992-8663-4068-918f-06fb4ab64dac',
        'X-Ig-Family-Device-Id': '821d929f-4bad-446b-a3ef-00c84bcd8724',
        'X-Ig-Android-Id': 'android-cb1ca12d04193807',
        'X-Ig-Timezone-Offset': '28800',
        'X-Ig-Nav-Chain': 'AjV:self_profile:2:main_profile::,ProfileMediaTabFragment:self_profile:3:button::,Jh5:bottom_sheet_profile:4:button::,AZr:settings_category_options:5:button::,ASE:privacy_options:6:button::,Bye:reel_settings:7:button::,BnH:audience_selection:8:button::',
        'X-Fb-Connection-Type': 'WIFI',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'Priority': 'u=3',
        'User-Agent': 'Instagram 237.0.0.14.102 Android (28/9; 240dpi; 720x1280; Asus; ASUS_I003DD; ASUS_I003DD; intel; ar_AR; 373310554)',
        'Accept-Language': 'ar-AR',
        'Authorization': f'Bearer IGT:2:{sessoin1}',
        'Accept-Language': 'ar-AR',
        'Ig-U-Ig-Direct-Region-Hint': f'RVA,{id3},1768651505:01f752b0a03959901a9902b51f60c856f3e3cf1feda67d09924a43127ec6b1a5e33dac80',
        'Ig-U-Ds-User-Id': f'{id3}',
        'Ig-U-Rur': f'LDC,{id3},1768666317:01f774b866da6e7a48abfa5e75d18374c217242916e56f0fb96b4ffe62d720190bab1e7d',
        'Ig-Intended-User-Id': f'{id3}',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',

    }
    data = {
        'module': 'audience_selection',
        'source': 'story_settings',
        'user_id': '{}'.format(idsx),
        '_uuid': '19390992-8663-4068-918f-06fb4ab64dac',
    }
    response = requests.post(
        'https://i.instagram.com/api/v1/stories/private_stories/add_member/',
        headers=headers,
        data=data,
    )
    if ('"status":"ok"') in response.text:
        a+=1
    else:
        l+=1

def loginaout(message):
    l1 = types.InlineKeyboardButton(text="تسجيل دخول",callback_data="l1")
    l2 = types.InlineKeyboardButton(text="اضف سيشن",callback_data="l2")
    l3 = types.InlineKeyboardMarkup(row_width=1)
    l3.add(l1,l2)
    message = bot.send_message(message.chat.id,"انت الان في عملية تغير البيانات في البوت - عليك الاختيار من القائمة",reply_markup=l3)

def comp(message):
    global couin
    text = message.text
    couin.append(text)
    bot.send_message(message.chat.id,"سيتم السحب الان يمكنك الاستعلام عن طريق ارسال كلمة استعلام")
    comp2(message)
def comp2(message):
    global sessoin,ids1,a,k,b,l,couin
    ids = random.choice(couin)
    sessoin1 = random.choice(sessoin)
    id3 = random.choice(ids1)
    nex = open('next.txt','r').read().splitlines()
    m = random.choice(nex)
    headers = {
        'Host': 'i.instagram.com',
        'X-Ig-App-Locale': 'en_US',
        'X-Ig-Device-Locale': 'en_US',
        'X-Ig-Mapped-Locale': 'en_US',
        'X-Pigeon-Session-Id': 'UFS-be761504-ccb9-40cf-b8bc-56a901b70885-0',
        'X-Pigeon-Rawclienttime': '1737373531.463',
        'X-Ig-Bandwidth-Speed-Kbps': '-1.000',
        'X-Ig-Bandwidth-Totalbytes-B': '0',
        'X-Ig-Bandwidth-Totaltime-Ms': '0',
        'X-Ig-App-Startup-Country': 'IQ',
        'X-Bloks-Version-Id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07',
        'X-Ig-Www-Claim': 'hmac.AR1joUMvWD2nG91UXxZiX0VLg9gABvWtLCwQbvsgrz27FDVs',
        'X-Bloks-Is-Layout-Rtl': 'false',
        'X-Ig-Device-Id': '19390992-8663-4068-918f-06fb4ab64dac',
        'X-Ig-Family-Device-Id': 'f7b96f74-ddba-4f4a-95d7-36c8b29b51b0',
        'X-Ig-Android-Id': 'android-cb1ca12d04193807',
        'X-Ig-Timezone-Offset': '28800',
        'X-Ig-Nav-Chain': 'ExploreFragment:explore_popular:5:main_search::,SingleSearchTypeaheadTabFragment:search_typeahead:6:button::,UserDetailFragment:profile:7:search_result::,ProfileMediaTabFragment:profile:8:button::,FollowListFragment:followers:9:button::',
        'X-Fb-Connection-Type': 'WIFI',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'Priority': 'u=3',
        'User-Agent': 'Instagram 237.0.0.14.102 Android (28/9; 240dpi; 720x1280; Asus; ASUS_I003DD; ASUS_I003DD; intel; en_US; 373310554)',
        'Accept-Language': 'en-US',
        'Authorization': f'Bearer IGT:2:{sessoin1}',
        'X-Mid': 'Z44vlQABAAEinpr0-kiBOPPlJPFK',
        'Ig-U-Ds-User-Id': f'{id3}',
        'Ig-U-Rur': f'LDC,{id3},1768909531:01f74a731323c1118db160ad8fb67846e7365c51a6ead6fba0caec3b1312508437909dec',
        'Ig-Intended-User-Id': f'{id3}',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
    }

    params = {
        'search_surface': 'follow_list_page',
        'max_id': f'{m}',
        'query': '',
        'enable_groups': 'true',
        'rank_token': 'fd238b76-a9f8-40c6-bc71-f825bdf17b9b',
    }

    response = requests.get(
        f'https://i.instagram.com/api/v1/friendships/{ids}/followers/',
        params=params,
        headers=headers,
    )
    try:
            
        for tx in json.loads(response.text)['users']:
            k+=1
            username = tx['pk_id']
            with open('ids.txt','a') as f0:
                f0.write(f'{username}\n')
            print(username)
        if 'next_max_id' in response.text:
            kc = json.loads(response.text)['next_max_id']
            with open('next.txt','w') as f0:
                f0.write(f'{kc}\n')
            comp2(message)
        else:
            bot.send_message(message.chat.id,"تم الانتهاء من السحب ")
    except KeyError as error:
        headers = {
            'Host': 'i.instagram.com',
            'X-Ig-App-Locale': 'en_US',
            'X-Ig-Device-Locale': 'en_US',
            'X-Ig-Mapped-Locale': 'en_US',
            'X-Pigeon-Session-Id': 'UFS-0f2d61ec-08ad-45f2-b109-0f85d6ca2e2e-0',
            'X-Pigeon-Rawclienttime': '1737382707.994',
            'X-Ig-Bandwidth-Speed-Kbps': '-1.000',
            'X-Ig-Bandwidth-Totalbytes-B': '0',
            'X-Ig-Bandwidth-Totaltime-Ms': '0',
            'X-Ig-App-Startup-Country': 'IQ',
            'X-Bloks-Version-Id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07',
            'X-Ig-Www-Claim': 'hmac.AR3SC-eJ9S5l1Lo09xvLhExgPrlYgZvnKB9G84FnngpS-u1e',
            'X-Bloks-Is-Layout-Rtl': 'false',
            'X-Ig-Device-Id': '19390992-8663-4068-918f-06fb4ab64dac',
            'X-Ig-Family-Device-Id': 'f7b96f74-ddba-4f4a-95d7-36c8b29b51b0',
            'X-Ig-Android-Id': 'android-cb1ca12d04193807',
            'X-Ig-Timezone-Offset': '28800',
            'X-Ig-Nav-Chain': 'SelfFragment:self_profile:2:main_profile::,ProfileMediaTabFragment:self_profile:3:button::,IgBloksScreenFragment:warning:28:button::,ProfileMediaTabFragment:self_profile:29:button::',
            'X-Fb-Connection-Type': 'WIFI',
            'X-Ig-Connection-Type': 'WIFI',
            'X-Ig-Capabilities': '3brTv10=',
            'X-Ig-App-Id': '567067343352427',
            'Priority': 'u=3',
            'User-Agent': 'Instagram 237.0.0.14.102 Android (28/9; 240dpi; 720x1280; Asus; ASUS_I003DD; ASUS_I003DD; intel; en_US; 373310554)',
            'Accept-Language': 'en-US',
            'Authorization': f'Bearer IGT:2:{sessoin1}',
            'X-Mid': 'Z44vlQABAAEinpr0-kiBOPPlJPFK',
            'Ig-U-Ds-User-Id': f'{id3}',
            'Ig-U-Rur': f'LDC,{id3},1768918709:01f7a7553288e5ad1fbceb03157abc08e82d16909d0f788533823121965c6d805f46378d',
            'Ig-Intended-User-Id': f'{id3}',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Fb-Http-Engine': 'Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
        }
        params = {
            'guid': '19390992-8663-4068-918f-06fb4ab64dac',
            'device_id': 'android-cb1ca12d04193807',
        }
        response = requests.get('https://i.instagram.com/api/v1/challenge/', params=params, headers=headers)
        print(response.text)
        if ('SCRAPING_WARNING') in response.text:
            k2  = json.loads(response.text)['challenge_context']
            headers = {
                'Host': 'i.instagram.com',
                'X-Ig-App-Locale': 'en_US',
                'X-Ig-Device-Locale': 'en_US',
                'X-Ig-Mapped-Locale': 'en_US',
                'X-Pigeon-Session-Id': 'UFS-06274ad6-e54f-4200-8ac7-4ea28c3ec60e-0',
                'X-Pigeon-Rawclienttime': '1737383989.047',
                'X-Ig-Bandwidth-Speed-Kbps': '-1.000',
                'X-Ig-Bandwidth-Totalbytes-B': '0',
                'X-Ig-Bandwidth-Totaltime-Ms': '0',
                'X-Ig-App-Startup-Country': 'IQ',
                'X-Bloks-Version-Id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07',
                'X-Ig-Www-Claim': 'hmac.AR1joUMvWD2nG91UXxZiX0VLg9gABvWtLCwQbvsgrz27FDVs',
                'X-Bloks-Is-Layout-Rtl': 'false',
                'X-Ig-Device-Id': '19390992-8663-4068-918f-06fb4ab64dac',
                'X-Ig-Family-Device-Id': 'f7b96f74-ddba-4f4a-95d7-36c8b29b51b0',
                'X-Ig-Android-Id': 'android-cb1ca12d04193807',
                'X-Ig-Timezone-Offset': '28800',
                'X-Ig-Nav-Chain': 'MainFeedFragment:feed_timeline:1:cold_start::,IgBloksScreenFragment:warning:2:button::',
                'X-Fb-Connection-Type': 'WIFI',
                'X-Ig-Connection-Type': 'WIFI',
                'X-Ig-Capabilities': '3brTv10=',
                'X-Ig-App-Id': '567067343352427',
                'Priority': 'u=3',
                'User-Agent': 'Instagram 237.0.0.14.102 Android (28/9; 240dpi; 720x1280; Asus; ASUS_I003DD; ASUS_I003DD; intel; en_US; 373310554)',
                'Accept-Language': 'en-US',
                'Authorization': f'Bearer IGT:2:{sessoin1}',
                'X-Mid': 'Z44vlQABAAEinpr0-kiBOPPlJPFK',
                'Ig-U-Ds-User-Id': f'{id3}',
                'Ig-U-Rur': f'LDC,{id3},1768919863:01f7c398afe9500f805ed96af3a70e7f4d596eecd09e80937f20721bba887f27bcbbfd80',
                'Ig-Intended-User-Id': f'{id3}',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'Content-Length': '570',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'X-Fb-Http-Engine': 'Liger',
                'X-Fb-Client-Ip': 'True',
                'X-Fb-Server-Cluster': 'True',
            }

            data = {
                '_uuid': '19390992-8663-4068-918f-06fb4ab64dac',
                'has_follow_up_screens': '0',
                'bk_client_context': '{"bloks_version":"8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07","styles_id":"instagram"}',
                'challenge_context': '{}'.format(k2),
                'bloks_versioning_id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07',
            }

            response = requests.post(
                'https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/',
                headers=headers,
                data=data,
              
            )
            if ('"status":"ok"') in response.text:
                bot.send_message(message.chat.id,'تم الموافقة على الشروط')
                comp2(message)
            else:
                bot.send_message(message.chat.id,'حدث خطا غير متوقع')
        elif ('"action":"close"') in response.text:
            login1(message)
        else:
            bot.send_message(message.chat.id,'السيشن لايعمل ')
def login1(message):
    global log
    
    try:

        mess1 = random.choice(log)
    except IndexError as error:
        bot.send_message(message.chat.id,'انت قمت باضافة سيشن ايدي لذا لايمكني عرض المعلومات او موافقة على الشروط')
    username = mess1.split(':')[0]
    password = mess1.split(':')[1]
    headers = {
            'Host': 'i.instagram.com',
            'X-Ig-App-Locale': 'en_US',
            'X-Ig-Device-Locale': 'en_US',
            'X-Ig-Mapped-Locale': 'en_US',
            'X-Pigeon-Session-Id': 'UFS-a6a2f7af-83fc-4ffd-9d60-57364756f87e-0',
            'X-Pigeon-Rawclienttime': '1737457108.767',
            'X-Ig-Bandwidth-Speed-Kbps': '6004.000',
            'X-Ig-Bandwidth-Totalbytes-B': '0',
            'X-Ig-Bandwidth-Totaltime-Ms': '0',
            'X-Bloks-Version-Id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
            'X-Ig-Www-Claim': '0',
            'X-Bloks-Is-Layout-Rtl': 'false',
            'X-Ig-Device-Id': '19390992-8663-4068-918f-06fb4ab64dac',
            'X-Ig-Family-Device-Id': 'bc791eb8-cf02-43db-8ae3-af84f73df394',
            'X-Ig-Android-Id': 'android-11222e167915c518',
            'X-Ig-Timezone-Offset': '28800',
            'X-Ig-Nav-Chain': 'SelfFragment:self_profile:2:main_profile:1737456043.500::,ProfileMediaTabFragment:self_profile:3:button:1737456043.671::,AccountSwitchFragment:account_switch_fragment:4:button:1737456045.627::,TRUNCATEDx4,LoginLandingFragment:login_landing:9:button:1737456067.635::,bloks_unknown_class:select_verification_method:10:button:1737456129.982::,bloks_unknown_class:login_support_v2_account_type:11:button:1737457062.404::,bloks_unknown_class:login_support_v2_input_contact_email_for_selfie:12:button:1737457066.226::,bloks_unknown_class:login_support_v2_account_type:13:button:1737457085.925::,bloks_unknown_class:select_verification_method:14:button:1737457087.729::,LoginLandingFragment:login_landing:15:button:1737457100.449::',
            'X-Fb-Connection-Type': 'WIFI',
            'X-Ig-Connection-Type': 'WIFI',
            'X-Ig-Capabilities': '3brTv10=',
            'X-Ig-App-Id': '567067343352427',
            'Priority': 'u=3',
            'User-Agent': 'Instagram 275.0.0.27.98 Android (28/9; 240dpi; 720x1280; Asus; ASUS_I003DD; ASUS_I003DD; intel; en_US; 458229257)',
            'Accept-Language': 'en-US',
            'X-Mid': 'Z46prQABAAEAgUDmNQdGb8B1aFkH',
            'Ig-Intended-User-Id': '0',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Content-Length': '1118',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Fb-Http-Engine': 'Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
    }
    tim1 = str(time.time()).split(':')[0]
  
    data = {
        'signed_body': 'SIGNATURE.{"jazoest":"22575","country_codes":"[{\\"country_code\\":\\"1\\",\\"source\\":[\\"default\\"]},{\\"country_code\\":\\"964\\",\\"source\\":[\\"sim\\"]}]","phone_id":"bc791eb8-cf02-43db-8ae3-af84f73df394","enc_password":"#PWD_INSTAGRAM:0:'+f'{tim1}:{password}","username":"{username}","adid":"baa63909-2662-41d1-b9f8-5cf20cd68d21","guid":"19390992-8663-4068-918f-06fb4ab64dac","device_id":"android-11222e167915c518","google_tokens":"[]","login_attempt_count":"4'+'"}',
    }
    response = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data)
    if ('"logged_in_user"') in response.text:
        name = response.json()['logged_in_user']['full_name']
        username = response.json()['logged_in_user']['username']
        #bot.send_message(message.chat.id,f"- تسجيل دخول ناجح\n- اسم الحساب : {name}\n- اسم المستخدم : {username}\n- ارسل /start لعرض القائمة الرئسية")
        ses = response.headers.get('Ig-Set-Authorization')
        if sessoin ==[]:
            idfs = response.json()['logged_in_user']['pk_id']
            ids1.append(idfs)
            sess = ses.split('Bearer IGT:2:')[1]
            #print(sess)
            sessoin.append(sess)
            comp2(message)
            
        elif sessoin !=[]:
            kdo = random.choice(sessoin)
            ikf = random.choice(ids1)
            ids1.remove(ikf)
            idfs = response.json()['logged_in_user']['pk_id']
            ids1.append(idfs)
            sessoin.remove(kdo)
            sess = ses.split('Bearer IGT:2:')[1]
            #print(sess)
            sessoin.append(sess)
            comp2(message)
            
            #يمكننا إرسال بريد إلكتروني إليك لمساعدتك في العودة إلى حسابك.
    elif ('"bad_password"') in response.text:
        bot.send_message(message.chat.id,'كلمة السر غير صحيحة')
    elif ('checkpoint_challenge_required') in response.text:
        bot.send_message(message.chat.id,"الحساب الذي ارسلتة سكيور")
    else:
        bot.send_message(message.chat.id,"غير قادر على تسجيل الدخول")
def info(message,id):
    global sessoin,ids1
    sessoin1 = random.choice(sessoin)
    id3 = random.choice(ids1)
    
    user = message.text
    headers = {
        'Host': 'i.instagram.com',
        'X-Ig-App-Locale': 'en_US',
        'X-Ig-Device-Locale': 'en_US',
        'X-Ig-Mapped-Locale': 'en_US',
        'X-Pigeon-Session-Id': 'UFS-0f2d61ec-08ad-45f2-b109-0f85d6ca2e2e-0',
        'X-Pigeon-Rawclienttime': '1737379100.837',
        'X-Ig-Bandwidth-Speed-Kbps': '-1.000',
        'X-Ig-Bandwidth-Totalbytes-B': '0',
        'X-Ig-Bandwidth-Totaltime-Ms': '0',
        'X-Ig-App-Startup-Country': 'IQ',
        'X-Bloks-Version-Id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07',
        'X-Ig-Www-Claim': 'hmac.AR3SC-eJ9S5l1Lo09xvLhExgPrlYgZvnKB9G84FnngpS-u1e',
        'X-Bloks-Is-Layout-Rtl': 'false',
        'X-Ig-Device-Id': '19390992-8663-4068-918f-06fb4ab64dac',
        'X-Ig-Family-Device-Id': 'f7b96f74-ddba-4f4a-95d7-36c8b29b51b0',
        'X-Ig-Android-Id': 'android-cb1ca12d04193807',
        'X-Ig-Timezone-Offset': '28800',
        'X-Ig-Nav-Chain': 'ExploreFragment:explore_popular:4:main_search::,SingleSearchTypeaheadTabFragment:search_typeahead:5:button::',
        'X-Fb-Connection-Type': 'WIFI',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'Priority': 'u=3',
        'User-Agent': 'Instagram 237.0.0.14.102 Android (28/9; 240dpi; 720x1280; Asus; ASUS_I003DD; ASUS_I003DD; intel; en_US; 373310554)',
        'Accept-Language': 'en-US',
        'Authorization': f'Bearer IGT:2:{sessoin1}',
        'X-Mid': 'Z44vlQABAAEinpr0-kiBOPPlJPFK',
        'Ig-U-Ds-User-Id': f'{id3}',
        'Ig-U-Rur': f'LDC,{id3},1768915101:01f706c531d4cf4f13c8d2f2eb6538e5778be42de4c252cf90403d604f0e99171f84cb6e',
        'Ig-Intended-User-Id': f'{id3}',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
    }

    params = {
        'search_surface': 'typeahead_search_page',
        'timezone_offset': '28800',
        'count': '30',
        'query': f'{user}',
        'context': 'blended',
    }

    response = requests.get('https://i.instagram.com/api/v1/fbsearch/ig_typeahead/', params=params, headers=headers).json()
    ids = response['list'][0]['user']['pk_id']
    nam = response['list'][0]['user']['full_name']
    message = bot.send_message(message.chat.id,f'اسم الحساب : {nam}? هل هذا حسابك عليك الاجابة بنعم او لا \n\nايدي الحساب : {ids}')
    bot.register_next_step_handler(message,cap,ids)
def cap(message,ids):
    global couin
    tr = message.text
    if tr == 'نعم':
        bot.send_message(message.chat.id,'سيتم سحب لستة بعد قليل')
        couin.append(ids)
        coi(message)
    elif tr == 'لا':
        bot.send_message(message.chat.id,'حسنا - ارسل اليوزر من جديد الان')
        bot.register_next_step_handler(info)
    else:
        bot.send_message(message.chat.id,"ارسال خطا عزيزي")
def coi(message):
    global sessoin,ids1,a,k,b,l,couin
    ids = random.choice(couin)
    sessoin1 = random.choice(sessoin)
    id3 = random.choice(ids1)
    lis = random.choice(listm)
    m = lis+25
    headers = {
        'Host': 'i.instagram.com',
        'X-Ig-App-Locale': 'en_US',
        'X-Ig-Device-Locale': 'en_US',
        'X-Ig-Mapped-Locale': 'en_US',
        'X-Pigeon-Session-Id': 'UFS-be761504-ccb9-40cf-b8bc-56a901b70885-0',
        'X-Pigeon-Rawclienttime': '1737373531.463',
        'X-Ig-Bandwidth-Speed-Kbps': '-1.000',
        'X-Ig-Bandwidth-Totalbytes-B': '0',
        'X-Ig-Bandwidth-Totaltime-Ms': '0',
        'X-Ig-App-Startup-Country': 'IQ',
        'X-Bloks-Version-Id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07',
        'X-Ig-Www-Claim': 'hmac.AR1joUMvWD2nG91UXxZiX0VLg9gABvWtLCwQbvsgrz27FDVs',
        'X-Bloks-Is-Layout-Rtl': 'false',
        'X-Ig-Device-Id': '19390992-8663-4068-918f-06fb4ab64dac',
        'X-Ig-Family-Device-Id': 'f7b96f74-ddba-4f4a-95d7-36c8b29b51b0',
        'X-Ig-Android-Id': 'android-cb1ca12d04193807',
        'X-Ig-Timezone-Offset': '28800',
        'X-Ig-Nav-Chain': 'ExploreFragment:explore_popular:5:main_search::,SingleSearchTypeaheadTabFragment:search_typeahead:6:button::,UserDetailFragment:profile:7:search_result::,ProfileMediaTabFragment:profile:8:button::,FollowListFragment:followers:9:button::',
        'X-Fb-Connection-Type': 'WIFI',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'Priority': 'u=3',
        'User-Agent': 'Instagram 237.0.0.14.102 Android (28/9; 240dpi; 720x1280; Asus; ASUS_I003DD; ASUS_I003DD; intel; en_US; 373310554)',
        'Accept-Language': 'en-US',
        'Authorization': f'Bearer IGT:2:{sessoin1}',
        'X-Mid': 'Z44vlQABAAEinpr0-kiBOPPlJPFK',
        'Ig-U-Ds-User-Id': f'{id3}',
        'Ig-U-Rur': f'LDC,{id3},1768909531:01f74a731323c1118db160ad8fb67846e7365c51a6ead6fba0caec3b1312508437909dec',
        'Ig-Intended-User-Id': f'{id3}',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
    }

    params = {
        'search_surface': 'follow_list_page',
        'max_id': f'{m}',
        'query': '',
        'enable_groups': 'true',
        'rank_token': 'fd238b76-a9f8-40c6-bc71-f825bdf17b9b',
    }

    response = requests.get(
        f'https://i.instagram.com/api/v1/friendships/{ids}/followers/',
        params=params,
        headers=headers,
    )
    for tx in json.loads(response.text)['users']:
        k+=1
        username = tx['pk_id']
        with open('ids.txt','a') as f0:
            f0.write(f'{username}\n')
        print(username)
    if 'next_max_id' in response.text:
        if k>= 240:
        
            kc = json.loads(response.text)['next_max_id']
            with open('next.txt','w') as f0:
                f0.write(f'{kc}\n')
            comp2(message)
        else:
            listm.remove(lis)
            listm.append(m)
            coi(message)
            
    else:
        print('Errror')
def iddss(message,acctive):
    
    id4 = str(message.from_user.id)
    url ='https://raw.githubusercontent.com/gzikk/IDcouin/refs/heads/main/ID.txt'
    urp = requests.get(url).text
    if id4 not in urp:
        print('ok')
        if acctive == True and acctive == False :
            checkid(message,id4,urp)
        elif acctive == None :
            checkid(message,id4,urp)
    else:
        checkid(message,id4,urp)

def checkid(message,id4,urp):
    global acctive
    print(id4,urp)
    if acctive == True and acctive == False:
        bot.send_message(message.chat.id,"ممنوع تعدل ع النسخة لك")
    elif acctive == None :
       
        ids = str(message.from_user.id)
        if id4 == ids and ids not in urp:
            acctive = True
        else:
            bot.send_message(message.chat.id,"انت محظور من البوت")
            acctive = False
    bot.send_message(message.chat.id,"تم التحقق من بيانات ارسل /start لظهارها @BBMZZ")



def logiaddsessoin(message,id,w1):
    global sessoin,ids1,log
    mess1 = message.text
    if w1 == False :
        if sessoin == []:
            ids = mess1.split('%')[0]
            ids1.append(ids)
            sample_string = '{"ds_user_id":'+f'"{ids}"'+f',"sessionid":"{mess1}'+'"}'
            print(sample_string)
            sample_string_bytes = sample_string.encode("ascii")

            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
            sessoin.append(base64_string)
            bot.send_message(message.chat.id,"تم اضافة سيشنك بشكل صحيح في البوت - ارسل /start")
            aoutfollow(message)
        else:
            io = random.choice(sessoin)
            idfp = random.choice(ids1)
            sessoin.remove(io)
            ids1.remove(idfp)
            ids = mess1.split('%')[0]
            ids1.append(ids)
            sample_string = '{"ds_user_id":'+f'"{ids}"'+f',"sessionid":"{mess1}'+'"}'
            sample_string_bytes = sample_string.encode("ascii")

            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
            sessoin.append(base64_string)
            bot.send_message(message.chat.id,"تم اضافة سيشنك بشكل صحيح في البوت - ارسل /start")
            aoutfollow(message)
    elif w1 == True :
        try:

            username = mess1.split(':')[0]
            password = mess1.split(':')[1]
            headers = {
                'Host': 'i.instagram.com',
                'X-Ig-App-Locale': 'en_US',
                'X-Ig-Device-Locale': 'en_US',
                'X-Ig-Mapped-Locale': 'en_US',
                'X-Pigeon-Session-Id': 'UFS-a6a2f7af-83fc-4ffd-9d60-57364756f87e-0',
                'X-Pigeon-Rawclienttime': '1737457108.767',
                'X-Ig-Bandwidth-Speed-Kbps': '6004.000',
                'X-Ig-Bandwidth-Totalbytes-B': '0',
                'X-Ig-Bandwidth-Totaltime-Ms': '0',
                'X-Bloks-Version-Id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
                'X-Ig-Www-Claim': '0',
                'X-Bloks-Is-Layout-Rtl': 'false',
                'X-Ig-Device-Id': '19390992-8663-4068-918f-06fb4ab64dac',
                'X-Ig-Family-Device-Id': 'bc791eb8-cf02-43db-8ae3-af84f73df394',
                'X-Ig-Android-Id': 'android-11222e167915c518',
                'X-Ig-Timezone-Offset': '28800',
                'X-Ig-Nav-Chain': 'SelfFragment:self_profile:2:main_profile:1737456043.500::,ProfileMediaTabFragment:self_profile:3:button:1737456043.671::,AccountSwitchFragment:account_switch_fragment:4:button:1737456045.627::,TRUNCATEDx4,LoginLandingFragment:login_landing:9:button:1737456067.635::,bloks_unknown_class:select_verification_method:10:button:1737456129.982::,bloks_unknown_class:login_support_v2_account_type:11:button:1737457062.404::,bloks_unknown_class:login_support_v2_input_contact_email_for_selfie:12:button:1737457066.226::,bloks_unknown_class:login_support_v2_account_type:13:button:1737457085.925::,bloks_unknown_class:select_verification_method:14:button:1737457087.729::,LoginLandingFragment:login_landing:15:button:1737457100.449::',
                'X-Fb-Connection-Type': 'WIFI',
                'X-Ig-Connection-Type': 'WIFI',
                'X-Ig-Capabilities': '3brTv10=',
                'X-Ig-App-Id': '567067343352427',
                'Priority': 'u=3',
                'User-Agent': 'Instagram 275.0.0.27.98 Android (28/9; 240dpi; 720x1280; Asus; ASUS_I003DD; ASUS_I003DD; intel; en_US; 458229257)',
                'Accept-Language': 'en-US',
                'X-Mid': 'Z46prQABAAEAgUDmNQdGb8B1aFkH',
                'Ig-Intended-User-Id': '0',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'Content-Length': '1118',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'X-Fb-Http-Engine': 'Liger',
                'X-Fb-Client-Ip': 'True',
                'X-Fb-Server-Cluster': 'True',
            }
            tim1 = str(time.time()).split(':')[0]
            tim5= datetime.datetime.now()
            crt = str(tim5.timestamp()).split('.')[0]
            data = {
                'signed_body': 'SIGNATURE.{"jazoest":"22575","country_codes":"[{\\"country_code\\":\\"1\\",\\"source\\":[\\"default\\"]},{\\"country_code\\":\\"964\\",\\"source\\":[\\"sim\\"]}]","phone_id":"bc791eb8-cf02-43db-8ae3-af84f73df394","enc_password":"#PWD_INSTAGRAM:0:'+f'{tim1}:{password}","username":"{username}","adid":"baa63909-2662-41d1-b9f8-5cf20cd68d21","guid":"19390992-8663-4068-918f-06fb4ab64dac","device_id":"android-11222e167915c518","google_tokens":"[]","login_attempt_count":"4'+'"}',
            }
            response = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data)
            #print(response.text)
            if ('"logged_in_user"') in response.text:
                log.append(mess1)
                name = response.json()['logged_in_user']['full_name']
                username = response.json()['logged_in_user']['username']
                bot.send_message(message.chat.id,f"- تسجيل دخول ناجح\n- اسم الحساب : {name}\n- اسم المستخدم : {username}\n- ارسل /start لعرض القائمة الرئسية")
                ses = response.headers.get('Ig-Set-Authorization')
                if sessoin ==[]:
                    idfs = response.json()['logged_in_user']['pk_id']
                    ids1.append(idfs)
                    sess = ses.split('Bearer IGT:2:')[1]
                    #print(sess)
                    sessoin.append(sess)
                    aoutfollow(message)
                
                elif sessoin !=[]:
                    kdo = random.choice(sessoin)
                    ikf = random.choice(ids1)
                    ids1.remove(ikf)
                    idfs = response.json()['logged_in_user']['pk_id']
                    ids1.append(idfs)
                    sessoin.remove(kdo)
                    sess = ses.split('Bearer IGT:2:')[1]
                    #print(sess)
                    sessoin.append(sess)
                    aoutfollow(message)
                    
                    #يمكننا إرسال بريد إلكتروني إليك لمساعدتك في العودة إلى حسابك.
            elif ('"bad_password"') in response.text:
                bot.send_message(message.chat.id,'كلمة السر غير صحيحة')
            elif ('checkpoint_challenge_required') in response.text:
                #bot.send_message(message.chat.id,"الحساب الذي ارسلتة سكيور")
                con1 = response.json()['challenge']['api_path']
                con2 = response.json()['challenge']['challenge_context']
            
                headers1 = {
                    'Host': 'i.instagram.com',
                    'X-Ig-App-Locale': 'en_US',
                    'X-Ig-Device-Locale': 'en_US',
                    'X-Ig-Mapped-Locale': 'en_US',
                    'X-Pigeon-Session-Id': 'UFS-a6a2f7af-83fc-4ffd-9d60-57364756f87e-0',
                    'X-Pigeon-Rawclienttime': '1737457110.634',
                    'X-Ig-Bandwidth-Speed-Kbps': '6004.000',
                    'X-Ig-Bandwidth-Totalbytes-B': '0',
                    'X-Ig-Bandwidth-Totaltime-Ms': '0',
                    'X-Bloks-Version-Id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
                    'X-Ig-Www-Claim': '0',
                    'X-Bloks-Is-Layout-Rtl': 'false',
                    'X-Ig-Device-Id': '19390992-8663-4068-918f-06fb4ab64dac',
                    'X-Ig-Family-Device-Id': 'bc791eb8-cf02-43db-8ae3-af84f73df394',
                    'X-Ig-Android-Id': 'android-11222e167915c518',
                    'X-Ig-Timezone-Offset': '28800',
                    'X-Ig-Nav-Chain': 'SelfFragment:self_profile:2:main_profile:1737456043.500::,ProfileMediaTabFragment:self_profile:3:button:1737456043.671::,AccountSwitchFragment:account_switch_fragment:4:button:1737456045.627::,TRUNCATEDx4,LoginLandingFragment:login_landing:9:button:1737456067.635::,bloks_unknown_class:select_verification_method:10:button:1737456129.982::,bloks_unknown_class:login_support_v2_account_type:11:button:1737457062.404::,bloks_unknown_class:login_support_v2_input_contact_email_for_selfie:12:button:1737457066.226::,bloks_unknown_class:login_support_v2_account_type:13:button:1737457085.925::,bloks_unknown_class:select_verification_method:14:button:1737457087.729::,LoginLandingFragment:login_landing:15:button:1737457100.449::',
                    'X-Fb-Connection-Type': 'WIFI',
                    'X-Ig-Connection-Type': 'WIFI',
                    'X-Ig-Capabilities': '3brTv10=',
                    'X-Ig-App-Id': '567067343352427',
                    'Priority': 'u=3',
                    'User-Agent': 'Instagram 275.0.0.27.98 Android (28/9; 240dpi; 720x1280; Asus; ASUS_I003DD; ASUS_I003DD; intel; en_US; 458229257)',
                    'Accept-Language': 'en-US',
                    'X-Mid': 'Z46prQABAAEAgUDmNQdGb8B1aFkH',
                    'Ig-Intended-User-Id': '0',
                    # 'Accept-Encoding': 'gzip, deflate, br',
                    'X-Fb-Http-Engine': 'Liger',
                    'X-Fb-Client-Ip': 'True',
                    'X-Fb-Server-Cluster': 'True',
                }

                params = {
                    'guid': '19390992-8663-4068-918f-06fb4ab64dac',
                    'device_id': 'android-11222e167915c518',
                    'challenge_context': f'{con2}',
                }

                response1 = requests.get(
                    f'https://i.instagram.com/api/v1{con1}',
                    params=params,
                    headers=headers1,
                )
                #print(response1.text)
                if ('select_verify_method') in response1.text:
                    
                    dat = json.loads(response1.text)['step_data']
                    email = dat['email']
                    non = response1.json()['nonce_code']
                    userid = response1.json()['user_id']
                    co2 = response1.json()['cni']
                    con4 = response1.json()['challenge_context']
                    message =bot.send_message(message.chat.id,f'معلوماتك السكيور هي : \nالايميل : {email}\nالايدي : {userid}\n\nهل تود ارسل كود عبر الايميل التالي : {email} ?\nعليك الاجابة بنعم او لا')
                    bot.register_next_step_handler(message,kk2,email,non,userid,co2,con4)
                elif ('"step_name":"verify_email"') in response1.text:
                    bot.send_message(message.chat.id,'عليك الدخول الى حسابك من التطبيق الانة تم ارسال كود سابق اليك - ايضا قم بتغير الباسورد وارسالة الى البوت')
            else:
                bot.send_message(message.chat.id,"غير قادر على تسجيل الدخول")
        except IndexError as errro:
            bot.send_message(message.chat.id,"")
def kk2(message,email,non,userid,co2,con4):
    tx1 = message.text
    if tx1 == 'نعم':
        

        headers = {
            'Host': 'i.instagram.com',
            'X-Ig-App-Locale': 'en_US',
            'X-Ig-Device-Locale': 'en_US',
            'X-Ig-Mapped-Locale': 'en_US',
            'X-Pigeon-Session-Id': 'UFS-a6a2f7af-83fc-4ffd-9d60-57364756f87e-0',
            'X-Pigeon-Rawclienttime': '1737457111.254',
            'X-Ig-Bandwidth-Speed-Kbps': '6004.000',
            'X-Ig-Bandwidth-Totalbytes-B': '0',
            'X-Ig-Bandwidth-Totaltime-Ms': '0',
            'X-Bloks-Version-Id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
            'X-Ig-Www-Claim': '0',
            'X-Bloks-Is-Layout-Rtl': 'false',
            'X-Ig-Device-Id': '19390992-8663-4068-918f-06fb4ab64dac',
            'X-Ig-Family-Device-Id': 'bc791eb8-cf02-43db-8ae3-af84f73df394',
            'X-Ig-Android-Id': 'android-11222e167915c518',
            'X-Ig-Timezone-Offset': '28800',
            'X-Ig-Nav-Chain': 'SelfFragment:self_profile:2:main_profile:1737456043.500::,ProfileMediaTabFragment:self_profile:3:button:1737456043.671::,AccountSwitchFragment:account_switch_fragment:4:button:1737456045.627::,TRUNCATEDx4,LoginLandingFragment:login_landing:9:button:1737456067.635::,bloks_unknown_class:select_verification_method:10:button:1737456129.982::,bloks_unknown_class:login_support_v2_account_type:11:button:1737457062.404::,bloks_unknown_class:login_support_v2_input_contact_email_for_selfie:12:button:1737457066.226::,bloks_unknown_class:login_support_v2_account_type:13:button:1737457085.925::,bloks_unknown_class:select_verification_method:14:button:1737457087.729::,LoginLandingFragment:login_landing:15:button:1737457100.449::',
            'X-Fb-Connection-Type': 'WIFI',
            'X-Ig-Connection-Type': 'WIFI',
            'X-Ig-Capabilities': '3brTv10=',
            'X-Ig-App-Id': '567067343352427',
            'Priority': 'u=3',
            'User-Agent': 'Instagram 275.0.0.27.98 Android (28/9; 240dpi; 720x1280; Asus; ASUS_I003DD; ASUS_I003DD; intel; en_US; 458229257)',
            'Accept-Language': 'en-US',
            'X-Mid': 'Z46prQABAAEAgUDmNQdGb8B1aFkH',
            'Ig-Intended-User-Id': '0',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Content-Length': '1085',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Fb-Http-Engine': 'Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
        }

        data = {
            'user_id': f'{userid}',
            'cni': f'{co2}',
            'nonce_code': f'{non}',
            'bk_client_context': '{"bloks_version":"8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb","styles_id":"instagram"}',
            'fb_family_device_id': 'bc791eb8-cf02-43db-8ae3-af84f73df394',
            'challenge_context': '{}'.format(con4),
            'bloks_versioning_id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
            'get_challenge': 'true',
        }

        response = requests.post(
            'https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/',
            headers=headers,
            data=data,
            
        )
        #print(response.text)
        if ('"status":"ok"') in response.text:
            co0 = response.text.split('\"Af')[1].split('\\"')[0]
            print(co0)
            headers2 = {
                'Host': 'i.instagram.com',
                'X-Ig-App-Locale': 'en_US',
                'X-Ig-Device-Locale': 'en_US',
                'X-Ig-Mapped-Locale': 'en_US',
                'X-Pigeon-Session-Id': 'UFS-a6a2f7af-83fc-4ffd-9d60-57364756f87e-0',
                'X-Pigeon-Rawclienttime': '1737458692.467',
                'X-Ig-Bandwidth-Speed-Kbps': '6004.000',
                'X-Ig-Bandwidth-Totalbytes-B': '0',
                'X-Ig-Bandwidth-Totaltime-Ms': '0',
                'X-Bloks-Version-Id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
                'X-Ig-Www-Claim': '0',
                'X-Bloks-Is-Layout-Rtl': 'false',
                'X-Ig-Device-Id': '19390992-8663-4068-918f-06fb4ab64dac',
                'X-Ig-Family-Device-Id': 'bc791eb8-cf02-43db-8ae3-af84f73df394',
                'X-Ig-Android-Id': 'android-11222e167915c518',
                'X-Ig-Timezone-Offset': '28800',
                'X-Ig-Nav-Chain': 'SelfFragment:self_profile:2:main_profile:1737456043.500::,ProfileMediaTabFragment:self_profile:3:button:1737456043.671::,AccountSwitchFragment:account_switch_fragment:4:button:1737456045.627::,TRUNCATEDx5,bloks_unknown_class:select_verification_method:10:button:1737456129.982::,bloks_unknown_class:login_support_v2_account_type:11:button:1737457062.404::,bloks_unknown_class:login_support_v2_input_contact_email_for_selfie:12:button:1737457066.226::,bloks_unknown_class:login_support_v2_account_type:13:button:1737457085.925::,bloks_unknown_class:select_verification_method:14:button:1737457087.729::,LoginLandingFragment:login_landing:15:button:1737457100.449::,bloks_unknown_class:select_verification_method:16:button:1737457111.931::',
                'X-Fb-Connection-Type': 'WIFI',
                'X-Ig-Connection-Type': 'WIFI',
                'X-Ig-Capabilities': '3brTv10=',
                'X-Ig-App-Id': '567067343352427',
                'Priority': 'u=3',
                'User-Agent': 'Instagram 275.0.0.27.98 Android (28/9; 240dpi; 720x1280; Asus; ASUS_I003DD; ASUS_I003DD; intel; en_US; 458229257)',
                'Accept-Language': 'en-US',
                'X-Mid': 'Z46prQABAAEAgUDmNQdGb8B1aFkH',
                'Ig-Intended-User-Id': '0',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'Content-Length': '901',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'X-Fb-Http-Engine': 'Liger',
                'X-Fb-Client-Ip': 'True',
                'X-Fb-Server-Cluster': 'True',
            }

            data2= {
                'choice': '1',
                'has_follow_up_screens': '0',
                'bk_client_context': '{"bloks_version":"8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb","styles_id":"instagram"}',
                'challenge_context': 'Af{}'.format(co0),
                'bloks_versioning_id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
            }

            response2 = requests.post(
                'https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/',
                headers=headers2,
                data=data2,
             
            )
            print(response2.text)
            if ('verify_email_code') in response2.text:
                message = bot.send_message(message.chat.id,f'تم ارسال رسالة الى البريد الالكتروني : {email}\n\nالان من فضلك ارسل الكود الذي يحتوي على عودة الى حسابك')
                codd = response2.text.split('\"Af')[2].split('\\"')[0]
                id0 = response2.text.split('\"Af')[0].split('bk.action.i32.Const, ')[1].split('),')[0]
                print(id0)
                bot.register_next_step_handler(message,checkcode,codd,id0)
                #bot.register_next_step_handler(message,codver,email,no)
        else:
            pass
    elif tx1 == 'لا':
        bot.send_message(message.chat.id,'تم الغاء العملية')
def checkcode(message,codd,id0):
    
    try:
        code = (message.text)
        

        headers = {
            'Host': 'i.instagram.com',
            'X-Ig-App-Locale': 'en_US',
            'X-Ig-Device-Locale': 'en_US',
            'X-Ig-Mapped-Locale': 'en_US',
            'X-Pigeon-Session-Id': 'UFS-a6a2f7af-83fc-4ffd-9d60-57364756f87e-0',
            'X-Pigeon-Rawclienttime': '1737470014.774',
            'X-Ig-Bandwidth-Speed-Kbps': '6004.000',
            'X-Ig-Bandwidth-Totalbytes-B': '0',
            'X-Ig-Bandwidth-Totaltime-Ms': '0',
            'X-Bloks-Version-Id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
            'X-Ig-Www-Claim': '0',
            'X-Bloks-Is-Layout-Rtl': 'false',
            'X-Ig-Device-Id': '19390992-8663-4068-918f-06fb4ab64dac',
            'X-Ig-Family-Device-Id': 'bc791eb8-cf02-43db-8ae3-af84f73df394',
            'X-Ig-Android-Id': 'android-11222e167915c518',
            'X-Ig-Timezone-Offset': '28800',
            'X-Ig-Nav-Chain': 'SelfFragment:self_profile:2:main_profile:1737456043.500::,ProfileMediaTabFragment:self_profile:3:button:1737456043.671::,AccountSwitchFragment:account_switch_fragment:4:button:1737456045.627::,TRUNCATEDx15,bloks_unknown_class:select_verification_method:20:button:1737468791.266::,LoginLandingFragment:login_landing:21:button:1737468793.571::,bloks_unknown_class:verify_email_code:23:button:1737469956.130::,bloks_unknown_class:select_verification_method:24:button:1737469960.515::,LoginLandingFragment:login_landing:25:button:1737469961.199::,bloks_unknown_class:select_verification_method:26:button:1737470004.558::,bloks_unknown_class:verify_email_code:27:button:1737470010.863::',
            'X-Fb-Connection-Type': 'WIFI',
            'X-Ig-Connection-Type': 'WIFI',
            'X-Ig-Capabilities': '3brTv10=',
            'X-Ig-App-Id': '567067343352427',
            'Priority': 'u=3',
            'User-Agent': 'Instagram 275.0.0.27.98 Android (28/9; 240dpi; 720x1280; Asus; ASUS_I003DD; ASUS_I003DD; intel; en_US; 458229257)',
            'Accept-Language': 'en-US',
            'X-Mid': 'Z46prQABAAEAgUDmNQdGb8B1aFkH',
            'Ig-Intended-User-Id': '0',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Content-Length': '939',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Fb-Http-Engine': 'Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
        }

        data = {
            'security_code': f'{code}',
            'perf_logging_id': f'{id0}',
            'has_follow_up_screens': '0',
            'bk_client_context': '{"bloks_version":"8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb","styles_id":"instagram"}',
            'challenge_context': f'Af{codd}',
            'bloks_versioning_id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
        }

        response = requests.post(
            'https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/',
            headers=headers,
            data=data,
            
        ) 
        if ('Please check the code we sent you and try again.') in response.text:
            bot.send_message(message.chat.id,'الكود الذي ارسلتة حطا')
        elif ('"username') in response.text:
            os.system('clear')
            bot.send_message(message.chat.id,"تم تسجيل الدخول بنجاح في السكيور عبر الاساسي /start")
            coid= response.headers.get('ig-set-authorization')
            if sessoin ==[]:
                idfs = response.json()['logged_in_user']['pk_id']
                ids1.append(idfs)
                sess = coid.split('Bearer IGT:2:')[1]
                #print(sess)
                sessoin.append(sess)
                aoutfollow(message)
               
            elif sessoin !=[]:
                kdo = random.choice(sessoin)
                ikf = random.choice(ids1)
                ids1.remove(ikf)
                idfs = response.json()['logged_in_user']['pk_id']
                ids1.append(idfs)
                sessoin.remove(kdo)
                sess = coid.split('Bearer IGT:2:')[1]
                #print(sess)
                sessoin.append(sess)
                aoutfollow(message)
    except ValueError as error:
        bot.send_message(message.chat.id,'ارسل رقما من فضلك ')
def aoutfollow(message):
    global sessoin,ids1
    id3 = random.choice(ids1)
    sessoin1 = random.choice(sessoin)
    headers = {
        'Host': 'i.instagram.com',
        'X-Ig-App-Locale': 'ar_AR',
        'X-Ig-Device-Locale': 'en_US',
        'X-Ig-Mapped-Locale': 'ar_AR',
        'X-Pigeon-Session-Id': 'UFS-9c4d7daa-9923-482a-96ac-e50789022ef3-0',
        'X-Pigeon-Rawclienttime': '1737166000.779',
        'X-Ig-Bandwidth-Speed-Kbps': '20181.000',
        'X-Ig-Bandwidth-Totalbytes-B': '5346595',
        'X-Ig-Bandwidth-Totaltime-Ms': '285',
        'X-Ig-App-Startup-Country': 'IQ',
        'X-Bloks-Version-Id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07',
        'X-Ig-Www-Claim': 'hmac.AR0Yzt_9JliyviDGGI-m_t_NQOWmV2spUIunOl20E_3fXl6r',
        'X-Bloks-Is-Layout-Rtl': 'true',
        'X-Ig-Device-Id': '19390992-8663-4068-918f-06fb4ab64dac',
        'X-Ig-Family-Device-Id': '6b2d9d30-c1b3-4d3e-837a-832bac4f9a44',
        'X-Ig-Android-Id': 'android-cb1ca12d04193807',
        'X-Ig-Timezone-Offset': '28800',
        'X-Ig-Nav-Chain': 'ExploreFragment:explore_popular:35:main_search::,SingleSearchTypeaheadTabFragment:search_typeahead:36:button::,UserDetailFragment:profile:37:search_result::,ProfileMediaTabFragment:profile:38:button::,ProfileFollowRelationshipFragment:following_sheet:39:button::,ProfileMediaTabFragment:profile:40:button::',
        'X-Fb-Connection-Type': 'WIFI',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'Priority': 'u=3',
        'User-Agent': 'Instagram 237.0.0.14.102 Android (28/9; 240dpi; 720x1280; Asus; ASUS_I003DD; ASUS_I003DD; intel; ar_AR; 373310554)',
        'Accept-Language': 'ar-AR',
        'Authorization': f'Bearer IGT:2:{sessoin1}',
        'X-Mid': 'Z4uVEQABAAHIjSvB_eq_eDK1iIpj',
        'Ig-U-Ds-User-Id': f'{id3}',
        'Ig-U-Rur': f'LDC,{id3},1768762646:01f7701a44369b95040e7fc906064be15238e8bd74b482c7985c626fdb13159fd9424edb',
        'Ig-Intended-User-Id': f'{id3}',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Content-Length': '644',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
    }

    data = {
        'signed_body': 'SIGNATURE.{"user_id":"48932473310","radio_type":"wifi-none",'+f'"_uid":"{id3}","device_id":"android-cb1ca12d04193807","_uuid":"19390992-8663-4068-918f-06fb4ab64dac","nav_chain":"ExploreFragment:explore_popular:35:main_search::,SingleSearchTypeaheadTabFragment:search_typeahead:36:button::,UserDetailFragment:profile:37:search_result::,ProfileMediaTabFragment:profile:38:button::,ProfileFollowRelationshipFragment:following_sheet:39:button::,ProfileMediaTabFragment:profile:40:button::'+'"}',
    }
    

    response = requests.post(
        'https://i.instagram.com/api/v1/friendships/create/48932473310/',
        headers=headers,
        data=data,
    
    ).text
    #print(response)
    if ('"status":"ok"') in response:
        pass
    else:
        pass
@bot.message_handler(func=lambda message:True)
def messs12(message):
    global tim3 
    mes = message.text
    if mes == 'استعلام':
        s4 = types.InlineKeyboardButton(text="Telegram",url="https://t.me/BBMZZ")
        s5 = types.InlineKeyboardMarkup(row_width=1)
        s5.add(s4)
        bot.send_message(message.chat.id,f"*>> Number list : {k}\n>> Telegram : @BBMZZ*",reply_markup=s5,parse_mode='markdown')
    elif mes == 'استعلام كلوز':
        s4 = types.InlineKeyboardButton(text="Telegram",url="https://t.me/BBMZZ")
        s5 = types.InlineKeyboardMarkup(row_width=1)
        s5.add(s4)
        bot.send_message(message.chat.id,f'>> Add Friend : {a}\n>> No Friend : {b}\nTelegram : @BBMZZ',reply_markup=s5)
    elif mes == 'تعديل السرعة':
        message = bot.send_message(message.chat.id,"ارسل السرعة من فضلك الان - ارسل رقما فقط - في حال ارسلت نص سيتم الايقاف او التوليد العشوائي\n\nاقصى رقما : 300\n")
        bot.register_next_step_handler(message,edithre)
    else:
        s4 = types.InlineKeyboardButton(text="Telegram",url="https://t.me/BBMZZ")
        s5 = types.InlineKeyboardMarkup(row_width=1)
        s5.add(s4)
        bot.send_message(message.chat.id,">> استعلام : عرض نتائج السحب لستة\n>> استعلام كلوز : عرض نتائج الاضافة\n>> تعديل السرعة : تعديل سرعة الاداة\n>> القائمة الرئسية : /start",reply_markup=s5)
def edithre(message):
    global th1
    th2 = random.choice(th1)
    try:
        me1 = int(message.text)
        if me1 >300:
            bot.send_message(message.chat.id,f"ارسلت رقما كبيرا لذا تم تحديد السرعة : {th2} في الثانية الواحدة")
        elif me1 <300:
            th1.remove(th2)
            th1.append(me1)
            bot.send_message(message.chat.id,f'تم تحديد السرعة : {me1} - ارسل استعلام كلوز لعرض النتائج')
    except ValueError as error:
        bot.send_message(message.chat.id,"تم تحديد السرعة بشكل عشوائي")

bot.infinity_polling()