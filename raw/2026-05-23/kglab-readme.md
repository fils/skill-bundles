# kglab

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4416034.svg)](https://doi.org/10.5281/zenodo.4416034)
![Licence](https://img.shields.io/github/license/DerwenAI/kglab)
![Repo size](https://img.shields.io/github/repo-size/DerwenAI/kglab)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/DerwenAI/kglab?style=plastic)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)


Welcome to *Graph Data Science*:
<https://derwen.ai/docs/kgl/>

The **kglab** library provides a simple abstraction layer in Python 3.11-3.13
for building knowledge graphs, leveraging Pandas, NetworkX, RAPIDS, RDFLib,
Morph-KGC, and many more.


## Getting Started

See the ["Getting Started"](https://derwen.ai/docs/kgl/start/)
section of the online documentation.

# pip
```bash
python3 -m pip install kglab
```

# poetry
```bash
poetry add kglab
```

# conda
```bash
conda env create -n kglab
conda activate kglab
pip install kglab
```

Then to run some simple uses of this library:
```python
import kglab

# create a KnowledgeGraph object
kg = kglab.KnowledgeGraph()

# load RDF from a URL
kg.load_rdf("http://bigasterisk.com/foaf.rdf", format="xml")

# measure the graph
measure = kglab.Measure()
measure.measure_graph(kg)

print("edges: {}\n".format(measure.get_edge_count()))
print("nodes: {}\n".format(measure.get_node_count()))

# serialize as a string in "Turtle" TTL format
ttl = kg.save_rdf_text()
print(ttl)
```

See the **tutorial notebooks** in the `examples` subdirectory for
sample code and patterns to use in integrating **kglab** with other
graph libraries in Python:
<https://derwen.ai/docs/kgl/tutorial/>


<details>
  <summary>Using Docker</summary>

For a simple approach to running the tutorials, see use of _docker compose_:
<https://derwen.ai/docs/kgl/tutorial/#use-docker-compose>

Also, container images for each release are available on DockerHub:
<https://hub.docker.com/repository/docker/derwenai/kglab>

To build a container image and run it for the tutorials:
```bash
docker build --pull --rm -f "docker/Dockerfile" -t kglab:latest .
docker run -p 8888:8888 -it kglab
