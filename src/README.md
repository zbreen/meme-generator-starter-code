The following is a program meant to generate memes via random quotes and images.

Install: Panda, Docx, pillow, requests, flask

QuoteEngine
-This folder utilizes various files in order to parse out a quote from files provided. These quotes gathered will be used on the page, so long as they follow the appropriate filetype.
-QuoteModel represents the way quotes should be read on the memes the program produces.
=It utilizes an IngestorInterface, which is meant to represent functions that'll be used to read the files.
-Ingestor is used to determine what steps should be taken to read the file.
-The subsequent Ingestors are used to read the quotes from the appropriate files.
-IngestorInterface is a superclass used for each files in the folder except for QuoteModel.
-QuoteModel is used in certain fileIngestors to set up the quotes, as well as used in meme.py and app.py

MemeGenerator
-This folder is used to take an image, and utilize files from QuoteEngine, to make a meme.
-MemeEngine sets up the variables, including output, as well as sets up the pictures before saving them to the output.

Src (app.py and meme.py)
-These files combine the QuoteEngine and the MemeGenerator in order to properly create a meme.
-app.py randomizes which among the files are selected for meme generation.
-meme.py allows the user the ability to choose the meme, body, and quote themselves. 