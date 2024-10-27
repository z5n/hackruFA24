from bs4 import BeautifulSoup
import os
import re
import shutil

root_path = os.path.abspath('.')
html_dir = os.path.join(root_path, 'html')
njtransit_dir = os.path.join(html_dir, 'njtransit')
index_file = os.path.join(njtransit_dir, 'index.html')
log_file = os.path.join(njtransit_dir, 'log.txt')
assets_dir = os.path.join(root_path, 'assets')

def modify_html(file_path):
    # read
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # remove
    div = soup.find("div", class_="overview-list")
    if div:
        div.decompose()

    # replace (using regex)
    modified_html = re.sub(r'(?<=["\'])\bjs/', 'assets/js/', str(soup))
    modified_html = re.sub(r'(?<=["\'])\bcss/', 'assets/css/', modified_html)

    # rewrite
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_html)

def restructure_directories():
    # create assets directory in root if it doesn't exist
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

    # move index.html to root and css, js to assets
    for item in ['index.html', 'css', 'js']:
        src = os.path.join(njtransit_dir, item)
        
        if item in ['css', 'js']:
            dest = os.path.join(assets_dir, item)
        else:
            dest = os.path.join(root_path, item)
        
        if os.path.exists(dest):
            if os.path.isfile(dest):
                os.remove(dest)
            else:
                shutil.rmtree(dest)
        
        shutil.move(src, dest)
    if os.path.exists(log_file):
        os.remove(log_file)
    if os.path.exists(njtransit_dir):
        shutil.rmtree(njtransit_dir)
    if os.path.exists(html_dir):
        shutil.rmtree(html_dir)

# restructure
modify_html(index_file)
restructure_directories()