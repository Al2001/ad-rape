#!/usr/bin/python

from selenium import webdriver
import os, random, time
from  profiles import *

exec_type = raw_input("\nDo you want to choose the search parameters [c] or 'randomly' execute [r]? ")

while exec_type not in ('c','r'):   
    print('\nValueError: Enter "c" to choose parameters and "r" to pseudo randomly execute the program: ')
    new_value = raw_input("\nDo you want to choose the search parameters [c] or 'randomly' execute [r]? ")
    exec_type = new_value

if exec_type == 'c':
    try:
        exec_num = int(raw_input('\nHow many search sessions do you want to execute [maximum=10]? '))
        print '\n'
    except ValueError:
        print '\n'
        print'ERROR: Invalid input. Enter an integer between 1 and 10. \n'
        exec_num = int(raw_input('\nHow many search sessions do you want to execute [maximum=10]? '))
    while exec_num < 1 or exec_num > 10:
        print '\nERROR: Invalid choice. \n'
        print '\nEnter a number between 1-10. \n'
        exec_num = int(raw_input('\nHow many search sessions do you want to execute [maximum=10]? '))

    for sessions in range(exec_num):
        
        print "\nProfiles: [0]japan fanatic[1]gay[2]old woman[3]real dude[4]rich person[5]preggers[6]gamer[7]80s[8]new age[9]christian"
        profile = [search0,search1,search2,search3,search4,search5,search6,search7,search8,search9]
	      search_profile = int(raw_input('\nEnter your choice: '))
	      choice = profile[search_profile]

       	print '\nYou can search [0] You Tube [1] Google or [2] Bing.'
        search_channel = int(raw_input('\nEnter your choice: '))

      	os.system('clear')

	      display_choice = {0:'japan fanatic',1:'gay',2:'old woman',3:"'real' dude",4:'preggers',5:'gamer',6:'80s',7:'new ager',8:'christian'}
	      profile_choice = display_choice.get(int(search_profile))
        channel_display = {0:'You Tube',1:'Google',2:'Bing'}
	      print('\nExecuting {0} session on {1}...').format(profile_choice,channel_choice) 

       	browser = webdriver.Firefox()
        browser.maximize_window()
         
      	for term in choice:

	          if search_channel == 0:
                #You Tube
                delay = random.randint(5,15)
                os.system('sleep %s' % delay)
                browser.get('https://www.youtube.com/results?search_query=%s' % term)

            elif search_channel == 1:
                # Google
                delay = random.randint(5,15)
                time.sleep(delay)
                browser.get('https://encrypted.google.com/#q=%s' % term)

            else:
                # Bing
                delay = random.randint(5,15)
                os.system('sleep %s' % delay)
                browser.get('https://www.bing.com/search?q=%s&go=Submit&qs=n&form=QBLH&pq=%s&sc=8-8&sp=-1&sk=&ghc=1&cvid=494fabbf283f44d6ab34343c0623e0f5' % (term, term))
        
	          os.system('clear')
	          browser.close()
else:
    try:
        exec_num = int(raw_input('\nHow many search sessions do you want to execute [maximum=10]? ')) 
        print '\n'
    except ValueError:
        print '\n'
        print'ERROR: Invalid input. Enter an integer between 1 and 10. \n'
        print '\n'
        exec_num = int(raw_input('\nHow many search sessions do you want to execute [maximum=10]? ')) 
    # sentinel loop???
    while exec_num < 1 or exec_num > 10:
        print '\nERROR: Invalid choice. \n'
        print '\nEnter a number between 1-10. \n'
        exec_num = int(raw_input('\nHow many search sessions do you want to execute [maximum=10]? ')) 

    # intialize total run time accumulator
    accumulator = 0

    for i in range(exec_num):
        # psuedo randomize search list   
        searchlist = [search0,search1,search2,search3,search4,search5,search6,search7,search8,search9]
        randomlist = random.randint(0,9)
        selectlist = searchlist[randomlist]
   
        # psuedo randomize order in which lists are searched
        randomorder = random.randint(0,2)
        # choice 1 == alphabetical

        if randomorder == 0:
            selectlist.sort()

        # choice 2 == reversed
        elif randomorder == 1:
            selectlist = selectlist[::-1]

        # choice 3 (by implication) == the order of the list as written
        
        # intialize selenium browser    
        browser = webdriver.Firefox()
        browser.maximize_window()
        
        if i == 0:
            print ('\nThe program will execute {0} browser sessions.\n'.format(exec_num))

        # initialize timer 
        starttime = time.time()
    
        # randomize search site-
        site = random.randint(0,2)
   
        if site == 0:
            # You Tube
            for term in selectlist:
                delay = random.randint(5,15)
                os.system('sleep %s' % delay)
                browser.get('https://www.youtube.com/results?search_query=%s' % term)

        elif site == 1:    
            # Google
            for term in selectlist:
                delay = random.randint(5,15)
                os.system('sleep %s' % delay)
                browser.get('https://encrypted.google.com/#q=%s' % term)

        else:
            # Bing
            for term in selectlist:
                delay = random.randint(5,15)
                os.system('sleep %s' % delay)
                browser.get('https://www.bing.com/search?q=%s&go=Submit&qs=n&form=QBLH&pq=%s&sc=8-8&sp=-1&sk=&ghc=1&cvid=494fabbf283f44d6ab34343c0623e0f5' % (term, term))

        browser.close()

        # timing
        endtime = time.time()
        total = starttime - endtime
        total = abs(total)/60 
        accumulator = accumulator + total
   
        # change type of selectlist and site for printing dictionary entry
        searchname = {'0':'japan fanatic','1':'gay curious','2':'old woman','3':"'real' dude",'4':'rich','5':'preggers','6':'gamer','7':'80s','8':'new age','9':'christian'}
        searchdict = searchname[str(randomlist)]
        sitename = {'0':'You Tube','1':'Google','2':'Bing'}
        sitedict = sitename[str(site)]
        print ('\nIt took {0:.1f} minutes to execute the {1} session on {2}. \n'.format(total,searchdict,sitedict))
        while i == exec_num - 1:
            print ('TOTAL TIME = {0:.1f} for {1} session(s). \n'.format(accumulator,exec_num))
            i += 1
