## Add pelican attila theme:
https://www.vogella.com/tutorials/GitSubmodules/article.html

```
(pelican) [unix@localhost markus-site]$
mkdir pelican-themes
cd pelican-themes/
#git submodule add -b master https://github.com/msvalina/attila.git
git submodule add -b master https://github.com/gilsondev/pelican-clean-blog.git
git submodule init
```
--> .gitmodules are created

delete submodule
```
git submodule deinit -f atilla
rm -rf .git/modules/attila
git rm -rf attila
```

## Add atilla without submodule:
```
mkdir pelican-themes
cd pelican-themes
git clone --recursive https://github.com/msvalina/attila.git
```

## Important to know:
Each pelican-theme uses its own static folder.
--> pelican-themes/pelican-clean-blog/static
--> pelican-themes/attila/static
*HEADER_COVER* ...pelican-clean-blog
*HOME_COVER* ...attila


######################################################################
# Delete a branches in github:
https://www.educative.io/edpresso/how-to-delete-remote-branches-in-git




# pelican-themes 2020-10-25
```
base) [unix@localhost pelican-themes]$ git submodule add https://github.com/msvalina/attila.git
Cloning into '/home/unix/dev/markus-site/pelican-themes/attila'...
remote: Enumerating objects: 383, done.
remote: Total 383 (delta 0), reused 0 (delta 0), pack-reused 383
Receiving objects: 100% (383/383), 1.95 MiB | 3.32 MiB/s, done.
Resolving deltas: 100% (227/227), done.
(base) [unix@localhost pelican-themes]$ git status
On branch pelican-themes
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   ../.gitmodules
        new file:   attila

(base) [unix@localhost pelican-themes]$ 
```


## List of all installed pelican themes
```
$ pelican-themes -l
notmyidea
simple
```

## Use a pelican theme (pelican.conf)
https://docs.getpelican.com/en/stable/settings.html
```
THEME = 'simple'
```


git submodule status

## If on git status a - sign that means, that the submodule is not initialized
http://www.christianlong.com/blog/more-on-pelican-themes.htm

```
$ git submodule status
(base) [unix@localhost pelican-themes]$ git submodule init attila
```




#  markus-site-pelican-themes
```
git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes
```
--> Schmarrn Cloning of all themes!

#  markus-site-pelican-themes
# $ pelican-quickstart (same as already know):
https://pythonforundergradengineers.com/how-i-built-this-site-3.html
```
git clone https://github.com/markusgoller/markus-site-pelican-themes.git
git submodule add https://github.com/getpelican/pelican-themes.git
git submodule init  
git submodule update --init --recursive
```
--> Maybe also cloning?



############################################################
mogrify:
? https://www.meinubuntu.de/2008/06/11/bilder-verkleinern-unter-linux/




############################################################
2020-11-15:  --> hurray it works
themes/attila

see repo: pelican-themes-better

# Make folder
```
mkdir themes
```

# Use a pelican theme
https://www.vogella.com/tutorials/GitSubmodules/article.html

```
(base) [unix@localhost themes]$ git submodule add -b master https://github.com/msvalina/attila.git
(pelican) [unix@localhost themes]$ git submodule init
```

# pelicanconf.py
Abhilfe:
1) --> copy image into pelican/attila theme oder so aehnlich
2) --> copy image from remote
3) --> use HOME_COLOR
```
# pelican-themes
THEME = "themes/attila"
```
# Can set individual COVERS
* HOME_COVER ...Does still not work

```
#HOME_COVER = '../images/bike_tour_berlin_notebook/IMG_20200819_130938_resize.jpg'
HOME_COLOR = 'green'
```

############################################################
https://docs.github.com/en/actions