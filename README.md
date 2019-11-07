# Pipeline Template
Template for automated data analysis pipelines using BDS

## Why?

Simplify complex workflows into a single commandline tool which is easily distributed and **just works**. 

## Design Principles

- System agnostic- Runs on your local machine or on your cluster with little modification

- Modular- The pipeline serves to pass files to modules written in whatever language is best for that task, makes dubugging and updating easier

- Parellelized- Fully parallelizes each step across samples and can specify the number of threads per task for parelleization within a module

- Self contained- Sets its own path at runtime so it won't interact with previously installed software or mess with your envs

- Self installing- Install with one line since it builds itself from source

- Verison controlled- Runs the same on every install

- Simple interface- One line, point it at your directory of files and let it go

- Flexible default parameters- Set them up once, and overwirte as necessary at run time

- Executed on experiment level directories not files, requires correct directory structure


## This Example

The pipeline included here just flips the contents of two input text files per "sample", concatenates them, and creates an output csv of all resulting strings and the "sample" they originated from. Saves all intermediates. Using the configs users can include addional text to be appended and change the order of the concatenation. 

### Input structure

This pipeline is run on directories which look like this, file contents in (): 

- Test/
    - Raw_Inputs/
        - Sample_1/
            - Some.foo (oof)
            - Thing.bar (rab)
        - Sample_2/
            - What.foo (iH)
            - Ever.bar (moM)
       
After running:

      ./Wrapper.sh -e Test/ 
      
The directory looks like this:

- Test/
    - Raw_Inputs/
        - Sample_1/
            - Some.foo (oof)
            - Thing.bar (rab)
        - Sample_2/
            - What.foo (iH)
            - Ever.bar (moM)
    - Intermediates/
        - Sample_1/
            - Sample_1.foo (This is a foo)
            - Sample_1.bar (bar test)
        - Sample_2/
            - Sample_2.foo (This is a Hi)
            - Sample_2.bar (Mom test)
    - Outputs/
        - Sample_1/
            - Sample_1.foobar (This is a foobar test)
        - Sample_2/
            - Sample_2.foobar (This is a HiMom test)
    - Final.csv

And Final.csv should look like this, though the rows may be swapped

Name | Foobar
-----|-------
Sample_1|This is a foobar test
Sample_2|This is a HiMom test


## Installation
      git clone https://github.com/mattisabrat/Pipeline_Template.git
      cd Pipeline_Template
      ./Install.sh


