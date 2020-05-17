# Source Folder

This folder is what I use to store all the pages on the site. Each page is stored as a .htm file.
The first line of each file is the page title, as seen in <TITLE> tags.
The rest of the file is the actual page body.
Files with no extension are reusable parts of pages, such as the header, footer and sidebar.
The "layout" file is the base for every page.

## Building

Running BUILD.py will combine each .htm file with the extensionless files to create the final pages.
These will be placed in the directory this folder is located in.