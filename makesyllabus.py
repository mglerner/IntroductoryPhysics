#!/usr/bin/env/python3

import pandas as pd
import glob
import urllib

from IPython.display import Image
from IPython.core.display import HTML 

import requests
from pptx import Presentation
from pptx.util import Inches


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
    """Handles special formatting for images and links. Also creates PPTX presentation, as a side effect.
    """
    prs0 = Presentation()
    scientists = glob.glob('Scientists/*.txt')
    for scientist in scientists:
        if verbose:
            print('adding scientist',scientist)
        #parts = dict(scientistparts(scientist))
        # Above doesn't work if we have duplicates
        parts ={'Textbook':[]}
        for (k,v) in scientistparts(scientist):
            if k == 'Photo':
                #v = Image(url=v)
                vv = ''
                for vvv in v.split():
                    vv += '<a href="Textbooks/{n}.pptx"><img src="{v}" width="300"/></a>'.format(
                        v=vvv,
                        n=urllib.parse.quote_plus(parts['Name']),
                    )
                v = vv
            elif k == 'Sources':
                i = 1
                formatted = ''
                for vv in v.split():
                    if vv.startswith('http'):
                        linkpart = vv.strip()
                        if linkpart.endswith('.'):
                            linkpart = linkpart[:-1]
                        formatted += '<a href="{vv}">Link{i}</a> '.format(vv=linkpart,i=i)
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
                if verbose:
                    print('df',df)
                textbook = textbook.append(df)
            else:
                if verbose: print('skipping',bp['Textbook'],'because it is not',textbookname)

        # Now, for extra cool, make a powerpoint slide!
        # This should loop through each of the photos, making a new slide in the presentation for each photo.
        if 'Photo' in parts and parts['Photo']:
            prs = Presentation()
            add_scientist_slide(prs0,scientist,name=parts['Name'],verbose=verbose)
            add_scientist_slide(prs,scientist,name=parts['Name'],verbose=verbose)
            # get the original, unparsed photos bit.
            prs.save('Textbooks/{n}.pptx'.format(n=parts['Name'].strip()))
    prs0.save('Textbooks/{n}.pptx'.format(n=textbookname))
    return textbook

def add_scientist_slide(prs,scientist,name,verbose=False):
    """Creates image file as side effect
    """
    for (k,v) in scientistparts(scientist):
        if k == 'Photo':
            break
    for p in v.split():
        img_path = 'test.jpg'
        if verbose:
            print(f'Grabbing image: {p}')
        img_data = requests.get(p).content
        with open(img_path, 'wb') as handler:
            handler.write(img_data)
        blank_slide_layout = prs.slide_layouts[5]

        slide = prs.slides.add_slide(blank_slide_layout)

        shapes = slide.shapes
        title_shape = shapes.title
        title_shape.text = name

        top = Inches(1.75)
        left = Inches(0.5)
        height = Inches(5)
        pic = slide.shapes.add_picture(img_path, left, top, height=height)

        notes_slide = slide.notes_slide
        text_frame = notes_slide.notes_text_frame
        text_frame.text = open(scientist).read()
    

def maketextbook(fname,verbose=False):
    d = pd.read_csv(fname)
    textbook = addscientists(d,'Knight, 3rd edition',verbose=verbose)
    # I want the order of columns
    cols = ['Chapter','Section','Topics','Photo','Name','Description','Sources']
    cols = cols + [i for i in textbook.columns.tolist() if i not in cols]
    textbook = textbook[cols]
    textbook = textbook.sort_values(by=['Chapter','Section','Topics','Description','Name'],
                                    ascending=[True, True, True, False, False])
    return textbook.fillna('').set_index(['Chapter', 'Section','Topics'])
