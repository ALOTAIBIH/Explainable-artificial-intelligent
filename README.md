# Explainable-artificial-intelligent
Counterfactual Explanations
==============================

This project uses the method proposed by Russell (2019) to generate multiple (diverse) counterfactual explanations.

Getting Started
------------
You need to install Gurobi, an optimization solver. You can get Gurobi from https://www.gurobi.com/

- Follow the instructions provided here (https://www.gurobi.com/gurobi-and-anaconda-for-windows/) to install Anaconda and Gurobi. I have Anaconda 4.10.1 and Python 3.8
- Create a free account (https://www.gurobi.com/academia/academic-program-and-licenses/) 
- Request a free academic license and follow instructions to install the license.



Try running the app using the following command, replacing the '*' with 'adult', 'hr', 'cv' (work in progress)

`python testcf-*.py`

You may need to install additional python packages.

Docker
------------
To run under Docker either use the docker-compose.yml file in the base of the repository or follow these steps

- Run `conda install -c gurobi gurobi`
- Obtain a web license (https://license.gurobi.com/manager/licenses/)
- Download the license file and store it somewhere (e.g. /home/jovyan/nlp_repo/explanation/gurobi.lic)
- Set the environment variable GRB_LICENCE_FILE to point to this license (e.g. GRB_LICENSE_FILE=/home/jovyan/nlp_repo/explanation/gurobi.lic )
- Copy the licence file into /opt/gurobi/gurobi.lic

Project Organization (To do)
------------

    ├── README.md          <- For developer notes; add details as necessary.
    |
    ├── testcf.pt          <- this file gives an example of how to use the existing algorithm for the HR domain
    │
    ....
    


--------

