import sys, os

file = open("layout")
layout = file.read()
file.close()

file = open("header")
header = file.read()
file.close()

file = open("footer")
footer = file.read()
file.close()

file = open("sidebar")
sidebar = file.read()
file.close()

for subdir, dirs, files in os.walk("."):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".htm"):
            print (filepath)
            out = layout
            out = out.replace("<!--header-->", header)
            out = out.replace("<!--footer-->", footer)
            out = out.replace("<!--sidebar-->", sidebar)
            file = open(filepath, "r")
            out = out.replace("<!--pagetitle-->", file.readline()[:-1])
            out = out.replace("<!--contents-->", file.read())
            file.close()
            print (out)
            outpath = "."+filepath+"l"
            os.makedirs(os.path.dirname(outpath), exist_ok=True)
            file = open(outpath, "w")
            file.write(out)
            file.close()
            print ('written to "'+outpath+'"');