# 🗺 Map

[View a live demo here 🧭](https://map.tmos.es "Live demo hosted with github pages and google cloud functions")

A simple mapping application written in Python, using [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra's_algorithm) to find a route,
[Pillow](https://pillow.readthedocs.io/en/stable/) to draw the path
and [Flask](https://flask.palletsprojects.com/en/2.0.x/) to return this as an image from a HTTP Request.

Currently hosted using (GitHub Pages)[https://pages.github.com] for the frontend
and [Google Cloud Functions](https://cloud.google.com/functions) for the backend.

<details>
  <summary>Frontend details</summary>
  
  The frontend could be served dynamically usign Flask to populate the list of available destinations, but I've chosen to serve it statically for this demo
  (because it's quicker for the user and saves on the number of calls being made to my Cloud Function).
  
  A JavaScript function is used to get the path image from the backend and overlay this on the map.
</details>
