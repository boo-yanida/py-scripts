# Convert html to markdown

import re

def main():
    html = 'This is in <em>italics</em>. So is <em>this</em>'
    result = html2markdown(html)  
    print(result)

def html2markdown(html):
    '''Take in html text as input and return markdown'''
    #print(html)
    markdown = re.sub(r'<em>(.*?)</em>',r'*\1*', html)  #italics
    markdown = re.sub(r'\s+',' ', markdown) #spaces
    markdown = re.sub(r'<p>(.*?)</p>',r'\1\n\n',markdown) #paragraphs
    markdown = re.sub(r'<a href="(.*?)">(.*?)</a>',r'[\2](\1)',markdown) #links
    markdown = markdown.strip()
    #print(markdown)
    return markdown

if __name__ == "__main__":
    main()