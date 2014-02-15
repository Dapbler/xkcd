import urllib.request
print('Romance,Sarcasm,Math and Language\nWelcome to xkcd Downloader 1.0\n\nAccepted Inputs :')
print('all : downloads all xkcd comics from the beginning to the latest one')
print('first : downloads the first xkcd comic')
print('latest : downloads the latest xkcd comic')
print('{Any number} : downloads the xkcd comic of that number',' ','Example:67')
print('{Range} : downloads the xkcd comics in that range',' ','Example:5-19')
print('If no input is given : downloads the latest xkcd comic by default\n')
def f(n):
    page = 'http://xkcd.com/' + n + '/'
    response = urllib.request.urlopen(page)
    text = str(response.read())
    #Now finding the link of the comic on the page
    ls = text.find('embedding')
    le = text.find('<div id="transcript"')
    link = text[ls+12:le-2]
    #Now finding the title of the comic
    ts = text.find('ctitle')
    te = text.find('<ul class="comicNav"')
    title = text[ts+8:te-8]
    img = title + '.jpg'
    #Now downloading the image
    print('Now downloading - '+ img)
    urllib.request.urlretrieve(link,img)
    print('Done')

def latest():
    new = urllib.request.urlopen('http://xkcd.com')
    content = str(new.read())
    #Now finding the latest comic number
    ns = content.find('this comic:')
    ne = content.find('<br />\\nImage URL')
    newest = content[ns+28:ne-1]
    return int(newest)

#Taking the input   
number = str(input('Enter the xkcd comic number : '))
#Declaring a variable for the range input
position = number.find('-')

if number == 'latest' or number == '':
    f(str(latest()))
elif number == 'first':
    f(str(1))
elif number == 'all':
    for o in range(1,latest()):
        f(str(o))
elif position > 0:
    #For the range input
    ll = int(number[0:position])
    ul = int(number[position+1:len(number)])
    if ul>ll and ul <= (latest()) and ll>0:
        for i in range(ll,ul):
            f(str(i))
            
    elif ul>(latest()) or ll <=0:
        print('Invalid range ...')
    else:
        print('Invalid range ...')
else:
    try:
        if 1 <= int(number) <= (latest()):
            #Calling the function for a direct input
            f(number)
        elif int(number) > (latest()):
            print('Not yet published ...')
        elif int(number) <= 0:
            print('Enter a number between 1 and the latest ...')        
    except ValueError:
            print('Invalid input')
    
x = input('\nPress Enter to exit ...')
