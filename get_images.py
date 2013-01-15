import re
import os
import shutil

def replace_image_paths(restfile, newpath, change_restfile=False,
        leave_fullpath=True, image_path='static/images'):
    """
    Find full paths to images in .rst files, copy them to `newpath`,
    then overwrite the restfile using the new path.
    Can leave the full path as a comment.
    """

    imre = re.compile("\.\. image:: (.*)")
    with open(restfile,'r') as r:
        images = []
        newlines = []
        for line in r:
            search = imre.search(line)
            if search is not None:
                impath = search.groups()[0]
                print impath
                images.append(impath)
                if os.path.exists(impath):
                    shutil.copy(impath,newpath)
                    if leave_fullpath:
                        newlines.append(".. {0}\n".format(impath))
                    newlines.append(".. image:: {newpath}/{filename}\n".format(
                        newpath=image_path.strip("/"),
                        filename=os.path.split(impath)[1]))
                else:
                    newlines.append(".. Could not find this image:\n")
                    newlines.append(line)
            else:
                newlines.append(line)

    if change_restfile:
        with open(restfile,'w') as w:
            w.writelines(newlines)


