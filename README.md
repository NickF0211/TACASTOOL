# This is the anonymous repository for TOOL

### prerequisite:
1. Python 3.5 and later

2. memtime for measuring time and memory usage: https://github.com/phuseman/memtime 
(only available on Linux OS). Please add memtime executable to the path.

3. z3-solver with python binding:
    `pip install z3-solver` or 
    `pip3 install z3-solver`
    
4. pysmt:
    `pip install pysmt` or 
    `pip3 install pysmt`
    


### repository structure


    1. Analyzer contains the implementation of the bounded satisfiability checking algorithm 
    2. CFH for case study CovidFree@Home
    3. PHIM for case study PHIM, and PHIM-A
    4. PBC for case study PBC
    5. NASA for case study NASA
    6. DGraph for case study DG
    7. magic_seqeunce for case study Magic
    8. Player for case study Player
    9. Banking for case study Bank
    


### launch experiments 
To launch experiment for case studies with aggregations, run `python3 benchmark_aggr.py`
To launch experiment for case studies without aggregations, run `python3 benchmark_non_aggr.py`
If (memtime) is not installed, change variable `memtime_available = False` before running the script.

To launch individual case study, go to the case study folder, and run `python3 {name}_exp.py`
where the name depends on the case study. 
