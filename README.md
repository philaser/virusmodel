# Virusmodel




Virusmodel is a simple simulation model that seeks to mimic virus spread in a controlled community environment. Virusmodel is written in [Python]

Virusmodel has three primary goals

  - Provide a simple interface for virus simulation
  - Provide key insights into the rate of virus spread in a controlled community environment
  - simulate and analsye the effects of introducing interventions to reduce virus spread.

# Current features

  - Generate a community of randomly linked nodes
  - Simulate virus spread within a custom number of days using a user defined infection rate




### Installation

Dillinger requires Python 3 to run.

To install, simply use the command below

```sh
$ pip install virus_model
```



### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### How to use
Currently, virusmodel has limited functionality. Simulations can however be carried out on any population size.
Simulations can also be carried out using any infection rate
Deaths however automatically occur after 7 days of infection


To begin, we import and initialize the Graph object. this is the primary object that we will interact with.
```python
from virus_model.virusmodel import Graph
community = Graph()
```
We can create nodes to populate the Graph object. this method takes in the number of nodes as a int:
```python
community.createNodes(100)
community.createLinks()
```
We call the  createLinks method to randomly link the nodes together. currently all nodes are linked with unidirectional links.

Simulation is done with the simulate method. this method takes 3 arguments: 
- The initial number of infected nodes as an int
- The rate of infection as a float between 0-1
- The number of days the simulation runs for
```python
community.simulate(1, 0.7, 100)
```

The output is then printed to the console showing day-by-day statistics.


### Todos

 - 	~~Add deaths~~
 - Add proper exception handling
 - add extra documentation/comments
 - add the ability to place interventions
 - Add Analytics!
 - Add Tests as the codebase becomes larger

License
----

MIT




[//]: #

   [Python]: <https://www.python.org/>
   
