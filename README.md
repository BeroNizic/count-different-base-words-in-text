# count-different-base-words-in-text

Count different lemmas ("base words")  in some txt file.

usage:

For Italian:
**python count_it.py *_input-txt [output-txt] [most-frequent-words]***

For English:
**python count_en.py *_input-txt [output-txt] [most-frequent-words]***

In *input-txt* counts total numbers of lemmas, total number of distinct lemmas and its variance.
Optional parameters: writes the first *most-frequent-word* in *output-txt*.

**Requirements:**

1. installed python

2. installed nltk for python

3. installed pattern for python for count_it.py 

   https://stackabuse.com/python-for-nlp-introduction-to-the-pattern-library/

   *pip install pattern*

What is lemma? It is something very similar to the base word. https://en.wikipedia.org/wiki/Lemma_(morphology)

Accuracy is, based on my very subjective estimate, around 90%. It is possible to do some smaller adjustments in count_it.py and count_en.py to make it even more accurate, but for my use case, as it is, is good enough.

### If you want to count words in Kindle book

Note: These are instruction for Windows. I am not familiar with Linux/Mac, but I expect that the procedure is similar.
If you try it on Linux/Mac, if you wish, please send me instructions so I will update this document.

**Requirements:**

1. old version of Kindle Reader

   I am using older version (1.17.44170) which is available at:
   https://kindle-for-pc.en.uptodown.com/windows/versions)
   https://kindle-for-pc.en.uptodown.com/windows/download/1041755

2. have already bought Kindle book

3. Calibre (version 5 or newer)

   https://calibre-ebook.com

4. DeDRM plugin for Calibre to remove DRM from Kindle books
   https://github.com/apprenticeharper/DeDRM_tools/releases

Kindle books are protected with DRM and that needs to be removed to convert it to txt. Removing DRM from Kindle book will not work in the newest version of Kindle app reader so you need to use older one.

With Calibre you can convert all kind of e-books to txt format. Once the book is imported in Calibre you can:
Select book -> right click mouse -> Convert (individually) -> Output format: TXT

If you have Kindle DRM protected book:

1. Open book in Kindle app at least once (to download it from the Cloud)
2. Calibre -> Add books -> go to the directory where is Kindle book (%USERPROFILE%\Documents\My Kindle Content) and select .azw file. The name of the file isn't friendly so it isn't obvious a what book it belongs so good luck with finding which azw belongs to the book you want to process - use trial and error. If there is some better hint how to find which one to use, please let me know. Once found, add it to the Calibre. DeDRM plugin will remove DRM protection and the book will be imported in Calibre.
3. Convert book to txt format
