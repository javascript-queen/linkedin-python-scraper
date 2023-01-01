# linkedin-python-scrapper

# LinkedIn Scraper

*It's a common misconception that web scraping is illegal—it isn't, nor is it hacking or data theft. There are no specific laws that prohibit data scraping. Professional scrapers follow data protection rules and access only publicly available data.*

##‼️IMPORTANT!
1. The code is slower than it can be to copy a human's behavior
2. There should be some alterations done for different files which I’ll explain below
3. If the script can’t find the desired url it’ll print ‘url not found’
4. The script will work only for urls(but I can mutate it if needed) and only for linkedin
5. I slowed down the time between clicking the button login and the login process so that if you’ll have to pass a security check, you can make it happen on time
6. The urls will be printed one by one to a separate csv file named output.csv
7. The script can handle 100 inputs(and more), I checked 100 at a time and wasn’t blocked. If you get more and more linkedin checks try to alter the time stamps (just prolong it)
8. The script can be stopped, so don’t leave it alone, check it from time to time. There was a woman with an emoji in her company name and this emoji stopped the whole script
9. I don’t break the script flow if you have a blank row! I totally can do it, but I was thinking what if you have blank rows and it’ll stop before you know. So, at the end of the excel doc you’ll need to just press Ctrl+C in the terminal to stop your script

## How to use the script

It’ll depend on your version of python and your Operating system, but either of these commands in terminal should work:

python scraper_1.py
or
python3 scraper_1.py

## What is login_credential.txt 

Here you can change your login info and password. Mine works for now, but who knows when this profile can be banned.

## Mutating Excel for your needs

It’s easier to just concatenate the columns you need in Excel. So, for instance, you need to search depending on the ‘Full Name’ and ‘Company’ which are A and D columns respectively. Then in the header E (which according to Python is column 4) type: =A1:A1000&" "&D1:D1000. Type the formula only in E1. I skip this line in the code, otherwise the script will be searching for that input: “=A1:A1000&" "&D1:D1000”. 


## What if the column is not the [n] one

In the script there are two lines which are in charge of the column count:

list(sheet.columns)[4]
for row, cellObj in enumerate(list(sheet.columns)[4])

### Change this 4. Remember that Python counts columns starting from 0.

## Changing file’s name / output file name

This is Excel file name line: 
 wb = openpyxl.load_workbook('selenium-tester.xlsx')

This is the output file name line(THERE ARE TWO SUCH LINES, BE CAREFUL, CHANGE BOTH!): 
with open('output.csv', 'a', newline = '') as file_output.
