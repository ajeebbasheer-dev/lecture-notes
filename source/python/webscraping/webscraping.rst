===================
Webscraping
===================

.. toctree::
   :maxdepth: 3
   :caption: Contents:

- Techniques to automate gathering of data from a website.
- Libraries: `BeautifulSoup`, `requests`.
- We use `chrome` browser but these tools are available for all major browsers.

Introduction
=============

website front-end components
-----------------------------

When a browser loads a website, it essentially contains three elements,

- HTML: Basic structure and content of a webpage. IT contains the actual content.
- CSS: To deals with look and design.
- Javascript: To define interactive elements of a webpage.


Python can view and extract this HTML and CSS programmatically.

Rules of Webscraping
---------------------

- Always try to get permission before scraping.
- If you make too many scraping attempts, your IP address could get blocked.
- Some websites blocks all scraping softwares.

Limitations of Webscraping
---------------------------

- Every website is unique which means every webscraping script is unique.
- Even a minor update in the website may break you complete script.
- We need to think in a generalized way when writing a script.