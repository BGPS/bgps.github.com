import re
import os
import shutil
import argparse
import glob

def replace_image_paths(restfile, newpath='content/images/', change_restfile=False,
        leave_fullpath=True, image_path='static/images', verbose=False):
    """
    Find full paths to images in .rst files, copy them to `newpath`,
    then overwrite the restfile using the new path.
    Can leave the full path as a comment.
    """

    if verbose:
        print "Replacing images in ",restfile

    imre = re.compile("\.\. image:: (.*)")
    with open(restfile,'r') as r:
        images = []
        newlines = []
        for line in r:
            search = imre.search(line)
            if search is not None:
                impath = search.groups()[0]
                if verbose:
                    print impath
                images.append(impath)
                if os.path.exists(impath):
                    shutil.copy(impath,newpath)
                    if leave_fullpath:
                        newlines.append(".. {0}\n".format(impath))
                    newlines.append(".. image:: {image_path}/{filename}\n".format(
                        image_path=image_path.strip("/"),
                        filename=os.path.split(impath)[1]))
                else:
                    newlines.append(".. Could not find this image:\n")
                    newlines.append(line)
            else:
                newlines.append(line)

    if change_restfile:
        with open(restfile,'w') as w:
            w.writelines(newlines)

def replace_all(path, suffix='.rst', **kwargs):
    """
    Find all files in path with specified suffix and run replace_image_paths on them
    """

    files = glob.glob(path+"/*.rst")

    for fn in files:
        replace_image_paths(fn, **kwargs)


def main():
    parser = argparse.ArgumentParser(description="""Tool to find images referenced in a .rst
            file and copy them to the content/images/ directory to be included in the website.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(dest='path', nargs=1,
        help='Path where to find the content files.',
        default=None)

    parser.add_argument('--imagepath',dest='imagepath',
        help='Path where to copy the image files.',
        default='content/images/')

    parser.add_argument('--filesuffix',dest='filesuffix',
        help='Suffix of file type',
        default='.rst')

    parser.add_argument('--change-restfile',dest='change_restfile',
        help='Overwrite the .rst files?',
        default=False, action='store_true')

    parser.add_argument('--leave-fullpath',dest='leave_fullpath',
        help='Leave a copy of the full path as a comment?',
        default=True)

    parser.add_argument('--image-path',dest='image_path',
        help='Path to the static/images/ directory for the blog',
        default='static/images/')

    parser.add_argument('--verbose',dest='verbose',
        help='Print file names each time they are found?',
        default=False, action='store_true')

    args = parser.parse_args()
    
    if os.path.isdir(args.path[0]):
        replace_all(args.path[0], suffix=args.filesuffix, newpath=args.imagepath,
                change_restfile=args.change_restfile,
                leave_fullpath=args.leave_fullpath, image_path=args.image_path,
                verbose=args.verbose)
    else:
        replace_image_paths(args.path[0], newpath=args.imagepath,
                change_restfile=args.change_restfile,
                leave_fullpath=args.leave_fullpath, image_path=args.image_path,
                verbose=args.verbose)

if __name__=="__main__":
    main()
