from flask import Flask, request, send_file
from mapper import getTownPath, getClearTownMap

def townMapper(request):
  start = str(request.args['start'])
  end = str(request.args['end'])
  path = getTownPath(start,end)
  filename = getClearTownMap(path)
  return send_file(filename, mimetype='image/gif')