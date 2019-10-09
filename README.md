# alcm-segmentation

## Samples sources

All the samples in /demo directory are taken from http://www.fki.inf.unibe.ch/databases/iam-handwriting-database

## Demo 

### Calculate avg height of a handwritten text line

    python features-samples.py -i demo/p03-080.png
    Detected average height of text line in pixels: 16

    python features-samples.py -i demo/p03-189.png
    Detected average height of text line in pixels: 30


## Bibliography

The idea and method description are given in:

@inproceedings{Shi:2005:TEG:1106779.1107021,
 author = {Shi, Zhixin and Setlur, Srirangaraj and Govindaraju, Venu},
 title = {Text Extraction from Gray Scale Historical Document Images Using Adaptive Local Connectivity Map},
 booktitle = {Proceedings of the Eighth International Conference on Document Analysis and Recognition},
 series = {ICDAR '05},
 year = {2005},
 isbn = {0-7695-2420-6},
 pages = {794--798},
 numpages = {5},
 url = {http://dx.doi.org/10.1109/ICDAR.2005.229},
 doi = {10.1109/ICDAR.2005.229},
 acmid = {1107021},
 publisher = {IEEE Computer Society},
 address = {Washington, DC, USA},
}