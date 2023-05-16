Anki addon to automatically add pitch accent graph from OJAD to cards.

* Installation
    * Install Python3 and PIP
    * Install package dependences 
        $ pip install geckodriver-autoinstaller==0.1.0 selenium==4.4.3 beautifulsoup4==4.11.1
    * Install package from ankiweb or execute $ make dist
        to generate an ankiaddon package, and import it

### Features
* modes
    * bulk add and remove
    * manual add/edit/remove for single cards(has to be implemented/tested)
* accent illustrations
    * pitch accent illustrations are created as PNG; 
    * illustrations include pitch annotations as well as aligned kana
* compatibility
    * accent illustrations sync to mobile and web versions of Anki
    * works for whole sentences and paragraphs

### Todos
* cleanup codebase
   * remove any obsolite code, caused by this hack
   * test/implement manual add/edit/remove for single cards

### Notes
* All generated graphs are scraped from the [OJAD](https://www.gavo.t.u-tokyo.ac.jp) website
* This repository was forked from [IllDepence](https://github.com/IllDepence/anki_add_pitch_plugin), I made just some changes to his code. If you like my work, you will like his to. Most of the code of this repostory wrote [IllDepence](https://github.com/IllDepence/anki_add_pitch_plugin) and the contributors on his repository.
