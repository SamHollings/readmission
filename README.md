# readmission
Repo to analyse readmission data

## Running the analysis

* Set up a virtual environment and install the packages in `requirements.txt`
* open `analysis.ipynb` and run

## Project structure

```text
|   .gitignore                        <- Files (& file types) automatically removed from version control for security purposes
|   config.toml                       <- Configuration file with parameters we want to be able to change (e.g. date)
|   requirements.txt                  <- Requirements for reproducing the analysis environment 
|   pyproject.toml                    <- Configuration file containing package build information
|   LICENCE                           <- License info for public distribution
|   README.md                         <- Quick start guide / explanation of your project
|
|   analysis.ipynb             <- Runs the overall pipeline to produce the publication     
|
+---src                               <- Scripts with functions for use in 'analysis.ipynb'. Contains project's codebase.
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |       utils                     <- functions used in the analysis - probably needs breaking down into more sections.
|
+---data                               <-  reference data and open source data used in the analysis (not best practice to store here - in future would move outside the repo)
|
+---tests
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |       test_utils.py             <- Tests for the functions in utils.py

```
## Contact
Leave any comments as issues.

## Licence

See [LICENCE](/LICENCE)
