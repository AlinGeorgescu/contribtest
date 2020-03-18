# Site generator from static pages

Encountered bugs:
* general:
  * added the shebang
  * imported sys and json
* list_files:
  * base was unused, I added it to yield
* read_file:
  * changed read mode from binary to text
* write_output:
  * if the folder does not exist I create it
* generate_site:
  * specified FileSystemLoader's package
  * added missing name in for

Other upgrades:
* solved TODO by adding output_path parameter
* replaced concat with os path join in generate_site
* changed coding style according to pylint3

Test script:
* Chosen solution: use system commands for comparison (needed to ignore blank
  lines in the rendered template)
* Other less easier solution: use file compare line by line and ignore blank
  lines
* A time consuming solution (not suitable for code size in this project,
  suitable for large projects): django minify response
* How to run:
  ./test.py - there should be no output