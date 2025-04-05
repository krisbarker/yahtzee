#!/usr/bin/env python3

"""
This should create a nice piece of yahtzee artwork.
"""


def get_artwork_string():

    artwork = """
        yy      yy
         yy    yy    aaaa    hh            tt       zzzzz        eeee        eeee
          yy  yy    aa  aa   hh            tt      zz   zz      ee   ee     ee   ee
           yyy           aa  hh         tttttttt         zz    ee     ee   ee     ee
           yy       aaaaaa   hh            tt           zz       eeeeee      eeeeee
           yy      aa    aa  hh hh hh      tt        zzzz      ee          ee
          yy      aa     aa  hh     hh     tt           zz    ee          ee
         yy        aa    aa  hh     hh     tt tt         zz    ee    ee    ee    ee 
        yy          aaaaaa   hh     hh      ttt         zz      eeeeee      eeeeee
                                                       zz 
                                                      zz  
                                                    zz
        """

    return artwork


def main():
    artwork = get_artwork_string()
    print(artwork)


if __name__ == '__main__':
    main()
