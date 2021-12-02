# SBU-CSE535-Distributed-Systems

CSE 525 | Fall 2021 | Distributed Systems | Scott Stoller

# Implementation of Twins and Testing of diemBFT

Team Members - 
1. Pratik Nagelia
2. Sumeet Pannu
3. Shubham Agrawal

## Platform
1. DistAlgo Version: 1.1.0b15
2. Python Implementation: CPython
3. Python Version: 3.7.12
4. OS: Ubuntu 20.04.3 LTS
5. Hosts: Google Cloud Platform (VM)

## Instructions

Instructions to build and run the system:  
Step 1: Install the below Pre-requisites  
Step 2: Run the program by below execution command  
Step 3: Check generated log files

### Step 1 : PreRequsites

1. Python (3.7.12)
2. pip
3. PyNacl & cffi
4. DistAlgo

```
pip3 install pynacl
pip3 install pyDistAlgo  
python3.7 -m pip install cffi
```

### Download
```
1. DistAlgo ( http://distalgo.cs.stonybrook.edu/tutorial )
2. pip install pynacl  ( to download Libsodium crypto library which is used for signatures and crypto hashing )
```

### Execution and scripts
#### Scenario Generator
Run scenario generator by executing below command:
```
cd twinsBFT/src
python3.7 -m da scenario_generator.da  ../config/config.json
```

#### Scenario Executer
Run scenario execuetr by executing below command:
```
cd twinsBFT/src
python3.7 -m da --message-buffer-size 65535 scenario_executer.da test_scenarios.json
```

### Bugs and Limitations

1. Sync-up of replicas not working
2. Sometimes random test cases cause the diem to run on infinite loop 


### Main Files

The `twinsBFT` directory is root directory in which `src` containing all the relevant files for the system.  
Scenario Generator : The `scenario_generator.da` is the main file which runs the scenario generator and generates all the test cases.
Scenario Executer : The `scenario_executer.da` is the main file which runs the scenario executer, spaws Network PlayGround and runs all the test cases.


### Code Size

Non Blank Non-comment lines of code

```
> brew install cloc
> cloc diemBFT
github.com/AlDanial/cloc v 1.90  T=0.01 s (1682.5 files/s, 250183.5 lines/s)
--------------------------------------------------------------------------------
Language                      files          blank        comment           code
--------------------------------------------------------------------------------
DAL                              19            367              0           1915
JSON                              3              0              0           1130
Bourne Again Shell                1              0              0              8
--------------------------------------------------------------------------------
SUM:                             23            367              0           3053
--------------------------------------------------------------------------------
```
Algorithm: 1915  
Other:  1130
Total:   3053
(Numbers generated using CLOC https://github.com/AlDanial/cloc) 

Approximately 622 Lines (Algo) are the main algorithm. Remaining 266 (0.30%) functionalities interleaved with the algorithm.

### Language Feature Usage

list comprehensions: 6  
dictionary comprehensions:  8 
set comprehensions:   
aggregations:   
quantifications:   
await statements: 3  
receive handlers: 7  

### Contributions

1. Sumeet Pannu - Understanding the algorithm, completed parts of code in Scenario Generator, Integration of Twins with Diem, Testing and documentation.

2. Pratik Nagelia - Understanding the algorithm, completed the parts of code in Scenario Executer & Network Playground, Integration of Twins with Diem,  Testing and documentation.

3. Shubham Agrawal - Understanding the algorithm, completed parts of code in Scenario Executer & Network Playground, Integration of Twins with Diem, Testing and documentation.
