#!/usr/bin/python3
from mdutils.mdutils import MdUtils

title = '<h1><img src="https://emojis.slackmojis.com/emojis/images/1531849430/4246/blob-sunglasses.gif?1531849430" width="30"/> Hello World ! </h1>'
resume = 'My name is {}. I work as a {} at {}.'

visitors = '![](http://estruyf-github.azurewebsites.net/api/VisitorHit?user={}&repo={}&countColorcountColor)'
languages = '![Github Languages](https://github-readme-stats.vercel.app/api/top-langs/?username={}&layout=compact&count_private=true)'
statistics = '![Github Statistics](https://github-readme-stats.vercel.app/api/?username={}&count_private=true&show_icons=true)'
contributions = '![Github Contributions](https://github-readme-streak-stats.herokuapp.com/?user={}&hide_border=true)'

def Run(username, name, job, company):
    
    mdFile = MdUtils(file_name='README', title=title)
    
    mdFile.new_paragraph(resume.format(name, job, company))
    mdFile.new_paragraph(visitors.format(username, username))
    mdFile.new_paragraph(languages.format(username))
    mdFile.new_paragraph(statistics.format(username))
    mdFile.new_paragraph(contributions.format(username))
    
    mdFile.create_md_file()
    
    print('✅ Github profile README.md file created successfully for {}'.format(username))
