# [How to search multiple pdf documents for words on Linux](http://xmodulo.com/2013/08/how-to-search-multiple-pdf-documents-for-words-on-linux.html)

When it comes to text search within a pdf document, pretty much every pdf reader software supports it (be it Adobe Reader or any third-party pdf viewer). However, it becomes tricky when there are more than one pdf document to search.

In Linux, there are command-line tools (e.g., `pdftotext` or `pdfgrep`) that can be used to do simple search on multiple pdf documents at once. Compare to these command-line utilities, a desktop application called [`recoll`](http://www.recoll.org/) is a much more advanced and user-friendly text search tool. In this tutorial, I will describe **how to search multiple pdf documents for text by using` recoll`**.

### What is Recoll?

`recoll` is an open-source desktop application specializing in text search. `recoll` maintains a database index for all document files in a target storage location (e.g., a specific folder, home directory, disk drive, etc). The document index contains texts extracted from document files with external helper programs. Using the document index, `recoll` can perform more advanced queries than simple regular expression based search.

The powerful features of `recoll` include:

  * Supports multiple document formats (e.g., pdf, doc, text, html, mailbox).
  * Automatically indexes document contents from files, emails, email attachments, compressed archives, etc.
  * Indexes web pages you visited (with the help of [Firefox extension](http://recollfirefox.sourceforge.net/)).
  * Supports multiple languages and Unicode-based multi-character sets.
  * Supports advanced search, such as proximity search and filtering based on file type, file system location, modification time, and file size.
  * Supports search with multiple entry fields such as document title, keyword, author, etc.



### Install Recoll on Linux

To install `recoll` and external helper programs on Debian, [Ubuntu](http://xmodulo.com/go/ubuntu_guide), or Linux Mint:

$ sudo apt-get install recoll poppler-utils antiword

To install `recoll` and external helper programs on Fedora:

$ sudo yum install recoll poppler-utils antiword

To install `recoll` on CentOS or RHEL, first [enable EPEL repository](http://xmodulo.com/2013/03/how-to-set-up-epel-repository-on-centos.html), and then run:

$ sudo yum install recoll poppler-utils antiword

To launch `recoll`, simply run:

$ recoll

The first time you launch `recoll`, you will see the screen shown below. Here you are asked to choose one of two menu before starting indexing: (1) “Indexing configuration” which controls how to build a document database index, or (2) “Indexing schedule” which controls how often to update a database index. For now, click on “Indexing configuration” menu.

[![](http://farm4.staticflickr.com/3807/9557706045_3c17da487f.jpg)](http://www.flickr.com/photos/xmodulo/9557706045/)

In the configuration window, you will see “Top directories” (directories which contain documents to search), and “Skipped paths” (file system paths to avoid when building a document index) under “General parameters” tab. In this example, I add “~/Documents” to “Top directories” field.

[![](http://farm6.staticflickr.com/5455/9557705999_351b7754d3.jpg)](http://www.flickr.com/photos/xmodulo/9557705999/)

Under “Local parameters” tab, you can specify other indexing criteria, such as file names to skip, max file size, etc. Once you are done, go ahead and create a document database index. The document index building process uses external programs (e.g., `pdftotext` for pdf documents,`antiword` for MS Word documents) to extract texts from individual documents, and create an index out of the extracted texts.

[![](http://farm8.staticflickr.com/7393/9560496286_6f5c9ed996.jpg)](http://www.flickr.com/photos/xmodulo/9560496286/)

Once an initial document index is built, you can check what kind of documents have been indexed, by going to “Help”–>”Show indexed types” menu. Make sure that “application/pdf” mime-type is included.

[![](http://farm8.staticflickr.com/7362/9557705861_869918336a.jpg)](http://www.flickr.com/photos/xmodulo/9557705861/)

### Search Multiple PDF Documents for Text

You are now ready to conduct document search. Enter any word or phrase (with quotes) to search for.

[![](http://farm4.staticflickr.com/3754/9560496276_e6412df1c1.jpg)](http://www.flickr.com/photos/xmodulo/9560496276/)

A search result shows a list of pdf documents along with document snippets and page number information that are matched with search query. The example output shows a list of pdf documents that contain a phrase “virtual machine”. You can check document previews, or open the matched documents by using an external pdf viewer.

[![](http://farm3.staticflickr.com/2853/9560496260_e4f788580e.jpg)](http://www.flickr.com/photos/xmodulo/9560496260/)

Using `recoll`, you can search pdf documents that contains specific word(s) in the document title. For example, by typing in “title:kernel” in search query, you can search for pdf documents which contain “kernel” in their titles.

[![](http://farm3.staticflickr.com/2806/9557705937_f96f418897.jpg)](http://www.flickr.com/photos/xmodulo/9557705937/)

Using advanced search option, you can define various other search criteria.

[![](http://farm8.staticflickr.com/7343/9560496206_5a99aba434.jpg)](http://www.flickr.com/photos/xmodulo/9560496206/)

As documents are added, updated or removed, you will need to update an existing document index. You can do it manually by clicking on “Update Index” menu.

[![](http://farm4.staticflickr.com/3802/9560496194_4c01cb5601.jpg)](http://www.flickr.com/photos/xmodulo/9560496194/)

You can also update an existing document index automatically, either with a periodic cron job or with a background daemon process.

[![](http://farm8.staticflickr.com/7387/9560496180_d03f2daf80.jpg)](http://www.flickr.com/photos/xmodulo/9560496180/)
