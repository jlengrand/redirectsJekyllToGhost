# Redirects Jekyll to Ghost

This repository contains a minimal script that I needed when moving my blog from a [Jekyll setup on Github pages](https://jekyllrb.com/docs/github-pages/) over to [Ghost](https://ghost.org/).


Besides [converting the posts themselves](https://docs.ghost.org/api/migration/), I also needed to keep supporting the old links, and redirect to the new link format. 
I decided to not go the NGINX route, and instead use **[this nice feature from Ghost itself](https://docs.ghost.org/tutorials/implementing-redirects/)**.

The script in this repository will take all the posts in your posts folder, and create a `redirects.json` file in output. There is an example output in the repository.

## Running the script

* Copy the posts folder locally
* Modify the `posts_directory` variable of the script, if needed.
* Run the script

A `redirects.json` file will be created that you can upload in your ghost instance (in the labs area).

You will only need `Python 3.X` to run the script.

## What is happening

The script takes every markdown file in the list, and creates a relation between :

* The jekyll format : `/yyyy/mm/filename_without_date`
* The Ghost format: `/title_of_article_in_yaml`
* Some additional magic is needed: 
  * Filtering of the special characters (such as '()!,-')
  * Removal of multi-spaces
  * Conversion from spaces to -

## Limitations

The point of this script for me was to save 90% of the manual conversion. Your mileage may vary

Known limitations :
* Not all special characters listed. Simply add them as you find new ones
* For very long titles, ghost uses the filename as well. I do not know about the characters limit exactly, it feels like around 50 characters. 

Once the file is generated, I hunted for discrepancies and changed a few links manually.

## Ideas for features

Next to fixing limitations, it would be amazing to have the script check for each link and see if it is valid by pinging the URL. It would allow to find discrepancies very quickly. 

## Author

Julien Lengrand-Lambert - @jlengrand

## LICENSE

See LICENSE for full text, but the license is Creative Commons Attribution NonCommercial ShareAlike (CC-NC-SA).