#!/usr/bin/python3
from mdutils.mdutils import MdUtils

title = '<h1><img src="https://emojis.slackmojis.com/emojis/images/1531849430/4246/blob-sunglasses.gif?1531849430" width="30"/> Hello World ! </h1>'
resume = 'My name is {}. I work as a {} at {}.'

visitors = '![](http://estruyf-github.azurewebsites.net/api/VisitorHit?user={}&repo={}&countColorcountColor)'
languages = '![Github Languages](https://github-readme-stats.vercel.app/api/top-langs/?username={}&layout=compact&count_private=true)'
statistics = '![Github Statistics](https://github-readme-stats.vercel.app/api/?username={}&count_private=true&show_icons=true)'
contributions = '![Github Contributions](https://github-readme-streak-stats.herokuapp.com/?user={}&hide_border=true)'

paragraph_init = '<p align="left">'
paragraph_end = '</p>'

linkedin = '<a href="{}"><img src="https://img.shields.io/badge/-LinkedIn-0077B5?style=flat&logo=Linkedin&logoColor=white"/></a>'
twitter = '<a href="{}"><img src="https://img.shields.io/badge/-Twitter-%231DA1F2?style=flat&logo=twitter&logoColor=white"/></a>'
medium = '<a href="{}"><img src="https://img.shields.io/badge/-Medium-%2312100E?style=flat&logo=medium&logoColor=white"/></a>'

def Run(username, name, job, company, linkedin_url, twitter_url, medium_url):
    
    mdFile = MdUtils(file_name='README', title=title)
    
    mdFile.new_paragraph(resume.format(name, job, company))
    mdFile.new_paragraph(visitors.format(username, username))
    
    mdFile.new_paragraph(languages.format(username))
    mdFile.new_paragraph(statistics.format(username))
    mdFile.new_paragraph(contributions.format(username))
    
    if linkedin_url is not None or twitter_url is not None or medium_url is not None:
        mdFile.new_paragraph(paragraph_init)
        if linkedin_url is not None:
            mdFile.new_paragraph(linkedin.format(linkedin_url))
        if twitter_url is not None:
            mdFile.new_paragraph(twitter.format(twitter_url))
        if medium_url is not None:
            mdFile.new_paragraph(medium.format(medium_url))
        mdFile.new_paragraph(paragraph_end)
    
    mdFile.create_md_file()
    
    print('✅ Github profile README.md file created successfully for {}'.format(username))
