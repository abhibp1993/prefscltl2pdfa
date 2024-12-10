# prefscltl2pdfa

`prefscltl2pdfa` is a tool for expressing PrefScLTL formulas and converting them to preference automata.
PrefScLTL formulas enable expressing preferences over ScLTL formulas.

This module utilizes the `spot` library to parse and process ScLTL formulas
into preference deterministic finite automata (PDFA). 
It also provides functions for validating and manipulating preference automata.

The online tool is available at [TBD]

The documentation is available at [TBD]


## Docker 

**[Under development, not released]**

A docker image with `prefscltl2pdfa` preinstalled is available 
at https://hub.docker.com/repository/docker/abhibp1993/prefscltl2pdfa/general.

Pull image using `docker pull abhibp1993/prefscltl2pdfa`.


## Installation

`prefscltl2pdfa` is only tested on ubuntu 22.04.  


### Spot Installation 

Follow instructions on https://spot.lre.epita.fr/install.html 

### Python Prerequisites
Install all dependencies listed `requirements.txt`.

### Installing prefscltl2pdfa 

```
git clone https://github.com/abhibp1993/prefscltl2pdfa.git
cd prefscltl2pdfa
pip install .
```