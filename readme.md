# Spotifier

 <a href="https://pypi.org/project/yeast-spotifier"><img src="https://badge.fury.io/py/yeast-spotifier.svg" alt="PyPI version"></a>
 
This script to covert pre-processed plate images into figures.

Nothing fancy at the moment, no deep learning segmentation ;-) the script works using plates spotted according to provided template. Still, this helps to get this task done quicker!

![](imgs/yWwr8DqnXT.gif)

! Download a set of templates for copper plates https://github.com/mmagnus/yeast-spotifier/releases/download/v1.0/templates-for-copper-plates.zip !

Table of Contents
=================

* [Spotifier](#spotifier)
  * [Options](#options)
  * [Prepare image](#prepare-image)
  * [Adjust the image to the template](#adjust-the-image-to-the-template)
  * [Prepare mapping file](#prepare-mapping-file)
* [Customization](#customization)
* [Mappings](#mappings)
* [For reporters](#for-reporters)
* [Digitifier](#digitifier)
* [Install](#install)
* [Changelog](#changelog)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Options

	usage: spotifier.py [-h] [-v] [-d] [--align] [-x X] [-y Y]
			    [--trim-rms TRIM_RMS] [--size SIZE] [-a]
			    map file [file ...]

	install to work on psd files: psd-tools3

	positional arguments:
	  map                  map
	  file                 pre-processed image(s)

	optional arguments:
	  -h, --help           show this help message and exit
	  -v, --verbose        be verbose
	  -d, --debug          be even more verbose
	  --align              align dots
	  -x X
	  -y Y
	  --trim-rms TRIM_RMS
	  --size SIZE
	  -a, --dont-annotate

![](imgs/jyvsjrgxpe.gif)

Fig. `-t`,  trim background to get nicely formatted dots.

## Prepare image
Open the image:
![](imgs/f1.jpeg)

Image -> Adjustments -> Black & white OR cmd+alt+shift+b

Inverse color (cmd+i) 

Adjust Levels (cmd+l), select black backgroud with the black pippette and white for the white pippette.
![](imgs/f2.jpeg)
![](imgs/f3.jpeg)
![](imgs/f4.jpeg)

Crop image and Edit -> Image Rotation -> Flip Canvas Horizontal.

## Adjust the image to the template
Open template.psd and drag and drop plate photo
![](imgs/f5.jpeg)

Lower opacity for the imported image, to around 30%, to see the template in the background.
![](imgs/f6.jpeg)

Use Move tool and Free transform fit the image to the template.
![](imgs/f7.jpeg)

Use Move tool and Free transform to move "Rectangle" to cover the plate.
![](imgs/f8.jpeg)

Switch off the Backgroud layer, set Opacity to 100.
![](imgs/f9.jpeg)

Save as a PSD (or jpeg) file, e.g., s02_30.jpeg.

## Prepare mapping file
Open a text editor and prepare a file used to map dots into figure. 

![](imgs/f10.jpeg)

Run the program:

    python spotifier.py testdata/02/map.txt testdata/02/s02_30.psd

The results should be like this:

![](imgs/f11.jpeg)

and the file `s02_30_spots.png` should be created in the folder next to the input file (in this case `testdata/s02/s02_30_spots.png`)

-------------------------------------------------------------------------------

TIP: If you want to introduce one extra, empty line, just add an empty line to a map file.
![](imgs/map_empty.jpeg)

# Customization

If you want to move single dots, use Preview and just move them around, save it (if you open a JPG, you will be asked if you want to convert the file to PNG, yeah, do it, remember only to change the file name in the command, `18_X.png`).

![](imgs/fix.jpeg)

and re-run:

	python spotifier.py testdata/02/map.txt testdata/02/18_X.png

-------------------------------------------------------------------------------

Use play with Opacity to see Backgound with the template to adjust positions of your dosts.

![](imgs/opacity.jpeg)

# Mappings
Some ideas for your plates ;-):

    5, 6, 7
    8, 9, 10

    12, 13, 14
    15, 16, 17

    20, 21, 22
    23, 24, 25

    28, 29, 30
    31, 32, 33

    36, 37, 38
    39, 40, 41

    44, 45, 46
    47, 48, 49
    
    1,2,3
    4,5,6
    7,8,9
    10,11,12
    13,14,15
    16,17,18
    19,20,21,
    22,23,24,
    25,26,27,
    28,29,30,
    31,32,33,
    34,35,36,
    37,38,39,
    40,41,42,
    46,47,48,
    49,50,51,
    52,53,54,
    55,56,57,
    58,59,60,
   
-------------------------------------------------------------------------------

    1, 2, 3
    5, 6, 7
    8, 9, 10
    12, 13, 14
    15, 16, 17
    21, 22, 23
    24, 25, 26
    28, 29, 30
    31, 32, 33
    36, 37, 38
    39, 40, 41
    44, 45, 46
    47, 48, 49
    51, 52, 53
    53, 54, 55
    57, 58, 59

# For reporters
For reporters, prepare each PSD file as described above. Run spotifier.py for each plate to check if everything is correct:

    python spotifier.py testdata/repoters/2.txt testdata/repoters/1.psd

![](imgs/reporter1.jpeg)

and then run this cmd to process each PSD files and combine all outputs into one figure.

    python spotifier.py testdata/repoters/2.txt testdata/repoters/*.psd

![](imgs/reporter2.jpeg)

# Digitifier
Process a figure into numbers:

![](imgs/1_all.jpeg)

      python digitifier.py 8 6 testdata/digitfier/1_all.png
    [  3.         238.12373299 434.86099169 -27.59790191  96.14306032
     289.4862576  391.415654   242.01505869]
              0
    0  0.066164
    1  0.574584
    2  1.000000
    3  0.000000
    4  0.267572
    5  0.685648
    6  0.906056
    7  0.582999
    Output created testdata/digitfier/1_all_plot.png

![](imgs/1_all_plot.png)
    
# Install
To download the tool and install it run (with this you will get all test files):

    pip install -e git+http://github.com/mmagnus/yeast-spotifier.git#egg=yeast-spotifier

or download the repository and install from the folder:

    pip install -e .

if you want to have only the code installed in your system, simply run:

    pip install yeast-spotifier
	
(to install requirements, `pip install psd-tools3==1.8.2 --user`)

# Changelog

v1.2 Works on Windows ;-)

Fixed #4 Font missing on Windows and now it works on Windows (install Git for Windows with the shell)

v1.1 

- --dont-align -> --align (align is worse right now hmm... so the default is --dont-align)
- use -1 in mapping to put a white box, you can use to make spacers for your figures

Mapping: 1,-1,2

![](imgs/spacer.jpg)

1.0 initial code taken from https://github.com/mmagnus/rna-tools 
