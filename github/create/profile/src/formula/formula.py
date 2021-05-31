#!/usr/bin/python3
from mdutils.mdutils import MdUtils

title = '<h1><img src="https://emojis.slackmojis.com/emojis/images/1531849430/4246/blob-sunglasses.gif?1531849430" width="30"/> Hello World ! </h1> <hr>'
resume = 'My name is {}. I work as a {} at {}.'

visitors = '![](http://estruyf-github.azurewebsites.net/api/VisitorHit?user={}&repo={}&countColorcountColor)'
languages = '![Github Languages](https://github-readme-stats.vercel.app/api/top-langs/?username={}&layout=compact&count_private=true)'
statistics = '![Github Statistics](https://github-readme-stats.vercel.app/api/?username={}&count_private=true&show_icons=true)'
contributions = '![Github Contributions](https://github-readme-streak-stats.herokuapp.com/?user={}&hide_border=true)'
skills = '![{}](https://img.shields.io/badge/-{}-05122A?style=flat&color={})&nbsp;'

paragraph_init = '<p align="left">'
paragraph_end = '</p>'

linkedin = '<a href="{}"><img src="https://img.shields.io/badge/-LinkedIn-0077B5?style=flat&logo=Linkedin&logoColor=white"/></a>'
twitter = '<a href="{}"><img src="https://img.shields.io/badge/-Twitter-%231DA1F2?style=flat&logo=twitter&logoColor=white"/></a>'
instagram = '<a href="{}"><img src="https://img.shields.io/badge/-Instagram-E4405F?style=flat&logo=instagram&logoColor=white"/></a>'
facebook = '<a href="{}"><img src="https://img.shields.io/badge/-Facebook-1877F2?style=flat&logo=facebook&logoColor=white"/></a>'
medium = '<a href="{}"><img src="https://img.shields.io/badge/-Medium-%2312100E?style=flat&logo=medium&logoColor=white"/></a>'


def run(username, name, job, company, hardskills, accounts):
    mdFile = MdUtils(file_name='README')

    add_title(mdFile, title)

    add_introduction(mdFile, username, name, job, company)

    if hardskills is not None:
        add_hardskills(mdFile, hardskills)

    add_analytics(mdFile, username)

    if accounts is not None:
        add_accounts_url(mdFile, accounts)

    mdFile.create_md_file()

    print('\n✅ \033[1mGithub profile README.md file created successfully for {} user!\033[0m'.format(username))


def add_title(mdFile, title):
    mdFile.new_paragraph(resume.format(title))

def add_introduction(mdFile, username, name, job, company):
    mdFile.new_paragraph(resume.format(name, job, company))
    mdFile.new_paragraph(visitors.format(username, username))


def add_analytics(mdFile, username):
    mdFile.write("\n\n### Analytics ⚙️")
    mdFile.new_paragraph(languages.format(username))
    mdFile.new_paragraph(statistics.format(username))
    mdFile.new_paragraph(contributions.format(username))


def add_hardskills(mdFile, hardskillset):
    mdFile.write("\n\n### Languages & Tools 🛠")
    hard_skill_list = hardskillset.split("|")
    mdFile.write('  \n')
    print("\n⚠️  \033[36mMultiplus skills must be separated with coma (e.g: Java,Kotlin,Spring)\033[0m")

    for hard_skill in hard_skill_list:

        if hard_skill == "Languages":
            language = input("➡️  Insert your \033[1mlanguages\033[0m skills: ")
            language = language.replace(" ", "")
            for item in language.split(","):
                mdFile.write(skills.format(item, item, "green"))
            mdFile.write('  \n')

        if hard_skill == "Frameworks":
            framework = input("➡️  Insert your \033[1mframeworks\033[0m skills: ")
            framework = framework.replace(" ", "")
            for item in framework.split(","):
                mdFile.write(skills.format(item, item, "orange"))
            mdFile.write('  \n')

        if hard_skill == "Data Banks":
            database = input("➡️  Insert your \033[1mdata banks\033[0m skills: ")
            database = database.replace(" ", "")
            for item in database.split(","):
                mdFile.write(skills.format(item, item, "yellow"))
            mdFile.write('  \n')

        if hard_skill == "Cloud":
            cloud = input("➡️  Insert your \033[1mcloud\033[0m skills: ")
            cloud = cloud.replace(" ", "")
            for item in cloud.split(","):
                mdFile.write(skills.format(item, item, "blue"))
            mdFile.write('  \n')

        if hard_skill == "Tools":
            tools = input("➡️  Insert your \033[1mtools\033[0m skills: ")
            tools = tools.replace(" ", "")
            for item in tools.split(","):
                mdFile.write(skills.format(item, item, "gray"))
            mdFile.write('  \n')


def add_accounts_url(mdFile, accounts):
    mdFile.write("\n\n### Let's connect? 🤝")
    social_networks_list = accounts.split("|")
    mdFile.new_paragraph(paragraph_init)

    for social_network in social_networks_list:

        if social_network == "LinkedIn":
            linkedin_url = input("➡️  LinkedIn Account URL: ")
            mdFile.new_paragraph(linkedin.format(linkedin_url))

        if social_network == "Twitter":
            twitter_url = input("➡️  Twitter Account URL: ")
            mdFile.new_paragraph(twitter.format(twitter_url))

        if social_network == "Instagram":
            instagram_url = input("➡️  Instagram Account URL: ")
            mdFile.new_paragraph(instagram.format(instagram_url))

        if social_network == "Facebook":
            facebook_url = input("➡️  Facebook Account URL: ")
            mdFile.new_paragraph(facebook.format(facebook_url))

        if social_network == "Medium":
            medium_url = input("➡️  Medium Account URL: ")
            mdFile.new_paragraph(medium.format(medium_url))

    mdFile.new_paragraph(paragraph_end)
