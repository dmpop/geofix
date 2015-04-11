<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Quicksand:300,400,700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,600,700' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
</head>
<title>Geofix</title>
<div id="content">
<h1>Geofix</h1>
<table border="0">
<tr><th>Date/Time</th><th>Latitude</th><th>Longitude</th><th>Place</th><th>Map</th></tr>
%for row in rows:
    %id = row[0]
    %dt = row[1]
    %lat = row[2]
    %lon = row[3]
    %place = row[4]
    %osm = row[5]
    <tr>
    <td class="col_style_1">{{dt}}</td>
    <td>{{lat}}</td>
    <td>{{lon}}</td>
    <td>{{place}}</td>
    <td class="col_style_2"><a href='{{osm}}' target='_blank'><i class="fa fa-map-marker"></i></a></td>
  </tr>
%end
</table>
</div>
