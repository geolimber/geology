# Small tools for my geological workflow

My geological workflow is quite unique, so this tools rarely could be used commonly, but with some modifications they are could be useful.
Generaly here you can find some python and shell scripts to work with different GPS data, which saves me a lot of time on my routines, and makes possible avoid using proprietary GIS software.

## csv2polygon.py
This script converts set of vertices of the mining concession (UTM coordinates) to polygon in *.wkt format (Well Known Text). Output file can be used in QGIS, which is great to plan field work and visualize limits of area of interest.

*Usage:*

Put this script to some forlder from your user path environment variable (for examle /usr/local/bin) and make shure script is executable.
Go to the folder where *.csv* file stored and run:
> $ csv2polygon.py file1.csv file2.csv file3.csv

*Expected input:*
```
X;Y
585000;8262500
585500;8262500
585500;8263500
586000;8263500
586000;8264500
586500;8264500
586500;8265000
587000;8265000
587000;8266000
...
```

*Generated output:*
```
id;wkt
1;POLYGON((585000 8262500,585500 8262500,585500 8263500,586000 8263500,586000 8264500,586500 8264500,586500 8265000,587000 8265000,587000 8266000...))
```

*TODO:*
- [X] Various files handling
- [ ] When there is no filename provided, process all *.csv* files in current folder.
