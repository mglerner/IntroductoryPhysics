#!/usr/bin/env/python3

import pandas as pd
import glob

from IPython.display import Image
from IPython.core.display import HTML 



knight = pd.read_csv('Textbooks/Knight3rdEdition.csv')

def scientistparts(fname):
    """The scientist file looks like
    # Name
    Margaret Murnane
    # Description
    Words words words
    words words words

    # Sources
    sourcy source

    ...

    This is an iterator that returns the (item name, content)

    The format keeps Chapter, Section, etc in the Textbook line because otherwise we have duplication (one for each textbook).
    """
    item_name,content = None,[]

    def combinecontent(content):
        return ' '.join([i.strip() for i in content if i.strip()])

    for line in open(fname):
        if line.startswith('#'):
            if item_name is not None:
                yield (item_name,combinecontent(content))
            item_name = line.replace('#','').strip()
            content = []
        else:
            content.append(line)
    if item_name is not None:
        yield(item_name,combinecontent(content))

def bookparts(txt):
    parts = txt.split(',')
    textbook,chapter,section = [],None,None
    for part in parts:
        _part = part.lower().strip()
        if _part.startswith('chapter'):
            chapter = int(_part.replace('chapter','').strip())
        elif _part.startswith('section'):
            section = int(_part.replace('section','').strip())
        else:
            textbook.append(part)
    return({'Textbook':','.join(textbook),
        'Chapter':chapter,
        'Section':section})
    
            

def addscientists(textbook,textbookname,verbose=False):
    """Handles special formatting for images and links.
    """
    scientists = glob.glob('Scientists/*.txt')
    for scientist in scientists:
        if verbose: print('adding scientist',scientist)
        #parts = dict(scientistparts(scientist))
        # Above doesn't work if we have duplicates
        parts ={'Textbook':[]}
        for (k,v) in scientistparts(scientist):
            if k == 'Photo':
                #v = Image(url=v)
                v = '<img src="{v}" width="1000">'.format(v=v)
            elif k == 'Sources':
                i = 1
                formatted = ''
                for vv in v.split():
                    if vv.startswith('http'):
                        formatted += '<a href="{vv}">Link{i}</a> '.format(vv=vv,i=i)
                        i += 1
                    else:
                        formatted += ' ' + vv
                v = formatted
            if k not in parts:
                parts[k] = v
            else:
                parts[k].append(v)
        for tb in parts['Textbook']:
            bp = bookparts(tb)
            if bp['Textbook'] == textbookname:
                parts.update(bp)
                df = pd.DataFrame(data=[parts])
                del df['Textbook']
                if verbose: print('df',df)
                textbook = textbook.append(df)
            else:
                if verbose: print('skipping',bp['Textbook'],'because it is not',textbookname)
    return textbook

def maketextbook(fname):
    d = pd.read_csv(fname)
    textbook = addscientists(d,'Knight, 3rd edition')
    # I want the order of columns
    cols = ['Chapter','Section','Topics','Name','Photo','Description','Sources']
    cols = cols + [i for i in textbook.columns.tolist() if i not in cols]
    textbook = textbook[cols]
    textbook = textbook.sort_values(by=['Chapter','Section','Topics','Description','Name'],
                                    ascending=[True, True, False, False, False])
    return textbook.fillna('').set_index(['Chapter', 'Section','Topics'])
