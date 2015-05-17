<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Quicksand:300,400,700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Oxygen+Mono' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
<title>Geofix</title>
</head>
<div id="content">
<h1> <i class="fa fa-globe"></i>GEOFIX</h1>
<table border="0">
<tr><th>ID</th><th>Date/Time</th><th>Latitude</th><th>Longitude</th><th>digiKam</th><th>Snapshot</th><th>Map</th></tr>
%for row in rows:
    %id = row[0]
    %dt = row[1]
    %lat = row[2]
    %lon = row[3]
    %digikam = row[4]
    %osm = row[5]
    <tr>
    <td class="col_style_0"><a href="/delete/{{dt}}">{{id}}</a></td>
    <td class="col_style_1">{{dt}}</td>
    <td>{{lat}}</td>
    <td>{{lon}}</td>
    <td>{{digikam}}</td>
    <td><a href='snapshot/{{dt}}'><img src="../static/Geofix/{{dt}}.jpg" width="75" /></a></td>
    <td class="col_style_2"><a href='{{osm}}' target='_blank'><font color="#8F8F7D"><i class="fa fa-map-marker fa-2x"></i></a></font></td>
  </tr>
%end
</table>
</div>
