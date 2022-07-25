The SRU API can Search for the following datafields (which we need + some more we don't):

pica.per / pica.prs (Author)

pica.isb (ISBN)

pica.bib (library id)

pica.tit (title)

from this, I can extract the neccessary metadata fields for the Author, Title and isbn.
I can't search for our library sigil (Frei 129 or DE-Frei129, since this requires a login; which isn't possible in our database)

The URL for the API is:
https://sru.k10plus.de/gvk!rec=1?version=1.1&operation=searchRetrieve&query=[pica.XXX]&maximumRecords=10&recordSchema=marcxml

the API can be searched for multiple fields at once, they need to be chained with either '+ and +' (to include the next query) or '+ not +' (to exclude the next query)
