#!/usr/bin/python3
from mdutils.mdutils import MdUtils

title  = '<h1><img src="https://emojis.slackmojis.com/emojis/images/1531849430/4246/blob-sunglasses.gif?1531849430" width="30"/> Hello World ! </h1>'
resume = 'My name is {}. I work as a {} at {}.'

visitors      = '![](http://estruyf-github.azurewebsites.net/api/VisitorHit?user={}&repo={}&countColorcountColor)'
languages     = '![Github Languages](https://github-readme-stats.vercel.app/api/top-langs/?username={}&layout=compact&count_private=true)'
statistics    = '![Github Statistics](https://github-readme-stats.vercel.app/api/?username={}&count_private=true&show_icons=true)'
contributions = '![Github Contributions](https://github-readme-streak-stats.herokuapp.com/?user={}&hide_border=true)'

paragraph_init = '<p align="left">'
paragraph_end  = '</p>'

linkedin  = '<a href="{}"><img src="https://img.shields.io/badge/-LinkedIn-0077B5?style=flat&logo=Linkedin&logoColor=white"/></a>'
twitter   = '<a href="{}"><img src="https://img.shields.io/badge/-Twitter-%231DA1F2?style=flat&logo=twitter&logoColor=white"/></a>'
instagram = '<a href="{}"><img src="https://img.shields.io/badge/-Instagram-E4405F?style=flat&logo=instagram&logoColor=white"/></a>'
facebook  = '<a href="{}"><img src="https://img.shields.io/badge/-Facebook-1877F2?style=flat&logo=facebook&logoColor=white"/></a>'
medium    = '<a href="{}"><img src="https://img.shields.io/badge/-Medium-%2312100E?style=flat&logo=medium&logoColor=white"/></a>'

def run(username, name, job, company, accounts):
    
    mdFile = MdUtils(file_name='README', title=title)

    add_introduction(mdFile, username, name, job, company)
    
    add_analytics(mdFile, username)
    
    if accounts is not None:
        add_accounts_url(mdFile, accounts)
    
    mdFile.create_md_file()
    
    print('✅ Github profile README.md file created successfully for {}'.format(username))

def add_introduction(mdFile, username, name, job, company):
    mdFile.new_paragraph(resume.format(name, job, company))
    mdFile.new_paragraph(visitors.format(username, username))

def add_analytics(mdFile, username):
    mdFile.write("\n\n### Analytics ⚙️")    
    mdFile.new_paragraph(languages.format(username))
    mdFile.new_paragraph(statistics.format(username))
    mdFile.new_paragraph(contributions.format(username))

def add_accounts_url(mdFile, accounts):
    mdFile.write("\n\n### Let's connect? 🤝")
    social_networks_list = accounts.split("|")
    mdFile.new_paragraph(paragraph_init)
    
    for social_network in social_networks_list:
        
        if social_network == "LinkedIn":
            linkedin_url = input("LinkedIn Account URL: ")
            mdFile.new_paragraph(linkedin.format(linkedin_url))
        
        if social_network == "Twitter":
            twitter_url = input("Twitter Account URL: ")
            mdFile.new_paragraph(twitter.format(twitter_url))
        
        if social_network == "Instagram":
            instagram_url = input("Instagram Account URL: ")
            mdFile.new_paragraph(instagram.format(instagram_url))
        
        if social_network == "Facebook":
            facebook_url = input("Facebook Account URL: ")
            mdFile.new_paragraph(facebook.format(facebook_url))
        
        if social_network == "Medium":
            medium_url = input("Medium Account URL: ")
            mdFile.new_paragraph(medium.format(medium_url))    
    
    mdFile.new_paragraph(paragraph_end)